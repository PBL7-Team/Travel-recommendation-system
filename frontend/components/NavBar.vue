<script setup>
import { ref } from 'vue'
import { mdiClose, mdiDotsVertical, mdiChevronUp, mdiChevronDown } from '@mdi/js'
import { containerMaxW } from '@/configs/config.js'
import BaseIcon from '@/components/BaseIcon.vue'
import NavBarMenuList from '@/components/NavBarMenuList.vue'
import NavBarItemPlain from '@/components/NavBarItemPlain.vue'
import UserAvatarCurrentUser from '@/components/UserAvatarCurrentUser.vue'
import { mdiBackburger, mdiForwardburger, mdiMenu, mdiAccount, mdiCogOutline, mdiEmail, mdiLogout } from '@mdi/js'

import { useAuthStore } from '@/stores/auth.store';
const userStore = useAuthStore()
const { user: authUser } = storeToRefs(userStore);
defineProps({
  menu: {
    type: Array,
    required: true
  },
  isLoggedIn: {
    type: Boolean,
    required: true
  }
})

const emit = defineEmits(['menu-click'])

const menuClick = (event, item) => {
  emit('menu-click', event, item)
}

const isMenuNavBarActive = ref(false)

// const isDropdown = ref(false)

// const profileItem = ref({
//   menu: [
//     {
//       icon: mdiAccount,
//       label: 'My Profile',
//       to: '/profile'
//     },
//     {
//       icon: mdiCogOutline,
//       label: 'Settings'
//     },
//     {
//       icon: mdiEmail,
//       label: 'Messages'
//     },
//     {
//       isDivider: true
//     },
//     {
//       icon: mdiLogout,
//       label: 'Log Out',
//       isLogout: true
//     }
//   ]
// })

</script>

<template>
  <nav class="top-0 inset-x-0 fixed bg-gray-50 h-14 z-30 transition-position w-screen lg:w-auto dark:bg-slate-800">
    <div class="flex lg:items-stretch" :class="containerMaxW">
      <Logo />
      <div class="flex flex-1 items-stretch h-14">
        <slot />
      </div>
      <div class="flex-none items-stretch flex h-14 lg:hidden">

        <NavBarItemPlain @click.prevent="isMenuNavBarActive = !isMenuNavBarActive">
          <BaseIcon :path="isMenuNavBarActive ? mdiClose : mdiDotsVertical" size="24" />
        </NavBarItemPlain>
      </div>
      <div
        class="max-h-screen-menu overflow-y-auto lg:overflow-visible absolute w-screen top-14 left-0 bg-gray-50 shadow-lg lg:w-auto lg:flex lg:static lg:shadow-none dark:bg-slate-800"
        :class="[isMenuNavBarActive ? 'block' : 'hidden']">
        <NavBarMenuList :menu="menu" @menu-click="menuClick" />
      </div>
     
    </div>
  </nav>
</template>
