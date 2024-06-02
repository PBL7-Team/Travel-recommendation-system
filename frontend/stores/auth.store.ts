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
        id: '',
        first_name: '',
        last_name: '',
        username: '',
        access_token: '',
        refresh_token: '',
        expired_time: '',
        isLoggedIn: false,
        user:null,
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
                    let format_sub= sub.replace("-",'')
                    this.getUserById(format_sub).then(
                        (data)=>{
                            this.$state.user=data
                            localStorage.setItem('user', JSON.stringify(data));
                            console.log(this.$state.user)
                        }
                    )
                 

                }else{
                    console.log('error status',result.status )
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
        async getUserById(userId: string) {
            try{
                let res = await axios.get(`${baseUrl}/users/${userId}`)
                if (res.status==200){
                    // console.log
                    return res.data
                }else{
                    
                }
            }catch(e){
                console.error(e)
            }
        },
        getUser(){
            return this.$state.user;
        },

        async logout() {
            await axios.post('/logout')
            this.resetState()
        },

        resetState() {
            this.$state.id = ''
            this.$state.first_name = ''
            this.$state.last_name = ''
            this.$state.username = ''
            this.$state.access_token = ''
            this.$state.isLoggedIn = false
        },
    }
});