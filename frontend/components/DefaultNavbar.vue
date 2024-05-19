<script setup>
import { ref } from 'vue'

defineProps({
    msg: String,
})

const showMobileMenu = ref(null)

const links = [
    {
        "name": "Plan Trip",
        "link": "/chatbot"
    },
    {
        "name": "Resources",
        "link": "/resources"
    },
    {
        "name": "Pricing",
        "link": "/pricing"
    },
    {
        "name": "Travel Blog",
        "link": "/blog"
    }
]
</script>

<template>
    <div class="sticky-wrap-2">
        <div class="nav-menu">
            <i class="fas fa-bars" @click="showMenu()">
            </i>
            <div class="nav-content" :class="showMobileMenu ? 'open-menu' : 'closed-menu'">
                <div class="logo"><img class="img" src="@/assets/images/team_logo1.png" alt="Logo" /></div>
                <ul class="nav-items">
                    <li class="md:mx-4" v-for="link in links">
                        <a :href="link.link" class="text-xl hover:text-green-500">{{ link.name }}</a>
                    </li>
                    <div class="nav-divider"></div>
                    <div class="wg-dropdown-1 w-dropdown">
                        <div class="wg-dd-1-togle w-dropdown-toggle">
                            <div class="wg-selector-text-wrapper">
                                <div class="wg-flag">
                                    <img src="https://assets-global.website-files.com/65d18725ed89c9029a244ef2/65d18725ed89c9029a244f3f_gb.svg"
                                        class="wg-flag-ico">
                                </div>
                                <div>EN</div>
                            </div>
                        </div>
                    </div>
                    <li class="md:mx-4">
                        <a href="/auth/login" class="text-xl hover:text-green-500">Login</a>
                    </li>
                    <li class="md:mx-4">
                        <a href="/signup" class="button-16 in-nav w-button">Sign up</a>
                    </li>
                </ul>
                <!-- <div class="login-button">Login</div> -->
            </div>
        </div>
    </div>
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
    color: black
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

.nav-items {
    display: flex;
    justify-content: center;
    align-items: center;
    list-style: none;
    margin: 0;
    padding: 0;

    li {
        padding: 0 0px;

        a &:hover {
            color: #434de7,
        }
    }
}

.nav-items li a:hover {
    color: #434de7;
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