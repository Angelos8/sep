// router.js

// import Vue from 'vue';
// import VueRouter from 'vue-router';

import { createRouter, createWebHistory } from 'vue-router';

// add here the page you want to link to
// import pageName from './views/pageName.vue';
import LoginSignup from './views/LoginSignup.vue';
import Search from './views/Search.vue';
import ViewFile from './views/ViewFile.vue';
import UserProfile from './views/UserProfile.vue';
import AdminProfile from './views/AdminProfile.vue';
import Annotator from './views/Annotator.vue';
import Settings from './views/Settings.vue';

// Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: Search,
  },
  {
    path: '/login',
    component: LoginSignup,
  },
  {
    path: '/viewfile',
    component: ViewFile,
  },
  {
    path: '/user',
    component: UserProfile,
  },
  {
    path: '/admin',
    component: AdminProfile,
  },
  {
    path: '/annotate',
    component: Annotator,
  },
  {
    path: '/settings',
    component: Settings,
  },
];

// const router = new VueRouter({
//   routes,
// });

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
