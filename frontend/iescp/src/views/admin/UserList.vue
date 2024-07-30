<template>
    <div>
        <AdminNavbar />
        <div class="container user-list">
            <h1 class="text-center">Users</h1>
            <div v-if="loading" class="text-center">
                <p>Loading...</p>
            </div>
            <div v-else>
                <div v-for="user in users" :key="user.id" class="user-card">
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
import AdminNavbar from '@/components/admin/AdminNavbar.vue';

export default {
    components: {
        AdminNavbar
    },
    data() {
        return {
            users: [],
            loading: true
        };
    },
    async created() {
        try {
            const response = await fetch('http://localhost:8085/api/user');
            if (response.ok) {
                this.users = await response.json();
            } else {
                console.error('Failed to fetch users:', response.statusText);
            }
        } catch (error) {
            console.error('Error fetching users:', error);
        } finally {
            this.loading = false;
        }
    }
};
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
</style>
