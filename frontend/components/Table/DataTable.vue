<script setup lang="ts">
import SearchBox from '@/components/Table/SearchBox.vue';
import { computed, ref } from 'vue';
import TableCheckboxCell from '@/components/TableCheckboxCell.vue';
import Pagination from './Pagination.vue';

const props = defineProps({
    items: {
        type: Array as () => Array<any>,
        required: true,
    },
    headers: {
        type: Array as () => Array<{ key: string; label: string }>,
        required: true,
    },
    totalPages: {
        type: Number as () => number,
        required: true,
    },
    currentPage: {
        type: Number as () => number,
        required: true,
    },
    checkable: Boolean,
    isDestination: Boolean,

    totalReviews: {
        type: Number as () => number,
        required: false,
    },
    totalRawReviews: {
        type: Number as () => number,
        required: false,
    },
});

const emit = defineEmits(['checked', 'page-changed', 'sync-data']);
const searchQuery = ref('');

const filterItems = computed(() => {
    if (searchQuery.value.trim() !== '') {
        const lowerCaseQuery = searchQuery.value.trim().toLowerCase();
        return props.items.filter(item =>
            props.headers.some(header =>
                String(item[header.key]).toLowerCase().includes(lowerCaseQuery)
            )
        );
    }
    return props.items;
});

const handleSearch = (search: string) => {
    searchQuery.value = search;
};

const showModal = ref(false);

const openModal = () => {
    showModal.value = true;
};

const handleCheck = (isChecked: boolean, item: any) => {
    emit('checked', isChecked, item);
};

const changePage = (page: number) => {
    emit('page-changed', page);
};

const handleClickSyncData = () => {
    emit('sync-data');
};
</script>

<template>
    <div class="p-6 xl:max-w-6xl xl:mx-auto flex-1">
        <div class="flex relative items-center justify-between">
            <!-- Search -->
            <SearchBox @search="handleSearch" />
            <button @click="handleClickSyncData" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
                Sync data
            </button>
        </div>
        <div v-if="isDestination" class="mt-4 text-gray-600 dark:text-gray-400">
            Total Destinations: {{ props.totalReviews }}
            <span class="mx-2">|</span>
            Total Unresolved Destinations: {{ props.totalRawReviews }}
        </div>
        <table
            class="w-full border border-collapse border-round-sm text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400 mt-4">
            <thead class="text-xs text-gray-700 uppercase bg-white dark:bg-gray-700 dark:text-gray-400">
                <tr>
                    <th v-if="props.checkable" />
                    <th v-for="header in headers" :key="header.key" class="px-4 py-3">{{ header.label }}</th>
                    <th class="px-4 py-3">
                        <span class="sr-only">Actions</span>
                    </th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="item in filterItems" :key="item.id"
                    class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700">
                    <TableCheckboxCell v-if="props.checkable" @checked="(isChecked) => handleCheck(isChecked, item)" />
                    <td v-for="header in headers" :key="header.key" class="px-4 py-3 text-ellipsis overflow-hidden">{{
                        item[header.key] }}</td>
                    <td class="px-4 py-3 flex items-center justify-end">
                        <a href="#" class="text-indigo-500 hover:underline">Details</a>
                    </td>
                </tr>
            </tbody>
        </table>
        <Pagination :totalPages="props.totalPages" :currentPage="props.currentPage" @change="changePage" />
    </div>
</template>
