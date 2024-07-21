import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        roles: []
    },
    mutations: {
        setRoles(state, roles) {
            state.roles = roles
        }
    },
    actions: {
        setRoles({ commit }, roles) {
            commit('setRoles', roles)
        }
    },
    getters: {
        roles: (state) => state.roles
    }
})
