<template>
  <div class="mt-8">
    <h4 class="text-gray-600">Buttons</h4>

    <div class="mt-4">
      <div class="flex rounded-md bg-white py-4 px-4 overflow-x-auto">
        <button
          :class="`px-6 py-3 bg-${c}-600 rounded-md text-white font-medium tracking-wide hover:bg-${c}-500 ${
            index && 'ml-3'
          }`"
          v-for="(c, index) in colors"
          :key="index"
        >
          Button
        </button>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, PropType } from "vue";

export default defineComponent({
  props: {
    colors: Object as PropType<Array<string>>,
  },
});
</script>
