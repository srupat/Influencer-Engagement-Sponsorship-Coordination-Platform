<template>
  <div class="chart-wrapper">
    <h2>Influencers Data</h2>
    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'InfluencersFollowersChart',
  components: {
    Bar
  },
  data() {
    return {
      chartData: null,
      chartOptions: {
        responsive: true,
        plugins: {
          legend: {
            display: true,
            position: 'top'
          },
          tooltip: {
            callbacks: {
              label: function (context) {
                let label = context.label || ''
                if (context.parsed) {
                  label += `: ${context.parsed} followers`
                }
                return label
              }
            }
          }
        },
        scales: {
          x: {
            stacked: false
          },
          y: {
            stacked: false,
            beginAtZero: true
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

        this.chartData = {
          labels: data.map((influencer) => influencer.name),
          datasets: [
            {
              label: 'Followers',
              data: data.map((influencer) => influencer.followers),
              backgroundColor: '#42A5F5',
              borderColor: '#1E88E5',
              borderWidth: 1
            }
          ]
        }
      } catch (error) {
        console.error('Error fetching influencers data:', error)
      }
    }
  },
  mounted() {
    this.fetchInfluencersData()
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
