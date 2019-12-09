import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueParticles from 'vue-particles'
import { VueSpinners } from '@saeris/vue-spinners'

Vue.use(VueParticles)
Vue.use(VueSpinners)

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
