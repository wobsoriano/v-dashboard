<template>
  <div>
    <h3 class="text-3xl font-medium text-gray-700">UI Elements</h3>

    <!-- Alerts -->
    <div class="mt-4">
      <h4 class="text-gray-600">Alerts</h4>

      <div class="mt-4">
        <div
          class="px-4 py-4 overflow-x-auto bg-white rounded-md whitespace-nowrap"
        >
          <div
            class="inline-flex w-full max-w-sm ml-3 overflow-hidden bg-white rounded-lg shadow-md"
          >
            <div class="flex items-center justify-center w-12 bg-green-500">
              <svg
                class="w-6 h-6 text-white fill-current"
                viewBox="0 0 40 40"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM16.6667 28.3333L8.33337 20L10.6834 17.65L16.6667 23.6166L29.3167 10.9666L31.6667 13.3333L16.6667 28.3333Z"
                />
              </svg>
            </div>

            <div class="px-4 py-2 -mx-3">
              <div class="mx-3">
                <span class="font-semibold text-green-500">Success</span>
                <p class="text-sm text-gray-600">
                  Your account was registered!
                </p>
              </div>
            </div>
          </div>

          <div
            class="inline-flex w-full max-w-sm ml-3 overflow-hidden bg-white rounded-lg shadow-md"
          >
            <div class="flex items-center justify-center w-12 bg-blue-500">
              <svg
                class="w-6 h-6 text-white fill-current"
                viewBox="0 0 40 40"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM21.6667 28.3333H18.3334V25H21.6667V28.3333ZM21.6667 21.6666H18.3334V11.6666H21.6667V21.6666Z"
                />
              </svg>
            </div>

            <div class="px-4 py-2 -mx-3">
              <div class="mx-3">
                <span class="font-semibold text-blue-500">Info</span>
                <p class="text-sm text-gray-600">
                  Channel archived by the owner.
                </p>
              </div>
            </div>
          </div>

          <div
            class="inline-flex w-full max-w-sm ml-3 overflow-hidden bg-white rounded-lg shadow-md"
          >
            <div class="flex items-center justify-center w-12 bg-yellow-500">
              <svg
                class="w-6 h-6 text-white fill-current"
                viewBox="0 0 40 40"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M20 3.33331C10.8 3.33331 3.33337 10.8 3.33337 20C3.33337 29.2 10.8 36.6666 20 36.6666C29.2 36.6666 36.6667 29.2 36.6667 20C36.6667 10.8 29.2 3.33331 20 3.33331ZM21.6667 28.3333H18.3334V25H21.6667V28.3333ZM21.6667 21.6666H18.3334V11.6666H21.6667V21.6666Z"
                />
              </svg>
            </div>

            <div class="px-4 py-2 -mx-3">
              <div class="mx-3">
                <span class="font-semibold text-yellow-500">Warning</span>
                <p class="text-sm text-gray-600">Image size is too large.</p>
              </div>
            </div>
          </div>

          <div
            class="inline-flex w-full max-w-sm ml-3 overflow-hidden bg-white rounded-lg shadow-md"
          >
            <div class="flex items-center justify-center w-12 bg-red-500">
              <svg
                class="w-6 h-6 text-white fill-current"
                viewBox="0 0 40 40"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M20 3.36667C10.8167 3.36667 3.3667 10.8167 3.3667 20C3.3667 29.1833 10.8167 36.6333 20 36.6333C29.1834 36.6333 36.6334 29.1833 36.6334 20C36.6334 10.8167 29.1834 3.36667 20 3.36667ZM19.1334 33.3333V22.9H13.3334L21.6667 6.66667V17.1H27.25L19.1334 33.3333Z"
                />
              </svg>
            </div>

            <div class="px-4 py-2 -mx-3">
              <div class="mx-3">
                <span class="font-semibold text-red-500">Error</span>
                <p class="text-sm text-gray-600">Your email is already used!</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Radio Buttons -->
    <div class="mt-8">
      <h4 class="text-gray-600">Radio Buttons</h4>

      <div class="mt-4">
        <div class="flex px-4 py-4 overflow-x-auto bg-white rounded-md">
          <label
            :class="`inline-flex items-center ${index && 'ml-3'}`"
            v-for="(c, index) in colors"
            :key="index"
          >
            <input
              type="radio"
              :class="`form-radio h-5 w-5 text-${c}-600`"
              name="radio"
            /><span class="ml-2 text-gray-700">label</span>
          </label>
        </div>
      </div>
    </div>

    <!-- Checkboxes -->
    <div class="mt-8">
      <h4 class="text-gray-600">Checkboxes</h4>

      <div class="mt-4">
        <div class="flex px-4 py-4 overflow-x-auto bg-white rounded-md">
          <label
            :class="`inline-flex items-center ${index && 'ml-3'}`"
            v-for="(c, index) in colors"
            :key="index"
          >
            <input
              type="checkbox"
              :class="`form-checkbox h-5 w-5 text-${c}-600`"
              checked
            /><span class="ml-2 text-gray-700">label</span>
          </label>
        </div>
      </div>
    </div>

    <!-- Buttons -->
    <div class="mt-8">
      <h4 class="text-gray-600">Buttons</h4>

      <div class="mt-4">
        <div class="flex px-4 py-4 overflow-x-auto bg-white rounded-md">
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

    <!-- Paginations -->
    <div class="mt-8">
      <h4 class="text-gray-600">Paginations</h4>

      <div class="mt-4">
        <div class="flex px-4 py-4 overflow-x-auto bg-white rounded-md">
          <div class="flex mr-4 rounded">
            <a
              href="#"
              class="px-3 py-2 ml-0 leading-tight text-blue-700 bg-white border border-r-0 border-gray-200 rounded-l hover:bg-indigo-500 hover:text-white"
              ><span>Previous</span></a
            >
            <a
              href="#"
              class="px-3 py-2 leading-tight text-blue-700 bg-white border border-r-0 border-gray-200 hover:bg-indigo-500 hover:text-white"
              ><span>1</span></a
            >
            <a
              href="#"
              class="px-3 py-2 leading-tight text-blue-700 bg-white border border-r-0 border-gray-200 hover:bg-indigo-500 hover:text-white"
              ><span>2</span></a
            >
            <a
              href="#"
              class="px-3 py-2 leading-tight text-blue-700 bg-white border border-r-0 border-gray-200 hover:bg-indigo-500 hover:text-white"
              ><span>3</span></a
            >
            <a
              href="#"
              class="px-3 py-2 leading-tight text-blue-700 bg-white border border-gray-200 rounded-r hover:bg-indigo-500 hover:text-white"
              ><span>Next</span></a
            >
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  setup() {
    const colors = ref<string[]>([
      "gray",
      "red",
      "orange",
      "yellow",
      "green",
      "teal",
      "blue",
      "indigo",
      "purple",
      "pink",
    ]);

    return {
      colors,
    };
  },
});
</script>
