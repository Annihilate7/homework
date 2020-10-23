import Vue from 'vue'
import Router from 'vue-router'
import Note from "../components/Note";
import User from "../components/User";
import Userdetail from "../components/Userdetail";

Vue.use(Router)

export default new Router({
    routes: [
        {path: '/', redirect: '/note'},
        {path: '/note', component: Note},
        {path: '/user', component: User},
        {path: '/detail/:id/:username/:age', component: Userdetail},
    ]
})
