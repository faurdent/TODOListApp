<template>
  <div class="pagination" style="display:flex; justify-content:space-between;">
    <button @click="showPreviousWeek">Previous week</button>
    <button @click="showNextWeek">Next week</button>
  </div>
</template>

<script setup>
import dateFormat from "dateformat";
import {computed} from "vue";
import {useRouter} from "vue-router";

const props = defineProps(["weekStart"])

const router = useRouter()

const nextWeekStart = computed(() => {
  const currentDate = new Date(props.weekStart)
  currentDate.setDate(currentDate.getDate() + 7)
  return dateFormat(currentDate, "yyyy-mm-dd")
})

const previousWeekStart = computed(() => {
  const currentDate = new Date(props.weekStart)
  currentDate.setDate(currentDate.getDate() - 7)
  return dateFormat(currentDate, "yyyy-mm-dd")
})

function showNextWeek() {
  router.push({name: 'MainTasksList', params: {weekStart: nextWeekStart.value}})
}

function showPreviousWeek() {
  router.push({name: 'MainTasksList', params: {weekStart: previousWeekStart.value}})
}
</script>

<style scoped>

</style>