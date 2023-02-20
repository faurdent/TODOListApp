<template>
  <div style="transition: margin-top; transition-duration: 0.25s">
    <router-link :to="`/day/${dayData.pk}`">
      <h2 style="display: inline;">{{ dayData.weekday }}</h2>
    </router-link>
    <ul>
      <li v-for="task in tasks">
        <the-task :taskData="task" @delete="deleteTask"/>
      </li>
    </ul>
  </div>
</template>

<script>
import TheTask from "@/components/WeekTasksComponents/TheTask.vue";

export default {
  name: "TheDay",
  components: {
    TheTask
  },
  props: {
    dayData: {
      type: Object,
      required: true
    },
  },
  data() {
    return {
      tasks: this.dayData.tasks
    }
  },
  methods: {
    async deleteTask(pk) {
      this.tasks = this.tasks.filter((task) => task.pk !== pk)
      await fetch(`http://localhost:8000/my-tasks/${pk}`, {method: "DELETE"})
    }
  }
}
</script>

<style scoped>

</style>
