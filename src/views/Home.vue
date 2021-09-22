<template>
  <div id="home">
    <div id="home-carousel">
      <div id="home-carousel-slides">
        <img class="home-carousel-slide" src="@/assets/img/Home/home1.png" />
        <img class="home-carousel-slide" src="@/assets/img/Home/home7.png" />
      </div>
      <div
        id="home-carousel-left"
        class="home-carousel-nav"
        @click="handleCarouselNav(-1)"
      >
        <i class="home-carousel-arrow fas fa-chevron-left" />
      </div>
      <div
        id="home-carousel-right"
        class="home-carousel-nav"
        @click="handleCarouselNav(1)"
      >
        <i class="home-carousel-arrow fas fa-chevron-right" />
      </div>
      <div id="home-nav">
        <router-link to="/explore" class="home-nav-button">
          Explore the Archive
        </router-link>
        <router-link to="/submit" class="home-nav-button">
          Submit to the Archive
        </router-link>
      </div>
    </div>
    <div id="home-featured">
      <p id="home-featured-header">FEATURED</p>
      <div id="home-featured-content">
        <div id="home-featured-left" class="home-featured-entry">
          <HoverPanel
            header="Endless Sorrow"
            subheader="David Greenfield (USA), 1981"
          />
        </div>
        <div id="home-featured-mid-top" class="home-featured-entry">
          <HoverPanel
            header="Endless Sorrow"
            subheader="David Greenfield (USA), 1981"
          />
        </div>
        <div id="home-featured-mid-bottom-left" class="home-featured-entry">
          <HoverPanel
            header="I Will Bury My Love Around You 2"
            subheader="Thamur Mejri (Tunisia), 2018"
          />
        </div>
        <div id="home-featured-mid-bottom-right" class="home-featured-entry">
          <HoverPanel
            header="Refuge 5"
            subheader="Basel Uraiqat (Jordan), 2018"
          />
        </div>
        <div id="home-featured-right" class="home-featured-entry">
          <div id="home-featured-right-caption">
            <p id="home-featured-right-subheader">
              March 1, 2021-March 31, 2021
            </p>
            <p id="home-featured-right-header">
              ARTIST IN RESIDENCE: QAIS AL-SINDY
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// Import global components
import HoverPanel from "@/components/global/HoverPanel";

export default {
  name: "Home",
  components: {
    HoverPanel,
  },
  data() {
    return {
      index: 0,
    };
  },
  methods: {
    // Carousel functions
    handleCarouselNav(inc) {
      // Edge cases
      if (inc !== 1 && inc !== -1)
        console.log("changeSlides() in Home.vue is being used incorrectly");
      // Left bound
      else if (inc === -1 && !this.index) return;
      // Right bound
      else if (inc === 1 && this.index === 1) return;
      this.index += inc;
      // Move slides
      this.handleSlides();
    },
    handleSlides() {
      // Slide
      document.getElementById("home-carousel-slides").style.marginLeft =
        -this.index * 0.8 * window.innerWidth + "px";
    },
  },
  mounted() {
    window.addEventListener("resize", this.handleSlides);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleSlides);
  },
};
</script>

