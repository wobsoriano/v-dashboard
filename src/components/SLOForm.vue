<template>
  <div class="flex-1 items-center justify-center">
    <form @submit.prevent="" class="bg-white shadow-md rounded px-4 pt-2 pb-2 mb-4">
      <slot name="header"></slot>

      <!-- Loop through formData object -->
      <div class="mb-4" v-for="(value, index) in formData" :key="index">

        <!-- Hidden formData, ignore -->
        <div v-if="index.startsWith('_')"></div>

        <!-- Simple values -->
        <div v-else-if="!isObject(value)">
          <label class="block text-gray-700 text-sm font-bold mb-2" for="value">
            {{ index }}</label
          >

          <!-- Text area -->
          <div v-if="index.startsWith('filter') || index.startsWith('query')">
            <textarea
              class="bshadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              v-model="formData[index]"
            />
          </div>

          <!-- Input -->
          <div v-else>
            <input
              type="text"
              class="shadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              v-model="formData[index]"
              v-if="isNaN(Number(formData[index]))"
            />
            <input
              type="number"
              step="0.0001"
              min="0"
              max="1"
              class="shadow appearance-none border rounded w-full py-5 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              v-model.number="formData[index]"
              v-else
            />
          </div>
        </div>

        <!-- Nested object -->
        <div v-else>
          <h3
            class="mt-10 text-gray-700 font-bold"
            :class="`text-${depth - 2}xl`"
          >
            {{ capitalize(index) }}
          </h3>
          <slo-form :formData="formData[index]" :defaultButtons="false" />
        </div>
      </div>

      <!-- Buttons -->
      <div class="flex gap-2 justify-end mt-4">
        <button
          v-if="defaultButtons"
          @click="this.$emit('saved')"
          class="bg-green-600 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transform hover:scale-110 motion-reduce:transform-none"
        >
          Save & Test
        </button>
        <button
          v-if="defaultButtons"
          @click="this.$emit('reset')"
          class="bg-gray-600 hover:bg-gray-800 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline transform hover:scale-110 motion-reduce:transform-none"
        >
          Reset
        </button>
      </div>
      <slot name="footer"></slot>
    </form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: 'slo-form',
  props: {
    formData: {
      type: Object,
      default: {},
    },
    title: {
      type: String,
      default: "",
    },
    defaultButtons: {
      type: Boolean,
      default: true,
    },
    depth: {
      type: Number,
      default: 3,
    },
    testLoading: {
      type: Boolean,
      default: false
    }
  },
  methods: {
    isObject(value: any) {
      return typeof value == "object";
    },
    capitalize: function (value: String) {
      if (!value) return "";
      value = value.toString();
      return value.charAt(0).toUpperCase() + value.slice(1);
    },
  },
});
</script>

