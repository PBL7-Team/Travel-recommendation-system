<script setup>
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
import { useAuthStore } from '@/stores/auth.store';
const userStore = useAuthStore()// use authenticateUser action from  auth store
const { user: authUser } = storeToRefs(userStore);

// test keyphrase extraction
const keyphrases = ref([]);


const messages = ref([
    {
        role: 'AI',
        message: 'Xin chào! Tôi có thể giúp gì cho bạn?'
    },
]);
const loading = ref(false);
const message = ref('');

const scrollToEnd = () => {
    setTimeout(() => {
        const chatMessages = document.querySelector('.chat-messages > div:last-child');
        chatMessages?.scrollIntoView({ behavior: 'smooth', block: 'end' });
    }, 100);
};

const sendPrompt = async () => {
    if (message.value === '') return;
    loading.value = true;

    messages.value.push({
        role: 'User',
        message: message.value
    });

    // // Extract keyphrases
    // keyphrases.value = extractKeyphrases(message.value);
    message.value = '';
    scrollToEnd();

    const lastMessage = messages.value[messages.value.length - 1].message;
    console.log(lastMessage)
    const userId = 'a54579edc369439abc090f45451301dd'
    if (authUser.value) {
        const userId = authUser.value.id
    }
    console.log('user Id', userId)

    const res = await fetch(`${baseUrl}/api/v1/chat-history`, {
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            // 'user': `${authUser.id}`,
            'user': userId,
            'chat_message': lastMessage
        }),
        method: 'post'
    });

    if (res.status === 200 || res.status === 201) {
        const response = await res.json();
        console.log('res', response)
        // Extract keyphrases from AI's system_answer and clean the message
        let systemAnswer = response?.system_answer || '';
        const keyphraseMatch = systemAnswer.match(/\{\[(.*?)\]\}/);

        if (keyphraseMatch) {
            const extractedKeyphrases = keyphraseMatch[1];
            keyphrases.value.push(...extractedKeyphrases.split(','));
            systemAnswer = systemAnswer.replace(/\{\[.*?\]\}/, '');
        }
        messages.value.push({
            role: 'AI',
            message: systemAnswer
        });
    } else {
        messages.value.push({
            role: 'AI',
            message: 'Xin lỗi, hệ thống có sự cố. Mong bạn thử lại sau'
        });
    }

    loading.value = false;
    scrollToEnd();
};
function processMessage(message) {
    // Replace \n with <br> tags
    if (message) {
        return message.replace(/\n/g, '<br>');
    }

    else {
        return 'The system is maintenance. Please come back later!'
    }
}
</script>

