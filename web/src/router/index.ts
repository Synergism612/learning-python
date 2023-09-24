import { createRouter, createWebHashHistory, Router } from 'vue-router';
import Index from '@/views/Index.vue';

const router: Router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Index
    }
  ]
});

export default router;
