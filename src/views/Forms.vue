<template>
  <h3 class="text-gray-700 text-3xl font-semibold">Forms</h3>

  <div class="mt-4">
    <h4 class="text-gray-600">Model Form</h4>

    <div class="mt-4">
      <div
        class="max-w-sm w-full bg-white shadow-md rounded-md overflow-hidden border"
      >
        <form>
          <div
            class="flex justify-between items-center px-5 py-3 text-gray-700 border-b"
          >
            <h3 class="text-sm">Add Category</h3>
            <button>
              <svg
                class="h-4 w-4"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  stroke-linecap="round"
                  stroke-linejoin="round"
                  stroke-width="2"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </button>
          </div>

          <div class="px-5 py-6 bg-gray-200 text-gray-700 border-b">
            <label class="text-xs">Name</label>

            <div class="mt-2 relative rounded-md shadow-sm">
              <span
                class="absolute inset-y-0 left-0 pl-3 flex items-center text-gray-600"
              >
                <svg
                  class="h-6 w-6"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    stroke-width="2"
                    d="M11 4a2 2 0 114 0v1a1 1 0 001 1h3a1 1 0 011 1v3a1 1 0 01-1 1h-1a2 2 0 100 4h1a1 1 0 011 1v3a1 1 0 01-1 1h-3a1 1 0 01-1-1v-1a2 2 0 10-4 0v1a1 1 0 01-1 1H7a1 1 0 01-1-1v-3a1 1 0 00-1-1H4a2 2 0 110-4h1a1 1 0 001-1V7a1 1 0 011-1h3a1 1 0 001-1V4z"
                  />
                </svg>
              </span>

              <input
                type="text"
                class="form-input w-full px-12 py-2 appearance-none rounded-md focus:border-indigo-600"
              />
            </div>
          </div>

          <div class="flex justify-between items-center px-5 py-3">
            <button
              class="px-3 py-1 text-gray-700 text-sm rounded-md bg-gray-200 hover:bg-gray-300 focus:outline-none"
            >
              Cancel
            </button>
            <button
              class="px-3 py-1 bg-indigo-600 text-white rounded-md text-sm hover:bg-indigo-500 focus:outline-none"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  <div class="mt-8">
    <h4 class="text-gray-600">Forms</h4>

    <div class="mt-4">
      <div class="p-6 bg-white rounded-md shadow-md">
        <h2 class="text-lg text-gray-700 font-semibold capitalize">
          Account settings
        </h2>

        <form @submit.prevent="register">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-6 mt-4">
            <div>
              <label class="text-gray-700" for="username">Username</label>
              <input
                class="form-input w-full mt-2 rounded-md focus:border-indigo-600"
                type="text"
                v-model="user.username"
              />
            </div>

            <div>
              <label class="text-gray-700" for="emailAddress"
                >Email Address</label
              >
              <input
                class="form-input w-full mt-2 rounded-md focus:border-indigo-600"
                type="email"
                v-model="user.email"
              />
            </div>

            <div>
              <label class="text-gray-700" for="password">Password</label>
              <input
                class="form-input w-full mt-2 rounded-md focus:border-indigo-600"
                type="password"
                v-model="user.password"
              />
            </div>

            <div>
              <label class="text-gray-700" for="passwordConfirmation"
                >Password Confirmation</label
              >
              <input
                class="form-input w-full mt-2 rounded-md focus:border-indigo-600"
                type="password"
                v-model="user.confirm"
              />
            </div>
          </div>

          <div class="flex justify-end mt-4">
            <button
              class="px-4 py-2 bg-gray-800 text-gray-200 rounded-md hover:bg-gray-700 focus:outline-none focus:bg-gray-700"
            >
              Save
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

interface User {
  username: string;
  email: string;
  password: string;
  confirm: string;
}

export default defineComponent({
  setup() {
    const user = ref<User>({
      username: '',
      email: '',
      password: '',
      confirm: '',
    });

    const register = () => {
      const data = JSON.parse(JSON.stringify(user.value));
      console.log('Registered: ', data);
    };

    return {
      user,
      register,
    };
  },
});
</script>
