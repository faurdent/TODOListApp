<template>
  <div v-if="weekDataStore.isDataLoaded">
    <h1>Start of the week: {{ weekDataStore.getStartDate }}</h1>
    <button @click="logout">Logout</button>
    <the-day v-for="day in weekDataStore.getWeekDays" :day-data="day"/>
    <weeks-pagination :week-start="weekStartString"/>
  </div>
</template>

<script setup>
import {useWeekDataStore} from "@/store/weekData";
import {computed} from "vue";
import dateFormat from "dateformat";

import TheDay from "@/components/WeekTasksComponents/TheDay.vue";
import WeeksPagination from "@/components/WeeksPagination.vue";
import { useAuthStore } from "@/store/auth";
import { useRouter } from "vue-router";


const weekDataStore = useWeekDataStore()
const authStore = useAuthStore()

const router = useRouter()

const props = defineProps(["weekStart"])

function logout() {
  authStore.logout()
  router.push("/login")
}

const weekStartString = computed(() => {
  if (!props.weekStart) {
    const nowDate = new Date()
    const nowDay = nowDate.getDay() || 7
    if (nowDay !== 1) {
      nowDate.setHours(-24 * (nowDay - 1))
    }
    return dateFormat(nowDate, "yyyy-mm-dd")
  }
  return props.weekStart
})

weekDataStore.fetchData(weekStartString.value)
</script>