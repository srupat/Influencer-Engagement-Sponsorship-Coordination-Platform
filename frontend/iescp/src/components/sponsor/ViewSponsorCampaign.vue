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
      selectedCampaign: null
    }
  },
  mounted() {
    this.fetchCampaigns()
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
