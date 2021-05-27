<template>
  <div class="home">
    <div class="home-carousel">
      <div class="home-archive-buttons">
        <router-link to="/browse" class="home-archive-button">
          Browse the Archive
        </router-link>
        <router-link to="/submit" class="home-archive-button">
          Submit to the archive
        </router-link>
      </div>
    </div>
    <p class="home-description">
      The Amplification Project is a community-led participatory public digital
      archive for artists and activists to document, preserve, and share art and
      activism inspired, influenced, or affected by experiences of conflict and
      displacement.
      <br />
      <br />
      Together, let's create a more diverse and inclusive story of
      border crossing, refuge, and belonging.
    </p>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style scoped lang="scss">
.home {
  // Sizing
  width: 100%;
  padding: 0 8rem;

  .home-carousel {
    background-image: url("../assets/img/test1.png");
    background-repeat: none;
    background-size: cover;
    // Sizing
    width: 100%;
    height: 30rem;
    // Positioning
    position: relative;
    // Spacing
    margin: 1rem 0;

    .home-archive-buttons {
      // Sizing
      width: 100%;
      height: 10rem;
      // Positioning for overlay
      position: absolute;
      bottom: 0;
      // Flexbox for layout
      display: flex;
      justify-content: space-evenly;
      align-items: center;

      .home-archive-button {
        // Button styling
        background: $accent-dark-teal;
        opacity: 0.85;
        padding: 0.625rem 0;
        border-radius: 10px;
        width: 15rem;
        // Typography
        font-family: $alt-font;
        font-weight: $bold;
        color: white;
        text-align: center;
        // Remove effects of router link
        text-decoration: none;
        // Smooth hover animation
        transition: all 0.2s ease;
      }
    }
  }

  .home-description {
    // Typography
    font-family: $alt-font;
    font-size: $caption-font-size;
    // Sizing
    width: 95%;
    // Spacing
    margin-bottom: 2.5rem;
  }
}

// Media queries
// Sticky hover
@media (hover: hover) {
  .home {
    .home-carousel {
      .home-archive-buttons {
        .home-archive-button {
          &:hover {
            background: $accent-light-teal;
            opacity: 1;
            transform: scale(1.05);
          }
        }
      }
    }
  }
}
</style>
