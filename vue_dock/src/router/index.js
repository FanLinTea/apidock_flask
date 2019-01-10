import Vue from 'vue'
import Router from 'vue-router'
import login from '@/components/login'
import home from '@/views/home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home,
      children:[
        {
          path:'/',
          name: '哈哈哈哈哈哈',
          icon: 'bookmarks',
          component:()=>import('@/views/test')
        },
        {
          path:'test1',
          name: '好矮好好',
          icon: 'dns',
          component:()=>import('@/views/test1')
        },

      ]
    },
    {
      path: '/login',
      name: 'login',
      component: login,
    },
  ]
})
