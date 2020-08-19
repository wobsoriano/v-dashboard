<template>
  <div class="flex h-screen bg-gray-200 font-roboto">
    <Sidebar :burgerClicked="burgerClicked" />

    <div class="flex-1 flex flex-col overflow-hidden">
      <Header @openSidebar="burgerClicked = true" />

      <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200">
        <div class="container mx-auto px-6 py-8">
          <slot />
        </div>
      </main>
    </div>
  </div>
</template>

<script lang="ts">
import Sidebar from './Sidebar.vue';
import Header from './Header.vue';
import { defineComponent, ref } from 'vue';

export default defineComponent({
  components: {
    Header,
    Sidebar,
  },
  setup() {
    const burgerClicked = ref(false);

    return {
      burgerClicked,
    };
  },
});
</script>
