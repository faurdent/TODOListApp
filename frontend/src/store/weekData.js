import {defineStore} from "pinia";
import {computed, ref} from "vue";
import axios from "axios";

export const useWeekDataStore = defineStore("weekData", () => {
    const weekStartDate = ref(null)
    const weekdays = ref([])
    const isDataLoaded = ref(false)
    const tasks = ref([])

    const getStartDate = computed(() => {
        return weekStartDate.value
    })

    const getWeekDays = computed(() => {
        return [...weekdays.value].sort((day, nextDay) => day.pk - nextDay.pk)
    })

    async function fetchData(weekStart) {
        isDataLoaded.value = false
        const response = await axios.get(`http://localhost:8000/my-tasks/week/${weekStart}`)

        weekStartDate.value = response.data.start_day
        weekdays.value = response.data.week_days
        tasks.value = response.data.tasks
        isDataLoaded.value = true
    }

    function deleteTask(dayPk, taskID, taskPk) {
        axios.delete(`http://localhost:8000/my-tasks/${taskPk}`).then(response => response.data)
        weekdays.value.forEach((day) => {
            if (day.pk === dayPk) {
                day.tasks.splice(taskID, 1)
            }
        })
    }

    async function addTask(dayPk, taskData) {
        console.log(dayPk)
        console.log(taskData)
        const response = await axios.post(`http://localhost:8000/my-tasks/${dayPk}`, taskData)
        console.log(response.data)
        tasks.value.push(response.data)
    }

    async function updateTask(taskPk, newTaskData) {
        const response = await axios.put(`http://localhost:8000/my-tasks/${taskPk}`, newTaskData)
        console.log(response.data)
        const taskIndex = tasks.value.findIndex((task) => task.pk === taskPk)
        tasks.value[taskIndex] = response.data
    }

    return {fetchData, deleteTask, addTask, updateTask, getWeekDays, getStartDate, isDataLoaded, tasks}
})
