<script setup>
import LayoutAuthenticated from '@/layouts/authenticated.vue'
const toast = useToast()
import axios from 'axios'
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
// let baseUrl = `${import.meta.env.VITE_API_URL}`;

const startCrawl = async () => {
    try {
        const response = await axios.get(`${baseUrl}/api/v1/start-crawl`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',
            }
        })
        if (response.status == 200) {
            toast.add({
                title: response.data.message,
                description: `${response.data.new_json_amount} new file json received`,
                timeout: 10000,
            })
        } else {
            toast.add({
                title: response.data.message|| 'Error while get crawl info',
                // description: `${response.data.new_json_amount} new file json received`,
                timeout: 10000,
            })
        }
        console.log('res: ', response)
    }
    catch (error) {
        toast.add({
            title: 'Error',
            description: error.response?.data.message || 'Failed to start crawl',
            timeout: 5000,
        })
    }
}

const calculateScore = async () => {
    try {
        const response = await axios.get(`${baseUrl}/api/v1/sentiment-calculate`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',

            }
        })
        toast.add({
            title: 'Calculation started',
            description: response.data.message || 'The sentiment scoring is in progress.',
            timeout: 10000,
        })
    } catch (error) {
        toast.add({
            title: 'Error',
            description: error.response?.data.message || 'Failed to start sentiment calculation',
            timeout: 5000,
        })
    }
}

const getCrawlInfo = async () => {
    try {
        const response = await axios.get(`${baseUrl}/api/v1/get-crawl-info`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',

            }
        })
        console.log('get crawl info', response)
        toast.add({
            title: 'Fetching Crawl Info',
            description: response.data.message || 'Fetching the latest crawl information.',
            timeout: 10000,
        })
    } catch (error) {
        toast.add({
            title: 'Error',
            description: error.response?.data.message || 'Failed to fetch crawl info',
            timeout: 5000,
        })
    }
}
const cancelCrawl = async () => {
    try {
        const response = await axios.get(`${baseUrl}/api/v1/stop-crawl`, {
            headers: {
                'ngrok-skip-browser-warning': 'skip-browser-warning',

            }
        })
        toast.add({
            title: 'Crawl Canceled',
            description: response.data.message || 'The crawling has been canceled.',
            timeout: 10000,
        })
    } catch (error) {
        toast.add({
            title: 'Error',
            description: error.response?.data.message || 'Failed to cancel crawl',
            timeout: 5000,
        })
    }
}
</script>
<template>
    <LayoutAuthenticated>
        <div class="grid grid-cols-3 gap-4 p-4 ">
            <CardBox>
                <button @click="startCrawl" class="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-700">
                    Start crawl
                </button>
            </CardBox>
            <CardBox>
                <button @click="getCrawlInfo" class="bg-red-500 text-white py-2 px-4 rounded hover:bg-red-700">
                    Get crawl info
                </button>
            </CardBox>
            <CardBox>
                <button @click="calculateScore" class="bg-green-500 text-white py-2 px-4 rounded hover:bg-green-700">
                    Calculate score
                </button>
            </CardBox>
            <CardBox>
                <button @click="cancelCrawl" class="bg-gray-500 text-white py-2 px-4 rounded hover:bg-gray-700">
                    Cancel crawl
                </button>
            </CardBox>
        </div>
    </LayoutAuthenticated>
</template>