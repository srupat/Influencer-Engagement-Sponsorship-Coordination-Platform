<template>
  <div class="container mt-3">
    <div class="row">
      <div class="col-md-4">
        <h5>Select Profile Picture</h5>
        <input type="file" @change="onFileChange" class="form-control" />
        <div class="mt-3 text-center">
          <img
            v-if="profileImage"
            :src="profileImage"
            alt="Profile Picture"
            class="img-thumbnail profile-pic"
          />
        </div>
        <div class="info mt-3">
          <h5>Profile Information</h5>
          <div v-if="influencer">
            <p><strong>Name:</strong> {{ influencer.name }}</p>
            <p><strong>Category:</strong> {{ influencer.category }}</p>
            <p><strong>Niche:</strong> {{ influencer.niche }}</p>
            <p><strong>Followers:</strong> {{ influencer.followers }}</p>
          </div>
          <p v-else>Loading...</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';

export default {
  data() {
    return {
      profileImage: null,
      influencer: null,
    };
  },
  computed: {
    ...mapGetters(['influencerID']),
  },
  async mounted() {
    try {
      const response = await fetch(
        `http://localhost:8085/api/influencer/${this.influencerID}`
      );
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      this.influencer = await response.json();
    } catch (error) {
      console.error('There was a problem with the fetch operation:', error);
    }
  },
  methods: {
    onFileChange(event) {
      const file = event.target.files[0];
      if (file) {
        this.profileImage = URL.createObjectURL(file);
      }
    },
  },
};
</script>

<style scoped>
.profile-pic {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
}

.info {
  background-color: #343a40; 
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
  margin-top: 10px;
  color: #ffffff; 
}

.info p {
  font-size: 14px;
  margin: 5px 0;
}

.info strong {
  color: #ffffff; 
}
</style>
