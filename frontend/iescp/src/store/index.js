import { createStore } from 'vuex'
import localStoragePlugin from './plugins/localStorage';

const store = createStore({
    state() {
        return {
            role: '',
            sponsorID: localStorage.getItem('sponsorID') || null
        }
    },
    mutations: {
        setRole(state, role) {
            state.role = role
        },
        clearRole(state) {
            state.role = ''
        },
        setSponsorID(state, sponsorID) {
            state.sponsorID = sponsorID
        },
        clearSponsorID(state) {
            state.sponsorID = null
        }
    },
    actions: {
        setRole({ commit }, role) {
            commit('setRole', role)
        },
        clearRole({ commit }) {
            commit('clearRole')
        },
        setSponsorID({ commit }, sponsorID) {
            commit('setSponsorID', sponsorID)
        },
        clearSponsorID({ commit }) {
            commit('clearSponsorID')
        }
    },
    getters: {
        role: (state) => state.role,
        sponsorID: (state) => state.sponsorID
    },
    plugins: [localStoragePlugin],
})

export default store
