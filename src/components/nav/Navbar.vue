<template>
  <div id="navbar">
    <router-link id="navbar-brand" to="/">
      <img
        id="navbar-logo"
        src="@/assets/logo.png"
        alt="Amplification Project Logo"
      />
      <div id="navbar-text">
        <h1 id="navbar-title">
          THE <span id="navbar-title-highlight"> AMPLIFICATION </span> PROJECT
        </h1>
        <em id="navbar-subtitle">
          Digital Archive for Forced Migration
          <br />
          Contemporary Art & Action
        </em>
      </div>
    </router-link>
    <div id="navbar-links">
      <div id="navbar-user-nav">
        <router-link class="navbar-user-link" to="/login"> LOGIN </router-link>
        |
        <router-link class="navbar-user-link" to="/signup">
          SIGN UP
        </router-link>
      </div>
      <div id="navbar-hamburger" @click="openNavMenu">
        <hr class="navbar-hamburger-line" v-for="i in 3" :key="i" />
      </div>
    </div>
    <Menu ref="menu" />
  </div>
</template>

<script>
// Import nav components
import Menu from "@/components/nav/Menu";

export default {
  name: "Navbar",
  components: {
    Menu,
  },
  methods: {
    // Use ref to open menu
    openNavMenu: function () {
      this.$refs.menu.openMenu();
    },
  },
  data() {
    return {
      windowWidth: window.innerWidth,
    };
  },
  // Add resize checking
  mounted() {
    window.addEventListener("resize", () => {
      this.windowWidth = window.innerWidth;
    });
  },
  // Clean up
  beforeUnmount() {
    window.removeEventListener("resize", () => {
      this.windowHeight = window.innerWidth;
    });
  },
};
</script>

<style scoped lang="scss">
#navbar {
  // Sizing
  height: $navbar-height;
  width: 100%;
  // Spacing
  padding: 3rem calc(clamp(1rem, -1rem + 8vw, 6rem));
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  align-items: center;
  // Color
  background: $bg-color;
  // Stick to top of screen
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  // Overlay navbar
  z-index: $navbar-content;
  // Border
  box-shadow: 0 0 5px $box-shadow;

  #navbar-brand {
    // Flexbox for alignment
    display: flex;
    justify-content: center;
    align-items: center;
    // Remove effects of router link
    text-decoration: none;
    color: $font-color;

    #navbar-logo {
      // Sizing
      height: clamp(3rem, 1.8rem + 4.8vw, 6rem);
      // Spacing
      margin-right: 16px;
    }

    #navbar-text {
      #navbar-title {
        // Typography
        font-size: clamp(1.25rem, 1rem + 1vw, 1.875rem);
        font-weight: bold;

        #navbar-title-highlight {
          // Typography
          color: $accent-teal;
        }
      }

      #navbar-subtitle {
        // Typography
        font-family: $alt-font;
        font-size: clamp(0.85rem, 0.69rem + 0.64vw, 1.25rem);
      }
    }
  }

  #navbar-links {
    // Typography
    font-family: $alt-font;
    font-size: $caption-font-size;
    // Sizing
    height: 100%;
    // Flexbox for layout
    display: flex;
    justify-content: center;
    align-items: center;

    #navbar-user-nav {
      .navbar-user-link {
        // Remove effects of router link
        color: $font-color;
        text-decoration: none;
        // Spacing
        margin: 16px;
      }
    }

    #navbar-hamburger {
      // Flexbox for layout
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      // Spacing
      margin: 0 16px;
      // Clickable
      cursor: pointer;

      .navbar-hamburger-line {
        // Color styling
        background: $accent-grey;
        // Sizing
        height: 3px;
        width: 30px;
        // Spacing
        margin: 0.2rem 0;
        // Remove default styling
        border: none;
      }
    }
  }
}

// Handle sticky hover
@media (hover: hover) {
  #navbar > #navbar-links > #navbar-hamburger {
    &:hover .navbar-hamburger-line {
      // Animate
      margin: 0.3rem 0;
    }

    .navbar-hamburger-line {
      // Smooth animation
      transition: margin 0.3s ease;
    }
  }
}

// Smaller layouts
@media screen and (max-width: 1023px) {
  #navbar > #navbar-links > #navbar-user-nav {
    // Hide on small displays
    display: none;
  }
}
</style>
