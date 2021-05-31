import { createWebHistory, createRouter } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home.vue"),
  },
  {
    path: "/about",
    name: "About",
    component: () => import("@/views/About.vue"),
  },
  {
    path: "/news",
    name: "News",
    component: () => import("@/views/News.vue"),
  },
  {
    path: "/events",
    name: "Events",
    component: () => import("@/views/Events.vue"),
  },
  {
    path: "/browse",
    name: "Browse",
    component: () => import("@/views/Browse.vue"),
  },
  {
    path: "/submit",
    name: "Submit",
    component: () => import("@/views/Submit.vue"),
  },
  {
    path: "/support",
    name: "Support",
    component: () => import("@/views/Support.vue"),
  },
  {
    path: "/termsandconditions",
    name: "Terms and Conditions",
    component: () => import("@/views/TermsAndConditions.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
