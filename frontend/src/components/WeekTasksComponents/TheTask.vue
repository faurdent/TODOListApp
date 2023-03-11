<template>
  <div>
    <h4>{{ taskData.title }}</h4>
    <p>Description: {{ taskData.description || "not provided" }}</p>
    <button @click="toggleForm">Update</button>
    <button @click="deleteTask">Delete</button>
    <the-modal-update @close="toggleForm" :task-data="taskData" v-if="isFormVisible"/>
    <div v-if="isFormVisible" id="overlay"></div>
  </div>
</template>

<script setup>
import {defineProps, ref} from "vue"
import {useWeekDataStore} from "@/store/weekData";
import TheModalUpdate from "@/components/WeekTasksComponents/TheModalUpdate.vue";

const store = useWeekDataStore()

const props = defineProps(["taskData", "index", "dayPk"])

const isFormVisible = ref(false)

function deleteTask() {
  store.deleteTask(props.taskData.pk)
}

function toggleForm() {
  isFormVisible.value = !isFormVisible.value
}
</script>

<style scoped>
#overlay {
  position: fixed;
  opacity: 1;
  transition: 0.2s ease-in-out;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.2);
  pointer-events: all;
}
</style>
