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
  computed: {
    ...mapGetters(['sponsorID'])
  },
  methods: {
    async submitForm() {
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
        const response = await fetch(`http://localhost:8085/api/campaign`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        })

        if (response.ok) {
          const data = await response.json()
          console.log(data)
          this.$router.push('/sponsor/dashboard')
        } else {
          console.error('Request failed with status:', response.status)
        }
      } catch (error) {
        console.error('Request failed:', error)
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
</style>
