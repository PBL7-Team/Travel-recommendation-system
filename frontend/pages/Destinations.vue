<script setup lang="ts">
import DataTable from '@/components/Table/DataTable.vue'
import LayoutAuthenticated from '@/layouts/authenticated.vue'
import api from '@/stores/api';
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
const destinations = ref([]);
const totalPages = ref(173)

const currentPage = ref(1)


async function refetch(pageNumber: any) {
  currentPage.value = pageNumber;
  await fetchData(); // Call the fetchData function to fetch data with the updated page number
}

// Function to fetch data from the API
async function fetchData() {
  try {
    const response = await api.get(`/api/v1/destinations`, {
      params: {
        page: currentPage.value, // Pass the page as a parameter
      }
    });

    // Check if the response status is in the range of 2xx
    if (response.status >= 200 && response.status < 300) {
      const data = response.data; // Axios automatically parses JSON
      destinations.value = data.results;
      totalPages.value = data.totalPages;
      console.log(data.totalPages);
    } else {
      console.error("Failed to fetch data with status:", response.status);
    }
  } catch (error) {
    console.error("An error occurred while fetching data:", error);
  }
}
// Fetch data when the component is mounted
onMounted(fetchData);



</script>
<template>
  <div>
    <LayoutAuthenticated>
      <DataTable :items="destinations" :totalPages="totalPages" :currentPage="currentPage" :headers="headers" />
    </LayoutAuthenticated>
  </div>


</template>
