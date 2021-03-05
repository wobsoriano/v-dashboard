<template>
<div>
  <!-- Title -->
  <div class="text-xs font-semibold">{{ title }}</div>
  <div class="flex items-center">

    <!-- Main gauge div -->
    <div
      class="flex items-center"
      :class="change > 0 ? 'text-green-400' : 'text-orange-600'"
    >
    
      <!-- Icon -->
      <slot></slot>

      <!-- Metric -->
      <div class="text-xl font-semibold">
        {{ value }}{{ unit }}
      </div>

      <!-- Metric footer / comparison -->
      <div class="flex mt-1 text-xs font-medium">

        <!-- Target -->
        <span class="px-1 text-gray-400" v-if="showTarget">
            / {{ target }}{{ unit }}
        </span>
        
        <!-- Change # and arrow indicator -->
        <div
          v-if="showChange"
          class="md:mt-1 lg:mt-0"
        >
          <!-- Increase indicator -->
          <div v-if="change > 0" class="flex">
            <svg
              class="h-4 w-5"
              fill="currentColor"
              stroke="currentColor"
              viewBox="0 0 10 20"
              aria-hidden="true"
            >
              <path
                fill-rule="evenodd"
                d="M5.293 9.707a1 1 0 010-1.414l4-4a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L11 7.414V15a1 1 0 11-2 0V7.414L6.707 9.707a1 1 0 01-1.414 0z"
                clip-rule="evenodd"
              />
            </svg>
            <span class="sr-only"> Increased by </span>
            {{ change }}{{ unit }}
          </div>

          <!-- Decrease indicator -->
          <div v-else class="flex items-center">
            <svg
              class="h-4 w-5"
              fill="currentColor"
              stroke="currentColor"
              viewBox="0 0 10 20"
              aria-hidden="true"
            >
              <path
                fill-rule="evenodd"
                d="M14.707 10.293a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 12.586V5a1 1 0 012 0v7.586l2.293-2.293a1 1 0 011.414 0z"
                clip-rule="evenodd"
              />
            </svg>
            <span class="sr-only"> Decreased by </span>
            {{ change }}{{ unit }}
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
export default defineComponent({
  props: {
    title: String,
    value: Number,
    target: Number,
    change: Number,
    unit: String,
    showTarget: {
      type: Boolean,
      default: false,
    },
    showChange: {
      type: Boolean,
      default: true,
    },
  },
});
</script>
