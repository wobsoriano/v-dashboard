<template>
  <div class="mt-8">
    <h4 class="text-gray-600">Paginations</h4>

    <div class="mt-4">
      <div class="flex rounded-md bg-white py-4 px-4 overflow-x-auto">
        <div class="flex rounded mr-4">
          <a
            href="#"
            class="py-2 px-3 leading-tight bg-white border border-gray-200 text-blue-700 border-r-0 ml-0 rounded-l hover:bg-indigo-500 hover:text-white"
            ><span>Previous</span></a
          >
          <a
            href="#"
            class="py-2 px-3 leading-tight bg-white border border-gray-200 text-blue-700 border-r-0 hover:bg-indigo-500 hover:text-white"
            ><span>1</span></a
          >
          <a
            href="#"
            class="py-2 px-3 leading-tight bg-white border border-gray-200 text-blue-700 border-r-0 hover:bg-indigo-500 hover:text-white"
            ><span>2</span></a
          >
          <a
            href="#"
            class="py-2 px-3 leading-tight bg-white border border-gray-200 text-blue-700 border-r-0 hover:bg-indigo-500 hover:text-white"
            ><span>3</span></a
          >
          <a
            href="#"
            class="py-2 px-3 leading-tight bg-white border border-gray-200 text-blue-700 rounded-r hover:bg-indigo-500 hover:text-white"
            ><span>Next</span></a
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({});
</script>
