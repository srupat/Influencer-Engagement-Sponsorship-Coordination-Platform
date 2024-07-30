<template>
    <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Admin Dashboard</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <router-link class="nav-link" to="/admin/dashboard">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/users">Users</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/about">About</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/contact">Contact</router-link>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#" @click.prevent="logout">Logout</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'AdminNavbar',
    methods: {
        async logout() {
            try {
                const response = await fetch('http://localhost:8085/auth/logout', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });

                if (response.ok) {
                    this.$router.push('/login');
                } else {
                    console.error('Logout failed:', response.statusText);
                }
            } catch (error) {
                console.error('Logout failed:', error);
            }
        }
    }
};
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
</style>
