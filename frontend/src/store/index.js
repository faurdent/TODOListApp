import {createStore} from "vuex";
import {auth} from "@/store/auth.module";

const store = createStore({
    modules: {
        auth: auth
    }
})

export default store
