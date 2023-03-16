<template>
  <div class="modal-window active-modal" id="modal">
    <div class="modal-header">
      <button class="close-button" @click="emit('close')">&times;</button>
    </div>
    <div class="modal-body">
      <form ref="addForm" @submit.prevent="updateTask">
        <div>
          <label for="title">Title</label>
          <input required v-model="taskDataUpdate.title" id="title" type="text">
        </div>
        <div>
          <label for="description">Description</label>
          <input v-model="taskDataUpdate.description" id="description" type="text">
        </div>
        <div>
          <label for="deadline">Deadline</label>
          <input required v-model="taskDataUpdate.deadline" id="deadline" type="time">
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import {useWeekDataStore} from "@/store/weekData";
import {computed} from "vue";

const props = defineProps(["taskData"])
const emit = defineEmits(["close"])

const weekDataStorage = useWeekDataStore()

const taskDataUpdate = computed(() => {
  return {...props.taskData}
})

function updateTask() {
  console.log(taskDataUpdate.value)
  weekDataStorage.updateTask(props.taskData.pk, taskDataUpdate.value)
  emit("close")
}

</script>

<style scoped>
.modal-window {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0);
  border: 1px solid black;
  transition: 0.2s ease-in-out;
  border-radius: 10px;
  z-index: 999;
  background: white;
  width: 500px;
  max-width: 80%;
}

.modal-window.active-modal {
  transform: translate(-50%, -50%) scale(1);
}

.modal-header {
  padding: 10px 15px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid black;
}

.modal-header > .close-button {
  cursor: pointer;
  border: none;
  outline: none;
  background: none;
  font-size: 1.25rem;
  font-weight: bold;
}

.modal-body {
  padding: 10px 15px;
  border-bottom: 1px solid black;
}

</style>