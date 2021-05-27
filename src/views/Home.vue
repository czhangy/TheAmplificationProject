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
      Together, let's create a more diverse and inclusive story of border
      crossing, refuge, and belonging.
    </p>
    <div class="home-featured">
      <h3 class="home-featured-header">featured</h3>
      <div class="home-featured-content">
        <div class="home-featured-left">
          <h4 class="home-featured-left-header">march 2</h4>
          <h5 class="home-featured-left-subheader">
            an interview with
            <br />kathy carbone
          </h5>
          <p class="home-featured-left-content">
            Hear from co-founder Dr. Kathy Carbone about the archive and its
            founding.
          </p>
          <img
            src="@/assets/img/test2.png
          "
            alt="Image of Kathy Carbone"
            class="home-featured-left-img"
          />
        </div>
        <div class="home-featured-mid-top"></div>
        <div class="home-featured-mid-bottom"></div>
        <div class="home-featured-right"></div>
      </div>
    </div>
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
  // Flexbox for alignment
  display: flex;
  flex-direction: column;
  align-items: center;

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

  .home-featured {
    // Sizing
    width: 100%;
    // Flexbox for layout
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .home-featured-header {
      // Typography
      text-transform: uppercase;
      font-size: $subheader-font-size;
    }

    .home-featured-content {
      // Grid for layout
      display: grid;
      grid-gap: 2rem;
      grid-template-columns: 23% auto auto 23%;
      grid-template-rows: auto auto auto auto;
      // Sizing
      width: 100%;
      height: 40rem;
      // Spacing
      padding: 1rem;
      margin-bottom: 2rem;

      .home-featured-left {
        // Background
        background: white;
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 5;
        grid-column-start: 1;
        grid-column-end: 2;
        // Border
        border: 1px solid $accent-grey;
        // Flexbox for layout
        display: flex;
        flex-direction: column;
        align-items: center;

        .home-featured-left-header {
          // Container color
          background: $accent-teal;
          // Typography
          text-align: center;
          font-size: $subheader-font-size;
          color: white;
          text-transform: uppercase;
          // Container sizing
          padding: 2rem 0;
          width: 100%;
        }

        .home-featured-left-subheader {
          // Typography
          text-align: center;
          font-size: $subheader-font-size;
          text-transform: uppercase;
          // Spacing
          margin-top: 1rem;
          margin-bottom: 2rem;
          width: 100%;
        }

        .home-featured-left-content {
          // Typography
          font-family: $alt-font;
          font-size: $caption-font-size;
          text-align: center;
          // Spacing
          margin: 0 3rem;
        }

        .home-featured-left-img {
          margin-top: 5rem;
        }
      }

      .home-featured-mid-top {
        background: green;
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 3;
        grid-column-start: 2;
        grid-column-end: 4;
      }

      .home-featured-mid-bottom {
        background: purple;
        // Grid positioning
        grid-row-start: 3;
        grid-row-end: 5;
        grid-column-start: 2;
        grid-column-end: 4;
      }

      .home-featured-right {
        background: yellow;
        // Grid positioning
        grid-column-start: 4;
        grid-row-start: 1;
        grid-row-end: 5;
      }
    }
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
