<script setup>
import SearchBox from '@/components/Table/SearchBox.vue'
import { computed, ref } from 'vue'
import TableCheckboxCell from '@/components/TableCheckboxCell.vue'
import Pagination from './Pagination.vue'

const props = defineProps({
    items: {
        type: Array,
        required: true
    },
    totalPages: {
        type: Number,
        required: true
    },
    currentPage: {
        type: Number,
        required: true
    }
});

const searchQuery = ref('')

const filterItems = computed(() => {
    if (searchQuery !== '') {
        return props.items.filter(item => item.name.includes(searchQuery.value))
    }
    return props.items
})
const handleSearch = (search) => {
    searchQuery.value = search;
}

</script>
<template>
    <div class="p-6 xl:max-w-6xl xl:mx-auto flex-1">
        <div class="flex relative items-center justify-between">
            <!-- Search -->
            <SearchBox @search="handleSearch" />
        </div>
        <table class="w-full">
            <thead class="text-xs text-gray-700 uppercase">
                <tr>
                    <th class="px-4 py-3">ID</th>
                    <th class="px-4 py-3">Name</th>
                    <th class="px-4 py-3">Address</th>
                    <th class="px-4 py-3">Tel Number</th>
                    <th class="px-4 py-3">Website</th>
                    <th class="px-4 py-3">Descriptions</th>
                    <th class="px-4 py-3">
                        <span class="sr-only">Actions</span>
                    </th>
                </tr>
            </thead>
            <tr v-for="item in filterItems" :key="item.id" class="border-b">
                <td class="px-4 py-3 font-medium text-gray-900">{{ item.ID }}</td>
                <td class="px-4 py-3 font-medium text-gray-900">{{ item.name }}</td>
                <td class="px-4 py-3">{{ item.address }}</td>
                <td class="px-4 py-3">{{ item.tel }}</td>
                <td class="px-4 py-3">{{ item.website }}</td>
                <td class="px-4 py-3 text-ellipsis overflow-hidden">{{ item.description }}</td>
                <td class="px-4 py-3 flex items-center justify-end">
                    <a href="#" class="text-indigo-500 hover:underline">Details</a>
                </td>
            </tr>
        </table>
        <Pagination :totalPage="props.totalPages" :currentPage="props.currentPage" />
    </div>
</template>