<script lang="ts" setup>
import {
    GoogleSignInButton,
    type CredentialResponse
} from 'vue3-google-signin'
import BaseIcon from '@/components/BaseIcon.vue'
import { mdiGoogle, mdiFacebook, mdiTwitter } from '@mdi/js'
import { storeToRefs } from 'pinia'; // import storeToRefs helper hook from pinia

const toast = useToast()
import { useAuthStore } from '@/stores/auth.store'; // import the auth store we just created
const router = useRouter();

const userStore = useAuthStore()// use authenticateUser action from  auth store

const isActive = ref(false);
const registerForm = ref({
    first_name: '',
    last_name: '',
    email: '',
    password: ''
});
const loginForm = ref({
    username: 'letrongbach02@gmail.com',
    password: 'bach12345'
});

const toggleActive = () => {
    isActive.value = !isActive.value;
};

const register = async () => {
    // Handle registration logic here
    await fetch('http://localhost:8000/api/v1/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        // credentials: 'include',
        body: JSON.stringify({
            first_name: registerForm.value.first_name,
            last_name: registerForm.value.last_name,
            username: registerForm.value.email,
            password: registerForm.value.password
        })
    });
    console.log('Register form submitted', registerForm.value);
};

const login = async () => {
    try {
        const result = await userStore.login(loginForm.value.username, loginForm.value.password)
        if (result?.data) {
            toast.add({
                title: 'Login Successfully',
                timeout: 1000,
            })
            router.push('/')
        }
    } catch (e) {
        console.error(e)
        toast.add({
            title: 'Login unsuccessfully',
            description: 'Invalid username or password, please check again',
            icon: 'i-octicon-desktop-download-24',
            timeout: 10000,
        })
    }

};
// const loginWithGoogle = async () => {
//     const result = await userStore.loginByGoogle()
//     if (result?.data) {
//         toast.add({
//             title: 'Login Successfully',
//             timeout: 1000,
//         })
//         router.push('/')
//     }
// };

const onLoginSuccess = async (resp: CredentialResponse) => {
    console.log("Login successful", resp);
    const result = await userStore.loginByGoogle(resp.credential)
    if (result?.data) {
        toast.add({
            title: 'Login Successfully',
            timeout: 10000,
        })
        router.push('/')
    } else {
        toast.add({
            title: 'Something went wrong',
            timeout: 10000,
        })
    }
};

const onLoginError = () => {
    console.error("Login failed");
};


</script>
<template>
    <div class="body">
        <div class="container" id="container" :class="{ active: isActive }">
            <div class="form-container sign-up">
                <form @submit.prevent="register">
                    <h1 class="text-xl text-black">Create Account</h1>
                    <GoogleSignInButton @success="onLoginSuccess" @error="onLoginError" size="large">
                    </GoogleSignInButton>
                    <!-- <div class="social-icons">
                        <a @click="loginWithGoogle" href="#" class="icon">
                            <BaseIcon :path="mdiGoogle" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiFacebook" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiTwitter" size="24" />
                        </a>
                    </div> -->
                    <span class="text-gray-500">or use your email for registration</span>
                    <div class="row">
                        <input type="text" v-model="registerForm.first_name" placeholder="First Name">
                        <input type="text" v-model="registerForm.last_name" placeholder="Last name">
                    </div>

                    <input type="email" v-model="registerForm.email" placeholder="Email">
                    <input type="password" v-model="registerForm.password" placeholder="Password">
                    <button>Sign Up</button>
                </form>
            </div>
            <div class="form-container sign-in">
                <form @submit.prevent="login">
                    <h1>Sign In</h1>
                    <GoogleSignInButton class="mt-5 mb-5" @success="onLoginSuccess" @error="onLoginError" size="large">
                    </GoogleSignInButton>
                    <!-- <div class="social-icons">
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiGoogle" size="24" />
                        </a>
                        <a href="#" class="icon">`
                            <BaseIcon :path="mdiFacebook" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiTwitter" size="24" />
                        </a>
                    </div> -->
                    <span class="text-black">or use your email password</span>
                    <input class="text-black" v-model="loginForm.username" type="email" placeholder="Email">
                    <span class="text-red"></span>
                    <input class="text-black" v-model="loginForm.password" type="password" placeholder="Password"
                        autocomplete="current-password">
                    <div class="w-full flex items-center justify-between">
                        <div class="flex items-center">
                            <input id="remember_me" type="checkbox"
                                class="bg-white w-4 h-4 border-gray-300 rounded focus:ring-blue-500">
                            <label for="remember_me" class="ml-2 text-black text-sm">Remember me</label>
                        </div>
                        <a href="#" class="text-sm text-blue-600 hover:underline r-0">Forgot password?</a>
                    </div>
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
<style scoped>
@import '@/assets/css/newlogin.css';

.form-check {
    display: block;
    min-height: 1.6rem;
    padding-left: 1.5em;
    margin-bottom: .125rem;
}

.form-check-input[type=checkbox]:checked {
    background-image: none;
    background-color: #3b71ca;
}

label {
    display: inline-block;
}
</style>