<template>
  <div id="about">
    <div id="about-grid">
      <div class="about-grid-container about-text-container">
        <p class="about-header">About</p>
        <p class="about-text">
          The Amplification Project is a public, participatory community-led
          digital archive of art and activism inspired, influenced, or affected
          by forced displacement. We offer artists, activists, and other
          cultural producers a platform to document, preserve, and share new or
          existing work that narrates or contemplates lived or observed
          experiences of forced displacement, crossing borders, seeking asylum,
          and refuge.
        </p>
        <br />
        <p class="about-text">
          The Amplification Project was founded in 2019 by an international
          group of artists, archivists, activists, and curators (see Collective
          Advisory Group/Founding Members below).
        </p>
      </div>
      <div class="about-grid-container about-img-container">
        <img
          class="about-img"
          src="@/assets/img/About/about1.jpg"
          alt="Nothing is True, Everything is Possible by Abbas Yousif, 2018"
        />
        <p class="about-img-caption">
          <em>Nothing is True, Everything is Possible</em> by Abbas Yousif,
          2018.
        </p>
      </div>
      <div class="about-grid-container about-img-container">
        <img
          class="about-img"
          src="@/assets/img/About/about2.png"
          alt="Refuge 2 by Basel Uraiqat, 2018"
        />
        <p class="about-img-caption">
          <em>Refuge 2</em> by Basel Uraiqat, 2018
        </p>
      </div>
      <div class="about-grid-container about-text-container">
        <div class="about-mission-panel" v-if="!altPanel || windowWidth < 1023">
          <div class="about-mission-header">
            <p class="about-header">Mission</p>
            <button class="about-mission-nav" @click="togglePanel">
              <i class="fas fa-arrow-right"></i>
            </button>
          </div>
          <p class="about-text">
            The mission of The Amplification Project: Digital Archive for Forced
            Migration, Contemporary Art, and Action is to
            <strong
              >document, preserve, and raise the visibility of art and activism
              inspired, influenced, or affected by forced migration.</strong
            >
          </p>
        </div>
        <div class="about-mission-panel" v-if="altPanel || windowWidth < 1023">
          <div class="about-mission-header">
            <button class="about-mission-nav" @click="togglePanel">
              <i class="fas fa-arrow-left" />
            </button>
            <p class="about-header">We are committed to:</p>
          </div>
          <ul id="about-mission-list">
            <li class="about-mission-entry">
              preserving and providing a platform for new and existing art and
              activism related to experiences of conflict, forced displacement,
              asylum, and refuge
            </li>
            <li class="about-mission-entry">
              disrupting public and political anti-refugee and xenophobic
              rhetoric
            </li>
            <li class="about-mission-entry">
              challenging depersonalized and dehumanized media and political
              representations of asylum seekers and refugees
            </li>
            <li class="about-mission-entry">
              mobilizing the archive to raise awareness about inequities and
              injustices imposed on refugees
            </li>
            <li class="about-mission-entry">
              building solidarities and community
            </li>
          </ul>
        </div>
      </div>
      <div class="about-grid-container about-text-container">
        <p class="about-header">Ways to participate</p>
        <p class="about-text">
          <strong class="about-text-emph">Submit</strong> your work to the
          archive
          <br />
          <br />
          <strong class="about-text-emph">Comment</strong> on work in the
          archive
          <br />
          <br />
          <strong class="about-text-emph">Join</strong> our Collective Advisory
          Group and help manage the archive. For more information,
          <strong>contact us: theamplificationproject@gmail.com</strong>
        </p>
      </div>
      <div class="about-grid-container about-img-container">
        <img
          class="about-img"
          src="@/assets/img/About/about3.png"
          alt="Mandela Project Venice: We Are Humanity by Lilli Muller, 2019"
        />
        <p class="about-img-caption">
          <em>Mandela Project Venice: We Are Humanity</em> by Lilli Muller, 2019
        </p>
      </div>
    </div>
    <div id="about-divider">
      <span id="about-line" />
    </div>
    <div id="about-banner">
      <p id="about-banner-header">Meet the Collective Advisory Group</p>
      <p id="about-banner-caption">
        <em>The Exiled-1</em>, by Qais Al-Sindy, 2015
      </p>
    </div>
    <div id="about-headshots">
      <div class="about-headshot-card">
        <img
          class="about-headshot"
          src="@/assets/img/About/about5.png"
          alt="Kathy Carbone"
        />
        <p class="about-headshot-caption">
          <strong>Kathy Carbone</strong>
          <br />
          <br />
          Project Director, Archivist, Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img
          class="about-headshot"
          src="@/assets/img/About/about6.png"
          alt="Elizabeth Shoshany Anderson"
        />
        <p class="about-headshot-caption">
          <strong>Elizabeth Shoshany Anderson</strong>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img
          class="about-headshot"
          src="@/assets/img/About/about7.png"
          alt="Vukašin Nedeljković"
        />
        <p class="about-headshot-caption">
          <strong>Vukašin Nedeljković</strong>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img
          class="about-headshot"
          src="@/assets/img/About/about8.png"
          alt="Pinar Öğrenci"
        />
        <p class="about-headshot-caption">
          <strong>Pinar Öğrenci</strong>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img
          class="about-headshot"
          src="@/assets/img/About/about9.png"
          alt="Habibah (Biba) Sheikh"
        />
        <p class="about-headshot-caption">
          <strong>Habibah (Biba) Sheikh </strong>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <p id="special-thanks">
        The Collective Advisory Group gives special thanks to Nick Schwieterman,
        students in UCLA's DH199: Designing the User-Centered Art Archive course
        (2020, 2021), Charles Zhang, Menachem Kornreich, Anne Gilliland, and
        James Lowry.
      </p>
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
    // Mission nav function
    handleTogglePanel: function () {
      this.altPanel = !this.altPanel;
    },
    // Event listener function
    handleWindowResize: function () {
      this.windowWidth = window.innerWidth;
    },
  },
  // Event listener
  mounted() {
    window.addEventListener("resize", this.handleWindowResize);
  },
  beforeUnmount() {
    window.removeEventListener("resize", this.handleWindowResize);
  },
};
</script>

