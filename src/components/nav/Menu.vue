<template>
  <div id="menu-overlay" @click="closeMenu">
    <div id="menu">
      <div id="menu-header">
        <i id="menu-close-button" class="fas fa-times" @click="closeMenu" />
        <div id="menu-user-nav">
          <router-link to="/login" class="menu-user-link"> login </router-link>
          |
          <router-link to="/signup" class="menu-user-link">
            sign up
          </router-link>
        </div>
      </div>
      <hr class="menu-separator" />
      <router-link class="menu-link" to="/about"> About </router-link>
      <hr class="menu-separator" />
      <router-link class="menu-link" to="/news"> News </router-link>
      <hr class="menu-separator" />
      <router-link class="menu-link" to="/events"> Events </router-link>
      <hr class="menu-separator" />
      <router-link class="menu-link" to="/submit">
        Submit to the Archive
      </router-link>
      <hr class="menu-separator" />
      <router-link class="menu-link" to="/explore">
        Explore the Archive
      </router-link>
      <hr class="menu-separator" />
      <router-link class="menu-link" to="/support"> Support Us </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Menu",
  methods: {
    openMenu: function () {
      document.getElementById("menu-overlay").style.top = 0;
      document.getElementById("menu").style.boxShadow = "0 0 10px #404040";
      this.disableScroll();
    },
    closeMenu: function () {
      document.getElementById("menu").style.boxShadow = "none";
      document.getElementById("menu-overlay").style.top = "-100vh";
      this.enableScroll();
    },
    initMenu: function () {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth < 1024) {
        document.getElementById("menu").style.width = "100%";
        document.getElementById("menu").style.right = "0";
      } else {
        document.getElementById("menu").style.width = "calc(max(30%, 400px))";
        document.getElementById("menu").style.right = "6rem";
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
#menu-overlay {
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

  #menu {
    // Position relative to overlay
    position: absolute;
    top: 0;
    right: 96px;
    // Color menu
    background: white;
    // Spacing
    padding: 16px;
    // Flexbox for layout
    display: flex;
    flex-direction: column;
    align-items: center;

    #menu-header {
      // Typography
      font-family: $alt-font;
      font-size: 1.2rem;
      // Flexbox for layout
      display: flex;
      flex-direction: row-reverse;
      justify-content: space-between;
      align-items: center;
      // Spacing
      margin-bottom: 32px;
      padding: 0 16px;
      // Sizing
      width: 100%;

      #menu-close-button {
        // Icon styling
        font-size: 2rem;
        color: black;
        // Clickable
        cursor: pointer;
      }

      #menu-user-nav {
        // Hide on default display
        display: none;

        .menu-user-link {
          // Typography
          text-transform: uppercase;
          font-size: 1rem;
          // Remove effects of router link
          text-decoration: none;
          color: $font-color;
          // Clickable
          cursor: pointer;
        }
      }
    }

    .menu-link {
      // Typography
      font-size: $subheader-font-size;
      font-weight: bold;
      padding: 32px;
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
      // Remove default styling
      border: none;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #menu-overlay > #menu > .menu-link:hover {
    // Animate
    background: lighten(lightgrey, 10);
  }
}

// Smaller layouts
@media screen and (max-width: 1023px) {
  #menu-overlay > #menu > #menu-header {
    #menu-close-button {
      // Resize
      font-size: 1.8rem;
    }

    #menu-user-nav {
      // Show
      display: block;
    }
  }
}
</style>