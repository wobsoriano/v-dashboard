<template>
  <div>
    <label class="block text-gray-700 text-sm font-bold mb-2" for="value">
      {{ index }}</label
    >

    <!-- Text area -->
    <div v-if="index.startsWith('filter') || index.startsWith('query')">
      <textarea
        class="bshadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="local"
      />
    </div>

    <!-- Text input -->
    <div v-else-if="isNaN(Number(local))">
      <input
        type="text"
        class="shadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
        v-model="local"
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
        v-model.number="local"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  props: ["index", "modelValue"],
  computed: {
    // proxy for 'modelValue'
    local: {
      get() { return this.modelValue },
      set(v) { this.$emit('update:modelValue', v) }
    }
  },
  methods: {},
});
</script>
