<template>
    <h4>Ongoing Campaigns</h4>
    <div v-for="campaign in campaigns" :key="campaign.id" class="horizontal-component">
        <div class="message">{{ campaign.name }}</div>
        <button class="btn btn-success">View</button>
    </div>
    <h4>Flagged Campaigns</h4>
    <div v-for="campaign in flaggedCampaigns" :key="campaign.id" class="horizontal-component">
        <div class="message">{{ campaign.name }}</div>
        <button class="btn btn-success">View</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            campaigns: [],
            flaggedCampaigns: []
        }
    },
    mounted() {
        this.fetchCampaigns();
    },
    methods: {
        async fetchCampaigns() {
            try {
                const response = await fetch('http://localhost:8085/api/campaign');
                const data = await response.json();
                console.log(data);
                this.campaigns = data.map(item => ({
                    id: item.id,
                    name: item.name,
                    start_date: item.start_date,
                    end_date: item.end_date,
                    budget: item.budget,
                    isPublic: item.is_public,
                    isFlagged: item.is_flagged
                }));
                
                this.flaggedCampaigns = this.campaigns.filter(campaign => campaign.isFlagged);
                this.campaigns = this.campaigns.filter(campaign => campaign.isPublic && !campaign.isFlagged);
            } catch (error) {
                console.error('Error:', error);
            }
        }
    },
    props: {
        message: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.horizontal-component {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 50px;
    background-color: lightblue; 
    margin-bottom: 20px;
    margin-top: 20px;
    width: 80%;
    border-radius: 10px; 
}
    
.message {
    flex: 1;
    margin: 20px; 
    color: #333; 
    font-size: 20px;
    font-weight: bold;
}

.btn-success {
    height: 30px;
    margin: 30px;
}

h4 {
    margin-top: 30px;
    margin-bottom: 30px;
    color: #40e0d0; 
}
</style>

        