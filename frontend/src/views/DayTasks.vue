<!--<script>-->
<!--import GoBack from "@/components/GoBack.vue";-->

<!--export default {-->
<!--  name: "DayTasks",-->
<!--  components: {GoBack},-->
<!--  props: {-->
<!--    id: {type: String, required: true}-->
<!--  },-->
<!--  data() {-->
<!--    return {-->
<!--      dayData: null-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    async getData() {-->
<!--      const response = await fetch(`http://localhost:8000/my-tasks/day/${this.id}`)-->
<!--      this.dayData = await response.json()-->
<!--    }-->
<!--  },-->
<!--  async created() {-->
<!--    await this.getData()-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<template>-->
<!--  <div v-if="dayData" class="day">-->
<!--    <div>{{ dayData }}</div>-->
<!--    <h1>{{ dayData.weekday }}</h1>-->
<!--    <GoBack/>-->
<!--    <ul>-->
<!--      <li v-for="task in dayData.tasks" :key="task.pk">-->
<!--        <h3>{{ task.title }}</h3>-->
<!--        <p>Description: {{ task.description || "Not provided" }}</p>-->
<!--      </li>-->
<!--    </ul>-->
<!--  </div>-->
<!--  <div v-else>-->
<!--    <h2>Loading...</h2>-->
<!--  </div>-->
<!--</template>-->

<template>
  <div>Day view blank</div>
</template>

<script setup>
import {defineProps} from "vue"
import {useWeekDataStore} from "@/store/weekData";

const props = defineProps(["weekdaySlug"])

const store = useWeekDataStore()
</script>
