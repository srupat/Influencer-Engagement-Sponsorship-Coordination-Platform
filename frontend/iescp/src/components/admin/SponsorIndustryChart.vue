<template>
  <div class="chart-wrapper">
    <h2>Sponsor Industries</h2>
    <Pie v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { Pie } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

export default {
  name: 'SponsorIndustryChart',
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
                  label += `: ${context.parsed.toFixed(0)} sponsors`
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
    async fetchSponsorData() {
      try {
        const response = await fetch('http://localhost:8085/api/sponsor')
        const sponsors = await response.json()

        const industryCounts = sponsors.reduce((acc, sponsor) => {
          if (acc[sponsor.industry]) {
            acc[sponsor.industry]++
          } else {
            acc[sponsor.industry] = 1
          }
          return acc
        }, {})

        this.chartData = {
          labels: Object.keys(industryCounts),
          datasets: [
            {
              label: 'Industries',
              data: Object.values(industryCounts),
              backgroundColor: this.generateColors(Object.keys(industryCounts).length),
              borderColor: '#fff',
              borderWidth: 1
            }
          ]
        }
      } catch (error) {
        console.error('Error fetching sponsor data:', error)
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
    this.fetchSponsorData()
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
