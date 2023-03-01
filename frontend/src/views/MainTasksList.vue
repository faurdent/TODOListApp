<script>
import dateFormat from "dateformat";
import TheDay from "@/components/WeekTasksComponents/TheDay.vue";
import WeeksPagination from "@/components/WeeksPagination.vue";
import authHeader from "@/services/auth-header";

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
      fetch(`http://localhost:8000/my-tasks/week/${this.weekStartString}`, {headers: authHeader()})
          .then(res1 => res1.json())
          .then(json => this.weekData = json)
          .catch(error => console.log(error))
    },
    async deleteTask(day, toDelete) {
      const taskIndex = day.tasks.findIndex(task => task.pk === toDelete)
      await fetch(`http://localhost:8000/my-tasks/${toDelete}`, {
        method: "DELETE",
        headers: authHeader()
      })
      day.tasks.splice(taskIndex, 1)
    },
    logout() {
      this.$store.dispatch("auth/logout")
      this.$router.push("/login")
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
    currentUser() {
      return this.$store.state.auth.user
    }
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
    <br>
    <button @click="logout">Logout</button>
    <p>{{ currentUser }}</p>
    <the-day v-for="day in weekData.week_days" :day-data="day"/>
  </div>
  <weeks-pagination :week-start="weekStartString"/>
</template>
