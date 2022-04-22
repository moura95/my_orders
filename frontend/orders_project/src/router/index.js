import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import CustomCompany from "../views/custom-company.vue";
import CustomProduct from "../views/custom-product.vue";
import CustomOrder from "../views/custom-order.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/company",
    name: "company",
    component: CustomCompany,
  },
  {
    path: "/product",
    name: "product",
    component: CustomProduct,
  },
  {
    path: "/order",
    name: "order",
    component: CustomOrder,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
