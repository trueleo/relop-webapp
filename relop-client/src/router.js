import Vue from 'vue'
import Router from 'vue-router'
import Completed from './views/Completed.vue'
import Login  from './views/Login.vue'
import Tasker from './views/Tasker.vue'
import About from './views/About.vue'
import NotFound from './views/NotFound.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: {
        name: "login"
      }
    },
    {
      path: '/todo',
      name: 'task',
      component: Tasker
    },
    {
      path: '/completed',
      name: 'completed',
      component: Completed
    },
    {
      path: '/about',
      name: 'about',
      component: About
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '*',
      component: NotFound
    }
  ]
})
