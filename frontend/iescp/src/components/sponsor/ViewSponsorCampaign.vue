<template>
    <div>
        <h4>Active Campaigns</h4>
        <div v-for="campaign in campaigns" :key="campaign.id" class="campaign-component">
            <div class="horizontal-component">
                <div class="message">{{ campaign.name }}</div>
                <button class="btn btn-success" @click="toggleViewCampaign(campaign.id)">View</button>
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
import { mapGetters, mapActions } from 'vuex';

export default {
    data() {
        return {
            campaigns: [],
            selectedCampaign: null
        };
    },
    async mounted() {
        if (!this.sponsorID) {
            await this.fetchSponsorID();
        }
        this.fetchCampaigns();
    },
    beforeUnmount() {
        this.clearUsername();
    },
    computed: {
        ...mapGetters(['username', 'sponsorID'])
    },
    methods: {
        ...mapActions(['clearUsername', 'setSponsorID']),
        async fetchCampaigns() {
            if (!this.sponsorID) {
                console.error('Sponsor ID is not set');
                return;
            }
            try {
                const response = await fetch(`http://localhost:8085/api/campaign/${this.sponsorID}`, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
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
            } catch (error) {
                console.error('Error:', error);
            }
        },
        toggleViewCampaign(id) {
            this.selectedCampaign = this.selectedCampaign === id ? null : id;
        },
        async fetchSponsorID() {
            try {
                const username = this.username;
                console.log(this.username);
                const response = await fetch(`http://localhost:8085/sponsor/${username}`, {
                    headers: {
                        'Content-Type': 'application/json'
                    }
                });
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                const data = await response.json();
                this.setSponsorID(data.id);
            } catch (error) {
                console.error('Error:', error);
            }
        }
    }
};
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

.btn-success {
    margin-left: 10px;
}

h4 {
    margin-top: 30px;
    margin-bottom: 30px;
    color: #40e0d0; 
}
</style>
