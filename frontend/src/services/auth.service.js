class AuthService {
    login(user) {
        return fetch("http://localhost:8000/access-token", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: "qwerty",
                password: "qwerty1234",
            })
        })
            .then(response => response.json())
            .then(data => {
                    if (data.access_token) {
                        localStorage.setItem('user', JSON.stringify(data))
                    }
                    return data
                }
            )
    }

    logout() {
        localStorage.removeItem('user')
    }

    register(user) {
        return fetch("http://localhost:8000/users/sign-up", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: "qwerty",
                password: "qwerty1234",
            })
        })
            .then(response => response.json())
            // .then(data => {
            //     return data
            // })
    }
}

export default new AuthService()
