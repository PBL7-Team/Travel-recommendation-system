export default defineNuxtRouteMiddleware((to, from) => {
    const { isLoggedIn } = storeToRefs(useAuthStore()); // make authenticated state reactive
    const accessToken = useCookie('token'); // get token from cookies
  
    if (accessToken.value) {
      // check if value exists
      isLoggedIn.value = true; // update the state to authenticated
    }
  
    // if token exists and url is /login redirect to homepage
    if (accessToken.value && to?.name === 'login') {
      return navigateTo('/');
    }
  
    // if token doesn't exist redirect to log in
    if (!accessToken.value && to?.name !== 'login') {
      abortNavigation();
      return navigateTo('/login');
    }
  });