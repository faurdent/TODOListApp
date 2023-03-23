import axios from "axios";
import authService from "./auth.service";
import authHeader from "./auth-header";

const axiosInstance = axios.create()

axiosInstance.interceptors.response.use(function(response) {
    return response
}, function(error) {
    const originalRequest = error.config
    if (error.response.status === 401 && !originalRequest.tokenRequested) {
        authService.logout()
        originalRequest.tokenRequested = true
        return authService.refreshToken().then(() => {
            originalRequest.headers = authHeader()
            return axiosInstance(originalRequest)
        })
    }
    return Promise.reject(error)
})


export default axiosInstance
