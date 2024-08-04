<template>
  <div>
    <AdminNavbar />
    <div class="newnav">
      <nav class="navbar bg-body-tertiary rounded bg-dark">
        <div class="container-fluid">
          <form class="d-flex justify-content-end align-items-center" role="search">
            <input
              class="form-control me-2"
              type="search"
              placeholder="Search"
              aria-label="Search"
              v-model="search"
            />
            <!-- <button class="btn btn-outline-success" type="submit">Search</button> -->
          </form>
        </div>
      </nav>
    </div>
    <div class="container user-list">
      <h4 class="text-center">Users</h4>
      <div>
        <div v-for="user in filteredUsers" :key="user.id" class="user-card">
          <div class="user-info">
            <h3 class="username">{{ user.username }}</h3>
            <p class="role">{{ user.role }}</p>
            <p class="email">{{ user.email }}</p>
          </div>
        </div>
        <div v-if="!users.length" class="text-center">
          <p>No users found.</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import AdminNavbar from '@/components/admin/AdminNavbar.vue'

export default {
  components: {
    AdminNavbar
  },
  data() {
    return {
      users: [],
      search: ''
    }
  },
  async created() {
    try {
      const response = await fetch('http://localhost:8085/api/user')
      if (response.ok) {
        this.users = await response.json()
      } else {
        console.error('Failed to fetch users:', response.statusText)
      }
    } catch (error) {
      console.error('Error fetching users:', error)
    }
  },
  computed: {
    filteredUsers() {
      return this.users.filter((user) => {
        return user.username.toLowerCase().includes(this.search.toLowerCase())
      })
    }
  }
}
</script>

<style scoped>
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

.text-center {
  text-align: center;
  color: #40e0d0;
}

.newnav {
  display: flex;
  justify-content: flex-start;
  align-items: flex-end;
  flex-direction: row;
  width: 200px;
}
</style>
