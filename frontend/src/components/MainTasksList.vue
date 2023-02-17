<script>
import dateFormat from "dateformat";

export default {
  name: "MainTasksList",
  props: {
    weekStart: {
      type: String
    }
  },
  data() {
    return {
      weekData: []
    }
  },
  methods: {
    async getData() {
      console.log(this.weekStartString)
      fetch(`http://localhost:8000/my-tasks/test-tasks/${this.weekStartString}`)
          .then(res1 => res1.json())
          .then(json => this.weekData = json)
    },
    async deleteTask(day, toDelete) {
      const taskIndex = day.tasks.findIndex(task => task.pk === toDelete)
      await fetch(`http://localhost:8000/my-tasks/${toDelete}`, {method: "DELETE"})
      day.tasks.splice(taskIndex, 1)
    },
  },
  computed: {
    weekStartString() {
      if (!this.weekStart) {
        const nowDate = new Date()
        const nowDay = nowDate.getDay() || 7
        if (nowDay !== 1) {
          nowDate.setHours(-24 * (nowDay - 1))
        }
        return dateFormat(nowDate, "yyyy-mm-dd")
      }
      return this.weekStart
    }
  },
  created() {
    this.getData()
  }

}
</script>

<template>
  <div>
    {{ this.weekData }}
    {{ this.weekStart }}
    <ul>

      <li v-for="day in weekData" :key="day.pk">
        <router-link :to="`/day/${day.pk}`">
          <h2>{{ day.weekday }}</h2>
        </router-link>
        <ul>
          <li v-for="task in day.tasks">
            {{ task.title }}
            <button @click.prevent="deleteTask(day, task.pk)">Delete</button>
            <div>Description:
              <span v-if="task.description">{{ task.description }}</span>
              <span v-else>not provided</span>
            </div>
          </li>
        </ul>
      </li>

    </ul>
  </div>
</template>