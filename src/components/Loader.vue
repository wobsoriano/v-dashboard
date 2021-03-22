<template>
  <div 
    v-if="loading"
    class="flex items-center px-3 py-3 m-3 text-gray-200 bg-gray-800">
    <svg
      xmlns="http://www.w3.org/2000/svg"
      fill="none"
      viewBox="0 0 24 24"
      class="animate-spin h-8 w-8"
      stroke="currentColor"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
      />
    </svg>
    <span class="px-3 text-xl">{{ text }}</span>
  </div>
</template>

<script>
import { defineComponent } from "vue";

export default defineComponent({
  props: {
    text: {
      type: String,
      default: "",
    },
    loading: {
      type: Boolean,
      default: false
    }
  },
});
</script>

