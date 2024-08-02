import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            role: '',
            username : '',
            sponsorID : null
        }
    },
    mutations: {
        setRole(state, role) {
            state.role = role
        },
        clearRole(state) {
            state.role = ''
        },
        setUsername(state, username) {
            state.username = username
        },
        clearUsername(state) {        
            state.username = ''
        },
        setSponsorID(state, sponsorID) {
            state.sponsorID = sponsorID
        },
    },
    actions: {
        setRole({ commit }, role) {
            commit('setRole', role)
        },
        clearRole({ commit }) {
            commit('clearRole')
        },
        setUsername({ commit }, username) {
            commit('setUsername', username)
        },
        clearUsername({ commit }) {
            commit('clearUsername')
        },
        setSponsorID({ commit }, sponsorID) {
            commit('setSponsorID', sponsorID)
        },
    },
    getters: {
        role: (state) => state.role,
        username: (state) => state.username,
        sponsorID: (state) => state.sponsorID
    }
})

export default store
