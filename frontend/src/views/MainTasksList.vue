<template>
  <div v-if="store.isDataLoaded">
    <h1>Start of the week: {{ store.getStartDate }}</h1>
    <the-day v-for="day in store.getWeekDays" :day-data="day"/>
    <weeks-pagination :week-start="weekStartString"/>
  </div>
</template>

<script setup>
import {useWeekDataStore} from "@/store/weekData";
import {computed} from "vue";
import dateFormat from "dateformat";

import TheDay from "@/components/WeekTasksComponents/TheDay.vue";
import WeeksPagination from "@/components/WeeksPagination.vue";


const store = useWeekDataStore()

const props = defineProps(["weekStart"])

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

store.fetchData(weekStartString.value)
</script>