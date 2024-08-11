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
            <button class="btn btn-warning" @click="ExportAsCSV()"><i class="bi bi-box-arrow-up-right"></i>Export Campaign Data as CSV</button>
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
import { mapGetters } from 'vuex';

export default {
    components: {
        SponsorNavbar,
        ViewSponsorCampaign
    },
    computed: {
        ...mapGetters(['sponsorID'])
    },
    methods: {
        AddCampaign() {
            this.$router.push('/add/campaign');
        },
        async ExportAsCSV() {
            const sponsorID = this.sponsorID;
            const response = await fetch(`http://localhost:8085/export_csv/${sponsorID}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                }
            });
            if(response.ok){
                alert('Campaign data exported as CSV');
            }
        },
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

.btn {
    margin-right: 10px;
}
</style>
