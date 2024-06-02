<script setup lang="ts">
import { ref } from 'vue'
import { storeToRefs } from 'pinia';
import { useAuthStore } from '@/stores/auth.store';
const userStore = useAuthStore()

const { user: authUser } = storeToRefs(userStore);


defineProps({
    msg: String,
    active: String
})

const isOpen = ref(false)

function drawer() {
    this.isOpen = !this.isOpen;
}


const links = [
    {
        "name": "Home",
        "link": "/",
        "active": true
    },
    {
        "name": "Plan Trip",
        "link": "/chatbot",
        "active": false
    },
    {
        "name": "Resources",
        "link": "/resources",
        "active": false
    },
    {
        "name": "Pricing",
        "link": "/pricing",
        "active": false
    },
    {
        "name": "Travel Blog",
        "link": "/blog",
        "active": false
    }
]


// Profile menu options
const profileMenuOptions = ref([
    { title: 'Profile' },
    { title: 'Settings' },
    { divider: true },
    { title: 'Logout' },
]);

const isProfileMenuOpen = ref(false);
const activeMenuOption = ref<number | null>(null);

const toggleProfileMenu = () => {
    isMenuOpen.value = !isMenuOpen.value;
};

const handleMenuOptionClick = (option: { title: string }) => {
    // Handle menu option click
    console.log(`Clicked on ${option.title}`);
};

const items = [
    [{
        label: 'ben@example.com',
        slot: 'account',
        disabled: true
    }], [{
        label: 'Settings',
        icon: 'i-heroicons-cog-8-tooth'
    }], [{
        label: 'Documentation',
        icon: 'i-heroicons-book-open'
    }, {
        label: 'Changelog',
        icon: 'i-heroicons-megaphone'
    }, {
        label: 'Status',
        icon: 'i-heroicons-signal'
    }], [{
        label: 'Sign out',
        icon: 'i-heroicons-arrow-left-on-rectangle'
    }]
]

</script>

