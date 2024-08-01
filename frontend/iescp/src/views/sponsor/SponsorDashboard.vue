<template>
    <div>
        <SponsorNavbar />
        <div class="container">
            <div class="row mt-5">
                <div class="col-12 text-center">
                    <h2 class="welcome">Hello, Sponsor!</h2>
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
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue';
import ViewCampaign from '@/components/admin/ViewCampaign.vue';

export default {
    components: {
        SponsorNavbar,
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
