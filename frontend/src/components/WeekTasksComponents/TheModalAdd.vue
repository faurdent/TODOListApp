<template>
  <div class="modal-window active-modal" id="modal">
    <h2>Add task for {{weekday}}</h2>
    <div class="modal-header">
      <button class="close-button" @click="$emit('close')">&times;</button>
    </div>
    <div class="modal-body">
      <form ref="addForm" @submit.prevent="addTask">
        <div>
          <label for="title">Title</label>
          <input required v-model="taskData.title" id="title" type="text">
        </div>
        <div>
          <label for="description">Description</label>
          <input v-model="taskData.description" id="description" type="text">
        </div>
        <div>
          <label for="deadline">Deadline</label>
          <input required v-model="taskData.deadline" id="deadline" type="time">
        </div>
        <button type="submit">Submit</button>
      </form>
    </div>
  </div>

</template>

<script setup>
import {ref} from "vue";

const props = defineProps(["weekday"])

const taskData = ref({
  title: "",
  description: "",
  deadline: "",
})
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

.modal-header > .title {
  font-size: 1.25rem;
  font-weight: bold;
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

.modal-footer {
  display: flex;
  padding: 10px 15px;
  justify-content: flex-end;
}

.button-cancel {
  background: white;
  border: rgb(64, 149, 191) 1px solid;
  color: rgb(64, 149, 191);
}

.button-cancel:hover {
  background: rgb(217, 234, 242);
}


</style>