import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'register-role',
    component: () => import('../views/auth/RegisterRole.vue')
  },
  {
    path: '/admin/register',
    name: 'admin-register',
    component: () => import('../views/auth/RegisterAdminView.vue')
  },
  {
    path: '/sponsor/register',
    name: 'sponsor-register',
    component: () => import('../views/auth/RegisterSponsorView.vue')
  },
  {
    path: '/influencer/register',
    name: 'influencer-register',
    component: () => import('../views/auth/RegisterInfluencerView.vue')
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
    path: '/sponsor/dashboard',
    name: 'sponsor-home',
    component: () => import('../views/sponsor/SponsorDashboard.vue')
  },
  {
    path: '/about/admin',
    name: 'about',
    component: () => import('../views/admin/AdminAboutComponent.vue')
  },
  {
    path: '/about/sponsor',
    name: 'about-sponsor',
    component: () => import('../views/sponsor/SponsorAboutComponent.vue')
  },
  {
    path: '/about/influencer',
    name: 'about-influencer',
    component: () => import('../views/influencer/InfluencerAboutComponent.vue')
  },
  {
    path: '/contact',
    name: 'contact',
    component: () => import('../views/common/ContactComponent.vue')
  },
  {
    path: '/users',
    name: 'users',
    component: () => import('../views/admin/UserList.vue')
  },
  {
    path: '/add/campaign',
    name: 'add-campaign',
    component: () => import('../views/sponsor/AddCampaign.vue')
  },
  {
    path: '/edit/campaign',
    name: 'edit-campaign',
    component: () => import('../views/sponsor/EditCampaign.vue')
  },
  {
    path: '/sponsor/ad-requests',
    name: 'ad-requests',
    component: () => import('../views/sponsor/AdRequests.vue')
  },
  {
    path: '/search/influencers',
    name: 'search-influencer',
    component: () => import('../views/sponsor/SearchInfluencer.vue')
  },
  {
    path: '/search/campaigns',
    name: 'search-campaigns',
    component: () => import('../views/influencer/SearchCampaigns.vue')
  },
  {
    path: '/campaign/goals',
    name: 'campaign-goals',
    component: () => import('../views/sponsor/CampaignGoals.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
