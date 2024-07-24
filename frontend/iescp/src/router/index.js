import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'register-role',
    component: () => import('../views/auth/RegisterRole.vue')
  },
  {
    path: '/register',
    name: 'register',
    component: () => import('../views/auth/RegisterView.vue')
  },
  {
    path: '/login/role',
    name: 'login-role',
    component: () => import('../views/auth/LoginRole.vue')
  },
  {
    path: '/login',
    name: 'login',
    component: () => import('../views/auth/LoginView.vue')
  },
  {
    path: '/admin/dashboard',
    name: 'admin-home',
    component: () => import('../views/admin/AdminDashboard.vue')
  },
  {
    path: '/influencer/dashboard',
    name: 'influencer-home',
    component: () => import('../views/influencer/InfluencerDashboard.vue')
  },
  {
    path: '/sponosr/dashboard',
    name: 'sponsor-home',
    component: () => import('../views/sponsor/SponsorDashboard.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
