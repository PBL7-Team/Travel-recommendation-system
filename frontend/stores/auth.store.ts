import { defineStore } from 'pinia';
import axios from "axios"
const toast = useToast()
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
// import { fetchWrapper, router } from '@/helpers';
import api from '@/stores/api';
const router = useRouter()

export const useAuthStore = defineStore({
    id: 'auth',
    state: () => ({
        // initialize state from local storage to enable user to stay logged in
        access_token: localStorage.getItem('access_token') || '',
        refresh_token: localStorage.getItem('refresh_token') || '',
        expired_time: localStorage.getItem('expired_time') || '',
        isLoggedIn: !!localStorage.getItem('access_token'),
        user: localStorage.getItem('user') || null,
    }),
    actions: {
        async login(username: string, password: string) {
            try {
                const formData = new FormData();
                formData.append("username", username);
                formData.append("password", password);
                const result = await axios.post(`${baseUrl}/api/v1/login`, formData, {
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
                    const token = useCookie('accessToken', { maxAge: result.data.expires_in * 1000 }); // useCookie new hook in nuxt 3
                    token.value = this.$state.access_token
                    console.log(format_sub)
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
        async loginByGoogle(credential: any) {
            const formData = new FormData();
            // formData.append("credential", credential);
            formData.append("access_token", credential);
            const result = await api.post(`/api/v1/google/login/`, formData, {
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
            return result;
        },
        // async getUserById(userId: string) {
        //     const { data, error } = await useFetch(`${baseUrl}/api/v1/users/${userId}`);
        //     console.log('getUserById',data.value)
        //     return data.value;
        // },
        // async getUserById(userId: string) {
        //     try {
        //         let res = await api.get(`/api/v1/users/${userId}`, {
        //             headers: {
        //                 'Content-Type':'application/json',
        //                 'Accept': 'application/json'
        //             }
        //         }
        //         )
        //         if (res.status == 200) {
        //             console.log('res: ', res)
        //             return res.data
        //         } else {
        //             console.error(`Server error ${res.status} when fetching user ${userId}`);
        //         }
        //         return null
        //     } catch (e) {
        //         console.error(e)
        //     }
        // },
        async getUserById(userId: string) {
            try {
                const response = await fetch(`${baseUrl}/api/v1/users/${userId}`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Authorization': `Bearer ${this.$state.access_token}`,
                        // 'ngrok-skip-browser-warning': 'skip-browser-warning'
                    }
                });
                
                console.log('response user: ',response)
                if (response.ok) { // Checks if the status is in the range 200-299
                    const data = await response.json(); // Parse the JSON response
                    console.log('res:', data);
                    return data;
                } else {
                    console.error(`Server error ${response.status} when fetching user ${userId}`);
                    return null;
                }
            } catch (error) {
                console.error('An error occurred while fetching user data:', error);
                return null;
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
            console.log("access_token: ", this.access_token)
            console.log("refresh_token: ", this.refresh_token)
            const res = await api.post(`/api/v1/logout`, formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
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
                toast.add({
                    title: 'Logout successfully',
                    timeout: 5000,
                })
            } else {
                console.error('Logout failed:', res.status, res.data);
            }
        },

        resetState() {
            this.$state.access_token = ''
            this.$state.isLoggedIn = false
        },

        async refreshAccessToken() {
            try {
                const formData = new FormData();
                formData.append("refresh_token", this.$state.refresh_token);
                const response = await axios.post(`/api/v1/refresh-token`, formData, {
                    headers: {
                        'Content-Type': 'multipart/form-data'
                    }
                });

                if (response.status === 200) {
                    this.$state.access_token = response.data.access_token;
                    this.$state.refresh_token = response.data.refresh_token;
                    const currentTime = new Date();
                    this.$state.expired_time = new Date(currentTime.getTime() + response.data.expires_in * 1000).toISOString();

                    // Update localStorage
                    localStorage.setItem('access_token', this.$state.access_token);
                    localStorage.setItem('refresh_token', this.$state.refresh_token);
                    localStorage.setItem('expired_time', this.$state.expired_time);

                    // Update the token cookie
                    const token = useCookie('accessToken');
                    token.value = this.$state.access_token;

                    return true; // Successfully refreshed
                } else {
                    return false; // Refresh failed
                }
            } catch (error) {
                console.error('Error refreshing token:', error);
                return false;
            }
        },
    }
});