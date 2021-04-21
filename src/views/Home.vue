<template>
  <div>
    <Carousel />
    <Store />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Carousel from '../components/home/Carousel.vue'
import Store from '../components/home/Store.vue'

export default defineComponent({
  components: {
    Carousel,
    Store
  },
  setup() {
    
  },
});
</script>
