<template>
  <div class="col-md-12">
    <div class="card card-container">
      <form name="form" @submit.prevent="handleRegister">
        <div class="form-group">
          <label for="username">Username</label>
          <input
              v-model="userData.username"
              type="text"
              class="form-control"
              name="username"
          />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
              v-model="userData.password"
              type="password"
              class="form-control"
              name="password">
        </div>
        <div class="form-group">
          <button class="btn btn-primary btn-block">
            <span>Sign Up</span>
          </button>
        </div>
        <div class="form-group">
          <div v-if="message" class="alert alert-danger" role="alert">{{ message }}</div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import {useAuthStore} from "@/store/auth";
import {ref} from "vue";
import dateFormat from "dateformat";
import {useRouter} from "vue-router";

const authStore = useAuthStore()
const router = useRouter()

const userData = ref({
  username: "",
  password: "",
})
const message = ref("")

if (authStore.userState.status.loggedIn) {
  router.push(`/week/${dateFormat(new Date(), "yyyy-mm-dd")}`);
}

function handleRegister() {
  if (userData.value.username && userData.value.password) {
    authStore.signUp(userData.value)
        .then(
            () => {
              router.push("/login")
            },
            error => {
              message.value = error.response.data.detail
            }
        )
  }
}

</script>

<style scoped>

</style>