<template>
  <div class="register-role">
    <h1>Login As</h1>
    <div class="role-images">
      <div class="role-container">
        <router-link to="/login" class="role-login" @click="setRole('admin')">
          <RoleImage class="role-image" label="Admin" :imageUrl="adminImage" />
          <p>Admin</p>
        </router-link>
      </div>
      <div class="role-container">
        <router-link to="/login" class="role-login" @click="setRole('influencer')">
          <RoleImage class="role-image" label="Influencer" :imageUrl="influencerImage" />
          <p>Influencer</p>
        </router-link>
      </div>
      <div class="role-container">
        <router-link to="/login" class="role-login" @click="setRole('sponsor')">
          <RoleImage class="role-image" label="Sponsor" :imageUrl="sponsorImage" />
          <p>Sponsor</p>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import RoleImage from '@/components/login/RoleImage.vue'
import adminImage from '@/assets/admin.png'
import influencerImage from '@/assets/influencer.png'
import sponsorImage from '@/assets/sponsor.jpeg'

export default {
  name: 'RegisterRole',
  components: {
    RoleImage
  },
  data() {
    return {
      adminImage,
      influencerImage,
      sponsorImage
    }
  }
}
</script>

<style>
.register-role {
  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.role-images {
  display: flex;
  justify-content: space-around;
  width: 100%;
  margin-top: 20px;
}

.role-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 100px;
}

.role-image {
  margin-bottom: 10px;
}

.role-link {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-decoration: none;
  color: inherit;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}
</style>
