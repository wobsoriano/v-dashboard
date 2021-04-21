<template>
  <div class="flex h-screen bg-gray-200 font-roboto">
    <Sidebar />

    <div class="flex flex-col flex-1 overflow-hidden">
      <Header />

      <main class="flex-1 overflow-x-hidden overflow-y-auto bg-gray-200">
        <div class="container px-6 py-8 mx-auto">
          <slot />
        </div>
      </main>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

import Sidebar from "../components/dashboard/Sidebar.vue";
import Header from "../components/dashboard/Header.vue";

export default defineComponent({
  components: {
    Header,
    Sidebar,
  },
});
</script>
