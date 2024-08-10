<template>
    <div>
      <SponsorNavbar />
      <div v-if="filteredGoals.length">
        <ul class="list-group">
          <li v-for="goal in filteredGoals" :key="goal.id" class="list-group-item d-flex justify-content-between align-items-center">
            <div class="d-flex align-items-center">
              <input type="checkbox" class="form-check-input me-2" @change="markGoalComplete(goal.id)" />
              <span>{{ goal.goal }}</span>
            </div>
          </li>
        </ul>
      </div>
      <div v-else>
        <p>No pending goals</p>
      </div>
    </div>
  </template>
  
  <script>
  import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue'
  import { mapGetters } from 'vuex'
  
  export default {
    components: {
      SponsorNavbar
    },
    computed: {
      ...mapGetters(['campaignID']),
      filteredGoals() {
        return this.campaignGoals.filter(goal => goal.is_completed === 0)
      }
    },
    data () {
      return {
        campaignGoals: []
      }
    },
    mounted() {
      this.fetchCampaignGoals()
    },
    methods: {
      async fetchCampaignGoals() {
        try {
          const response = await fetch(`http://localhost:8085/api/goal/${this.campaignID}`)
          if (response.ok) {
            this.campaignGoals = await response.json()
          } else {
            console.error('Error:', response.statusText)
          }
        } catch (error) {
          console.error('Error fetching campaign goals:', error)
        }
      },
      async markGoalComplete(id) {
        try {
          const response = await fetch(`http://localhost:8085/campaign/complete/${id}`, {
            method: 'PUT'
          })
          if (response.ok) {
            this.fetchCampaignGoals() 
          } else {
            console.error('Error:', response.statusText)
          }
        } catch (error) {
          console.error('Error marking goal as complete:', error)
        }
      }
    }
  }
  </script>
  
  <style scoped>
  .list-group-item {
    background-color: #f8f9fa;
    border: 1px solid #dee2e6;
    margin-bottom: 10px;
  }
  
  .form-check-input {
    accent-color: #007bff; 
  }
  
  .d-flex {
    align-items: center;
  }
  
  .me-2 {
    margin-right: 8px;
  }
  </style>
  