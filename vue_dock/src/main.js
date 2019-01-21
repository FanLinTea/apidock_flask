// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import MuseUI from 'muse-ui';
import 'muse-ui/dist/muse-ui.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import Vuex from 'vuex';
import axios from '@/request.js';
import {dm_config,apidoc} from '@/http_head.js';
import Toast from 'muse-ui-toast';

Vue.use(Toast);
Vue.use(MuseUI);
Vue.use(ElementUI);
Vue.use(Vuex);

Vue.prototype.$dm_config = {
  post: function (url, data) {
    return axios.post(`${dm_config}${url}`,data)
  },
  get: function (url, data) {
    return axios.post(`${dm_config}${url}`)
  },
}

Vue.prototype.$apidoc = {
  post: function (url, data) {
    return axios.post(`${apidoc}${url}`,data)
  },
  get: function (url, data) {
    return axios.post(`${apidoc}${url}`)
  },
}

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  methods: {
    toast () {
      this.$toast.message('hello world');
      this.$toast.success('hello world');
      this.$toast.info('hello world');
      this.$toast.warning('hello world');
      this.$toast.error('hello world');
    }
  }
})


