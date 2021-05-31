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
      <router-link to="/" class="navbar-auth"> login </router-link>
      |
      <router-link to="/" class="navbar-auth"> register </router-link>
      <div class="navbar-hamburger" @click="openMenu">
        <span v-for="i in 3" :key="i" />
      </div>
    </div>
    <div class="nav-menu-overlay" @click="closeMenu">
      <div class="nav-menu">
        <div class="nav-menu-header">
          EN | LANG
          <i class="fas fa-times" @click="closeMenu"></i>
        </div>
        <span class="nav-menu-separator"></span>
        <router-link to="/about" class="nav-menu-link"> About Us </router-link>
        <span class="nav-menu-separator"></span>
        <router-link to="/news" class="nav-menu-link"> News </router-link>
        <span class="nav-menu-separator"></span>
        <router-link to="/events" class="nav-menu-link"> Events </router-link>
        <span class="nav-menu-separator"></span>
        <router-link to="/submit" class="nav-menu-link"> Submit to the Archive </router-link>
        <span class="nav-menu-separator"></span>
        <router-link to="/browse" class="nav-menu-link"> Browse the Archive </router-link>
        <span class="nav-menu-separator"></span>
        <router-link to="/support" class="nav-menu-link"> Support Us </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  data() {
    return {
      menuOpen: false,
    };
  },
  methods: {
    openMenu: function () {
      this.menuOpen = true;
      document.getElementsByClassName("nav-menu-overlay")[0].style.top = 0;
    },
    closeMenu: function () {
      this.menuOpen = false;
      document.getElementsByClassName("nav-menu-overlay")[0].style.top =
        "-100vh";
    },
  },
};
</script>

<style scoped lang="scss">
.navbar {
  // Sizing
  height: $navbar-height;
  width: 100%;
  // Spacing
  padding: 3rem 6rem;
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
  z-index: 9;

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
      height: 6rem;
      // Spacing
      margin-right: 1rem;
    }

    .navbar-text {
      .navbar-text-header {
        // Typography
        text-transform: uppercase;
        font-size: 1.875rem;

        span {
          // Typography
          color: $accent-teal;
        }
      }

      .navbar-text-caption {
        // Typography
        font-family: $alt-font;
        font-weight: $normal;
        font-size: 1.25rem;
        font-style: italic;
      }
    }
  }

  .navbar-links {
    // Typography
    font-family: $alt-font;
    text-transform: uppercase;
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
      }
    }
  }
  .nav-menu-overlay {
    // Position relative to navbar
    position: absolute;
    top: -100vh;
    left: 0;
    height: 100vh;
    width: 100vw;
    // Overlay all other elements
    z-index: 999;
    // Smooth animation
    transition: top 0.2s ease;

    .nav-menu {
      // Position relative to overlay
      position: absolute;
      top: 0;
      right: 6rem;
      width: 30%;
      // Color menu
      background: white;
      // Spacing
      padding: 1rem;
      // Flexbox for layout
      display: flex;
      flex-direction: column;
      align-items: center;

      .nav-menu-header {
        // Typography
        font-family: $alt-font;
        font-size: 1.2rem;
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        align-items: center;
        // Spacing
        margin-bottom: 2rem;
        // Sizing
        width: 100%;

        i {
          // Icon styling
          font-size: 3rem;
          color: black;
          // Clickable
          cursor: pointer;
        }
      }

      .nav-menu-link {
        // Typography
        font-size: $subheader-font-size;
        padding: 2rem;
        // Remove effects of router link
        color: $font-color;
        text-decoration: none;
        // Sizing
        width: 100%;
      }

      .nav-menu-separator {
        // Sizing
        height: 1px;
        width: 100%;
        background: lightgrey;
      }
    }
  }
}
</style>
