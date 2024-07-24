import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            role: ''
        }
    },
    mutations: {
        setRole(state, role) {
            state.role = role
        },
        clearRole(state) {
            state.role = ''
        }
    },
    actions: {
        setRole({ commit }, role) {
            commit('setRole', role)
        },
        clearRole({ commit }) {
            commit('clearRole')
        }
    },
    getters: {
        role: (state) => state.role
    }
})

export default store
