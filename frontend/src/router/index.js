import {createRouter, createWebHistory} from "vue-router"

import MainTasksList from "@/views/MainTasksList.vue";
import DayTasks from "@/views/DayTasks.vue";
import Login from "@/views/Login.vue";

const routes = [
    {path: "/week/:weekStart?", name: "MainTasksList", component: MainTasksList, props: true},
    {path: "/day/:id", name: "DayTasks", component: DayTasks, props: true},
    {path: "/login", name: "Login", component: Login},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
