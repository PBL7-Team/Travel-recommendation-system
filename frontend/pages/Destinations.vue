<script setup lang="ts">
import DataTable from '@/components/Table/DataTable.vue'
import LayoutAuthenticated from '@/layouts/authenticated.vue'
import api from '@/stores/api';
const config = useRuntimeConfig();
const baseUrl = config.public.apiUrl;
const toast = useToast()
// const userStore = useAuthStore()
const { isLoggedIn, access_token } = storeToRefs(useAuthStore());
import axios from 'axios'
// definePageMeta({
//   layout: 'authenticated'
// })

const headers = [
  { key: 'id', label: 'ID' },
  { key: 'attraction_name', label: 'Name' },
  { key: 'reviews_count', label: 'Total reviews' },
  { key: 'summary', label: 'Descriptions' },
  { key: 'review_count_non_calc', label: 'raw review' },
];
// Reactive state variables
const destinations = ref([]);
const totalPages = ref(1);
const currentPage = ref(1);
const checkedRows = ref<any[]>([]);
const totalReviews = ref(1);
const totalRawReviews = ref(1);
// Fetch data from the API
async function fetchData() {
  try {
    const response = await axios.get(`${baseUrl}/api/v1/attractions`, {
      params: { page: currentPage.value },
      headers: {
        'ngrok-skip-browser-warning': 'skip-browser-warning',
        // 'Authorization': `Bearer ${access_token}`
      }
    });
    console.log('res: ', response.data)
    if (response.status >= 200 && response.status < 300) {
      const data = response.data;
      destinations.value = data.results.data;
      totalPages.value = data.totalPages;
      totalReviews.value = data.count;
      totalRawReviews.value = data.results.raw_reviews_count;
    } else {
      console.error("Failed to fetch data with status:", response.status);
    }
  } catch (error) {
    console.error("An error occurred while fetching data:", error);
  }
}

const fetchAndSaveAttractions = async () => {
  try {
    const response = await axios.get(`${baseUrl}/api/v1/attractions/fetch-and-save`,
      {
        headers: {
          'ngrok-skip-browser-warning': 'skip-browser-warning',
        }
      }
    );
    if (response.status === 200 || response.status === 201 || response.status === 301) {
      console.log('Attractions fetched and saved successfully!');
      toast.add({
        title: 'Attractions fetched and saved successfully!',
        timeout: 10000,
      })
      // Thực hiện các thao tác cập nhật UI hoặc hiển thị thông báo thành công tại đây
    } else {
      toast.add({
        title: 'Error!',
        timeout: 10000,
      })
      console.error(`${response.status} - Failed to fetch and save attractions:${response.data}`);
    }
  } catch (error) {
    console.error('An error occurred while fetching and saving attractions:', error);
    // Xử lý khi gặp lỗi, ví dụ hiển thị thông báo lỗi
  }
};

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
        :checkable="true" @checked="true" :isDestination="true" @page-changed="refetch"
        @sync-data="fetchAndSaveAttractions" :totalReviews="totalReviews" :totalRawReviews="totalRawReviews" />
    </LayoutAuthenticated>
  </div>


</template>
