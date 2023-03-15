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
    
    logout() {
        localStorage.removeItem("user")
    }
}


export default new AuthService()
