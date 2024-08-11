<template>
  <div class="admin-stats">
    <AdminNavbar />

    <div class="charts-container">
      <div class="chart-item">
        <RolesPieChart />
      </div>
      <div class="chart-item">
        <SponsorBudgetChart />
      </div>
      <div class="chart-item">
        <InfluencerCategoriesChart />
      </div>
      <div class="chart-item">
        <SponsorIndustryChart />
      </div>
      <div class="chart-item">
        <InfluencerFollowersChart />
      </div>
    </div>
  </div>
</template>

<script>
import AdminNavbar from '@/components/admin/AdminNavbar.vue'
import InfluencerCategoriesChart from '@/components/admin/InfluencerCategoriesChart.vue'
import SponsorIndustryChart from '@/components/admin/SponsorIndustryChart.vue'
import InfluencerFollowersChart from '@/components/admin/InfluencerFollowersChart.vue'
import RolesPieChart from '@/components/admin/RolesPieChart.vue'
import SponsorBudgetChart from '@/components/admin/SponsorBudgetChart.vue'

export default {
  name: 'AdminStats',
  components: {
    AdminNavbar,
    InfluencerCategoriesChart,
    SponsorIndustryChart,
    InfluencerFollowersChart,
    RolesPieChart,
    SponsorBudgetChart
  }
}
</script>

<style scoped>
.admin-stats {
  display: flex;
  flex-direction: column;
  padding: 20px;
}

.charts-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.chart-item {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}
</style>
