<script>
export default {
  name: "DayTasks",
  props: {
    id: {type: String, required: true}
  },
  data() {
    return {
      tasks: null
    }
  },
  methods: {
    async getData() {
      const response = await fetch(`http://localhost:8000/my-tasks/day/${this.id}`)
      this.tasks = await response.json()
    }
  },
  async created() {
    await this.getData()
  }
}
</script>

<template>
<div>{{tasks}}</div>
</template>