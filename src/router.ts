import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

import Login from "./views/Login.vue";
import SLOs from "./views/SLOs.vue";
import SLOView from "./views/SLOView.vue";
import SLOEdit from "./views/SLOEdit.vue";
import Alerts from "./views/Alerts.vue";

const routes: RouteRecordRaw[] = [
  {
    path: "/",
    name: "Login",
    component: Login,
    meta: { layout: "empty" },
  },
  {
    path: "/alerts",
    name: "Alerts",
    component: Alerts,
  },
  {
    path: "/slos",
    name: "SLOs",
    component: SLOs,
  },
  {
    path: "/slo/:name/view",
    name: "SLO View",
    component: SLOView,
    props: true
  },
  {
    path: "/slo/:name/edit",
    name: "SLO Edit",
    component: SLOEdit
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
