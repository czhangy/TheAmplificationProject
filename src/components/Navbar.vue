<template>
  <div class="navbar">
    <router-link to="/" class="navbar-brand">
      <img
        src="@/assets/logo.png"
        alt="Amplification Project Logo"
        class="navbar-logo"
      />
      <div class="navbar-text">
        <h1 class="navbar-text-header">
          the <span> amplification </span> project
        </h1>
        <h2 class="navbar-text-caption">
          Digital Archive for Forced Migration
          <br />
          Contemporary Art & Activism
        </h2>
      </div>
    </router-link>
    <div class="navbar-links">
      <div v-if="windowWidth > 900">
        <router-link to="/" class="navbar-auth"> login </router-link>
        |
        <router-link to="/" class="navbar-auth"> register </router-link>
      </div>
      <div class="navbar-hamburger" @click="openNavMenu">
        <span v-for="i in 3" :key="i" />
      </div>
    </div>
    <Menu ref="menu" />
  </div>
</template>

<script>
import Menu from "@/components/Menu";
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
.navbar {
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

  .navbar-brand {
    // Flexbox for alignment
    display: flex;
    justify-content: center;
    align-items: center;
    // Remove effects of router link
    text-decoration: none;
    color: $font-color;

    .navbar-logo {
      // Sizing
      height: clamp(3rem, 1.800rem + 4.800vw, 6rem);
      // Spacing
      margin-right: 1rem;
    }

    .navbar-text {
      .navbar-text-header {
        // Typography
        text-transform: uppercase;
        font-size: clamp(1.25rem, 1rem + 1vw, 1.875rem);

        span {
          // Typography
          color: $accent-teal;
        }
      }

      .navbar-text-caption {
        // Typography
        font-family: $alt-font;
        font-weight: $normal;
        font-size: clamp(0.85rem, 0.69rem + 0.64vw, 1.25rem);
        font-style: italic;
      }
    }
  }

  .navbar-links {
    // Typography
    font-family: $alt-font;
    text-transform: uppercase;
    font-size: $caption-font-size;
    // Sizing
    height: 100%;
    // Flexbox for layout
    display: flex;
    justify-content: center;
    align-items: center;

    .navbar-auth {
      // Remove effects of router link
      color: $font-color;
      text-decoration: none;
      // Spacing
      margin: 1rem;
    }

    .navbar-hamburger {
      // Flexbox for layout
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      // Spacing
      margin: 0 1rem;
      // Clickable
      cursor: pointer;

      span {
        // Color styling
        background: $accent-grey;
        // Sizing
        height: 3px;
        width: 1.875rem;
        // Bar styling
        border-radius: 1px;
        // Create hamburger icon
        margin: 0.2rem 0;
        // Handle transition
        transition: margin 0.3s ease;
      }
    }
  }
}

// Media queries
// Handle sticky hover
@media (hover: hover) {
  .navbar {
    .navbar-links {
      .navbar-hamburger {
          &:hover span {
            margin: 0.3rem 0;
          }
      }
    }
  }
}
</style>
