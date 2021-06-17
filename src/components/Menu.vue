<template>
  <div class="menu-overlay" @click="closeMenu">
    <div class="menu">
      <div class="menu-header">
        <i class="fas fa-times" @click="closeMenu"></i>
        <div v-if="windowWidth < 900">
          <router-link to="/login" class="menu-auth"> login </router-link>
          |
          <router-link to="/signup" class="menu-auth"> sign up </router-link>
        </div>
      </div>
      <span class="menu-separator"></span>
      <router-link to="/about" class="menu-link"> About </router-link>
      <span class="menu-separator"></span>
      <router-link to="/news" class="menu-link"> News </router-link>
      <span class="menu-separator"></span>
      <router-link to="/events" class="menu-link"> Events </router-link>
      <span class="menu-separator"></span>
      <router-link to="/submit" class="menu-link">
        Submit to the Archive
      </router-link>
      <span class="menu-separator"></span>
      <router-link to="/explore" class="menu-link">
        Explore the Archive
      </router-link>
      <span class="menu-separator"></span>
      <router-link to="/support" class="menu-link"> Support Us </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Menu",
  methods: {
    openMenu: function () {
      document.getElementsByClassName("menu-overlay")[0].style.top = 0;
      document.getElementsByClassName("menu")[0].style.boxShadow =
        "0 0 10px #404040";
      this.disableScroll();
    },
    closeMenu: function () {
      document.getElementsByClassName("menu")[0].style.boxShadow = "none";
      document.getElementsByClassName("menu-overlay")[0].style.top = "-100vh";
      this.enableScroll();
    },
    initMenu: function () {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth < 900) {
        document.getElementsByClassName("menu")[0].style.width = "100%";
        document.getElementsByClassName("menu")[0].style.right = "0";
      } else {
        document.getElementsByClassName("menu")[0].style.width =
          "calc(max(30%, 400px))";
        document.getElementsByClassName("menu")[0].style.right = "6rem";
      }
    },
    disableScroll: function () {
      // Get the current page scroll position
      let scrollTop = window.pageYOffset || document.documentElement.scrollTop;
      let scrollLeft =
        window.pageXOffset || document.documentElement.scrollLeft;
      // If any scroll is attempted, set this to the previous value
      window.onscroll = function () {
        window.scrollTo(scrollLeft, scrollTop);
      };
    },
    enableScroll: function () {
      // Override disable scroll with a blank method to re-enable scrolling
      window.onscroll = function () {};
    },
  },
  data() {
    return {
      windowWidth: window.innerWidth,
    };
  },
  mounted() {
    // Handle menu sizing
    this.initMenu();
    window.addEventListener("resize", this.initMenu);
  },
  beforeUnmount() {
    // Clean up
    window.removeEventListener("resize", this.initMenu);
  },
};
</script>

<style scoped lang="scss">
.menu-overlay {
  // Position relative to navbar
  position: absolute;
  top: -100vh;
  left: 0;
  height: 100vh;
  width: 100vw;
  // Overlay all other elements
  z-index: $menu-content;
  // Smooth animation
  transition: top 0.2s ease;

  .menu {
    // Position relative to overlay
    position: absolute;
    top: 0;
    right: 6rem;
    // Color menu
    background: white;
    // Spacing
    padding: 1rem;
    // Flexbox for layout
    display: flex;
    flex-direction: column;
    align-items: center;

    .menu-header {
      // Typography
      font-family: $alt-font;
      font-size: 1.2rem;
      // Flexbox for layout
      display: flex;
      flex-direction: row-reverse;
      justify-content: space-between;
      align-items: center;
      // Spacing
      margin-bottom: 2rem;
      padding: 0 1rem;
      // Sizing
      width: 100%;

      i {
        // Icon styling
        font-size: 3rem;
        color: black;
        // Clickable
        cursor: pointer;
      }

      .menu-auth {
        // Typography
        text-transform: uppercase;
        // Remove effects of router link
        text-decoration: none;
        color: $font-color;
        // Clickable
        cursor: pointer;
      }
    }

    .menu-link {
      // Typography
      font-size: $subheader-font-size;
      padding: 2rem;
      // Remove effects of router link
      color: $font-color;
      text-decoration: none;
      // Sizing
      width: 100%;
    }

    .menu-separator {
      // Sizing
      height: 1px;
      width: 100%;
      // Bar styling
      background: lightgrey;
    }
  }
}
</style>