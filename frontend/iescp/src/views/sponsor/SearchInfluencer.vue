<template>
  <div>
    <SponsorNavbar />

    <div class="container mt-3">
      <div class="row">
        <div class="col">
          <input
            type="text"
            class="form-control"
            placeholder="Search Influencers"
            v-model="searchText"
          />
        </div>
        <div class="col">
          <select class="form-select" v-model="selectedCategory">
            <option value="">All Categories</option>
            <option v-for="category in categories" :key="category" :value="category">
              {{ category }}
            </option>
          </select>
        </div>
        <div class="col">
          <input
            type="number"
            class="form-control"
            placeholder="Min Followers"
            v-model.number="minFollowers"
          />
          <input
            type="number"
            class="form-control mt-2"
            placeholder="Max Followers"
            v-model.number="maxFollowers"
          />
        </div>
      </div>

      <div class="row mt-3">
        <div class="col-12">
          <div
            v-for="influencer in filteredInfluencers"
            :key="influencer.name"
            class="card mb-2 influencer-card"
          >
            <div class="card-body">
              <h5 class="card-title">{{ influencer.name }}</h5>
              <p class="card-text">Category: {{ influencer.category }}</p>
              <p class="card-text">Niche: {{ influencer.niche }}</p>
              <p class="card-text">Followers: {{ influencer.followers }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import SponsorNavbar from '@/components/sponsor/SponsorNavbar.vue'

export default {
  components: {
    SponsorNavbar
  },
  data() {
    return {
      influencers: [],
      searchText: '',
      selectedCategory: '',
      categories: ['Fashion', 'Tech', 'Food', 'Travel'],
      minFollowers: 0,
      maxFollowers: Infinity
    }
  },
  computed: {
    filteredInfluencers() {
      return this.influencers.filter((influencer) => {
        const matchesName = influencer.name.toLowerCase().includes(this.searchText.toLowerCase())
        const matchesCategory =
          this.selectedCategory === '' || influencer.category === this.selectedCategory
        const matchesFollowers =
          influencer.followers >= this.minFollowers && influencer.followers <= this.maxFollowers
        return matchesName && matchesCategory && matchesFollowers
      })
    }
  },
  created() {
    this.fetchInfluencers()
  },
  methods: {
    async fetchInfluencers() {
      try {
        const response = await fetch('http://localhost:8085/api/influencer')
        const data = await response.json()
        this.influencers = data

        const fetchedCategories = [
          ...new Set(this.influencers.map((influencer) => influencer.category))
        ]
        this.categories = [...new Set([...this.categories, ...fetchedCategories])]
      } catch (error) {
        console.error('Error fetching influencers:', error)
      }
    }
  }
}
</script>

<style scoped>
.influencer-card {
  background-color: white;
  color: #333;
  border: 1px solid #ddd;
  border-radius: 5px;
}
.card-title {
  font-weight: bold;
}
.card-text {
  margin: 0;
}
</style>
