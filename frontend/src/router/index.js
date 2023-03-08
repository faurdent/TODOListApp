import {createRouter, createWebHistory} from "vue-router"

import {useWeekDataStore} from "@/store/weekData";

import MainTasksList from "@/views/MainTasksList.vue";

const routes = [
    {
        path: "/week/:weekStart",
        name: "MainTasksList",
        component: MainTasksList,
        props: true,
        beforeEnter: (to, from) => {
            const store = useWeekDataStore()
            store.fetchData(to.params.weekStart)
        },
    },
    // {path: "/week/:weekStart/:weekdaySlug", name: "DayTasks", component: DayTasks, props: true},
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
