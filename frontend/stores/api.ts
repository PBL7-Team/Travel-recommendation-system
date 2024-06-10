import axios from 'axios';
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
const api = axios.create({
    baseURL: baseUrl,
});
const router = useRouter()
api.interceptors.request.use(
    async (config) => {
        const authStore = useAuthStore();
        console.log(authStore.$state.expired_time)
        // Check if the access token is expired
        if (new Date(authStore.$state.expired_time) <= new Date()) {
            const refreshed = await authStore.refreshAccessToken();

            if (!refreshed) {
                // Redirect to login if token refreshing fails
                // await authStore.logout();
                localStorage.clear();

                // Xóa token từ cookie
                const token = useCookie('accessToken');
                token.value = null;

                // Cập nhật trạng thái xác thực

                // toast.add({
                //     title: 'Logout successfully',
                //     timeout: 5000,
                // });
                router.push('/auth/newlogin');
                return Promise.reject(new Error('Token expired'));
            }
        }

        // Set Authorization header
        config.headers['Authorization'] = `Bearer ${authStore.$state.access_token}`;
        config.headers['Accept'] = 'application/json';
        return config;
    },
    (error) => Promise.reject(error)
);

export default api;