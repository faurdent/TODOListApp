<template>
  <div>
    <h4>{{ taskData.title }}</h4>
    <p>Description: {{ taskData.description || "not provided" }}</p>
  </div>
  <button @click.prevent="$emit('delete', taskData.pk)" style="display: inline">Delete</button>
</template>

<script>
export default {
  name: "TheTask",
  props: {
    taskData: {
      type: Object,
      required: true
    }
  },
  emits: ["delete"]
}
</script>

<style scoped>

</style>