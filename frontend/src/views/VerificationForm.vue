<template>
    <div>
        <h1>Account verification</h1>
        <p>Click on the link in the email, or input code here:</p>
        <form @submit.prevent="handleVerification">
            <label for="verification-code">Your code: </label>
            <input v-model="verificationCode" id="verification-code" type="text">
            <button type="submit">Submit</button>
            <p>{{ errorMessage }}</p>
        </form>
    </div>
</template>

<script setup>

import {ref} from "vue";
import {useAuthStore} from "@/store/auth";
import {useRouter} from "vue-router";

const authStore = useAuthStore()

const router = useRouter()

const verificationCode = ref("")
const errorMessage = ref("")

function handleVerification() {
    if (verificationCode.value) {
        authStore.verifyAccount(verificationCode.value).then(
            () => {
                router.push("/login")
            },
            error => errorMessage.value = error.response.data.detail
        )
    }
}
</script>

<style scoped>

</style>