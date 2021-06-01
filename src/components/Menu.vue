<template>
  <div class="menu-overlay" @click="closeMenu">
    <div class="menu">
      <div class="menu-header">
        EN | LANG
        <i class="fas fa-times" @click="closeMenu"></i>
      </div>
      <span class="menu-separator"></span>
      <router-link to="/about" class="menu-link"> About Us </router-link>
      <span class="menu-separator"></span>
      <router-link to="/news" class="menu-link"> News </router-link>
      <span class="menu-separator"></span>
      <router-link to="/events" class="menu-link"> Events </router-link>
      <span class="menu-separator"></span>
      <router-link to="/submit" class="menu-link">
        Submit to the Archive
      </router-link>
      <span class="menu-separator"></span>
      <router-link to="/browse" class="menu-link">
        Browse the Archive
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
    },
    closeMenu: function () {
      document.getElementsByClassName("menu")[0].style.boxShadow =
        "none";
      document.getElementsByClassName("menu-overlay")[0].style.top = "-100vh";
    },
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
    width: 30%;
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