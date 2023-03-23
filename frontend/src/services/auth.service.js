import axios from "axios";

const BASE_URL = "http://localhost:8000"

class AuthService {
    async login(user) {
        const response = await axios.post(`${BASE_URL}/access-token`, {
            email: user.email,
            password: user.password
        })
        const userData = response.data
        if (userData.access_token) {
            localStorage.setItem("user", JSON.stringify(userData))
        }
        return userData
    }
    
    async refreshToken() {
        try {
            const response =  await axios.get(`${BASE_URL}/refresh-token`, {withCredentials: true})
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

    logout() {
        localStorage.removeItem("user")
    }

}


export default new AuthService()
