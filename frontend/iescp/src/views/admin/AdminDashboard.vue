<template>
    <nav>
        <router-link to="/admin/home">Home</router-link>
        <router-link to="/admin/users">Users</router-link>
        <router-link to="/about">About</router-link>

    </nav>
    <div>
        <h1>{{ message }}</h1>
    </div>
</template>

<script>
export default {
    data() {
        return {
            message: 'Hello admin'
        }
    }
}
</script>

<style scoped>
h1 {
    color: blue;
}
</style>