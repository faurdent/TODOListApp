<script>
export default {
  name: "DayTasks",
  props: {
    id: {type: String, required: true}
  },
  data() {
    return {
      dayData: null
    }
  },
  methods: {
    async getData() {
      const response = await fetch(`http://localhost:8000/my-tasks/day/${this.id}`)
      this.dayData = await response.json()
    }
  },
  async created() {
    await this.getData()
  }
}
</script>

<template>
  <div v-if="dayData" class="day">
    <div>{{ dayData }}</div>
    <h1>{{ dayData.weekday }}</h1>
    <ul>
      <li v-for="task in dayData.tasks" :key="task.pk">
        <h3>{{ task.title }}</h3>
        <p>Description: {{ task.description || "Not provided" }}</p>
      </li>
    </ul>
  </div>
  <div v-else>
    <h2>Loading...</h2>
  </div>
</template>