<template>
  <div>
    <h4>Active Campaigns</h4>
    <div v-for="campaign in campaigns" :key="campaign.id" class="campaign-component">
      <div class="horizontal-component">
        <div class="message">{{ campaign.name }}</div>
        <div
          class="progress"
          role="progressbar"
          aria-label="Basic example"
          aria-valuenow="25"
          aria-valuemin="0"
          aria-valuemax="100"
        >
          <div class="progress-bar" style="width: 25%">25%</div>
        </div>
        <button type="button" class="btn btn-info" @click="goToAdRequestsPage(campaign.id)">
          <i class="bi bi-badge-ad"></i>
        </button>
        <button class="btn btn-success" @click="toggleViewCampaign(campaign.id)">View</button>
        <button class="btn btn-warning" @click="EditCampaign(campaign.id)">Edit</button>
        <button class="btn btn-danger" @click="removeCampaign(campaign.id)">Delete</button>
      </div>
      <div v-if="selectedCampaign === campaign.id" class="campaign-details">
        <p><strong>Start Date:</strong> {{ campaign.start_date }}</p>
        <p><strong>End Date:</strong> {{ campaign.end_date }}</p>
        <p><strong>Budget:</strong> {{ campaign.budget }}</p>
        <p><strong>Status:</strong> {{ campaign.isPublic ? 'Public' : 'Private' }}</p>
        <button class="btn btn-secondary" @click="makePublic(campaign.id)">Make Campaign Public</button>
      </div>
    </div>
    <h4>Requests</h4>
    <div v-for="request in requests" :key="request.id" class="campaign-component">
      <div class="horizontal-component">
        <div class="message">{{ request.name }}</div>
        <button class="btn btn-info" @click="toggleViewRequest(request.id)">Influencer Info</button>
        <button class="btn btn-success" @click="acceptRequest(request.id)">Accept</button>
        <button class="btn btn-danger" @click="rejectRequest(request.id)">Reject</button>
      </div>
      <div v-if="selectedRequest === request.id" class="campaign-details">
        <p><strong>Name:</strong> {{ influencer.name }}</p>
        <p><strong>Category:</strong> {{ influencer.category }}</p>
        <p><strong>Niche:</strong> {{ influencer.niche }}</p>
        <p><strong>Followers:</strong> {{ influencer.followers }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
  data() {
    return {
      campaigns: [],
      selectedCampaign: null,
      requests: [],
      selectedRequest: null,
      influencer: null
    }
  },
  async mounted() {
    await this.fetchCampaigns()
    this.fetchRequests()
  },
  computed: {
    ...mapGetters(['sponsorID'])
  },
  methods: {
    ...mapActions(['setCampaignID']),
    async fetchCampaigns() {
      const sponsorID = this.sponsorID
      console.log(this.$store.state.sponsorID)
      if (!sponsorID) {
        console.error('Sponsor ID is not set')
        return
      }
      try {
        const response = await fetch(`http://localhost:8085/api/campaign/sponsor/${sponsorID}`, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`)
        }
        const data = await response.json()
        console.log(data)
        this.campaigns = data.map((item) => ({
          id: item.id,
          name: item.name,
          start_date: item.start_date,
          end_date: item.end_date,
          budget: item.budget,
          isPublic: item.is_public,
          isFlagged: item.is_flagged
        }))
      } catch (error) {
        console.error('Error:', error)
      }
    },
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
          influencer_id: item.influencer_id,
          campaign_id: item.campaign_id
        }))

        const campaignIDs = this.campaigns.map((campaign) => campaign.id)
        console.log(this.requests)
        console.log(campaignIDs)
        this.requests = this.requests.filter(
          (request) => campaignIDs.includes(request.campaign_id) && request.isPending && request.influencer_id
        )

        console.log(this.requests)
      } catch (error) {
        console.error('Error:', error)
      }
    },
    toggleViewCampaign(id) {
      this.selectedCampaign = this.selectedCampaign === id ? null : id
    },
    EditCampaign(id) {
      this.setCampaignID(id)
      this.$router.push('/edit/campaign')
    },
    async removeCampaign(id) {
      try {
        const response = await fetch(`http://localhost:8085/api/campaign/${id}`, {
          method: 'DELETE'
        })
        if (response.ok) {
          this.fetchCampaigns()
        } else {
          console.error('Error:', response.statusText)
        }
      } catch (error) {
        console.error('Error:', error)
      }
    },
    goToAdRequestsPage(id) {
      this.setCampaignID(id)
      this.$router.push('/sponsor/ad-requests')
    },
    async makePublic(id) {
      const response = await fetch(`http://localhost:8085/campaign/public/${id}`, {
        method: 'PUT'
      })
      if (response.ok) {
        this.fetchCampaigns()
      } else {
        console.error('Error:', response.statusText)
      }
    },
    async toggleViewRequest(id) {
      if (this.selectedRequest === id) {
        this.selectedRequest = null
        this.influencer = null
      } else {
        this.selectedRequest = id
        const request = this.requests.find((req) => req.id === id)
        if (request) {
          const influencerID = request.influencer_id
          try {
            const response = await fetch(`http://localhost:8085/api/influencer/${influencerID}`)
            if (response.ok) {
              const data = await response.json()
              this.influencer = data
            } else {
              console.error(`Failed to fetch influencer: ${response.statusText}`)
              this.influencer = null
            }
          } catch (error) {
            console.error('Error:', error)
            this.influencer = null
          }
        }
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

.progress {
  width: 150px;
  height: 20px;
  background-color: #e9ecef;
  border-radius: 10px;
  overflow: hidden;
  margin-left: 10px;
  margin-right: 10px;
}

.progress-bar {
  height: 100%;
  background-color: #2c28a7;
  transition: width 0.6s ease;
}

.btn-success,
.btn-warning,
.btn-danger {
  margin-left: 10px;
}

h4 {
  margin-top: 30px;
  margin-bottom: 30px;
  color: #40e0d0;
}

i {
  color: black;
}
</style>
