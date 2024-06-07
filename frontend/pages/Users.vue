<script setup>
import DataTable from '@/components/Table/DataTable.vue'
import LayoutAuthenticated from '@/layouts/authenticated.vue'
// const { users } = await useFetch('/api/users');
import { ref, onMounted } from 'vue';
import axios from 'axios';  
const users = ref([]);
const loading = ref(false);
// onMounted(() => {
//     console.log('user: ', users)
// })
onMounted(async () => {
    try {
        const { data } = await axios.get('/api/v1/users');
        users.value = data.results;
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
            <DataTable v-if="!loading" :items="users" :headers="headers"/>
            <NuxtLoadingIndicator v-else/>
        </LayoutAuthenticated>
    </div>
</template>