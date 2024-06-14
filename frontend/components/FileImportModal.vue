<!-- ImportModal.vue -->
<template>
    <transition name="fade">
      <div v-if="show" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
        <div class="bg-white rounded-lg p-8 shadow-lg w-1/3">
          <h2 class="text-2xl mb-4">Import File</h2>
          <form @submit.prevent="importFile">
            <input type="file" @change="handleFileChange" class="mb-4">
            <div class="flex justify-end">
              <button type="button" @click="closeModal" class="mr-2 px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600">Cancel</button>
              <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Import</button>
            </div>
          </form>
        </div>
      </div>
    </transition>
  </template>
  
  <script setup>
  import { ref, watch } from 'vue'
  import { useEmitter } from 'nuxt/app'
  
  // Reactive state for file input
  const file = ref(null)
  
  // Function to handle file change
  const handleFileChange = (event) => {
    file.value = event.target.files[0]
  }
  
  // Function to close the modal
  const closeModal = () => {
    showModal.value = false
  }
  
  // Function to import the file
  const importFile = () => {
    if (file.value) {
      // Handle file import logic here
      console.log('Importing file:', file.value)
      closeModal()
    } else {
      alert('Please select a file to import.')
    }
  }
  
  // Emit state management for modal visibility
  const emitter = useEmitter()
  const showModal = ref(false)
  watch(() => emitter.showModal, (value) => {
    showModal.value = value
  })
  </script>
  
  <style scoped>
  .fade-enter-active, .fade-leave-active {
    transition: opacity 0.5s;
  }
  .fade-enter, .fade-leave-to {
    opacity: 0;
  }
  </style>
  