<template>
    <!-- <div class="sticky-wrap-2">
        <div class="nav-menu" :class="isOpen ? 'open-menu' : 'closed-menu'"> -->
    <nav
        class="fixed w-full p-6 bg-white border-b border-[#f2f3ff] top-0 shadow-[0_20px_30px_-10px_rgba(29,1,80,0.1)] z-1">
        <div class="flex items-center justify-between">

            <!-- Header logo -->
            <div class="logo"><img class="img" src="@/assets/images/team_logo1.png" alt="Logo" /></div>

            <!-- Mobile toggle -->
            <div class="md:hidden">
                <button @click="drawer()">
                    <svg class="h-8 w-8 fill-current text-black" fill="none" stroke-linecap="round"
                        stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                        <path d="M4 6h16M4 12h16M4 18h16"></path>
                    </svg>
                </button>
            </div>

            <div class="hidden md:block">
                <ul class="flex space-x-8 text-sm font-sans items-center justify-between">
                    <li v-for="link in links" class="nav_items">
                        <a :href="link.link" :class="link.active ? 'nav_active_link' : 'nav_link'">{{ link.name }}</a>
                    </li>
                    <div class="nav-divider"></div>
                    <!-- <div class="wg-dropdown-1 w-dropdown">
                        <div class="wg-dd-1-togle w-dropdown-toggle">
                            <div class="wg-selector-text-wrapper">
                                <div class="wg-flag">
                                    <img src="https://assets-global.website-files.com/65d18725ed89c9029a244ef2/65d18725ed89c9029a244f3f_gb.svg"
                                        class="wg-flag-ico">
                                </div>
                                <div>EN</div>
                            </div>
                        </div>
                    </div> -->

                    <!-- <li v-if="authUser == null">
                        <a href="/auth/newlogin" class="nav_link hover:text-green-500">Login</a>
                    </li> -->
                    <li v-if="authUser == null">
                        <a href="/auth/newlogin"
                            class="cta inline-block bg-blue-600 text-white hover:bg-blue-500 px-3 py-2 rounded">Get
                            Started</a>
                    </li>
                    <li v-if="authUser != null">
                        <!-- Profile Dropdown menu -->

                        <UDropdown :items="items" :ui="{ item: { disabled: 'cursor-text select-text' } }"
                            :popper="{ placement: 'bottom-start' }">
                            <UAvatar src="https://avatars.githubusercontent.com/u/739984?v=4" />

                            <template #account="{ item }">
                                <div class="text-left">
                                    <p>
                                        Signed in as {{ authUser.first_name }}
                                    </p>
                                    <p class="truncate font-medium text-gray-900 dark:text-white">
                                        {{ item.label }}
                                    </p>
                                </div>
                            </template>

                            <template #item="{ item }">
                                <span class="truncate">{{ item.label }}</span>

                                <UIcon :name="item.icon"
                                    class="flex-shrink-0 h-4 w-4 text-gray-400 dark:text-gray-500 ms-auto" />
                            </template>
                        </UDropdown>
                    </li>
                </ul>
            </div>

            <!-- Drawer Menu -->
            <aside
                class="p-5 transform top-0 left-0 w-64 bg-white fixed h-full overflow-auto ease-in-out transition-all duration-300 z-30"
                :class="isOpen ? 'translate-x-0' : '-translate-x-full'">

                <div class="close">
                    <button class="absolute top-0 right-0 mt-4 mr-4" @click=" isOpen = false">
                        <svg class="w-6 h-6" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                            viewBox="0 0 24 24" stroke="currentColor">
                            <path d="M6 18L18 6M6 6l12 12"></path>
                        </svg>
                    </button>
                </div>

                <span @click="isOpen = false" class="flex w-full items-center p-4 border-b">
                    <div class="logo"><img class="img" src="@/assets/images/team_logo1.png" alt="Logo" /></div>
                </span>

                <ul class="divide-y font-sans">
                    <li v-for="link in links" class="">
                        <a :href="link.link" class="nav_link my-4 inline-block">{{ link.name
                            }}</a>
                    </li>
                    <li><a href="#" @click="isOpen = false"
                            class="my-8 w-full text-center font-semibold cta inline-block bg-blue-500 hover:bg-blue-600 px-3 py-2 rounded ">Sign
                            Up</a></li>
                </ul>

                <div class="follow">
                    <p class="italic font-sans text-sm">follow us:</p>
                    <div class="social flex space-x-5 mt-4 ">
                        <a href="#">
                            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="twitter"
                                class="h-5 w-5 fill-current text-gray-600" role="img" xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 512 512">
                                <path fill="currentColor"
                                    d="M459.37 151.716c.325 4.548.325 9.097.325 13.645 0 138.72-105.583 298.558-298.558 298.558-59.452 0-114.68-17.219-161.137-47.106 8.447.974 16.568 1.299 25.34 1.299 49.055 0 94.213-16.568 130.274-44.832-46.132-.975-84.792-31.188-98.112-72.772 6.498.974 12.995 1.624 19.818 1.624 9.421 0 18.843-1.3 27.614-3.573-48.081-9.747-84.143-51.98-84.143-102.985v-1.299c13.969 7.797 30.214 12.67 47.431 13.319-28.264-18.843-46.781-51.005-46.781-87.391 0-19.492 5.197-37.36 14.294-52.954 51.655 63.675 129.3 105.258 216.365 109.807-1.624-7.797-2.599-15.918-2.599-24.04 0-57.828 46.782-104.934 104.934-104.934 30.213 0 57.502 12.67 76.67 33.137 23.715-4.548 46.456-13.32 66.599-25.34-7.798 24.366-24.366 44.833-46.132 57.827 21.117-2.273 41.584-8.122 60.426-16.243-14.292 20.791-32.161 39.308-52.628 54.253z">
                                </path>
                            </svg>
                        </a>
                        <a href="#">
                            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="facebook-f"
                                class="h-5 w-5 fill-current text-gray-600" role="img" xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 320 512">
                                <path fill="currentColor"
                                    d="M279.14 288l14.22-92.66h-88.91v-60.13c0-25.35 12.42-50.06 52.24-50.06h40.42V6.26S260.43 0 225.36 0c-73.22 0-121.08 44.38-121.08 124.72v70.62H22.89V288h81.39v224h100.17V288z">
                                </path>
                            </svg>
                        </a>
                        <a href="#">
                            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="instagram"
                                class="h-5 w-5 fill-current text-gray-600" role="img" xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 448 512">
                                <path fill="currentColor"
                                    d="M224.1 141c-63.6 0-114.9 51.3-114.9 114.9s51.3 114.9 114.9 114.9S339 319.5 339 255.9 287.7 141 224.1 141zm0 189.6c-41.1 0-74.7-33.5-74.7-74.7s33.5-74.7 74.7-74.7 74.7 33.5 74.7 74.7-33.6 74.7-74.7 74.7zm146.4-194.3c0 14.9-12 26.8-26.8 26.8-14.9 0-26.8-12-26.8-26.8s12-26.8 26.8-26.8 26.8 12 26.8 26.8zm76.1 27.2c-1.7-35.9-9.9-67.7-36.2-93.9-26.2-26.2-58-34.4-93.9-36.2-37-2.1-147.9-2.1-184.9 0-35.8 1.7-67.6 9.9-93.9 36.1s-34.4 58-36.2 93.9c-2.1 37-2.1 147.9 0 184.9 1.7 35.9 9.9 67.7 36.2 93.9s58 34.4 93.9 36.2c37 2.1 147.9 2.1 184.9 0 35.9-1.7 67.7-9.9 93.9-36.2 26.2-26.2 34.4-58 36.2-93.9 2.1-37 2.1-147.8 0-184.8zM398.8 388c-7.8 19.6-22.9 34.7-42.6 42.6-29.5 11.7-99.5 9-132.1 9s-102.7 2.6-132.1-9c-19.6-7.8-34.7-22.9-42.6-42.6-11.7-29.5-9-99.5-9-132.1s-2.6-102.7 9-132.1c7.8-19.6 22.9-34.7 42.6-42.6 29.5-11.7 99.5-9 132.1-9s102.7-2.6 132.1 9c19.6 7.8 34.7 22.9 42.6 42.6 11.7 29.5 9 99.5 9 132.1s2.7 102.7-9 132.1z">
                                </path>
                            </svg>
                        </a>
                        <a href="#">
                            <svg aria-hidden="true" focusable="false" data-prefix="fab" data-icon="youtube"
                                class="h-5 w-5 fill-current text-gray-600" role="img" xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 576 512">
                                <path fill="currentColor"
                                    d="M549.655 124.083c-6.281-23.65-24.787-42.276-48.284-48.597C458.781 64 288 64 288 64S117.22 64 74.629 75.486c-23.497 6.322-42.003 24.947-48.284 48.597-11.412 42.867-11.412 132.305-11.412 132.305s0 89.438 11.412 132.305c6.281 23.65 24.787 41.5 48.284 47.821C117.22 448 288 448 288 448s170.78 0 213.371-11.486c23.497-6.321 42.003-24.171 48.284-47.821 11.412-42.867 11.412-132.305 11.412-132.305s0-89.438-11.412-132.305zm-317.51 213.508V175.185l142.739 81.205-142.739 81.201z">
                                </path>
                            </svg>
                        </a>
                    </div>
                </div>

            </aside>
        </div>
    </nav>
