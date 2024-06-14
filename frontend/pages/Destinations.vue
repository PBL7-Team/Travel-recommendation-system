<script setup lang="ts">
import DataTable from '@/components/Table/DataTable.vue'
import LayoutAuthenticated from '@/layouts/authenticated.vue'
import api from '@/stores/api';
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
import axios from 'axios'
// definePageMeta({
//   layout: 'authenticated'
// })

const headers = [
  { key: 'ID', label: 'ID' },
  { key: 'name', label: 'Name' },
  { key: 'address', label: 'Address' },
  { key: 'tel', label: 'Tel Number' },
  { key: 'website', label: 'Website' },
  { key: 'description', label: 'Descriptions' }
];
// Reactive state variables
const destinations = ref([]);
const totalPages = ref(1);
const currentPage = ref(1);
const checkedRows = ref<any[]>([]);

// Fetch data from the API
async function fetchData() {
  try {
    const response = await axios.get(`${baseUrl}/api/v1/destinations`, {
      params: { page: currentPage.value },
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning'
      }
    });
    console.log('res: ', response.data)
    if (response.status >= 200 && response.status < 300) {
      const data = response.data;
      destinations.value = data.results;
      totalPages.value = data.totalPages;
    } else {
      console.error("Failed to fetch data with status:", response.status);
    }
  } catch (error) {
    console.error("An error occurred while fetching data:", error);
  }
}

// Fetch data when the component is mounted
onMounted(fetchData);

// Handle row check/uncheck
const handleChecked = (isChecked: boolean, item: any) => {
  if (isChecked) {
    checkedRows.value.push(item);
  } else {
    checkedRows.value = checkedRows.value.filter(row => row.ID !== item.ID);
  }
};
// Refetch data when page changes
const refetch = async (pageNumber: number) => {
  currentPage.value = pageNumber;
  await fetchData();
};
</script>

<template>
  <div>
    <LayoutAuthenticated>
      <DataTable :items="destinations" :totalPages="totalPages" :currentPage="currentPage" :headers="headers"
        :checkable="true" @checked="checked" @page-changed="refetch" />
    </LayoutAuthenticated>
  </div>


</template>
