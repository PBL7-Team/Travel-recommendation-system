export default defineNuxtRouteMiddleware((to, from) => {
  const { isLoggedIn, access_token } = storeToRefs(useAuthStore()); // make authenticated state reactive
  const accessToken = useCookie('accessToken'); // get token from cookies
  const localAccessToken = useCookie('accessToken'); // lấy token từ cookie

  // Đồng bộ trạng thái đăng nhập
  if (localAccessToken.value) {
    access_token.value = localAccessToken.value; // Gán giá trị từ cookie vào access_token
    isLoggedIn.value = true; // Cập nhật trạng thái đã đăng nhập
  } else {
    isLoggedIn.value = false; // Cập nhật trạng thái chưa đăng nhập
  }

  // Nếu token tồn tại và trang đích là trang login, chuyển hướng về trang chủ
  if (isLoggedIn.value && to?.name === 'login') {
    return navigateTo('/');
  }

  // Nếu token không tồn tại và trang đích không phải là trang login, chuyển hướng về trang login
  if (!isLoggedIn.value && to?.name !== 'login') {
    abortNavigation();
    return navigateTo('/auth/login');
  }

  // Nếu token không tồn tại và trang đích là trang dashboard, chuyển hướng về trang login
  if (!isLoggedIn.value && to?.name === 'dashboard') {
    abortNavigation();
    return navigateTo('/auth/login');
  }
});