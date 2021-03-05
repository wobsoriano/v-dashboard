<template>
  <div class="w-full px-6 sm:w-1/2 xl:w-1/3">
    <div class="flex items-center px-5 py-6 shadow-sm rounded-md bg-white">
      <div class="p-3 rounded-full bg-opacity-75" :class="iconColor">
        <slot></slot>
      </div>

      <div class="mx-5">
        <h4 class="text-2xl font-semibold text-gray-700">{{ value }}</h4>
        <div class="text-gray-500">{{ title }}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from "vue";
export default defineComponent({
  props: {
    title: {
      type: String,
      default: "Default",
    },
    value: {
      type: Number,
      default: 1000,
    },
    iconColor: {
      type: String,
      default: "bg-indigo-600",
    },
  },
});
</script>
