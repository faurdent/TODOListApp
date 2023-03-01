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
import authHeader from "@/services/auth-header";

export default {
  name: "AddTask",
  components: {GoBack},
  // props: {
  //   taskInfo: {
  //     type: Object,
  //     required: true
  //   }
  // },
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      taskInfo: {
        title: "",
        description: "",
        deadline: "",
      }
    }
  },
  methods: {
    commitForm() {
      fetch(`http://localhost:8000/my-tasks/${this.id}`, {
        headers: authHeader(),
        body: JSON.stringify(this.taskInfo),
        method: "POST"
      })
    }
  }
}
</script>

<style scoped>

</style>