</template>

<style lang="scss" scoped>
img {
    vertical-align: middle;
    max-width: 100%;
    display: inline-block;
    width: 260px;
    height: auto;
}

body {
    color: #333;
    font-family: Inter, sans-serif;
    font-size: 14px;
    line-height: 20px;
}

a {
    text-decoration: none;
}

.navbar-container {
    justify-content: space-between;
    align-items: center;
    width: 100%;
    max-width: 1100px;
    height: 100%;
    margin-left: auto;
    margin-right: auto;
    display: flex;
}

.navbar-logo-link-2 {
    max-width: 140px;
    padding-top: 5px;
    padding-left: 0;
}

.w-nav-brand {
    float: left;
    color: #333;
    text-decoration: none;
    position: relative;
}

.sticky-wrap-2 {
    z-index: 99999;
    background-color: #fff;
    border-bottom: 1px solid #f2f3ff;
    position: sticky;
    top: 0;
    box-shadow: 0 20px 30px -10px rgba(29, 1, 80, .1);
}

.nav-menu {
    background-color: white;
}

.nav-content {
    display: flex;
    justify-content: space-between;
    padding: 10px 30px;
    align-items: center;
}



.nav_items {
    @apply flex mx-2 inline-block justify-items-center
}


.nav_link {
    @apply text-black hover:text-blue-500
}

