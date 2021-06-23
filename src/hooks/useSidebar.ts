import { ref } from "vue";

const isOpen = ref(false)

export function useSidebar() {
  return {
    isOpen
  };
}
