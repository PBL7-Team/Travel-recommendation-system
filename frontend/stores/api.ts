import axios from 'axios';
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
const api = axios.create({
    baseURL: baseUrl,
    headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
});
const router = useRouter()
api.interceptors.request.use(
    async (config) => {
        const authStore = useAuthStore();

        // Check if the access token is expired
        if (new Date(authStore.$state.expired_time) <= new Date()) {
            const refreshed = await authStore.refreshAccessToken();

            if (!refreshed) {
                // Redirect to login if token refreshing fails
                await authStore.logout();
                router.push('/auth/newlogin');
                return Promise.reject(new Error('Token expired'));
            }
        }

        // Set Authorization header
        config.headers['Authorization'] = `Bearer ${authStore.$state.access_token}`;
        if (config.data instanceof FormData) {
            config.headers['Content-Type'] = 'multipart/form-data';
        } else {
            // Otherwise, use application/json
            config.headers['Content-Type'] = 'application/json';
        }
        config.headers['Accept'] = 'application/json';
        return config;
    },
    (error) => Promise.reject(error)
);

export default api;