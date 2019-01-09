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
      meta: {
        display: true
      },
      children:[
        {
          path:'/',
          component:()=>import('@/views/test')
        },
        {
          path:'test1',
          component:()=>import('@/views/test1')
        }

      ]
    },
    {
      path: '/login',
      name: 'login',
      component: login,
      meta: {
        display: false
      }
    },
  ]
})
