import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/home/home'
import MenuComponent from '@/components/menu/MenuComponent'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/menu',
      name: 'MenuComponent',
      component: MenuComponent
    }
  ],
  mode:'history'
})
