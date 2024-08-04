<template>
  <div class="container">
    <form @submit.prevent="submitForm">
      <div class="form-group">
        <label for="desc">Description:</label>
        <input type="text" class="form-control" id="desc" v-model="desc" />
      </div>
      <div class="form-group">
        <label for="req">Requirements:</label>
        <input type="text" class="form-control" id="req" v-model="req" />
      </div>
      <div class="form-group">
        <label for="amount">Payment Amount:</label>
        <input type="number" class="form-control" id="amount" v-model="amount" />
      </div>
      <div class="form-group">
        <label for="influencer">Influencer:</label>
        <select class="form-control" id="influencer" v-model="selectedInfluencer">
          <option v-for="influencer in influencers" :key="influencer.id" :value="influencer.id">
            {{ influencer.name }}
          </option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">Submit</button>
    </form>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  props: {
    flag: {
      type: Boolean,
      required: true
    }
  },
  data() {
    return {
      desc: '',
      req: '',
      amount: '',
      influencers: [],
      selectedInfluencer: null
    }
  },
  computed: {
    ...mapGetters(['campaignID'])
  },
  async mounted() {
    this.fetchInfluencers()
  },
  methods: {
    async submitForm() {
      try {
        const requestBody = {
          description: this.desc,
          requirements: this.req,
          payment_amount: this.amount,
          campaign_id: this.campaignID,
          influencer_id: this.selectedInfluencer
        }
        console.log('Request Body:', requestBody)

        const response = await fetch('http://localhost:8085/api/ad_request', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(requestBody)
        })
        if (response.ok) {
          this.$emit('formSubmitted')
        } else {
          console.error('Failed to submit ad request:', response.statusText)
        }
      } catch (error) {
        console.error('Error submitting ad request:', error)
      }
    },
    async fetchInfluencers() {
      try {
        const response = await fetch('http://localhost:8085/api/influencer')
        if (response.ok) {
          this.influencers = await response.json()
        } else {
          console.error('Failed to fetch influencers:', response.statusText)
        }
      } catch (error) {
        console.error('Error fetching influencers:', error)
      }
    }
  }
}
</script>

<style scoped>
.form-group {
  margin-bottom: 20px;
}
</style>
