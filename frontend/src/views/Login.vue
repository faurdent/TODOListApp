<template>
  <div class="col-md-12">
    <div class="card card-container">
      <form name="form" @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="username">Username</label>
          <input
              v-model="userData.email"
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
          <button class="btn btn-primary btn-block" :disabled="loading">
            <span v-show="loading" class="spinner-border spinner-border-sm"></span>
            <span>Login</span>
          </button>
        </div>
        <div>
          <p>Dont have an account?</p>
          <router-link to="/sign-up">Sign Up</router-link>
        </div>
        <div class="form-group">
          <div v-if="message" class="alert alert-danger" role="alert">{{ message }}</div>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/store/auth"
import { useRoute, useRouter } from "vue-router";
import dateFormat from "dateformat";

const authStore = useAuthStore()

const router = useRouter()
const route = useRoute()

const userData = ref({
    email: "",
    password: "",
})
const loading = ref(false)
const message = ref("")

if (authStore.userState.status.loggedIn) {
  redirect()
}

function redirect() {
  const redirectURL = route.query.redirectURL
  if (redirectURL) {
    router.push(redirectURL)
    return
  }
  router.push(`/week/${dateFormat(new Date(), "yyyy-mm-dd")}`);
}

async function handleLogin() {
      if (userData.value.email && userData.value.password) {
        authStore.login(userData.value)
        .then(
            () => {
              redirect()
            },
            error => {
              loading.value = false;
              message.value = error.response.data.detail.msg
            }
        );
    }
}
</script>
