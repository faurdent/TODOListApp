<template>
  <div>
    <h4>{{ taskData.title }}</h4>
    <p>Description: {{ taskData.description || "not provided" }}</p>
  </div>
  <button @click.prevent="$emit('delete', taskData.pk)" style="display: inline">Delete</button>
<!--  <router-link :to="{name: 'TaskUpdate',-->
<!--  params: {id: dayId, taskInfo: {title: taskData.title, description: taskData.description, deadline: taskData.deadline}}}"-->
<!--  >-->
    <button @click="$router.push({name: 'TaskUpdate', params: {id: dayId, taskInfo: taskData}})">Update</button>
<!--  </router-link>-->

</template>

<script>
export default {
  name: "TheTask",
  props: {
    taskData: {
      type: Object,
      required: true
    },
    dayId: {
      type: Number,
      required: true
    }
  },
  emits: ["delete"]
}
</script>

<style scoped>

</style>