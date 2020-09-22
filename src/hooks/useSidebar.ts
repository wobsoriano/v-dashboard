import { reactive, ref, toRefs } from "vue";

const state = reactive({
  isOpen: false,
});

export function useSidebar() {
  return {
    ...toRefs(state),
  };
}
