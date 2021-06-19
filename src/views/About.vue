<template>
  <div class="about">
    <div class="about-container">
      <div class="about-text">
        <h1>ABOUT</h1>
        <h2>THE AMPLIFICATION PROJECT</h2>
        <p>
          The Amplification Project is a community-led participatory public
          digital archive for artists and activists to document, preserve, and
          share art and activism inspired, influenced, or affected by
          experiences of conflict and displacement.
        </p>
      </div>
      <img
        src="@/assets/img/about1.png"
        alt="A New Generation of Forced Migration"
        v-if="windowWidth > 900"
      />
    </div>
    <div class="about-container">
      <img
        src="@/assets/img/about2.png"
        alt="REPLACE ME"
        v-if="windowWidth > 900"
      />
      <div class="about-text">
        <div v-if="!altPanel || windowWidth < 900" class="about-mission-panel">
          <div class="about-mission-nav">
            <h3>Mission</h3>
            <button @click="togglePanel" v-if="windowWidth > 900">
              <i class="fas fa-arrow-right"></i>
            </button>
          </div>
          <p>
            The mission of The Amplification Project: Digital Archive for Forced
            Migration, Contemporary Art, and Action is to
            <span
              >document, preserve, and raise the visibility of art and activism
              inspired, influenced, or affected by forced migration.</span
            >
            <br />
            <br />
            We are a community-led public participatory digital archive to which
            any artist and activist can preserve and share their work, and
            anyone with an account can comment on the archive's content. The
            Amplification Project was founded in 2019 by an international group
            of artists, archivists, activists, and curators (see Collective
            Advisory Group/Founding Members below).
          </p>
        </div>
        <div v-if="altPanel || windowWidth < 900" class="about-mission-panel">
          <div class="about-mission-nav">
            <button @click="togglePanel" v-if="windowWidth > 900">
              <i class="fas fa-arrow-left"></i>
            </button>
            <h3>We are committed to:</h3>
          </div>
          <ul>
            <li>
              preserving and providing a platform for new and existing artistic
              and activist productions related to forced migration
            </li>
            <li>
              in public and political anti-refugee and xenophobic rhetoric
            </li>
            <li>
              being a counterpoint to the often depersonalized and dehumanized
              visual representation of asylum seekers and refugees in the media
            </li>
            <li>
              using archiving to raise awareness about and speak to injustices
              around refugeehood and displacement
            </li>
            <li>
              building community, fostering dialogue, and supporting artists'
              and activists' archiving needs
            </li>
          </ul>
        </div>
      </div>
    </div>
    <div class="about-container">
      <div class="about-text">
        <h3>Ways to Participate</h3>
        <p>
          <span class="about-text-emph">Submit</span> your artwork or activist
          project to the archive: Click the Submit menu tab to submit materials
          easily (no registration necessary).
          <br />
          <br />
          <span class="about-text-emph">Comment</span> on art and activist
          projects in the archive: Create an account or login (top right of each
          webpage).
          <br />
          <br />
          <span class="about-text-emph">Join</span> our Collective Advisory
          Group and help manage the archive. For more information,
          <span>contact us: theamplificationproject@gmail.com</span>
        </p>
      </div>
      <img
        src="@/assets/img/about3.png"
        alt="REPLACE ME"
        v-if="windowWidth > 900"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      altPanel: false,
      windowWidth: window.innerWidth,
    };
  },
  methods: {
    togglePanel: function () {
      this.altPanel = !this.altPanel;
    },
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
.about {
  // Flexbox for layout
  display: flex;
  flex-direction: column;

  img {
    // Sizing
    width: 50%;
    height: 100%;
  }

  .about-container {
    // Flexbox for layout
    display: flex;

    .about-text {
      // Sizing
      width: 50%;
      // Flexbox for layout
      display: flex;
      flex-direction: column;
      justify-content: center;
      // Spacing
      padding: 0 calc(clamp(2rem, -12.400rem + 25.600vw, 5rem));

      .about-text-emph {
        color: $accent-teal;
      }

      .about-mission-nav {
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        align-items: flex-start;

        button {
          // Sizing
          height: 3rem;
          width: 3rem;
          font-size: $subheader-font-size;
          // Clickable
          cursor: pointer;
          box-shadow: 0 3px 5px $box-shadow;
          // Button shape
          border-radius: 50%;
          // Remove default button styling
          border: none;
        }
      }

      h1,
      h3 {
        // Typography
        font-size: calc(clamp(1.5rem, -0.300rem + 3.200vw, 2.5rem));
        color: $accent-teal;
        // Spacing
        margin-bottom: 3rem;
      }

      h2 {
        // Typography
        font-size: calc(clamp(2rem, 1.400rem + 2.400vw, 3.5rem));
        margin-bottom: 3rem;
      }

      p {
        // Typography
        font-family: $alt-font;
        font-size: calc(clamp(1rem, 0.100rem + 1.600vw, 1.2rem));
        // Spacing
        line-height: 1.8;
      }

      span {
        // Typography
        font-weight: $bold;
      }

      ul {
        // Spacing
        margin-top: 1.5rem;
        // Typography
        font-family: $alt-font;
        font-size: calc(clamp(1rem, 0.100rem + 1.600vw, 1.2rem));

        li {
          // Spacing
          margin-bottom: calc(clamp(1rem, -0.800rem + 3.200vw, 2rem));
          line-height: 1.6;
        }
      }
    }
  }
}

// Media queries
// Sticky hover
@media (hover: hover) {
  .about {
    .about-container {
      .about-text {
        .about-mission-nav {
          button {
            &:hover {
              // Animate
              transition: transform 0.2s ease;
              transform: scale(1.1);
            }
          }
        }
      }
    }
  }
}
// Mobile layout
@media screen and (max-width: $mobile) {
  .about {
    // Spacing
    margin: 2rem 0;
    .about-container {
      .about-text {
        // Reduce spacing
        padding: 0 2rem;
        // Sizing
        width: 100%;

        .about-mission-panel {
          margin: 2rem 0;

          ul {
            // Spacing
            margin: 0;
            padding: 0 2rem;
          }
        }
      }
    }
  }
}
</style>