.nav_active_link {
    @apply text-black border-b-2 border-blue-500 pb-1
}



i {
    display: none;
}

.nav-divider {
    background-color: #e4ebf3;
    width: 1px;
    height: 22px;
    margin-left: 15px;
    margin-right: 15px;
}

// Language flag:
.wg-dropdown-1 {
    text-transform: uppercase;
    flex-direction: column;
    align-items: stretch;
    width: auto;
    font-weight: 700;
}

.w-dropdown {
    text-align: left;
    z-index: 900;
    margin-left: auto;
    margin-right: auto;
    display: inline-block;
    position: relative;
}

.wg-dd-1-togle {
    z-index: 1;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    flex-direction: column;
    width: 100%;
    padding: 10px 15px;
}

.w-dropdown-toggle {
    -webkit-user-select: none;
    -ms-user-select: none;
    user-select: none;
    cursor: pointer;
    padding-right: 40px;
    display: inline-block;
}

.w-dropdown-btn,
.w-dropdown-toggle,
.w-dropdown-link {
    vertical-align: top;
    color: #222;
    text-align: left;
    white-space: nowrap;
    margin-left: auto;
    margin-right: auto;
    padding: 20px;
    text-decoration: none;
    position: relative;
}

.wg-selector-text-wrapper {
    align-items: center;
    width: 100%;
    display: flex;
}

.wg-flag {
    justify-content: center;
    align-items: center;
    width: 20px;
    height: 16px;
    margin-right: 10px;
    display: flex;
}

.wg-flag-ico {
    object-fit: cover;
    width: 100%;
    max-width: none;
    height: 100%;
}

.button-16 {
    color: #fff;
    background-color: #434de7;
    border-radius: 10px;
    height: 50px;
    padding: 15px 35px;
    font-size: 15px;
    font-weight: 500;
    box-shadow: 0 10px 20px -3px rgba(29, 1, 80, .1);
}

.button-16.in-nav {
    background-color: #175cd3;
    color: #fff;
    height: auto;
    margin-left: 10px;
    padding: 9px 17px;
    font-size: 14px;
}

// Mobile version - hidden hamburger menu
@media screen and (max-width: 1106px) {
    .nav-menu {
        padding-top: 10px;
        position: absolute;
        width: 100%;
    }

    .open-menu {
        opacity: 1;
        height: 150px;
    }

    .closed-menu {
        opacity: 0;
        height: 0;
        padding: 0;
    }

    .nav-content {
        flex-direction: column;
        z-index: 100;
        position: relative;
        transition: all 0.2s ease-out;
    }

    .nav-items {
        flex-direction: column;
    }

    i {
        display: block;
        text-align: right;
        padding: 0 10px 10px 0;
    }
}
</style>
