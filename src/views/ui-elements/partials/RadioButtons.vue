<template>
  <div class="mt-8">
    <h4 class="text-gray-600">Radio Buttons</h4>

    <div class="mt-4">
      <div class="flex rounded-md bg-white py-4 px-4 overflow-x-auto">
        <label
          :class="`inline-flex items-center ${index && 'ml-3'}`"
          v-for="(c, index) in colors"
          :key="index"
        >
          <input
            type="radio"
            :class="`form-radio h-5 w-5 text-${c}-600`"
            checked
          /><span class="ml-2 text-gray-700">label</span>
        </label>
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
