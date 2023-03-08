<template>
  <div style="transition: margin-top; transition-duration: 0.25s">
    <h2 style="display: inline;">{{ dayData.weekday }}</h2>
    <button @click="toggleForm">Add Task</button>
    <the-modal-add @close="toggleForm" :weekday="dayData.weekday" v-if="isModalVisible"/>
    <div v-if="isModalVisible" id="overlay"></div>
    <ul>
      <li v-for="(task, index) in tasks">
        <the-task :dayPk="dayData.pk" :index="index" :taskData="task"/>
      </li>
    </ul>
  </div>
</template>


<script setup>
import {defineProps, ref} from "vue"

import TheTask from "@/components/WeekTasksComponents/TheTask.vue";
import {useWeekDataStore} from "@/store/weekData";
import {useRouter} from "vue-router";
import TheModalAdd from "@/components/WeekTasksComponents/TheModalAdd.vue";

const props = defineProps(["dayData"])

const weekDataStore = useWeekDataStore()

const tasks = ref(props.dayData.tasks)
const router = useRouter()

const isModalVisible = ref(false)
//
const taskData = ref({
  title: "",
  description: "",
  deadline: "",
})

function toggleForm() {
  isModalVisible.value = !isModalVisible.value
}

function formClear() {
  for (const key in taskData.value) {
    taskData.value[key] = ""
  }
}

function addTask() {
  weekDataStore.addTask(props.dayData.pk, taskData.value)
  formClear()
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
