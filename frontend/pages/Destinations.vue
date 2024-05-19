<script setup lang="ts">
import DataTable from '@/components/Table/DataTable.vue'
import LayoutAuthenticated from '@/layouts/authenticated.vue'

// definePageMeta({
//   layout: 'authenticated'
// })


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
    const response = await fetch(`http://localhost:8000/api/destinations?page=${currentPage.value}`, {
      method: 'GET',
    });
    if (response.ok) {
      const data = await response.json();
      destinations.value = data.results;
      console.log(data.totalPages)
      totalPages.value = data.totalPages;
    } else {
      console.error("Failed to fetch data");
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
      <DataTable :items="destinations" :totalPages="totalPages" :currentPage="currentPage"/>
    </LayoutAuthenticated>
  </div>


</template>
