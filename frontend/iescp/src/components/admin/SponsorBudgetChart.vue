<template>
  <div class="chart-wrapper">
    <h2>Sponsor Budgets</h2>
    <Bar v-if="chartData" :data="chartData" :options="chartOptions" />
    <p v-else>Loading...</p>
  </div>
</template>

<script>
import { Bar } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'SponsorBudgetChart',
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
            position: 'top'
          },
          tooltip: {
            callbacks: {
              label: function(context) {
                let label = context.label || '';
                if (context.parsed.y !== undefined) {
                  label += `: $${context.parsed.y}`;
                }
                return label;
              }
            }
          }
        },
        scales: {
          x: {
            beginAtZero: true
          },
          y: {
            beginAtZero: true
          }
        }
      }
    }
  },
  methods: {
    async fetchSponsorData() {
      try {
        const response = await fetch('http://localhost:8085/api/sponsor');
        const sponsors = await response.json();
        this.chartData = {
          labels: sponsors.map(sponsor => sponsor.name),
          datasets: [{
            label: 'Budget',
            data: sponsors.map(sponsor => sponsor.budget),
            backgroundColor: '#42A5F5',
            borderColor: '#1E88E5',
            borderWidth: 1
          }]
        }
      } catch (error) {
        console.error('Error fetching sponsor data:', error);
      }
    }
  },
  mounted() {
    this.fetchSponsorData();
  }
}
</script>

<style scoped>
.chart-wrapper {
  width: 100%;
  height: 400px;
}

@media (max-width: 600px) {
  .chart-wrapper {
    height: 300px;
  }
}

h2 {
  color: black;
}
</style>
