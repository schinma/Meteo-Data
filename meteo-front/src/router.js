import Vue from "vue";
import Router from "vue-router";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      redirect: "/index",
    },
    {
      path: "/graph/:name",
      name: "graph",
      component: () => import("./components/GraphContainer")
    },
    {
      path: "/index",
      name: "index",
      component: () => import("./components/Index")
    }
  ]
});
