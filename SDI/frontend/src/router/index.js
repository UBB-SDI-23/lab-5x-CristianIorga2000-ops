import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthorsView from '../views/AuthorsView.vue'
import AuthorDetails from '../views/AuthorDetails.vue'
import AddAuthor from '../views/AddAuthor.vue'
import StatisticsView from '../views/StatisticsView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomeView
  },
  {
    path: '/authors',
    name: 'Authors',
    component: AuthorsView
  },
  {
    path: '/authors/add',
    name: 'AddAuthor',
    component: AddAuthor
  },
  {
    path: '/authors/:id',
    name: 'AuthorDetails',
    component: AuthorDetails,
    props: true
  },
  {
    path: '/statistics',
    name: 'Statistics',
    component: StatisticsView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
