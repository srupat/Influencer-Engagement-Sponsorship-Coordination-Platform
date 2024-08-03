<template>
    <div>
        <SponsorNavbar />
        <div class="container">
            <div class="row mt-5">
                <div class="col-12 text-center">
                    <h2 class="welcome">Hello, Sponsor!</h2>
                </div>
            </div>
            <button class="btn btn-success" @click="AddCampaign()"><i class="bi bi-plus-circle"></i>Add Campaign</button>
            <div class="row mt-3">
                <div class="col-12">
                    <ViewSponsorCampaign />
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue';
import ViewSponsorCampaign from '@/components/sponsor/ViewSponsorCampaign.vue';

export default {
    components: {
        SponsorNavbar,
        ViewSponsorCampaign
    },
    methods: {
        AddCampaign() {
            this.$router.push('/add/campaign');
        }
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

i {
    color: black;
    margin-right: 15px;
}
</style>
