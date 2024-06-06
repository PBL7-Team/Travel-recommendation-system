import { defineStore } from 'pinia';
import axios from "axios"
const toast = useToast()
// import { fetchWrapper, router } from '@/helpers';

let baseUrl = `${import.meta.env.VITE_API_URL}`;
const router = useRouter()
export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        access_token: localStorage.getItem('access_token') || '',
        refresh_token: localStorage.getItem('refresh_token') || '',
        expired_time: localStorage.getItem('expired_time') || '',
        isLoggedIn: !!localStorage.getItem('access_token'),
        user: localStorage.getItem('user'),
    }),
    actions: {
        async login(username: string, password: string) {
            try {
                const formData = new FormData();
                formData.append("username", username);
                formData.append("password", password);
                const result = await axios.post(`${baseUrl}/login`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });
                if (result.status == 200) {
                    this.$state.access_token = result.data.access_token;
                    this.$state.refresh_token = result.data.refresh_token;
                    this.$state.isLoggedIn = true;
                    const { sub, iat, exp, nbf, scope } = decodeToken(this.$state.access_token);
                    let format_sub = sub.replace("-", '')
                    const currentTime = new Date();
                    this.$state.expired_time = new Date(currentTime.getTime() + result.data.expires_in * 1000).toISOString();
                    const token = useCookie('accessToken'); // useCookie new hook in nuxt 3
                    token.value = this.$state.access_token
                    const userData = await this.getUserById(format_sub);
                    this.$state.user = userData;

                    // Persist the state to localStorage
                    // Save tokens and expiration time to localStorage
                    localStorage.setItem('access_token', this.$state.access_token);
                    localStorage.setItem('refresh_token', this.$state.refresh_token);
                    localStorage.setItem('expired_time', this.$state.expired_time);
                    localStorage.setItem('user', JSON.stringify(this.$state.user));
                } else {
                    console.log('error status', result.status)
                }
                console.log(result.data)

                return result

            } catch (error) {
                toast.add({
                    title: 'Login unsuccessfully',
                    description: 'Invalid username or password, please check again',
                    icon: 'i-octicon-desktop-download-24',
                    timeout: 10000,
                })
                console.error("Login error:", error);
            }
        },
        async loginByGoogle() {
            const result = await axios.post(`${baseUrl}/google/`, {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            });
            console.log(result)
            return result

        },

        async getUserById(userId: string) {
            try {
                let res = await axios.get(`${baseUrl}/users/${userId}`)
                if (res.status == 200) {
                    // console.log
                    return res.data
                } else {

                }
            } catch (e) {
                console.error(e)
            }
        },
        getUser() {
            return this.$state.user;
        },
        isUserLoggedIn() {
            // Check if the access token exists and has not expired
            return this.isLoggedIn && new Date(this.expired_time) > new Date();
        },
        async logout() {
            const formData = new FormData();
            formData.append("access_token", this.access_token);
            formData.append("refresh_token", this.refresh_token);
            // Log the tokens to verify they are not null or malformed
            console.log("Access Token:", this.access_token);
            console.log("Refresh Token:", this.refresh_token);
            const res = await axios.post(`${baseUrl}/logout`, formData, {
                headers: {
                    'Authorization': `Bearer ${this.access_token}`
                }
            });
            console.log(res)
            // const token = useCookie('accessToken'); // useCookie new hook in nuxt 3
            // this.isLoggedIn = false; // set authenticated  state value to false
            // token.value = null
            // this.resetState()
            if (res.status === 200) {
                // Clear all data from localStorage
                localStorage.clear();

                // Clear the token from cookies
                const token = useCookie('accessToken'); // useCookie new hook in nuxt 3
                token.value = null;

                // Update the authentication state
                this.isLoggedIn = false; // Set authenticated state value to false
                this.resetState(); // Reset any additional state if necessary
            } else {
                console.error('Logout failed:', res.status, res.data);
            }
        },

        resetState() {
            this.$state.access_token = ''
            this.$state.isLoggedIn = false
        },
    }
});