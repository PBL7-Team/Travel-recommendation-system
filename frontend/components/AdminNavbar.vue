<script lang="ts" setup>
import { ref } from 'vue'
import { mdiClose, mdiDotsVertical } from '@mdi/js'

const containerMaxW = 'xl:max-w-6xl xl:mx-auto'
import BaseIcon from '@/components/BaseIcon.vue'
import NavbarMenuList from '@/components/NavBarMenuList.vue'
import NavbarItemPlain from '@/components/NavBarItemPlain.vue'

defineProps({
    menu: {
        type: Array,
        required: true
    },
    currentLang: {
        type: Object,
        required: false
    }
})

const emit = defineEmits(['menu-click', 'language-toggle'])

const menuClick = (event: MouseEvent, item: object) => {
    emit('menu-click', event, item)
}

const setLanguage = (lang: any) => {
    console.log(lang)
    emit('language-toggle', lang)
    toggleDropdown()
}

const isMenuNavBarActive = ref(false)


const languages = [
    {
        name: "English (US)",
        code: "en",
    },
    {
        name: "VietNam (VN)",
        code: "vi",
    },
];

// const currentLang = ref({
//     name: "English (US)",
//     code: "en"
// })


const isShowLanguage = ref(false)


const toggleDropdown = () => {
    isShowLanguage.value = !isShowLanguage.value;
}


</script>

<template>
    <nav
        class="top-0 inset-x-0 fixed bg-white h-16 z-30 transition-position w-screen lg:w-auto dark:bg-slate-800 shadow-custom-shadow">
        <div class="flex lg:items-stretch" :class="containerMaxW">
            <div class="flex flex-1 items-stretch ">
                <slot />
            </div>
            <!-- Navbar toggle -->
            <div class="flex-none items-center flex h-14 lg:hidden">
                <NavbarItemPlain @click.prevent="isMenuNavBarActive = !isMenuNavBarActive">
                    <BaseIcon :path="isMenuNavBarActive ? mdiClose : mdiDotsVertical" size="24" />
                </NavbarItemPlain>
            </div>
            <div class="max-h-screen-menu overflow-y-auto lg:overflow-visible absolute w-screen top-14 left-1/2 transform -translate-x-1/2 bg-white shadow-lg lg:w-auto lg:flex lg:static lg:shadow-none dark:bg-slate-800 mr-4"
                :class="[isMenuNavBarActive ? 'block' : 'hidden']">
                <NavbarMenuList :menu="menu" @menu-click="menuClick" />
                <!-- Toogle language -->
                <div
                    class="relative flex text-black dark:bg-gray-600 dark:text-white items-center space-x-1 md:space-x-0 rtl:space-x-reverse rounded">
                    <div>
                        <button @click="toggleDropdown()" type="button" data-dropdown-toggle="language-dropdown-menu"
                            class=" inline-flex items-center font-medium justify-center px-4 py-2 text-sm  rounded-lg cursor-pointer hover:bg-gray-100 dark:hover:bg-gray-700 dark:hover:text-white ">
                            <div v-if="currentLang?.code == 'en'">
                                <img class="w-5 h-5 rounded-full me-3" src="@/assets/icons/US.png" />
                            </div>
                            <div v-else>
                                <img class="w-5 h-5 rounded-full me-3" src="@/assets/icons/VN.png" />
                            </div>
                            <span class="">{{ currentLang?.name }}</span>
                        </button>
                    </div>

                    <!-- Dropdown -->
                    <div :class="!isShowLanguage ? 'hidden' : ''"
                        class=" absolute mt-40 left-0 z-50 bg-white text-base list-none divide-y divide-gray-100 rounded-lg shadow dark:bg-gray-700 "
                        id="language-dropdown-menu">
                        <ul class="py-2 font-medium" role="none">
                            <li v-for="lang in languages">
                                <a href="#" @click="setLanguage(lang)"
                                    class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 dark:text-gray-400 dark:hover:bg-gray-600 dark:hover:text-white"
                                    role="menuitem">
                                    <div class="inline-flex items-center">
                                        <div v-if="lang.code == 'en'">
                                            <img class="w-5 h-5 rounded-full me-3" src="@/assets/icons/US.png" />
                                        </div>
                                        <div v-else>
                                            <img class="w-5 h-5 rounded-full me-3" src="@/assets/icons/VN.png" />
                                        </div>
                                        {{ lang.name }}
                                    </div>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </nav>
</template>
