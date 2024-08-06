<template>
  <div>
    <InfluencerNavbar />
    <div class="profile-requests-container">
      <ProfileInfo />
      <ViewInfluencerRequests />
    </div>
  </div>
</template>

<script>
import InfluencerNavbar from '@/components/influencer/InfluencerNavbar.vue'
import ProfileInfo from '@/components/influencer/ProfileInfo.vue';
import ViewInfluencerRequests from '@/components/influencer/ViewInfluencerRequests.vue';

export default {
  components: {
    InfluencerNavbar,
    ProfileInfo, 
    ViewInfluencerRequests
  }
}
</script>

<style scoped>
.profile-requests-container {
  display: grid;
  grid-template-columns: auto auto;
  gap: 0px; 
  margin: 0; 
  padding: 0; 
}

.ProfileInfo, .ViewInfluencerRequests {
  margin: 0; 
  padding: 0; 
}

.ViewInfluencerRequests {
  width: 100%; 
  min-width: 300px; 
}
</style>
