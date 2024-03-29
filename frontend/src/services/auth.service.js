import axios from "axios";
import authHeader from "@/services/auth-header";

const BASE_URL = "http://localhost:8000"

class AuthService {
    async login(user) {
        const response = await axios.post(`${BASE_URL}/access-token`, {
            email: user.email,
            password: user.password
        }, {
            withCredentials: true, headers: {'Access-Control-Allow-Origin': 'http://127.0.0.1:8000'}
        })
        const userData = response.data
        if (userData.access_token) {
            localStorage.setItem("user", JSON.stringify(userData))
        }
        return userData
    }

    async refreshToken() {
        try {
            const response = await axios.get(`${BASE_URL}/refresh-token`, {withCredentials: true})
            localStorage.setItem("user", JSON.stringify(response.data))
            return response.data.access_token
        } catch (error) {
            console.error(error)
        }
    }

    async signUp(user) {
        const response = await axios.post(`${BASE_URL}/users/sign-up/`, {
            email: user.username,
            password: user.password,
        })
        return response.data
    }

    async verifyAccount(verificationCode) {
        const response = await axios.get(`${BASE_URL}/users/verify/${verificationCode}`)
        return response.data
    }

    async sendVerificationEmail() {
        const response = await axios.post(`${BASE_URL}/users/send-verification-email`, {},
            {headers: authHeader()}
        )
        return response.data
    }

    logout() {
        localStorage.removeItem("user")
    }

}


export default new AuthService()
