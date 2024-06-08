<script setup lang="ts">
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
import DataTable from '@/components/Table/DataTable.vue'
import LayoutAuthenticated from '@/layouts/authenticated.vue'
// const { users } = await useFetch('/api/users');
import axios from 'axios';
import api from '@/stores/api';
import { ref, onMounted } from 'vue';
const users = ref([]);
const loading = ref(false);
const currentPage = ref(1)
const totalPages = ref(1)
// onMounted(() => {
//     console.log('user: ', users)
// })
// const { data } = await useFetch('/api/users');
onMounted(async () => {
    try {
        const response = await axios.get(`http://singular-joey-normally.ngrok-free.app/api/v1/users/`);
        console.log('res: ', response)
        users.value = response.data.results;
        totalPages.value = response.data.num_pages
    } catch (error) {
        console.log('Error fetching users:', error);
    } finally {
        loading.value = false;
    }
});

const headers = [
    { key: 'ID', label: 'ID' },
    { key: 'email', label: 'Email' },
    { key: 'first_name', label: 'First name' },
    { key: 'last_name', label: 'Last name' },
];
</script>
<template>
    <div>
        <LayoutAuthenticated>
            <!-- <div>{{data}}</div> -->
            <DataTable v-if="!loading" :items="users" :headers="headers" :currentPage="currentPage"
                :totalPages="totalPages" />
            <NuxtLoadingIndicator v-else />
        </LayoutAuthenticated>
    </div>
</template>