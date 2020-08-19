import { ref } from 'vue';

export function useSidebar() {
  const sidebarOpen = ref(false);

  function openSidebar() {
    sidebarOpen.value = true;
  }

  function closeSidebar() {
    sidebarOpen.value = false;
  }

  return {
    sidebarOpen,
    openSidebar,
    closeSidebar,
  };
}
