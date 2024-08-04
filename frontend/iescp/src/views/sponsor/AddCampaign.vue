<template>
  <SponsorNavbar />

  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" class="form-control" id="name" v-model="name" />
      </div>

      <div class="form-group">
        <label for="startDate">Start Date:</label>
        <input type="date" id="startDate" v-model="startDate" />
      </div>

      <div class="form-group">
        <label for="endDate">End Date:</label>
        <input type="date" id="endDate" v-model="endDate" />
      </div>

      <div class="form-group">
        <label for="budget">Budget:</label>
        <input type="number" class="form-control" id="budget" v-model="budget" />
      </div>

      <div v-for="(goal, index) in goals" :key="index" class="form-group">
        <label :for="'goal-' + index">Goal {{ index + 1 }}:</label>
        <input type="text" :id="'goal-' + index" v-model="goal.text" class="form-control" />
      </div>

      <div class="form-group">
        <button type="button" class="btn btn-success" @click="addGoal">
          <i class="bi bi-plus-circle"></i> Add New Goal
        </button>
      </div>

      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue'
import { mapGetters } from 'vuex'

export default {
  components: {
    SponsorNavbar
  },
  data() {
    return {
      name: '',
      startDate: '',
      endDate: '',
      budget: '',
      goals: [], 
    }
  },
  computed: {
    ...mapGetters(['sponsorID', 'campaignID'])
  },
  methods: {
    addGoal() {
      this.goals.push({ text: '' }) 
    },
    async submitForm() {
      if (this.goals.some(goal => goal.text.trim() === '')) {
        alert('Please fill in all goal fields before submitting.')
        return
      }

      const formattedStartDate = new Date(this.startDate).toISOString()
      const formattedEndDate = new Date(this.endDate).toISOString()

      const formData = {
        name: this.name,
        start_date: formattedStartDate,
        end_date: formattedEndDate,
        budget: this.budget,
        sponsor_id: this.sponsorID
      }

      try {
        const campaignResponse = await fetch(`http://localhost:8085/api/campaign`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        })

        if (campaignResponse.ok) {
          const campaignData = await campaignResponse.json()
          console.log('Campaign created:', campaignData)

          const campaignID = campaignData.id 

          await this.submitGoals(campaignID)

          this.$router.push('/sponsor/dashboard')
        } else {
          console.error('Campaign request failed with status:', campaignResponse.status)
        }
      } catch (error) {
        console.error('Campaign request failed:', error)
      }
    },
    async submitGoals(campaignID) {
      console.log('Submitting goals:', this.goals) 

      for (const goal of this.goals) {
        const goalData = {
          campaign_id: campaignID,
          goal: goal.text
        }

        console.log('Submitting goal:', goalData) 

        try {
          const goalResponse = await fetch(`http://localhost:8085/api/goal`, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(goalData)
          })

          if (goalResponse.ok) {
            const goalResponseData = await goalResponse.json()
            console.log('Goal created:', goalResponseData)
          } else {
            console.error('Goal request failed with status:', goalResponse.status)
          }
        } catch (goalError) {
          console.error('Goal request failed:', goalError)
        }
      }
    }
  }
}
</script>

<style scoped>
.container {
  margin-top: 20px;
}

.form-group {
  margin-bottom: 20px;
}

i {
  color: black;
  margin-right: 15px;
}
</style>
