<template>
    <div>
        <AdminNavbar />
        <div class="container">
            <div class="row mt-5">
                <div class="col-12 text-center">
                    <h2 class="welcome">Hello, Admin!</h2>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-12">
                    <ViewCampaign />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import AdminNavbar from '@/components/admin/AdminNavbar.vue';
import ViewCampaign from '@/components/admin/ViewCampaign.vue';

export default {
    components: {
        AdminNavbar,
        ViewCampaign
    }
};
</script>

<style scoped>
.welcome {
    color: #40e0d0; 
    margin-bottom: 30px;
}

.container {
    max-width: 1200px;
}

.row {
    margin-bottom: 20px;
}
</style>
