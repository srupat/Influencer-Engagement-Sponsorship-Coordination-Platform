<template>
  <div>
    <h2>Influencer Categories</h2>
    <pie-chart v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default {
  name: 'InfluencerCategoriesChart',
  components: {
    PieChart: Pie
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
                if (context.parsed !== null) {
                  label += `: ${context.parsed} influencers`
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
    async fetchInfluencersData() {
      try {
        const response = await fetch('http://localhost:8085/api/influencer')
        const data = await response.json()

        const categoryCounts = data.reduce((acc, influencer) => {
          acc[influencer.category] = (acc[influencer.category] || 0) + 1
          return acc
        }, {})

        this.chartData = {
          labels: Object.keys(categoryCounts),
          datasets: [
            {
              label: 'Categories',
              data: Object.values(categoryCounts),
              backgroundColor: this.generateColors(Object.keys(categoryCounts).length),
              borderColor: '#fff',
              borderWidth: 1
            }
          ]
        }
      } catch (error) {
        console.error('Error fetching influencers data:', error)
      }
    },
    generateColors(count) {
      const colors = [
        '#FF6384',
        '#36A2EB',
        '#FFCE56',
        '#4BC0C0',
        '#9966FF',
        '#FF9F40',
        '#FF6B6B',
        '#C4E538',
        '#8E44AD',
        '#2ECC71'
      ]
      return colors.slice(0, count)
    }
  },
  mounted() {
    this.fetchInfluencersData()
  }
}
</script>

<style scoped>
h2 {
  color: black;
}
</style>
