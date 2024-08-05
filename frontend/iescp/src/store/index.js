import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import localStoragePlugin from './plugins/localStorage';

const store = createStore({
  state() {
    return {
      role: '',
      sponsorID: localStorage.getItem('sponsorID') || null,
      campaignID: localStorage.getItem('campaignID') || null,
      influencerID: localStorage.getItem('influencerID') || null
    };
  },
  mutations: {
    setRole(state, role) {
      state.role = role;
    },
    clearRole(state) {
      state.role = '';
    },
    setSponsorID(state, sponsorID) {
      state.sponsorID = sponsorID;
    },
    clearSponsorID(state) {
      state.sponsorID = null;
    },
    setCampaignID(state, campaignID) {
      state.campaignID = campaignID;
    },
    clearCampaignID(state) {
      state.campaignID = null;
    },
    setInfluencerID(state, influencerID) {
      state.influencerID = influencerID;
    },
    clearInfluencerID(state) {
      state.influencerID = null;
    }
  },
  actions: {
    setRole({ commit }, role) {
      commit('setRole', role);
    },
    clearRole({ commit }) {
      commit('clearRole');
    },
    setSponsorID({ commit }, sponsorID) {
      commit('setSponsorID', sponsorID);
    },
    clearSponsorID({ commit }) {
      commit('clearSponsorID');
    },
    setCampaignID({ commit }, campaignID) {
      commit('setCampaignID', campaignID);
    },
    clearCampaignID({ commit }) {
      commit('clearCampaignID');
    },
    setInfluencerID({ commit }, influencerID) {
      commit('setInfluencerID', influencerID);
    },
    clearInfluencerID({ commit }) {
      commit('clearInfluencerID');
    }
  },
  getters: {
    role: state => state.role,
    sponsorID: state => state.sponsorID,
    campaignID: state => state.campaignID,
    influencerID: state => state.influencerID
  },
  plugins: [createPersistedState(), localStoragePlugin],
});

export default store;
