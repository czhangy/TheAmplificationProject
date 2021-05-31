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
      The Amplification Project is a public, participatory community-led digital
      archive of art and activism inspired, influenced, or affected by forced
      displacement. The Amplification Project offers a platform for artists,
      activists, and other cultural producers to document, preserve, and share
      work that narrates or contemplates lived or observed experiences of
      displacement and refugeehood.
      <br />
      <br />
      <b
        >Together let's create a more diverse and inclusive story of crossing
        borders, refuge, and belonging.</b
      >
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
            src="@/assets/img/test2.png"
            alt="Image of Kathy Carbone"
            class="home-featured-left-img"
          />
        </div>
        <div class="home-featured-mid-top">
          <HoverPanel
            header="Endless Sorrow"
            subheader="David Greenfield (USA), 1981"
          />
        </div>
        <div class="home-featured-mid-bottom-left">
          <HoverPanel
            header="I Will Bury My Love Around You 2"
            subheader="Thamur Mejri (Tunisia), 2018"
          />
        </div>
        <div class="home-featured-mid-bottom-right">
          <HoverPanel
            header="Refuge 5"
            subheader="Basel Uraiqat (Jordan), 2018"
          />
        </div>
        <div class="home-featured-right">
          <div class="home-featured-right-caption">
            <p class="home-featured-right-subheader">
              March 1, 2021-March 31, 2021
            </p>
            <h6 class="home-featured-right-header">
              ARTIST IN RESIDENCE: QAIS AL-SINDY
            </h6>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HoverPanel from "@/components/HoverPanel";
export default {
  name: "Home",
  components: {
    HoverPanel,
  },
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
    width: calc(min(100%, 1400px));
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
    width: calc(min(100%, 1400px));
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
      grid-gap: 1rem;
      grid-template-columns: 1fr 1fr 1fr 1fr;
      grid-template-rows: 1fr 1fr;
      // Sizing
      width: calc(min(100%, 1400px));
      height: 40rem;
      // Spacing
      padding: 1rem;
      margin-bottom: 2rem;
      
      .home-featured-left {
        // Background
        background: white;
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 3;
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
          margin-top: 3rem;
        }
      }

      .home-featured-mid-top {
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 2;
        grid-column-start: 2;
        grid-column-end: 4;
        // Image
        background-image: url("../assets/img/test3.png");
        background-repeat: none;
        background-size: cover;
      }

      .home-featured-mid-bottom-left {
        // Grid positioning
        grid-row-start: 2;
        grid-row-end: 3;
        grid-column-start: 2;
        grid-column-end: 3;
        // Image
        background-image: url("../assets/img/test4.png");
        background-repeat: none;
        background-size: cover;
      }

      .home-featured-mid-bottom-right {
        // Grid positioning
        grid-row-start: 2;
        grid-row-end: 3;
        grid-column-start: 3;
        grid-column-end: 4;
        // Image
        background-image: url("../assets/img/test5.png");
        background-repeat: none;
        background-size: cover;
      }

      .home-featured-right {
        // Grid positioning
        grid-column-start: 4;
        grid-row-start: 1;
        grid-row-end: 3;
        // Image
        background-image: url("../assets/img/test6.png");
        background-size: cover;
        background-repeat: none;
        // Positioning for children
        position: relative;

        .home-featured-right-caption {
          // Position in container
          position: absolute;
          bottom: 0;
          // Overlay effect
          background: rgba(0, 0, 0, 0.6);
          // Spacing
          padding: 2rem 1rem;
          // Sizing
          width: 100%;
          // Typography
          color: white;

          .home-featured-right-header {
            // Typography
            text-transform: uppercase;
            font-size: $subheader-font-size;
            letter-spacing: 1px;
          }

          .home-featured-right-subheader {
            // Typography
            font-family: $alt-font;
            font-size: $caption-font-size;
          }
        }
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
