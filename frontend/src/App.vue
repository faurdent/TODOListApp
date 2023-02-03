<script>
export default {
  data() {
    return {
      week_data: []
    }
  },
  methods: {
    async getData() {
      // const res = await fetch("http://0.0.0.0:8000/")
      fetch("http://localhost:8000/my-tasks/test-tasks/2023-01-01")
          .then(res1 => res1.json())
          .then(json => this.week_data = json)
    }
  },
  mounted() {
    this.getData()
  }

}
</script>

<template>
  <div>
    {{ this.week_data }}
    <ul v-for="day in week_data">
      <li>
        <h2>{{ day.weekday }}</h2>
        <ul v-for="task in day.tasks">
          <li>{{ task }}</li>
        </ul>
      </li>
    </ul>
  </div>
</template>