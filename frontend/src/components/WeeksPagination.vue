<template>
  <div class="pagination" style="display:flex; justify-content:space-between;">
    <button @click="showPreviousWeek">Previous week</button>
    <button @click="showNextWeek">Next week</button>
  </div>
</template>

<script>
import dateFormat from "dateformat";

export default {
  name: "WeeksPagination",
  props: {
    weekStart: {
      type: String,
      required: true
    }
  },
  methods: {
    showNextWeek() {
      this.$router.push({name: 'MainTasksList', params: {weekStart: this.nextWeekStart}})
    },
    showPreviousWeek() {
      this.$router.push({name: 'MainTasksList', params: {weekStart: this.previousWeekStart}})
    }
  },
  computed: {
    nextWeekStart() {
      const currentDate = new Date(this.weekStart)
      currentDate.setDate(currentDate.getDate() + 7)
      return dateFormat(currentDate, "yyyy-mm-dd")
    },
    previousWeekStart() {
      const currentDate = new Date(this.weekStart)
      currentDate.setDate(currentDate.getDate() - 7)
      return dateFormat(currentDate, "yyyy-mm-dd")
    }
  }
}
</script>

<style scoped>

</style>