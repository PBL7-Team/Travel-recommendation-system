<script setup>
import Footer from '@/components/IndexFooter.vue'
import menuNavBar, { createLoggedOutMenu } from '~/configs/menuNavBar.js'
import { mdiBackburger, mdiForwardburger, mdiMenu, mdiAccount, mdiCogOutline, mdiEmail, mdiLogout } from '@mdi/js'
// Authentication
definePageMeta({
  middleware: 'auth'
})
  
import { useAuthStore } from '@/stores/auth.store';

const userStore = useAuthStore()
const { user: authUser } = storeToRefs(userStore);
const { isLoggedIn } = storeToRefs(useAuthStore());
onMounted(() => {
  console.log('login?:', isLoggedIn.value)
  // menu.value = menuNavBar
})

const createMenu = (isLoggedIn) => {
  return isLoggedIn ? menuNavBar : createLoggedOutMenu()
}

const menu = computed(() => createMenu(isLoggedIn.value))
// const layoutAsidePadding = 'xl:pl-60'

const darkModeStore = useDarkModeStore()

const router = useRouter()

const isAsideMobileExpanded = ref(false)
const isAsideLgActive = ref(false)

router.beforeEach(() => {
  isAsideMobileExpanded.value = false
  isAsideLgActive.value = false
})
const menuClick = (event, item) => {
  if (item.isToggleLightDark) {
    darkModeStore.set()
  }

  if (item.isLogout) {
    //
    userStore.logout().then(() => {
      // menu.value = createMenu(false)
      router.push('/')
    }).catch((err) => {
      console.log('err')
    })

  }
}
</script>
<template>
  <!-- <Navbar /> -->
  <div :class="{
    'overflow-hidden lg:overflow-visible': isAsideMobileExpanded
  }">

    <div
      class="pt-14 min-h-screen w-screen transition-position lg:w-auto bg-white dark:bg-slate-800 dark:text-slate-100">

      <NavBar :menu="menu" :isLoggedIn="isLoggedIn" :class="[{ 'ml-60 lg:ml-0': isAsideMobileExpanded }]"
        @menu-click="menuClick">

        <NavBarItemPlain display="flex lg:hidden" @click.prevent="isAsideMobileExpanded = !isAsideMobileExpanded">
          <BaseIcon :path="isAsideMobileExpanded ? mdiBackburger : mdiForwardburger" size="24" />
        </NavBarItemPlain>
        <NavBarItemPlain display="hidden lg:flex xl:hidden" @click.prevent="isAsideLgActive = true">
          <BaseIcon :path="mdiMenu" size="24" />
        </NavBarItemPlain>

        <!-- <NavBarItemPlain use-margin>
          <FormControl placeholder="Search (ctrl+k)" ctrl-k-focus transparent borderless />
        </NavBarItemPlain> -->

      </NavBar>
      <slot />
      <Footer />
    </div>
  </div>
</template>
