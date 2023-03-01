import {createRouter, createWebHistory} from "vue-router"

import MainTasksList from "@/views/MainTasksList.vue";
import DayTasks from "@/views/DayTasks.vue";
import Login from "@/views/Login.vue";
import AddTask from "@/views/AddTask.vue";
import UpdateTask from "@/views/UpdateTask.vue";

const routes = [
    {path: "/week/:weekStart?", name: "MainTasksList", component: MainTasksList, props: true},
    {
        path: "/day/:id", name: "DayTasks", component: DayTasks, props: true
    },
    {path: "/login", name: "Login", component: Login},
    {path: "/day/:id/task-add", name: "TaskAdd", component: AddTask, props: true},
    {path: "/day/:id/task-update", name: "TaskUpdate", component: UpdateTask, props: true}
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
