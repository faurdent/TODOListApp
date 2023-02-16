<script>
export default {
  name: "MainTasksList",
  data() {
    return {
      week_data: []
    }
  },
  methods: {
    async getData() {
      // const res = await fetch("http://0.0.0.0:8000/")
      fetch("http://localhost:8000/my-tasks/test-tasks/2023-04-09")
          .then(res1 => res1.json())
          .then(json => this.week_data = json)
    }
  },
  created() {
    this.getData()
  }

}
</script>

<template>
  <div>
    {{ this.week_data }}
    <ul>

      <li v-for="day in week_data" :key="day.pk">
        <router-link :to="`/day/${day.pk}`">
          <h2>{{ day.weekday }}</h2>
        </router-link>
        <ul>
          <li v-for="task in day.tasks">
            {{ task.title }}
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