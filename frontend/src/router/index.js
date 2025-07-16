// frontend/src/router/index.js

import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue' // 假设您有 About 页面

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  // 可以添加更多路由，例如登录页，域名列表页等
  // {
  //   path: '/domains',
  //   name: 'domains',
  //   component: () => import('../views/DomainListView.vue') // 懒加载
  // },
  // {
  //   path: '/login',
  //   name: 'login',
  //   component: () => import('../views/LoginView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL), // Vue 3 with Vite
  routes
})

export default router