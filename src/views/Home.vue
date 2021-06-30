<template>
  <div class="home">
    <div class="home-carousel">
      <div class="home-archive-buttons">
        <router-link to="/explore" class="home-archive-button">
          Explore the Archive
        </router-link>
        <router-link to="/submit" class="home-archive-button">
          Submit to the Archive
        </router-link>
      </div>
    </div>
    <div class="home-featured">
      <h3 class="home-featured-header">featured</h3>
      <div class="home-featured-content">
        <div class="home-featured-left">
          <HoverPanel
            header="Endless Sorrow"
            subheader="David Greenfield (USA), 1981"
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
  padding: 0 calc(clamp(2rem, -0.4rem + 9.6vw, 8rem));
  // Flexbox for alignment
  display: flex;
  flex-direction: column;
  align-items: center;

  .home-carousel {
    background-image: url("../assets/img/Home/home1.png");
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
      // Positioning for overlay
      position: absolute;
      bottom: 0;
      // Flexbox for layout
      display: flex;
      justify-content: flex-end;
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
        font-size: calc(clamp(0.8rem, 0.640rem + 0.640vw, 1.2rem));
        color: white;
        text-align: center;
        // Remove effects of router link
        text-decoration: none;
        // Smooth hover animation
        transition: all 0.2s ease;
        // Spacing
        margin: 1rem 0.5rem;
      }
    }
  }

  .home-featured {
    // Sizing
    width: 100%;
    // Flexbox for layout
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    // Spacing
    margin-top: 4rem;

    .home-featured-header {
      // Typography
      text-transform: uppercase;
      font-size: $subheader-font-size;
    }

    .home-featured-content {
      // Grid for layout
      display: grid;
      grid-gap: 1rem;
      grid-template-columns: repeat(4, 1fr);
      grid-template-rows: repeat(2, 1fr);
      // Sizing
      width: calc(min(100%, 1400px));
      height: 40rem;
      // Spacing
      padding: 1rem;
      margin-bottom: 2rem;

      .home-featured-left {
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 3;
        grid-column-start: 1;
        grid-column-end: 2;
        // Border
        border: 1px solid $accent-grey;
        // Image
        background-image: url("../assets/img/Home/home6.png");
      }

      .home-featured-mid-top {
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 2;
        grid-column-start: 2;
        grid-column-end: 4;
        // Image
        background-image: url("../assets/img/Home/home3.png");
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
        background-image: url("../assets/img/Home/home4.png");
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
        background-image: url("../assets/img/Home/home5.png");
        background-repeat: none;
        background-size: cover;
      }

      .home-featured-right {
        // Grid positioning
        grid-column-start: 4;
        grid-row-start: 1;
        grid-row-end: 3;
        // Image
        background-image: url("../assets/img/Home/home6.png");
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

// Mobile layout
@media screen and (max-width: 900px) {
  .home {
    .home-featured {
      .home-featured-content {
        display: flex;
        justify-content: center;

        .home-featured-left {
          display: none;
        }

        .home-featured-mid-top {
          display: none;
        }

        .home-featured-mid-bottom-left {
          display: none;
        }

        .home-featured-mid-bottom-right {
          display: none;
        }

        .home-featured-right {
          width: 100%;
        }
      }
    }
  }
}
</style>
