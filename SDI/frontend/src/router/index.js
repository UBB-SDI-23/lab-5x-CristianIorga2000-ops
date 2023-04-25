import { createRouter, createWebHistory } from 'vue-router';
import AuthorList from '../views/AuthorList.vue';
import AuthorForm from '../views/AuthorForm.vue';
import StatisticsPage from '../views/StatisticsPage.vue';

const routes = [
  {
    path: '/authors',
    name: 'AuthorList',
    component: AuthorList,
  },
  {
    path: '/authors/create',
    name: 'CreateAuthor',
    component: AuthorForm,
  },
  {
    path: '/authors/:id/edit',
    name: 'EditAuthor',
    component: AuthorForm,
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: StatisticsPage,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router; 
