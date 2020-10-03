<template>
  <div class="mt-4">
    <h4 class="text-gray-600">Alerts</h4>

    <div class="mt-4">
      <div
        class="rounded-md bg-white py-4 px-4 overflow-x-auto whitespace-no-wrap"
      >
        <Alert title="Success" content="Your account was registered!" success />
        <Alert title="Warning" content="Image size is too large." warning />
        <Alert title="Error" content="Your email is already used!" error />
        <Alert title="Info" content="Channel archived by the owner." />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Alert from "../../../components/Alert.vue";

export default defineComponent({
  components: {
    Alert,
  },
});
</script>
