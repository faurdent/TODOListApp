<template>
  <div>
    <go-back/>
    <form @submit.prevent="commitForm">
      <label for="title">Title</label>
      <input id="title" required type="text" v-model="taskInfo.title">
      <label for="description">Description</label>
      <input id="description" type="text" v-model="taskInfo.description">
      <label for="deadline">Deadline</label>
      <input id="deadline" required type="time" v-model="taskInfo.deadline">
      <button type="submit">Submit</button>
    </form>
  </div>
</template>

<script>
import GoBack from "@/components/GoBack.vue";

export default {
  name: "UpdateTask",
  components: {GoBack},
  props: {
    taskInfo: {
      type: Object,
      required: true
    },
    id: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>

</style>