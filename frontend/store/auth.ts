import { defineStore } from 'pinia';

interface UserPayloadInterface {
  username: string;
  password: string;
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    authenticated: false,
    loading: false,
  }),
  actions: {
    async login({ username, password }: UserPayloadInterface) {
      console.log(username, password)
      const formData = new FormData();
      formData.append('username', username);
      formData.append('password', password);
      const { data, pending }: any = await useFetch('http://localhost:8000/api/v1/login', {
        method: 'POST',
        headers: { 'Content-Type': 'multipart/form-data' },
        credentials: 'include',
        // body: JSON.stringify({
        //   username: username,
        //   password: password
        // })
        body: formData
      });
      this.loading = pending;
      console.log("data",data)
      if (data.value) {
        const token = useCookie('token'); // useCookie new hook in nuxt 3
        token.value = data?.value?.token; // set token to cookie
        this.authenticated = true; // set authenticated  state value to true
      }
    },
    logUserOut() {
      const token = useCookie('token'); // useCookie new hook in nuxt 3
      this.authenticated = false; // set authenticated  state value to false
      token.value = null; // clear the token cookie
    },
  },
});