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
      <div class="navbar-hamburger">
        <span v-for="i in 3" :key="i" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar",
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
}
</style>
