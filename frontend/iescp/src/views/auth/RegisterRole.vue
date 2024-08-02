<template>
  <nav>
    <router-link to="/">Register</router-link>
    <router-link to="/login/role">Login</router-link>
  </nav>
  <div class="register-role">
    <h1>Register As</h1>
    <div class="role-images">
      <div class="role-container">
        <div class="role-link" @click="selectRole('Admin')">
          <RoleImage class="role-image" label="Admin" :imageUrl="adminImage" />
          <p class="green">Admin</p>
        </div>
      </div>
      <div class="role-container">
        <div class="role-link" @click="selectRole('Influencer')">
          <RoleImage class="role-image" label="Influencer" :imageUrl="influencerImage" />
          <p class="green">Influencer</p>
        </div>
      </div>
      <div class="role-container">
        <div class="role-link" @click="selectRole('Sponsor')">
          <RoleImage class="role-image" label="Sponsor" :imageUrl="sponsorImage" />
          <p class="green">Sponsor</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import RoleImage from '@/components/auth/RoleImage.vue'
import adminImage from '@/assets/admin.png'
import influencerImage from '@/assets/influencer.png'
import sponsorImage from '@/assets/sponsor.jpeg'
import { mapActions, mapGetters } from 'vuex'

export default {
  name: 'RegisterRole',
  components: {
    RoleImage
  },
  computed: {
    ...mapGetters(['role'])
  },
  data() {
    return {
      adminImage,
      influencerImage,
      sponsorImage
    }
  },
  methods: {
    ...mapActions(['setRole']),
    selectRole(role) {
      this.setRole(role)
      // console.log(this.$store.state.role);
      if (this.role === 'Admin') {
        this.$router.push('/admin/register')
      } else if (this.role === 'Sponsor') {
        this.$router.push('/sponsor/register')
      } else {
        this.$router.push('/influencer/register')
      }
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
  cursor: pointer;
}

.role-link:hover {
  background-color: hsla(160, 100%, 37%, 0.2); /* Optional: change to the hover effect you want */
}

p {
  font-size: 24px;
  margin-bottom: 20px;
}
</style>
