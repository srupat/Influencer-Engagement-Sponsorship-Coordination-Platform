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
                        <router-link class="nav-link" to="/admin/users">Users</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/about">About</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/contact">Contact</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link" to="/logout">Logout</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
</template>

<script>
export default {
    name: 'AdminNavbar'
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
