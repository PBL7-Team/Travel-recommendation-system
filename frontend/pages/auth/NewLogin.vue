<script lang="ts" setup>
import BaseIcon from '@/components/BaseIcon.vue'
import { mdiGoogle, mdiFacebook, mdiTwitter } from '@mdi/js'
import { storeToRefs } from 'pinia'; // import storeToRefs helper hook from pinia
import { useAuthStore } from '~/store/auth'; // import the auth store we just created
const router = useRouter();

const { authenticateUser } = useAuthStore(); // use authenticateUser action from  auth store

const { authenticated } = storeToRefs(useAuthStore()); // make authenticated state reactive with storeToRefs


const username = useCookie('username')
const password = useCookie('password')
const isRememberMe = ref(false)

const isActive = ref(false);
const registerForm = ref({
    first_name: '',
    last_name: '',
    email: '',
    password: ''
});
const loginForm = ref({
    username: '',
    password: ''
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
        console.log('value', loginForm.value)
        await authenticateUser(loginForm.value); // call authenticateUser and pass the user object
        // redirect to homepage if user is authenticated
        if (authenticated) {
            // router.push('/');
            // this.$toast.success('Successfully authenticated')
            // toast.add({ title: 'Successfully authenticated!' })
            console.log("Success")
        }
        else {
            // this.$toast.global.my_error() //Using custom toast
            // toast.add({ title: 'Error while authenticating' })
            // this.$toast.error('Error while authenticating')
            console.log('Error while authenticating')
        }
    } catch (e) {
        console.error(e)
    }

};
const loginWithGoogle = async () => {
    await fetch('http://localhost:8000/api/v1/login', {
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        credentials: 'include', // Để gửi cookies, authentication headers
        body: JSON.stringify({
            username: loginForm.value.username,
            password: loginForm.value.password
        })
    });
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
                    <div class="social-icons">
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiGoogle" size="24" />
                        </a>
                        <a href="#" class="icon">`
                            <BaseIcon :path="mdiFacebook" size="24" />
                        </a>
                        <a href="#" class="icon">
                            <BaseIcon :path="mdiTwitter" size="24" />
                        </a>
                    </div>
                    <span class="text-black">or use your email password</span>
                    <input class="text-black" v-model="loginForm.username" type="email" placeholder="Email">
                    <span class="text-red"></span>
                    <input class="text-black" v-model="loginForm.password" type="password" placeholder="Password"
                        autocomplete="current-password">
                    <div class="flex flex-row mb-4">
                        <div class="flex-col d-flex justify-content-center">
                            <div class="form-check">
                                <input class="form-check-input" type="checkbox" value="isRememberMe" id="rememberMe">
                                <label class="text-black" for="rememberMe">Remember
                                    me</label>
                            </div>
                        </div>
                    </div>



                    <!-- <a href="#">Forget Your Password?</a> -->

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