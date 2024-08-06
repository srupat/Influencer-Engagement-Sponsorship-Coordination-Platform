<template>
    <div>
        <h4>Ongoing Campaigns</h4>
        <div v-for="campaign in campaigns" :key="campaign.id" class="campaign-component">
            <div class="horizontal-component">
                <div class="message">{{ campaign.name }}</div>
                <button class="btn btn-success" @click="toggleViewCampaign(campaign.id)">View</button>
                <button class="btn btn-warning" @click="flagCampaign(campaign.id)">Flag</button>
            </div>
            <div v-if="selectedCampaign === campaign.id" class="campaign-details">
                <p><strong>Start Date:</strong> {{ campaign.start_date }}</p>
                <p><strong>End Date:</strong> {{ campaign.end_date }}</p>
                <p><strong>Budget:</strong> {{ campaign.budget }}</p>
                <p><strong>Status:</strong> {{ campaign.isPublic ? 'Public' : 'Private' }}</p>
                <!-- <p><strong>Flagged:</strong> {{ campaign.isFlagged ? 'Yes' : 'No' }}</p> -->
            </div>
        </div>
        <h4>Flagged Campaigns</h4>
        <div v-for="campaign in flaggedCampaigns" :key="campaign.id" class="campaign-component">
            <div class="horizontal-component">
                <div class="message">{{ campaign.name }}</div>
                <button class="btn btn-success" @click="toggleViewCampaign(campaign.id)">View</button>
                <button class="btn btn-danger" @click="removeCampaign(campaign.id)">Remove</button>
            </div>
            <div v-if="selectedCampaign === campaign.id" class="campaign-details">
                <p><strong>Start Date:</strong> {{ campaign.start_date }}</p>
                <p><strong>End Date:</strong> {{ campaign.end_date }}</p>
                <p><strong>Budget:</strong> {{ campaign.budget }}</p>
                <p><strong>Status:</strong> {{ campaign.isPublic ? 'Public' : 'Private' }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            campaigns: [],
            flaggedCampaigns: [],
            selectedCampaign: null
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
        },
        async removeCampaign(id) {
            try {
                const response = await fetch(`http://localhost:8085/api/campaign/${id}`, {
                    method: 'DELETE'
                });
                if (response.ok) {
                    this.fetchCampaigns();
                } else {
                    console.error('Error:', response.statusText);
                }
            } catch (error) {
                console.error('Error:', error);
            }
        },
        toggleViewCampaign(id) {
            this.selectedCampaign = this.selectedCampaign === id ? null : id;
        },
        flagCampaign(id) {
            const campaign = this.campaigns.find(campaign => campaign.id === id);
            campaign.isFlagged = true;
            this.flaggedCampaigns.push(campaign);
            this.campaigns = this.campaigns.filter(campaign => campaign.id !== id);
        }
    }
}
</script>

<style scoped>
.campaign-component {
    margin-bottom: 20px;
}

.horizontal-component {
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #cce7ff; 
    padding: 10px;
    border-radius: 10px; 
}

.message {
    flex: 1;
    color: #333; 
    font-size: 20px;
    font-weight: bold;
}

.campaign-details {
    background-color: #fff;
    padding: 10px;
    border-radius: 5px;
    margin-top: 10px;
    border: 1px solid #cce7ff;
    color: #333;
    font-size: smaller;
}

.btn-success, .btn-danger, .btn-warning {
    margin-left: 10px;
}



h4 {
    margin-top: 30px;
    margin-bottom: 30px;
    color: #40e0d0; 
}
</style>
