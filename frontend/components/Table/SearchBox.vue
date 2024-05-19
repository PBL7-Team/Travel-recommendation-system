<script setup>
const emit = defineEmits(['search'])
const search= (e)=>{
    const searchValue = e.target.value
    // console.log(searchValue);
    emit('search',searchValue)
}
</script>
<template>
   <form class="py-3 px-4 flex items-center">
    <label class="sr-only">Search</label>
    <div class="relative w-full">
        <input type="text" @input="search" placeholder="Search" class="bg-gray-50 border border-gray-300 text-gray-900 rounded-sm"/>
    </div>
   </form>
</template>