<style scoped lang="scss">
#about {
  // Flexbox for layout
  display: flex;
  flex-direction: column;

  #about-grid {
    // Grid for layout
    display: grid;
    grid-template-rows: 1fr 1fr 1fr;
    grid-template-columns: 1fr 1fr;

    .about-grid-container {
      // Sizing
      width: 100%;
    }

    .about-text-container {
      // Flexbox for layout
      display: flex;
      flex-direction: column;
      justify-content: center;
      // Spacing
      padding: 2rem calc(clamp(2rem, -12.4rem + 25.6vw, 5rem));

      .about-header {
        // Typography
        font-size: calc(clamp(1.5rem, -0.3rem + 3.2vw, 2.5rem));
        font-weight: bold;
        color: $accent-teal;
        // Spacing
        margin-bottom: 48px;
      }

      .about-text {
        // Typography
        font-family: $alt-font;
        font-size: calc(clamp(1rem, 0.1rem + 1.6vw, 1.2rem));
        // Spacing
        line-height: 1.8;
      }

      .about-text-emph {
        // Typography
        color: $accent-teal;
      }

      .about-mission-panel {
        // Display
        display: block;

        .about-mission-header {
          // Flexbox for layout
          display: flex;
          justify-content: space-between;
          align-items: flex-start;

          .about-mission-nav {
            // Sizing
            height: 48px;
            width: 48px;
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

        #about-mission-list {
          // Spacing
          margin-top: 24px;
          // Typography
          font-family: $alt-font;
          font-size: calc(clamp(1rem, 0.1rem + 1.6vw, 1.2rem));

          .about-mission-entry {
            // Spacing
            margin-bottom: calc(clamp(1rem, -0.8rem + 3.2vw, 2rem));
            line-height: 1.6;
          }
        }
      }
    }

    .about-img-container {
      // Display
      display: block;
      // Positioning for children
      position: relative;
      // Sizing
      height: 1000px;

      .about-img {
        // Sizing
        height: 100%;
        width: 100%;
        // Darken
        filter: brightness(70%);
        // Preserve aspect ratio
        object-fit: cover;
      }

      .about-img-caption {
        // Typography
        color: white;
        font-family: $alt-font;
        // Positioning within container
        position: absolute;
        bottom: 8px;
        right: 24px;
      }
    }
  }

  #about-divider {
    // Spacing
    padding: calc(clamp(3rem, 1rem + 8vw, 8rem)) 0;
    // Flexbox for alignment
    display: flex;
    justify-content: center;

    #about-line {
      // Color the separator
      background: grey;
      // Sizing
      height: 1px;
      width: 20vw;
    }
  }

  #about-banner {
    // Background
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
      url("../assets/img/About/about4.png");
    background-size: cover;
    // Flexbox for alignment
    display: flex;
    align-items: center;
    flex-direction: column;
    // Positioning for children
    position: relative;
    // Spacing
    padding: 8rem calc(clamp(0.5rem, -0.1rem + 2.4vw, 2rem));
    // Centering
    text-align: center;

    #about-banner-header {
      // Typography
      font-size: calc(clamp(2rem, 1.2rem + 3.2vw, 4rem));
      font-weight: bold;
      color: white;
    }

    #about-banner-caption {
      // Positioning
      position: absolute;
      right: 24px;
      bottom: 0;
      // Spacing
      margin-bottom: 16px;
      // Typography
      font-family: $alt-font;
      font-weight: $normal;
      color: white;
      font-size: calc(clamp(0.8rem, 0.42rem + 1.52vw, 1.75rem));
    }
  }

  #about-headshots {
    // Flexbox for layout
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    // Spacing
    margin-top: 64px;
    padding: 0 16px;

    .about-headshot-card {
      // Flexbox for reasons
      display: flex;
      align-items: center;
      flex-direction: column;
      // Sizing
      width: 550px;
      // Spacing
      margin-bottom: 64px;

      .about-headshot-caption {
        // Centering
        text-align: center;
        // Spacing
        margin-top: 1rem;
        // Typography
        font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
        font-family: $alt-font;
        font-weight: $normal;

        strong {
          // Typography
          font-size: calc(clamp(1.5rem, 1.3rem + 0.8vw, 2rem));
          font-family: $main-font;
        }
      }
    }

    #special-thanks {
      // Sizing
      width: 70%;
      // Centering
      margin: 0 auto;
      text-align: center;
      // Typography
      font-family: $alt-font;
      // Spacing
      margin-bottom: 32px;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #about
    > #about-grid
    > .about-grid-container
    > .about-mission-panel
    > .about-mission-header
    > .about-mission-nav {
    // Smooth animation
    transition: transform 0.2s ease;

    &:hover {
      // Animate
      transform: scale(1.1);
    }
  }
}

// Smaller layout
@media screen and (max-width: 1023px) {
  #about {
    // Respace
    margin: 32px 0;

    #about-grid {
      // Column layout
      grid-template-rows: auto;
      grid-template-columns: 1fr;

      .about-text-container {
        // Reduce inner spacing
        padding: 0 2rem;
        // Add spacing
        margin: 2rem 0;

        .about-mission-panel {
          &:first-child {
            // Add spacing
            margin-bottom: 64px;
          }

          .about-mission-header > .about-mission-nav {
            // Hide on small displays
            display: none;
          }

          #about-mission-list {
            // Spacing
            margin: 0;
            padding: 0 32px;
          }
        }
      }

      .about-img-container {
        // Hide on small displays
        display: none;
      }
    }
  }
}
</style>
