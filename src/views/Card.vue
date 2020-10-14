<template>
  <div>
    <h3 class="text-gray-700 text-3xl font-semibold">Card</h3>
    <div class="mt-4 mb-3">
      <h4 class="text-gray-700">Stacked</h4>

      <div class="max-w-sm rounded bg-white overflow-hidden shadow-lg mt-6">
        <img
          class="w-full"
          src="https://picsum.photos/id/1016/384/234"
          alt="Sunset in the mountains"
        />
        <div class="px-6 py-4">
          <div class="text-gray-900 font-bold text-xl mb-2">The Coldest Sunset</div>
          <p class="text-gray-700 text-base">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit.
            Voluptatibus quia, nulla! Maiores et perferendis eaque,
            exercitationem praesentium nihil.
          </p>
        </div>
        <div class="px-6 pt-4 pb-2">
          <span
            class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
            >#photography</span
          >
          <span
            class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
            >#travel</span
          >
          <span
            class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2"
            >#winter</span
          >
        </div>
      </div>
    </div>
    <hr />
    <div class="mt-5">
      <h4 class="text-gray-700">Horizontal</h4>
      <div class="max-w-sm w-full lg:max-w-full lg:flex mt-6">
        <div
          class="h-48 lg:h-auto lg:w-48 flex-none bg-cover rounded-t lg:rounded-t-none lg:rounded-l text-center overflow-hidden"
          style="background-image: url('https://picsum.photos/id/0/192/213')"
          title="Woman holding a mug"
        ></div>
        <div
          class="border-r border-b border-l border-gray-400 lg:border-l-0 lg:border-t lg:border-gray-400 bg-white rounded-b lg:rounded-b-none lg:rounded-r p-4 flex flex-col justify-between leading-normal"
        >
          <div class="mb-8">
            <p class="text-sm text-gray-600 flex items-center">
              <svg
                class="fill-current text-gray-500 w-3 h-3 mr-2"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path
                  d="M4 8V6a6 6 0 1 1 12 0v2h1a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2v-8c0-1.1.9-2 2-2h1zm5 6.73V17h2v-2.27a2 2 0 1 0-2 0zM7 6v2h6V6a3 3 0 0 0-6 0z"
                />
              </svg>
              Members only
            </p>
            <div class="text-gray-900 font-bold text-xl mb-2">
              Can coffee make you a better developer?
            </div>
            <p class="text-gray-700 text-base">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Voluptatibus quia, nulla! Maiores et perferendis eaque,
              exercitationem praesentium nihil.
            </p>
          </div>
          <div class="flex items-center">
            <img
              class="w-10 h-10 rounded-full mr-4"
              src="https://via.placeholder.com/50"
              alt="Avatar of Jonathan Reinink"
            />
            <div class="text-sm">
              <p class="text-gray-900 leading-none">Jonathan Reinink</p>
              <p class="text-gray-600">Aug 18</p>
            </div>
          </div>
        </div>
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
