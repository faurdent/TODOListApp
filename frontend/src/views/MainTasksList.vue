<script>
import dateFormat from "dateformat";
import TheDay from "@/components/WeekTasksComponents/TheDay.vue";
import WeeksPagination from "@/components/WeeksPagination.vue";

export default {
  name: "MainTasksList",
  components: {TheDay, WeeksPagination},
  props: {
    weekStart: {
      type: String
    }
  },
  data() {
    return {
      weekData: []
    }
  },
  methods: {
    async getData() {
      fetch(`http://localhost:8000/my-tasks/test-tasks/${this.weekStartString}`)
          .then(res1 => res1.json())
          .then(json => this.weekData = json)
    },
    async deleteTask(day, toDelete) {
      const taskIndex = day.tasks.findIndex(task => task.pk === toDelete)
      await fetch(`http://localhost:8000/my-tasks/${toDelete}`, {method: "DELETE"})
      day.tasks.splice(taskIndex, 1)
    },
  },
  computed: {
    weekStartString() {
      if (!this.weekStart) {
        const nowDate = new Date()
        const nowDay = nowDate.getDay() || 7
        if (nowDay !== 1) {
          nowDate.setHours(-24 * (nowDay - 1))
        }
        return dateFormat(nowDate, "yyyy-mm-dd")
      }
      return this.weekStart
    },
  },
  created() {
    this.getData()
  }

}
</script>

<template>
  <div>
    {{ this.weekData }}
    {{ this.weekStart }}
    <the-day v-for="day in weekData" :day-data="day"/>
  </div>
  <weeks-pagination :week-start="weekStartString"/>
</template>
