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
    component: () => import("@/views/Explore/Explore.vue"),
  },
  {
    path: "/submit",
    name: "Submit",
    component: () => import("@/views/Submit/Submit.vue"),
  },
  {
    path: "/submission",
    name: "Submission",
    component: () => import("@/views/Submit/Submission.vue"),
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
    component: () => import("@/views/User/Login.vue"),
  },
  {
    path: "/signup",
    name: "Sign Up",
    component: () => import("@/views/User/SignUp.vue"),
  },
  // Catch-all for 404 pages
  {
    path: "/:pathMatch(.*)*",
    name: "Page Not Found",
    component: () => import("@/views/PageNotFound.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
  // Scroll to top of page on redirect
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition;
    else return { left: 0, top: 0 };
  },
});

export default router;
