<template>
  <div>
    <label class="block text-gray-700 text-sm font-bold mb-2" for="value">
      {{ index }}</label
    >

    <!-- Text area -->
    <div v-if="index.startsWith('filter') || index.startsWith('query')">
      <textarea
        class="bshadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        @input="$emit('input', $event.target.value)"
      />
    </div>

    <!-- Text input -->
    <div v-else-if="isNaN(Number(value))">
      <input
        type="text"
        class="shadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        @input="$emit('input', $event.target.value)"
      />
    </div>

    <!-- Number input -->
    <div v-else>
      <input
        type="number"
        step="0.0001"
        min="0"
        max="1"
        class="shadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        @input="$emit('input', parseFloat($event.target.value))"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["index", "value"],
  methods: {},
});
</script>
