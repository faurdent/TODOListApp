<template>
  <div style="transition: margin-top; transition-duration: 0.25s">
    <h2 style="display: inline;">{{ dayData.weekday }}</h2>
    <button @click="toggleForm">Add Task</button>
    <the-modal-add @close="toggleForm" :weekday="dayData.pk" v-if="isModalVisible"/>
    <div v-if="isModalVisible" id="overlay"></div>
    <TransitionGroup name="fade" tag="ul" class="container">
      <li :key="task.pk"  v-for="(task, index) in dayTasks">
        <the-task class="item" :dayPk="dayData.pk" :index="index" :taskData="task"/>
      </li>
    </TransitionGroup>
  </div>
</template>


<script setup>
import {computed, ref} from "vue"

import TheTask from "@/components/WeekTasksComponents/TheTask.vue";
import {useWeekDataStore} from "@/store/weekData";
import {useRouter} from "vue-router";
import TheModalAdd from "@/components/WeekTasksComponents/TheModalAdd.vue";

const props = defineProps(["dayData"])

const weekDataStore = useWeekDataStore()
const router = useRouter()

const isModalVisible = ref(false)

const dayTasks = computed(() => {
  const tasksFiltered = weekDataStore.tasks.filter((task) => {
    return task.day_id === props.dayData.pk
  })
  tasksFiltered.sort((firstTask, secondTask) => firstTask.is_done - secondTask.is_done)
  return tasksFiltered
})

function toggleForm() {
  isModalVisible.value = !isModalVisible.value
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
  z-index: 300;
  background: rgba(0, 0, 0, 0.2);
  pointer-events: all;
}

.container {
  position: relative;
  padding: 0;
}

.item {
  width: 100%;
  height: 8rem;
  background-color: #f3f3f3;
  border: 1px solid #666;
  box-sizing: border-box;
}

.fade-move,
.fade-enter-active,
.fade-leave-active {
  transition: all 0.5s cubic-bezier(0.55, 0, 0.1, 1);
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: scaleY(0.01) translate(30px, 0);
}

.fade-leave-active {
  position: absolute;
}
</style>
