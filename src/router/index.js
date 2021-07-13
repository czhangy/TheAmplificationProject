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
    path: "/explore",
    name: "Explore",
    component: () => import("@/views/Explore.vue"),
  },
  {
    path: "/submit",
    name: "Submit",
    component: () => import("@/views/Submit.vue"),
  },
  {
    path: "/submission",
    name: "Submission",
    component: () => import("@/views/Submission.vue"),
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
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/Login.vue"),
  },
  {
    path: "/signup",
    name: "Sign Up",
    component: () => import("@/views/SignUp.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition;
    else return { left: 0, top: 0 };
  },
});

export default router;
