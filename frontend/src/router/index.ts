import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import DeciderView from "../views/DeciderView.vue";
import DashboardView from "../views/DashboardView.vue";
import LoginView from "../views/LoginView.vue";
import ListProductView from "../views/ListProductView.vue";
import ProductPageView from "../views/ProductPageView.vue";
const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "decider",
    component: DeciderView,
  },
  {
    path: "/dashboard",
    name: "dashboard",
    component: DashboardView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/products",
    name: "products",
    component: ListProductView,
  },
  {
    path: "/product/:id",
    name: "ProductPage",
    component: ProductPageView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
