import {createRouter, createWebHistory} from "vue-router"

import MainTasksList from "@/components/MainTasksList.vue";
import DayTasks from "@/components/DayTasks.vue";

const routes = [
    {path: "/", name: "MainTasksList", component: MainTasksList},
    {path: "/day/:id", name: "DayTasks", component: DayTasks, props: true},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
