<script setup>
import LayoutAuthenticated from '@/layouts/authenticated.vue'
const toast = useToast()
import axios from 'axios'
let baseUrl = `${import.meta.env.VITE_API_URL}`;

const startCrawl = async () => {
    try {
        const response = await axios.get(`${baseUrl}/start-crawl`)
        toast.add({
            title: 'The data is crawling',
            description: response.data.message || 'Wait for a few minutes',
            timeout: 10000,
        })
    } catch (error) {
        toast.add({
            title: 'Error',
            description: error.response?.data.message || 'Failed to start crawl',
            timeout: 5000,
        })
    }
}

const calculateScore = async () => {
    try {
        const response = await axios.get(`${baseUrl}/sentiment-calculate`)
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
        const response = await axios.get(`${baseUrl}/get-crawl-info`)
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

        </div>
    </LayoutAuthenticated>
</template>