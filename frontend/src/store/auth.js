import { defineStore } from "pinia";
import authService from "@/services/auth.service";
import { computed } from "vue";

const user = JSON.parse(localStorage.getItem("user"))
const initialState = user ? {status: {loggedIn: true}, user: user} : {status: {loggedIn: false}, user: null}

export const useAuthStore = defineStore("auth", () => {
    const userState = initialState
    async function login(user) {
        return authService.login(user).then(
            user => {
                initialState.status.loggedIn = true
                initialState.user = user
                return Promise.resolve(user)
            },
            error => {
                initialState.status.loggedIn = false
                initialState.user = null
                return Promise.reject(error)
            }
        )
    }

    function logout() {
        localStorage.removeItem("user")
        userState.status.loggedIn = false
        userState.user = null
    }

    return {login, logout, userState}
})
