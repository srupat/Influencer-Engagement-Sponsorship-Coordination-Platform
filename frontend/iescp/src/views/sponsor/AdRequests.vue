<template>
  <div>
    <SponsorNavbar />
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <h1>Ad Requests</h1>
          <button class="btn btn-success" @click="toggleNewAdRequest">
            <i class="bi bi-plus-circle"></i>Add Ad Request
          </button>
          <NewAdRequest v-if="flag" @formSubmitted="handleFormSubmitted" />
          <div class="user-list">
            <div v-for="request in requests" :key="request.id" class="user-card">
              <div class="user-info">
                <p class="username">{{ request.description }}</p>
                <p class="role">{{ request.requirements }}</p>
                <p class="email">{{ request.payment_amount }}</p>
              </div>
              <div class="options">
                <button class="btn btn-warning" @click="toggleNewEditAdRequest">Edit</button>
                <button class="btn btn-danger" @click="DeleteRequest(request.id)">Delete</button>
              </div>
              <EditRequest v-if="Editflag" @editFormSubmitted="handleEditFormSubmitted" :RequestID="request.id"/>
            </div>
            <div v-if="!requests.length" class="text-center">
              <p>No requests found.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import NewAdRequest from '@/components/sponsor/NewAdRequest.vue'
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue'
import EditRequest from '@/components/sponsor/EditRequest.vue';
import { mapGetters } from 'vuex'

export default {
  components: {
    SponsorNavbar,
    NewAdRequest, 
    EditRequest
  },
  data() {
    return {
      requests: [],
      flag: false,
      Editflag: false
    }
  },
  computed: {
    ...mapGetters(['campaignID'])
  },
  async mounted() {
    this.fetchRequests()
  },
  methods: {
    async fetchRequests() {
      try {
        const response = await fetch(
          `http://localhost:8085/api/campaign/request/${this.campaignID}`
        )
        if (response.ok) {
          this.requests = await response.json()
        } else {
          console.error('Failed to fetch requests:', response.statusText)
        }
      } catch (error) {
        console.error('Error fetching requests:', error)
      }
    },
    toggleNewAdRequest() {
      this.flag = !this.flag
    },
    toggleNewEditAdRequest() {
      this.Editflag = !this.Editflag
    },
    handleFormSubmitted() {
      this.toggleNewAdRequest()
      this.fetchRequests() 
    },
    handleEditFormSubmitted() {
      this.toggleNewEditAdRequest()
      this.fetchRequests()
    },
  //   },
  //   async EditRequest(id) {
      
  // },
  async DeleteRequest(id) {
    try {
      const response = await fetch(
        `http://localhost:8085/api/ad_request/${id}`,
        {
          method: 'DELETE'
        }
      )
      if (response.ok) {
        this.fetchRequests()
      } else {
        console.error('Failed to delete request:', response.statusText)
      }
    } catch (error) {
      console.error('Error deleting request:', error)
    }
  }
}
}
</script>

<style scoped>
.btn-success,
h1 {
  margin-top: 20px;
}

i {
  color: black;
  margin-right: 15px;
}

.user-list {
  padding: 20px;
}

.user-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  margin-bottom: 15px;
  padding: 15px;
  display: flex;
  flex-direction: column;
}

.user-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.username {
  font-size: 1.25rem;
  font-weight: bold;
  color: #333;
  margin: 0;
}

.role {
  font-size: 1rem;
  color: #007bff;
  margin: 5px 0;
}

.email {
  font-size: 0.875rem;
  color: #666;
}

.options {
  display: flex;
  justify-content: space-between;
  margin-top: 10px;
}
</style>
