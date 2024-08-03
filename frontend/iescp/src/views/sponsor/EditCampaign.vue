<template>
    <div>
      <SponsorNavbar />
  
      <div class="container">
        <form @submit.prevent="submitForm">
          <div class="form-group">
            <label for="name">Name:</label>
            <input type="text" class="form-control" id="name" v-model="name">
          </div>
  
          <div class="form-group">
            <label for="startDate">Start Date:</label>
            <input type="date" id="startDate" v-model="startDate">
          </div>
  
          <div class="form-group">
            <label for="endDate">End Date:</label>
            <input type="date" id="endDate" v-model="endDate">
          </div>
  
          <div class="form-group">
            <label for="budget">Budget:</label>
            <input type="number" class="form-control" id="budget" v-model="budget">
          </div>
  
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </template>
  
  <script>
  import { mapGetters } from 'vuex';
  import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue'
  
  export default {
    components: {
        SponsorNavbar
    },
    data() {
      return {
        name: '',
        startDate: '',
        endDate: '',
        budget: 0
      };
    },
    computed: {
      ...mapGetters(['sponsorID', 'campaignID'])
    },
    methods: {
      async submitForm() {
        const formattedStartDate = new Date(this.startDate).toISOString();
        const formattedEndDate = new Date(this.endDate).toISOString();
  
        const formData = {
          name: this.name,
          start_date: formattedStartDate,
          end_date: formattedEndDate,
          budget: this.budget
        };
  
        try {
          const response = await fetch(`http://localhost:8085/api/campaign/${this.campaignID}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
          });
  
          if (response.ok) {
            const data = await response.json();
            console.log(data);
          } else {
            console.error('Request failed with status:', response.status);
          }
        } catch (error) {
          console.error('Request failed:', error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .container {
    margin-top: 20px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  </style>
  