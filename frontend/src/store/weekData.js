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
        console.log(weekStart)
        const response = await axios.get(`http://localhost:8000/my-tasks/week/${weekStart}`)

        weekStartDate.value = response.data.start_day
        weekdays.value = response.data.week_days
        isDataLoaded.value = true
        // weekDataObj.value = response.data
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
        const response = await axios.post(`http://localhost:8000/my-tasks/${dayPk}`, taskData)
        console.log(response.data)
        weekdays.value.forEach((day) => {
            if (day.pk === dayPk) {
                day.tasks.push(response.data)
            }
        })
    }

    async function updateTask(dayPk, newTaskData, taskPk) {
        const response = await axios.put(`http://localhost:8000/my-tasks/${taskPk}`, newTaskData)
        weekdays.value.forEach((day) => {
            if (day.pk === dayPk) {
                day.tasks.forEach((task, index) => {
                    if (task.pk === taskPk) {
                        day.tasks[index] = response.data
                    }
                })
            }
        })
    }

    return {fetchData, deleteTask, addTask, updateTask, getWeekDays, getStartDate, isDataLoaded}
})
