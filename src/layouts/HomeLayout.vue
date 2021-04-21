<template>
  <div class="text-base leading-normal tracking-normal text-gray-600 bg-white work-sans">
    <Nav />
    <slot />
    <About />
    <Footer />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Nav from '../components/home/Nav.vue'
import About from '../components/home/About.vue'
import Footer from '../components/home/Footer.vue'

export default defineComponent({
  components: {
    Nav,
    About,
    Footer
  },
});
</script>

<style>
    .work-sans {
        font-family: 'Work Sans', sans-serif;
    }
            
    #menu-toggle:checked + #menu {
        display: block;
    }
    
    .hover\:grow {
        transition: all 0.3s;
        transform: scale(1);
    }
    
    .hover\:grow:hover {
        transform: scale(1.02);
    }
</style>

