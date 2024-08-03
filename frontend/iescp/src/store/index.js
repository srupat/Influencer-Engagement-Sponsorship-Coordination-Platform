import { createStore } from 'vuex';
import createPersistedState from 'vuex-persistedstate';
import localStoragePlugin from './plugins/localStorage';

const store = createStore({
  state() {
    return {
      role: '',
      sponsorID: localStorage.getItem('sponsorID') || null,
      campaignID: localStorage.getItem('campaignID') || null
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
    }
  },
  getters: {
    role: state => state.role,
    sponsorID: state => state.sponsorID,
    campaignID: state => state.campaignID
  },
  plugins: [createPersistedState(), localStoragePlugin],
});

export default store;
