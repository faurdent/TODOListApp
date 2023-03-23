import {createRouter, createWebHistory} from "vue-router"

import MainTasksList from "@/views/MainTasksList.vue";
import Login from "@/views/Login.vue"
import SignUp from "@/views/SignUp.vue";

import { useAuthStore } from "@/store/auth";


const routes = [
    {
        path: "/week/:weekStart",
        name: "MainTasksList",
        component: MainTasksList,
        props: true,
        meta: {requiresAuth: true}
    },
    {
        path: "/login",
        name: "login",
        component: Login
    },
    {
        path: "/sign-up",
        name: "signUp",
        component: SignUp,
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

router.beforeEach((to, from) => {
    const authStore = useAuthStore() 
    if (to.meta.requiresAuth && authStore.userState.status.loggedIn === false) {
        return {name: "login", query: {redirectURL: to.fullPath}}
    }
})

export default router
