<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script lang="ts">
const defaultLayout = "default";
</script>

<script lang="ts" setup>
import { computed } from "vue";
import { useRouter } from "vue-router";

const { currentRoute } = useRouter();

const layout = computed(
  () => `${currentRoute.value.meta.layout || defaultLayout}-layout`
);
</script>
