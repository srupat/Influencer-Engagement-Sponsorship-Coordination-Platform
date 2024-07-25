<template>
    <nav class="navbar">
        <!-- <router-link to="/admin/home">Home</router-link> -->
        <router-link to="/admin/users">Users</router-link>
        <router-link to="/about">About</router-link>
        <router-link to="/contact">Contact</router-link>
        <router-link to="/logout">Logout</router-link>
    </nav>
    <div>
        <h2 class="welcome">{{ message }}</h2>
    </div>
    <ViewCampaign :message="msg" />
</template>

<script>
// use v-for for adding a for loop for each campaign that you fetch from the backend
import ViewCampaign from '@/components/admin/ViewCampaign.vue'
export default {
    data() {
        return {
            message: 'Welcome, admin',
            msg: 'Campaign 1'
        }
    }, 
    components: {
        ViewCampaign
    }
}
</script>

<style scoped>
.navbar {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    /* background-color: #f2f2f2; */
    padding: 10px;
}

.navbar a{
    margin-right: 10px;
    color: hsla(160, 100%, 37%, 1);
    text-decoration: none;
}

.welcome {
    text-align: center;
    color: rgb(0, 189, 170);
}
</style>
