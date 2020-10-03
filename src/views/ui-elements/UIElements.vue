<template>
  <h3 class="text-gray-700 text-3xl font-medium">UI Elements</h3>

  <!-- Alerts -->
  <alerts-partial />

  <!-- Radio Buttons -->
  <radio-buttons-partial :colors="colors" />

  <!-- Checkboxes -->
  <checkboxes-partial :colors="colors" />

  <!-- Buttons -->
  <buttons-partial :colors="colors" />

  <!-- Paginations -->
  <pagination-partial />
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import AlertsPartial from "./partials/Alerts.vue";
import RadioButtonsPartial from "./partials/RadioButtons.vue";
import CheckboxesPartial from "./partials/Checkboxes.vue";
import ButtonsPartial from "./partials/Buttons.vue";
import PaginationPartial from "./partials/Pagination.vue";

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
  components: {
    AlertsPartial,
    RadioButtonsPartial,
    CheckboxesPartial,
    ButtonsPartial,
    PaginationPartial,
  },
});
</script>
