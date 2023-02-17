import {createRouter, createWebHistory} from "vue-router"

import MainTasksList from "@/components/MainTasksList.vue";
import DayTasks from "@/components/DayTasks.vue";

const routes = [
    {path: "/week/:weekStart?", name: "MainTasksList", component: MainTasksList, props: true},
    {path: "/day/:id", name: "DayTasks", component: DayTasks, props: true},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
