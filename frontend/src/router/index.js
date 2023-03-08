import {createRouter, createWebHistory} from "vue-router"

import MainTasksList from "@/views/MainTasksList.vue";

const routes = [
    {
        path: "/week/:weekStart",
        name: "MainTasksList",
        component: MainTasksList,
        props: true,
    },
    // {path: "/week/:weekStart/:weekdaySlug", name: "DayTasks", component: DayTasks, props: true},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
