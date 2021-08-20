<template>
  <div class="about">
    <div class="about-container">
      <div class="about-text">
        <h1>About</h1>
        <p>
          The Amplification Project is a public, participatory community-led
          digital archive of art and activism inspired, influenced, or affected
          by forced displacement. We offer artists, activists, and other
          cultural producers a platform to document, preserve, and share new or
          existing work that narrates or contemplates lived or observed
          experiences of forced displacement, crossing borders, seeking asylum,
          and refuge.
        </p>
        <br />
        <p>
          The Amplification Project was founded in 2019 by an international
          group of artists, archivists, activists, and curators (see Collective
          Advisory Group/Founding Members below).
        </p>
      </div>
      <div class="about-img" v-if="windowWidth > 900">
        <img
          src="@/assets/img/About/about1.jpg"
          alt="Nothing is True, Everything is Possible by Abbas Yousif, 2018"
        />
        <p>
          <em>Nothing is True, Everything is Possible</em> by Abbas Yousif,
          2018.
        </p>
      </div>
    </div>
    <div class="about-container">
      <div class="about-img" v-if="windowWidth > 900">
        <img
          src="@/assets/img/About/about2.png"
          alt="Refuge 2 by Basel Uraiqat, 2018"
        />
        <p><em>Refuge 2</em> by Basel Uraiqat, 2018</p>
      </div>
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
              preserving and providing a platform for new and existing art and
              activism related to experiences of conflict, forced displacement,
              asylum, and refuge
            </li>
            <li>
              disrupting public and political anti-refugee and xenophobic
              rhetoric
            </li>
            <li>
              challenging depersonalized and dehumanized media and political
              representations of asylum seekers and refugees
            </li>
            <li>
              mobilizing the archive to raise awareness about inequities and
              injustices imposed on refugees
            </li>
            <li>building solidarities and community</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="about-container">
      <div class="about-text">
        <h3>Ways to participate</h3>
        <p>
          <span class="about-text-emph">Submit</span> your work to the archive
          <br />
          <br />
          <span class="about-text-emph">Comment</span> on work in the archive
          <br />
          <br />
          <span class="about-text-emph">Join</span> our Collective Advisory
          Group and help manage the archive. For more information,
          <span>contact us: theamplificationproject@gmail.com</span>
        </p>
      </div>
      <div class="about-img" v-if="windowWidth > 900">
        <img
          src="@/assets/img/About/about3.png"
          alt="Mandela Project Venice: We Are Humanity by Lilli Muller, 2019"
        />
        <p><em>Mandela Project Venice: We Are Humanity</em> by Lilli Muller, 2019</p>
      </div>
    </div>
    <div class="about-gap">
      <span />
    </div>
    <div class="about-banner">
      <h2>Meet the Collective Advisory Group</h2>
      <h5><em>The Exiled-1</em>, by Qais Al-Sindy, 2015</h5>
    </div>
    <div class="about-headshots">
      <div class="about-headshot-card">
        <img src="@/assets/img/About/about5.png" alt="Kathy Carbone" />
        <p>
          <span>Kathy Carbone</span>
          <br />
          <br />
          Project Director, Archivist, Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img
          src="@/assets/img/About/about6.png"
          alt="Elizabeth Shoshany Anderson"
        />
        <p>
          <span>Elizabeth Shoshany Anderson</span>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img src="@/assets/img/About/about7.png" alt="Vukašin Nedeljković" />
        <p>
          <span>Vukašin Nedeljković</span>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img src="@/assets/img/About/about8.png" alt="Pinar Öğrenci" />
        <p>
          <span>Pinar Öğrenci</span>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img src="@/assets/img/About/about9.png" alt="Habibah (Biba) Sheikh" />
        <p>
          <span>Habibah (Biba) Sheikh </span>
          <br />
          <br />
          Founding Member
        </p>
      </div>
      <div class="about-headshot-card">
        <img src="@/assets/img/About/about10.png" alt="Nick Schwieterman" />
        <p>
          <span>Nick Schwieterman </span>
          <br />
          <br />
          PhD student in information studies
        </p>
      </div>
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

  .about-img {
    // Positioning
    position: relative;
    // Sizing
    width: 50%;

    img {
      // Sizing
      height: 100%;
      width: 100%;
      // Darken
      filter: brightness(70%);
    }

    p {
      // Typography
      color: white;
      font-family: $alt-font;
      // Positioning within container
      position: absolute;
      bottom: 0.5rem;
      right: 1.5rem;
    }
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
      padding: 2rem calc(clamp(2rem, -12.4rem + 25.6vw, 5rem));

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
        font-size: calc(clamp(1.5rem, -0.3rem + 3.2vw, 2.5rem));
        color: $accent-teal;
        // Spacing
        margin-bottom: 3rem;
      }

      h2 {
        // Typography
        font-size: calc(clamp(2rem, 1.4rem + 2.4vw, 3.5rem));
        margin-bottom: 3rem;
      }

      p {
        // Typography
        font-family: $alt-font;
        font-size: calc(clamp(1rem, 0.1rem + 1.6vw, 1.2rem));
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
        font-size: calc(clamp(1rem, 0.1rem + 1.6vw, 1.2rem));

        li {
          // Spacing
          margin-bottom: calc(clamp(1rem, -0.8rem + 3.2vw, 2rem));
          line-height: 1.6;
        }
      }
    }
  }

  .about-gap {
    // Spacing
    padding: calc(clamp(3rem, 1rem + 8vw, 8rem)) 0;
    // Flexbox for alignment
    display: flex;
    justify-content: center;

    span {
      // Color the separator
      background: grey;
      // Sizing
      height: 1px;
      width: 20vw;
    }
  }

  .about-banner {
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

    h2 {
      // Typography
      font-size: calc(clamp(2rem, 1.2rem + 3.2vw, 4rem));
      color: white;
    }

    h5 {
      // Positioning
      position: absolute;
      right: 1.5rem;
      bottom: 0;
      // Spacing
      margin-bottom: 1rem;
      // Typography
      font-family: $alt-font;
      font-weight: $normal;
      color: white;
      font-size: calc(clamp(0.8rem, 0.42rem + 1.52vw, 1.75rem));
    }
  }
  .about-headshots {
    // Flexbox for layout
    display: flex;
    justify-content: space-evenly;
    flex-wrap: wrap;
    // Spacing
    margin-top: 4rem;
    padding: 0 1rem;

    .about-headshot-card {
      // Flexbox for reasons
      display: flex;
      align-items: center;
      flex-direction: column;
      // Sizing
      width: 550px;
      // Spacing
      margin-bottom: 4rem;

      span {
        // Typography
        font-size: calc(clamp(1.5rem, 1.3rem + 0.8vw, 2rem));
        font-family: $main-font;
      }

      p {
        // Centering
        text-align: center;
        // Spacing
        margin-top: 1rem;
        // Typography
        font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
        font-family: $alt-font;
        font-weight: $normal;
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
