<template>
  <nav class="navbar navbar-expand-lg navbar-light rounded">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">Sponsor Dashboard</a>
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/sponsor/dashboard"
              ><i class="bi bi-house"></i
            ></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/about"
              ><i class="bi bi-question-circle-fill"></i
            ></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/sponsor/stats"
              ><i class="bi bi-bar-chart-line"></i
            ></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/search/influencers"
              ><i class="bi bi-search"></i
            ></router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/contact"
              ><i class="bi bi-telephone"></i
            ></router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/logout" @click.prevent="logout"
              ><i class="bi bi-box-arrow-right"></i
            ></a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'SponsorNavbar',
  data() {
    return {
      Logout: 'Logout'
    }
  },
  methods: {
    async logout() {
      try {
        const response = await fetch('http://localhost:8085/auth/logout', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          credentials: 'include'
        })

        if (response.ok) {
          this.$router.push('/login')
        } else {
          console.error('Logout failed:', response.statusText)
        }
      } catch (error) {
        console.error('Logout failed:', error)
      }
    }
  }
}
</script>

<style scoped>
.navbar {
  background-color: #cce7ff;
  margin-bottom: 10px;
}

.navbar-brand {
  font-weight: bold;
}

.navbar-nav .nav-link {
  margin-right: 10px;
  color: #5340e0;
  text-decoration: none;
  font-weight: bold;
}

.container-fluid {
  border-radius: 8px;
}

i {
  color: black;
}
</style>
