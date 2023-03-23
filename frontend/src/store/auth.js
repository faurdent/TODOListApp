import { defineStore } from "pinia";
import authService from "@/services/auth.service";
import {useRouter} from "vue-router"

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
        authService.logout()
        userState.status.loggedIn = false
        userState.user = null
    }

    function signUp(user) {
        return authService.signUp(user).then(
            user => Promise.resolve(user),
            error => Promise.reject(error),
        )
    }

    return {login, signUp, logout, userState}
})
