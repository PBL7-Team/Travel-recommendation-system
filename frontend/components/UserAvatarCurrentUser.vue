<script setup>
// import { useMainStore } from '@/stores/main'
// import UserAvatar from '@/components/UserAvatar.vue'
import { useAuthStore } from '@/stores/auth.store';
const userStore = useAuthStore()

// const user = computed(() => userStore.user)
// const userAvatar = computed(() => {
//   if (user.value && user.value.email) {
//     return `https://api.dicebear.com/7.x/avataaars/svg?seed=${user.value.email.replace(/[^a-z0-9]+/gi, '-')}`;
//   }
//   return '';
// });

// Define reactive variables
const user = ref(null);
const name = ref('')
const userAvatar = ref('');

// onMounted lifecycle hook
onMounted(() => {
  const storedUser = JSON.parse(localStorage.getItem('user'));
  console.log('su', storedUser.user)
  if (storedUser) {
    user.value = storedUser
    name.value = storedUser.first_name + ' ' + storedUser.last_name
    userAvatar.value = `https://api.dicebear.com/7.x/avataaars/svg?seed=Oscar`;
  }
  else {
    name.value = 'Guest'
    userAvatar.value = `https://api.dicebear.com/7.x/avataaars/svg?seed=Oscar`;
  }
});

// const mainStore = useMainStore()
</script>

<template>
  <UserAvatar :username="name" :avatar="userAvatar">
    <slot />
  </UserAvatar>
</template>
