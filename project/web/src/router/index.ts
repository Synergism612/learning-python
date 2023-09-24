import { createRouter, createWebHashHistory, Router } from 'vue-router';
import IndexVue from '@/views/Index.vue';
import GraphicVue from '@/views/Graphic .vue';

const router: Router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: IndexVue
    },
    {
      path: '/graphic',
      name: 'graphic',
      component: GraphicVue
    }
  ]
});

export default router;
