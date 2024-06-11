<script setup lang="ts">
import SearchBox from '@/components/Table/SearchBox.vue'
import { computed, ref } from 'vue'
import TableCheckboxCell from '@/components/TableCheckboxCell.vue'
import Pagination from './Pagination.vue'

const props = defineProps({
    items: {
        type: Array,
        required: true
    },
    headers: {
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
    },

    checkable: {
        type: Boolean,
        required: false
    }
});

const searchQuery = ref('')
// Define emits
const emit = defineEmits(['checked', 'page-changed']);


const filterItems = computed(() => {
    if (searchQuery.value !== '') {
        return props.items.filter(item =>
            props.headers.some(header =>
                item[header.key]?.toString().toLowerCase().includes(searchQuery.value.toLowerCase())
            )
        )
    }
    return props.items
})
const handleSearch = (search) => {
    searchQuery.value = search;
}



// Modal import 
// Reactive state for modal visibility
const showModal = ref(false)

// Function to open the modal
const openModal = () => {
    showModal.value = true
}

// Handle checkbox click
const handleCheck = (isChecked: boolean, item: any) => {
    emit('checked', isChecked, item);
};

// Handle page change
const changePage = (page: number) => {
    emit('page-changed', page);
};


</script>
<template>
    <div class="p-6 xl:max-w-6xl xl:mx-auto flex-1">
        <div class="flex relative items-center justify-between">
            <!-- Search -->
            <SearchBox @search="handleSearch" />
            <button @click="openModal" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                Import data
            </button>
        </div>
        <table class="w-full border border-collapse border-round-sm text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
            <thead class="text-xs text-gray-700 uppercase bg-white dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th v-if="props.checkable" />
                    <th v-for="header in headers" :key="header.key" class="px-4 py-3">{{ header.label }}</th>
                    <th class="px-4 py-3">
                        <span class="sr-only">Actions</span>
                    </th>
                </tr>
            </thead>
            <tr v-for="item in filterItems" :key="item.id"
                class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                <TableCheckboxCell v-if="props.checkable" @checked="(isChecked) => handleCheck(isChecked, item)" />
                <td v-for="header in headers" :key="header.key" class="px-4 py-3 text-ellipsis overflow-hidden">{{
                    item[header.key] }}</td>
                <td class="px-4 py-3 flex items-center justify-end">
                    <a href="#" class="text-indigo-500 hover:underline">Details</a>
                </td>
            </tr>
        </table>
        <Pagination :totalPage="props.totalPages" :currentPage="props.currentPage" />
    </div>
</template>