<template>
  <div>
    <h4>Ongoing Campaign Requests</h4>
    <div v-for="request in requests" :key="request.id" class="campaign-component">
      <div class="horizontal-component">
        <div class="message">{{ request.name }}</div>
        <button class="btn btn-info" @click="toggleViewRequest(request.id)">View</button>
      </div>
      <div v-if="selectedRequest === request.id" class="campaign-details">
        <p><strong>Descriptions:</strong> {{ request.description }}</p>
        <p><strong>Requirements:</strong> {{ request.requirements }}</p>
        <p><strong>Payment amount:</strong> {{ request.payment_amount }}</p>
      </div>
    </div>
    <h4>New Requests</h4>
    <div v-for="request in requestedRequests" :key="request.id" class="campaign-component">
      <div class="horizontal-component">
        <div class="message">{{ request.name }}</div>
        <button class="btn btn-info" @click="toggleViewRequest(request.id)">View</button>
        <button class="btn btn-success" @click="acceptRequest(request.id)">Accept</button>
        <button class="btn btn-danger" @click="rejectRequest(request.id)">Reject</button>
      </div>
      <div v-if="selectedRequest === request.id" class="campaign-details">
        <p><strong>Descriptions:</strong> {{ request.description }}</p>
        <p><strong>Requirements:</strong> {{ request.requirements }}</p>
        <p><strong>Payment amount:</strong> {{ request.payment_amount }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  data() {
    return {
      requests: [],
      requestedRequests: [],
      selectedRequest: null
    }
  },
  computed: {
    ...mapGetters(['influencerID'])
  },
  mounted() {
    this.fetchRequests()
  },
  methods: {
    async fetchRequests() {
      try {
        const response = await fetch('http://localhost:8085/api/ad_request')
        const data = await response.json()
        this.requests = data.map((item) => ({
          id: item.id,
          name: item.name,
          description: item.description,
          requirements: item.requirements,
          payment_amount: item.payment_amount,
          isPending: item.is_pending,
          influencer_id: item.influencer_id
        }))

        this.requestedRequests = this.requests.filter(
          (request) => request.isPending && request.influencer_id === this.influencerID
        )
        this.requests = this.requests.filter(
          (request) => !request.isPending && request.influencer_id === this.influencerID
        )

        console.log(this.requests);
        
      } catch (error) {
        console.error('Error:', error)
      }
    },
    async acceptRequest(id) {
      try {
        const response = await fetch(`http://localhost:8085/api/ad_request/accept/${id}`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            is_pending: 0
          })
        })
        if (response.ok) {
          this.fetchRequests()
        } else {
          console.error('Error:', response.statusText)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    async rejectRequest(id) {
      try {
        const response = await fetch(`http://localhost:8085/api/ad_request/reject/${id}`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({})
        })
        if (response.ok) {
          this.fetchRequests()
        } else {
          console.error('Error:', response.statusText)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    toggleViewRequest(id) {
      this.selectedRequest = this.selectedRequest === id ? null : id
    }
  }
}
</script>

<style scoped>
.campaign-component {
  margin-bottom: 20px;
}

.horizontal-component {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background-color: #cce7ff;
  padding: 10px;
  border-radius: 10px;
}

.message {
  flex: 1;
  color: #333;
  font-size: 20px;
  font-weight: bold;
}

.campaign-details {
  background-color: #fff;
  padding: 10px;
  border-radius: 5px;
  margin-top: 10px;
  border: 1px solid #cce7ff;
  color: #333;
  font-size: smaller;
}

.btn-success,
.btn-danger,
.btn-warning {
  margin-left: 10px;
}

h4 {
  margin-top: 30px;
  margin-bottom: 30px;
  color: #40e0d0;
}
</style>
