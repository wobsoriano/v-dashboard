import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';

import Dashboard from './views/Dashboard.vue';
import Forms from './views/Forms.vue';
import Tables from './views/Tables.vue';
import UIElements from './views/UIElements.vue';
import Blank from './views/Blank.vue';
import Login from './views/Login.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    name: 'Login',
    component: Login,
    meta: { layout: 'empty' },
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/forms',
    name: 'Forms',
    component: Forms,
  },
  {
    path: '/tables',
    name: 'Tables',
    component: Tables,
  },
  {
    path: '/ui-elements',
    name: 'UIElements',
    component: UIElements,
  },
  {
    path: '/blank',
    name: 'Blank',
    component: Blank,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes: routes,
});

export default router;
