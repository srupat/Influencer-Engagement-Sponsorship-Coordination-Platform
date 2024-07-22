import { createStore } from 'vuex'

const store = createStore({
    state() {
        return {
            roles: []
        }
    },
    mutations: {
        setRoles(state, roles) {
            state.roles = roles
        },
        clearRoles(state) {
            state.roles = []
        }
    },
    actions: {
        setRoles({ commit }, roles) {
            commit('setRoles', roles)
        }, 
        clearRoles({ commit }) {
            commit('clearRoles')
        }
    },
    getters: {
        roles: (state) => state.roles
    }
})


export default store
