<template>
  <div class="admin-stats">
    <InfluencerNavbar />

    <div class="charts-container">
      <div class="chart-item">
        <SponsorBudgetChart />
      </div>

      <div class="chart-item">
        <SponsorIndustryChart />
      </div>
    </div>
  </div>
</template>

<script>
import InfluencerNavbar from '@/components/influencer/InfluencerNavbar.vue'
import SponsorIndustryChart from '@/components/admin/SponsorIndustryChart.vue'
import SponsorBudgetChart from '@/components/admin/SponsorBudgetChart.vue'

export default {
  name: 'InfluencerStats',
  components: {
    InfluencerNavbar,
    SponsorIndustryChart,
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
