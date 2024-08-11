<template>
  <div class="admin-stats">
    <SponsorNavbar />

    <div class="charts-container">
      <div class="chart-item">
        <InfluencerCategoriesChart />
      </div>

      <div class="chart-item">
        <InfluencerFollowersChart />
      </div>
    </div>
  </div>
</template>

<script>
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue'
import InfluencerCategoriesChart from '@/components/admin/InfluencerCategoriesChart.vue'

import InfluencerFollowersChart from '@/components/admin/InfluencerFollowersChart.vue'

export default {
  name: 'SponsorStats',
  components: {
    SponsorNavbar,
    InfluencerCategoriesChart,

    InfluencerFollowersChart
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