<template>
    <!-- <Navbar /> -->
    <NuxtLayout>
        <div class="max-w-xl mx-auto text-black">
            <!-- <a href="https://vercel.com/templates/next.js/blob-sveltekit"
            class="flex justify-center px-10 py-2 mx-auto space-x-1 text-sm font-medium text-center text-gray-600 transition-all rounded-full shadow-sm group bg-white/30 ring-1 ring-gray-900/5 hover:shadow-lg active:shadow-sm">
            Deploy your own to Vercel
        </a> -->
            <h3 class="my-4 text-xl text-center text-black">BVH chatbot</h3>
            <h1 class="my-2 text-4xl font-bold text-center text-black">Your Personal AI Travel Advisor</h1>
            <div class="max-w-xl mx-auto">
                <div class="bg-white rounded-md shadow h-[60vh] flex flex-col justify-between">
                    <div class="h-full overflow-auto chat-messages">
                        <div v-for="(message, i) in messages" :key="i" class="flex flex-col p-4">
                            <div v-if="message.role === 'AI'" class="pr-8 mr-auto">
                                <div class="p-2 mt-1 text-sm text-gray-700 bg-gray-200 rounded-lg text-smp-2">
                                    <!-- {{ message.message }} -->
                                    <span v-html="processMessage(message.message)"></span>
                                </div>
                            </div>
                            <div v-else class="pl-8 ml-auto">
                                <div class="p-2 mt-1 text-sm text-white bg-blue-400 rounded-lg">
                                    <!-- {{ message.message }} -->
                                    <span v-html="processMessage(message.message)"></span>
                                </div>
                            </div>
                        </div>
                        <div class="p-4 ml-10 mr-auto" v-if="loading">
                            <span class="loader"></span>
                        </div>
                    </div>
                    <form @submit.prevent="sendPrompt">
                        <div class="flex items-center w-full p-4">
                            <input v-model="message" type="text" placeholder="Type here..."
                                class="w-full p-3 text-sm text-black bg-transparent bg-gray-100 border rounded-md shadow border-white/40 grow" />
                            <button :disabled="loading" type="submit"
                                class="flex items-center justify-center flex-none w-10 h-10 ml-2 bg-green-500 rounded-full">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none"
                                    xmlns="http://www.w3.org/2000/svg">
                                    <path d="M22 2L11 13" stroke="white" stroke-width="1.5" stroke-linecap="round"
                                        stroke-linejoin="round" />
                                    <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="white" stroke-width="1.5"
                                        stroke-linecap="round" stroke-linejoin="round" />
                                </svg>
                            </button>
                        </div>
                    </form>
                </div>
            </div>
            <!-- Add a textarea for keyphrases -->
            <div class="mt-4">
                <h4 class="text-lg text-center">Keyphrases</h4>
                <textarea v-model="keyphrases" readonly class="w-full p-2 border rounded-md shadow"></textarea>
            </div>

            <!--  -->
            <div class="container mx-auto px-4">
                <div class="py-16">
                    <div class="text-center">
                        <div class="max-w-lg mx-auto">
                            <h2 class="text-2xl font-semibold">Upgrade to Premium</h2>
                            <div class="mt-2"></div>
                            <div>Get unlimited access for $9.99 per month.</div>
                            <div class="mt-6"></div>
                            <div class="flex flex-col sm:flex-row justify-center space-y-4 sm:space-y-0 sm:space-x-4">
                                <div class="w-full sm:max-w-xs">
                                    <a href="/sign-up"
                                        class="flex items-center justify-center gap-2 border border-gray-300 bg-white text-gray-700 text-center whitespace-nowrap rounded-md px-4 py-2.5 font-sans text-base font-semibold leading-6 no-underline transition-all duration-300 shadow-sm">Sign
                                        up for
                                        Free</a>
                                </div>
                                <div class="w-full sm:max-w-xs">
                                    <a href="/pricing"
                                        class="flex items-center justify-center gap-2 border border-gray-300  whitespace-nowrap rounded-md px-4 py-2.5 font-sans text-base font-semibold leading-6 no-underline transition-all duration-300 bg-blue-600 text-white text-center py-2 rounded">Try
                                        Premium</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>


        </div>
    </NuxtLayout>
</template>

<style>
.loader {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    display: block;
    position: relative;
    color: #d3d3d3;
    box-sizing: border-box;
    animation: animloader 2s linear infinite;
}

@keyframes animloader {
    0% {
        box-shadow: 14px 0 0 -2px, 38px 0 0 -2px, -14px 0 0 -2px, -38px 0 0 -2px;
    }

    25% {
        box-shadow: 14px 0 0 -2px, 38px 0 0 -2px, -14px 0 0 -2px, -38px 0 0 2px;
    }

    50% {
        box-shadow: 14px 0 0 -2px, 38px 0 0 -2px, -14px 0 0 2px, -38px 0 0 -2px;
    }

    75% {
        box-shadow: 14px 0 0 2px, 38px 0 0 -2px;
    }
}

textarea {
    height: 100px;
    resize: none;
    margin-top: 8px;
    padding: 8px;
    border: 1px solid #d3d3d3;
    border-radius: 4px;
    width: 100%;
    box-sizing: border-box;
}
</style>