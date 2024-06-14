<template>
    <nav aria-label="Page navigation example">
        <ul class="inline-flex -space-x-px text-sm">
            <!-- First Page button -->
            <li>
                <button @click="changePage(1)" :disabled="currentPage === 1"
                    class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                    First
                </button>
            </li>

            <!-- Previous button -->
            <li>
                <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1"
                    class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                    Previous
                </button>
            </li>

            <!-- Pagination numbers -->
            <template v-if="totalPages <= 10">
                <!-- Show all pages if total pages are less than or equal to 10 -->
                <li v-for="pageNumber in totalPages" :key="pageNumber">
                    <button @click="changePage(pageNumber)" :class="[
                        'flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white',
                        { 'text-blue-600 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:bg-gray-700 dark:text-white': currentPage === pageNumber }
                    ]">
                        {{ pageNumber }}
                    </button>
                </li>
            </template>
            <template v-else>
                <!-- Limit number of pages and show ellipsis -->
                <li v-for="pageNumber in visiblePages" :key="pageNumber">
                    <button @click="changePage(pageNumber)" :class="[
                        'flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white',
                        { 'text-blue-600 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:bg-gray-700 dark:text-white': currentPage === pageNumber }
                    ]">
                        {{ pageNumber }}
                    </button>
                </li>
                <li v-if="visiblePages[visiblePages.length - 1] < totalPages - 1">
                    <span
                        class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400">
                        ...
                    </span>
                </li>
                <li v-for="pageNumber in [1, 2]" v-if="currentPage >= totalPages - 3" :key="pageNumber">
                    <button @click="changePage(pageNumber)" :class="[
                        'flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white',
                        { 'text-blue-600 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:bg-gray-700 dark:text-white': currentPage === pageNumber }
                    ]">
                        {{ pageNumber }}
                    </button>
                </li>
                <li v-if="visiblePages[visiblePages.length - 1] < totalPages - 1">
                    <span
                        class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400">
                        ...
                    </span>
                </li>
                <li v-for="pageNumber in [totalPages - 1, totalPages]" :key="pageNumber" v-if="currentPage === totalPages">
                    <button @click="changePage(pageNumber)" :class="[
                        'flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white',
                        { 'text-blue-600 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:bg-gray-700 dark:text-white': currentPage === pageNumber }
                    ]">
                        {{ pageNumber }}
                    </button>
                </li>
            </template>

            <!-- Next button -->
            <li>
                <button @click="changePage(currentPage + 1)" :disabled="currentPage === totalPages"
                    class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                    Next
                </button>
            </li>

            <!-- Last Page button -->
            <li>
                <button @click="changePage(totalPages)" :disabled="currentPage === totalPages"
                    class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">
                    Last
                </button>
            </li>
        </ul>
    </nav>
</template>

<script setup>
import { defineProps, defineEmits, ref, watch } from 'vue';

const props = defineProps({
    totalPages: Number,
    currentPage: Number,
});

const emit = defineEmits(['change']);

// Track visible pages
const visiblePages = ref([]);

// Initialize visible pages on component mount
watch(() => props.currentPage, () => {
    updateVisiblePages();
});

const updateVisiblePages = () => {
    const pages = [];
    if (props.totalPages <= 10) {
        for (let i = 1; i <= props.totalPages; i++) {
            pages.push(i);
        }
    } else {
        const currentPageIndex = props.currentPage - 1;
        const half = Math.floor(5 / 2);
        let start = currentPageIndex - half;
        let end = currentPageIndex + half;

        if (start < 0) {
            start = 0;
            end = 4;
        } else if (end > props.totalPages - 1) {
            start = props.totalPages - 5;
            end = props.totalPages - 1;
        }

        for (let i = start; i <= end; i++) {
            pages.push(i + 1);
        }
    }
    visiblePages.value = pages;
};

const changePage = (page) => {
    if (page >= 1 && page <= props.totalPages) {
        emit('change', page);
        updateVisiblePages();
    }
};
</script>

<style scoped>
nav {
    margin-top: 20px; /* Điều chỉnh khoảng cách giữa phân trang và bảng */
}
</style>
