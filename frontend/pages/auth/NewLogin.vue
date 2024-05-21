<script setup>
// import { CIcon } from '@coreui/icons-vue';
// import { cibFacebook, cibGoogle } from '@coreui/icons';
import BaseIcon from '@/components/BaseIcon.vue'
import { mdiGoogle, mdiFacebook, mdiTwitter } from '@mdi/js'
const isActive = ref(false);
const registerForm = ref({
    name: '',
    email: '',
    password: ''
});
const loginForm = ref({
    email: '',
    password: ''
});

const toggleActive = () => {
    isActive.value = !isActive.value;
};

const register = async () => {
    // Handle registration logic here
    await fetch('http://localhost:8000/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
            email: loginForm.value.email,
            password: this.loginForm.value.password
        })
    });
    console.log('Register form submitted', registerForm.value);
};

const login = async () => {
    await fetch('http://localhost:8000/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include',
        body: JSON.stringify({
            email: loginForm.value.email,
            password: this.loginForm.value.password
        })
    });
    // Handle login logic here
    // try {
    //     let response = await this.$auth.loginWith('local', { data: this.login })
    //     this.$router.replace({ name: 'auth-user' })
    // } catch (err) {
    //     console.log(err)
    // }
};
</script>
<template>
    <div class="body">
        <div class="container" id="container" :class="{ active: isActive }">
            <div class="form-container sign-up">
                <form @submit.prevent="register">
                    <h1 class="text-xl text-black">Create Account</h1>
                    <div class="social-icons">
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiGoogle" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiFacebook" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiTwitter" size="24" />
                        </a>
                    </div>
                    <span class="text-gray-500">or use your email for registeration</span>
                    <input type="text" placeholder="Name">
                    <input type="email" placeholder="Email">
                    <input type="password" placeholder="Password">
                    <button>Sign Up</button>
                </form>
            </div>
            <div class="form-container sign-in">
                <form @submit.prevent="login">
                    <h1>Sign In</h1>
                    <div class="social-icons">
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiGoogle" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiFacebook" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiGoogle" size="24" />
                        </a>
                    </div>
                    <span class="text-black">or use your email password</span>
                    <input class="text-black" type="email" placeholder="Email">
                    <input class="text-black" type="password" placeholder="Password">
                    <a href="#">Forget Your Password?</a>
                    <button>Sign In</button>
                </form>
            </div>
            <div class="toggle-container">
                <div class="toggle">
                    <div class="toggle-panel toggle-left">
                        <h1>Welcome Back!</h1>
                        <p>Enter your personal details to use all of site features</p>
                        <button @click="toggleActive" id="login">Sign In</button>
                    </div>
                    <div class="toggle-panel toggle-right">
                        <h1 class="text-white">Hello, Friend!</h1>
                        <p>Register with your personal details to use all of site features</p>
                        <button @click="toggleActive" id="register">Sign Up</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<style>
@import '@/assets/css/newlogin.css'
</style>