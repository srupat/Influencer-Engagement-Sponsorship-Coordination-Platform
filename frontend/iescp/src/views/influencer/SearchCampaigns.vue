<template>
  <div>
    <InfluencerNavbar />

    <div class="container mt-3">
      <div class="row">
        <div class="col">
          <input
            type="text"
            class="form-control"
            placeholder="Search Campaigns"
            v-model="searchText"
          />
        </div>
      </div>

      <div class="row mt-3">
        <div class="col-12">
          <div
            v-for="campaign in filteredCampaigns"
            :key="campaign.id"
            class="card mb-2 campaign-card"
          >
            <div class="card-body">
              <h5 class="card-title">{{ campaign.name }}</h5>
              <p class="card-text">Start Date: {{ campaign.start_date }}</p>
              <p class="card-text">End Date: {{ campaign.end_date }}</p>
              <p class="card-text">Budget: {{ campaign.budget }}</p>
              <button class="btn btn-primary" @click="viewAdRequests(campaign.id)">
                View Ad Requests
              </button>
            </div>
            <div v-if="adRequests[campaign.id]">
              <div
                v-for="request in adRequests[campaign.id]"
                :key="request.id"
                class="card mt-2 ad-request-card"
              >
                <div class="card-body">
                  <h6 class="card-title">{{ request.name }}</h6>
                  <p class="card-text">{{ request.description }}</p>
                  <p class="card-text">Requirements: {{ request.requirements }}</p>
                  <p class="card-text">Payment Amount: {{ request.payment_amount }}</p>
                  <button class="btn btn-success" @click="requestRequest(request.id)">
                    Request
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import InfluencerNavbar from '@/components/influencer/InfluencerNavbar.vue'
import { mapActions, mapGetters } from 'vuex'

export default {
  components: {
    InfluencerNavbar
  },
  data() {
    return {
      campaigns: [],
      searchText: '',
      adRequests: {}
    }
  },
  computed: {
    filteredCampaigns() {
      return this.campaigns.filter((campaign) => {
        const matchesName = campaign.name.toLowerCase().includes(this.searchText.toLowerCase())
        const isPublicAndNonFlagged = campaign.is_public && !campaign.is_flagged
        return matchesName && isPublicAndNonFlagged
      })
    },
    ...mapGetters(['influencerID']),
    ...mapGetters(['campaignID']),
  },
  created() {
    this.fetchCampaigns()
  },
  methods: {
    ...mapActions(['setCampaignID']),
    async fetchCampaigns() {
      try {
        const response = await fetch('http://localhost:8085/api/campaign')
        const data = await response.json()
        this.campaigns = data
      } catch (error) {
        console.error('Error fetching campaigns:', error)
      }
    },
    async viewAdRequests(campaignID) {
      this.setCampaignID(campaignID)
      try {
        const response = await fetch(`http://localhost:8085/api/campaign/request/${campaignID}`)
        const data = await response.json()
        this.adRequests = {
          ...this.adRequests,
          [campaignID]: data.filter((request) => request.is_pending && !request.is_completed)
        }
      } catch (error) {
        console.error('Error fetching ad requests:', error)
      }
    },
    async requestRequest(id) {
      try {
        const response = await fetch(`http://localhost:8085/request/${id}/${this.influencerID}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          }
        })
        if(response.ok){
            await this.viewAdRequests(this.campaignID)
        }
      } catch (error) {
        console.error('Error requesting request:', error)
      }
    }
  }
}
</script>

<style scoped>
.campaign-card {
  background-color: white;
  color: #333;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.ad-request-card {
  background-color: white;
  color: #555;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.card-title {
  font-weight: bold;
}
.card-text {
  margin: 0;
}
</style>
