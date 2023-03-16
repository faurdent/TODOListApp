<template>
  <div>
    <h4>{{ taskData.title }}</h4>
    <p>Description: {{ taskData.description || "not provided" }}</p>
    <input :key="taskData.pk" type="checkbox" :checked="taskData.is_done" @click="setDoneStatus">
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

const weekDataStore = useWeekDataStore()

const props = defineProps(["taskData", "index", "dayPk"])

const isFormVisible = ref(false)

function deleteTask() {
  weekDataStore.deleteTask(props.taskData.pk)
}

function setDoneStatus() {
  const taskDataUpdate = {...props.taskData}
  taskDataUpdate.is_done = !taskDataUpdate.is_done
  console.log(taskDataUpdate)
  weekDataStore.updateTask(props.taskData.pk, taskDataUpdate)
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
  z-index: 300;
  pointer-events: all;
}
</style>
