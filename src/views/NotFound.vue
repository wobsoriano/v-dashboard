<template>
  <div class="py-12 bg-white flex h-screen justify-center items-center">
    <div class="max-w-screen-xl mx-auto px-9 sm:px-6 lg:px-8 ">
      <div class="lg:text-center align-middle">
        <p
          class="text-base leading-6 text-indigo-600 font-semibold tracking-wide uppercase"
        >
          Page not found
        </p>
        <h3
          class="mt-2 text-3xl leading-8 font-extrabold tracking-tight text-gray-900 sm:text-4xl sm:leading-10"
        >
          &#9785; 404
        </h3>
        <p class="mt-4 max-w-2xl text-xl leading-7 text-gray-500 lg:mx-auto">
          The page you are looking for was moved, removed, renamed or might
          never exist!
        </p>
        <button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-full mt-5" @click.prevent="back">
          Back
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  setup() {
    const router = useRouter();

    function back() {
      router.push('/dashboard');
    }

    return {
      back,
    };
  },
});
</script>