<style scoped lang="scss">
#home {
  // Flexbox for alignment
  display: flex;
  flex-direction: column;
  align-items: center;

  #home-carousel {
    // Sizing
    width: 80%;
    height: 30rem;
    // Positioning for nav buttons
    position: relative;
    // Spacing
    margin-top: 48px;
    margin-bottom: 16px;
    // Hide excess slides
    overflow-x: hidden;

    #home-carousel-slides {
      // Sizing
      width: 100%;
      height: 100%;
      // Flexbox for layout
      display: flex;
      // Transition slides
      transition: margin-left 0.5s ease;

      .home-carousel-slide {
        // Preserve aspect ratio
        object-fit: cover;
        // Force cover
        min-width: 100%;
      }
    }

    .home-carousel-nav {
      // Positioning for overlay
      position: absolute;
      top: 0;
      // Sizing
      height: 100%;
      // Style background
      background: black;
      opacity: 0.5;
      // Inner spacing
      padding: 0 24px;
      // Flexbox for centering
      display: flex;
      align-items: center;
      // Clickable
      cursor: pointer;

      .home-carousel-arrow {
        // Icon styling
        color: white;
        font-size: 2rem;
      }
    }

    #home-carousel-left {
      // Positioning
      left: 0;
    }

    #home-carousel-right {
      // Positioning
      right: 0;
    }

    #home-nav {
      // Sizing
      width: 100%;
      // Positioning for overlay
      position: absolute;
      right: 80px;
      bottom: 0;
      // Flexbox for layout
      display: flex;
      justify-content: flex-end;
      align-items: center;

      .home-nav-button {
        // Button styling
        background: $accent-dark-teal;
        padding: 10px 4px;
        border-radius: 10px;
        width: 240px;
        // Typography
        font-family: $alt-font;
        font-weight: $bold;
        font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
        color: white;
        text-align: center;
        // Remove effects of router link
        text-decoration: none;
        // Spacing
        margin: 16px 8px;
      }
    }
  }

  #home-featured {
    // Sizing
    width: 100%;
    // Flexbox for layout
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    // Spacing
    margin-top: 64px;

    #home-featured-header {
      // Typography
      font-size: $subheader-font-size;
      font-weight: bold;
    }

    #home-featured-content {
      // Grid for layout
      display: grid;
      grid-gap: 16px;
      grid-template-columns: repeat(4, 1fr);
      grid-template-rows: repeat(2, 1fr);
      // Sizing
      width: calc(min(100%, 1400px));
      height: 640px;
      // Spacing
      padding: 16px 64px;
      margin-bottom: 32px;

      .home-featured-entry {
        // Image aspect ratio
        background-size: cover;
        background-repeat: none;
      }

      #home-featured-left {
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

      #home-featured-mid-top {
        // Grid positioning
        grid-row-start: 1;
        grid-row-end: 2;
        grid-column-start: 2;
        grid-column-end: 4;
        // Image
        background-image: url("../assets/img/Home/home3.png");
      }

      #home-featured-mid-bottom-left {
        // Grid positioning
        grid-row-start: 2;
        grid-row-end: 3;
        grid-column-start: 2;
        grid-column-end: 3;
        // Image
        background-image: url("../assets/img/Home/home4.png");
      }

      #home-featured-mid-bottom-right {
        // Grid positioning
        grid-row-start: 2;
        grid-row-end: 3;
        grid-column-start: 3;
        grid-column-end: 4;
        // Image
        background-image: url("../assets/img/Home/home5.png");
      }

      #home-featured-right {
        // Grid positioning
        grid-column-start: 4;
        grid-row-start: 1;
        grid-row-end: 3;
        // Image
        background-image: url("../assets/img/Home/home6.png");
        // Positioning for children
        position: relative;

        #home-featured-right-caption {
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

          #home-featured-right-header {
            // Typography
            text-transform: uppercase;
            font-size: $subheader-font-size;
            font-weight: bold;
            letter-spacing: 1px;
          }

          #home-featured-right-subheader {
            // Typography
            font-family: $alt-font;
            font-size: $caption-font-size;
          }
        }
      }
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #home > #home-carousel {
    .home-carousel-nav:hover {
      // Animate
      opacity: 0.7;
    }

    #home-nav > .home-nav-button:hover {
      // Animate
      background: $accent-light-teal;
    }
  }
}

// Mobile layout
@media screen and (max-width: 1023px) {
  #home {
    #home-carousel {
      .home-carousel-nav {
        // Hide nav
        display: none;
      }

      #home-nav {
        // Column layout
        flex-direction: column;
        left: 50%;
        margin-left: -50%;

        .home-nav-button {
          // Resize
          width: 192px;
        }
      }
    }

    #home-featured > #home-featured-content {
      // Simpler layout
      display: flex;
      justify-content: center;

      .home-featured-entry {
        // Hide
        display: none;
      }

      #home-featured-right {
        // Resize
        width: 100%;
        // Show
        display: block;
      }
    }
  }
}
</style>
