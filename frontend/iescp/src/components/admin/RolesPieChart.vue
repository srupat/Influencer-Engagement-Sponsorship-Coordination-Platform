<template>
  <div class="chart-wrapper">
    <h2>User Roles Distribution</h2>
    <Pie v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement)

export default {
  name: 'RolesPieChart',
  components: {
    Pie
  },
  data() {
    return {
      chartData: null,
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top'
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                let label = context.label || ''
                if (context.parsed) {
                  label += `: ${context.parsed} users`
                }
                return label
              }
            }
          }
        }
      }
    }
  },
  methods: {
    async fetchRoleData() {
      try {
        const response = await fetch('http://localhost:8085/roles')
        const data = await response.json()

        this.chartData = {
          labels: ['Admin', 'Sponsor', 'Influencer'],
          datasets: [
            {
              label: 'Number of Users',
              data: [data.Admins, data.Sponsors, data.Influencers],
              backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
              borderColor: '#fff',
              borderWidth: 1
            }
          ]
        }
      } catch (error) {
        console.error('Error fetching role data:', error)
      }
    }
  },
  mounted() {
    this.fetchRoleData()
  }
}
</script>

<style scoped>
.chart-wrapper {
  width: 100%;
  height: 400px;
}

h2 {
  color: black;
}

@media (max-width: 600px) {
  .chart-wrapper {
    height: 300px;
  }
}
</style>
