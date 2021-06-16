<template>
  <div class="about">
    <h2 class="about-header">About Us</h2>
    <div class="about-nav">
      <button class="about-nav-archive" @click="showArchive">
        the archive
      </button>
      <button class="about-nav-team" @click="showTeam">the team</button>
    </div>
    <div class="about-content">
      <div class="about-content-archive" v-if="mainBody">
        <h4 class="about-content-subheader">our mission</h4>
        <p>
          The mission of The Amplification Project: Digital Archive for Forced
          Migration, Contemporary Art, and Action is to document, preserve, and
          raise the visibility of art and activism inspired, influenced, or
          affected by forced migration.
          <br />
          <br />
          We are a community-led public participatory digital archive to which
          any artist and activist can preserve and share their work, and anyone
          with an account can comment on the archive's content. The
          Amplification Project was founded in 2019 by an international group of
          artists, archivists, activists, and curators (see Collective Advisory
          Group/Founding Members below). We are committed to:
        </p>
        <ul>
          <li>
            Preserving and providing a platform for new and existing artistic
            and activist productions related to forced migration
          </li>
          <li>
            Intervening in public and political anti-refugee and xenophobic
            rhetoric
          </li>
          <li>
            Being a counterpoint to the often depersonalized and dehumanized
            visual representation of asylum seekers and refugees in the media
          </li>
          <li>
            Using archiving to raise awareness about and speak to injustices
            around refugeehood and displacement
          </li>
          <li>
            Building community, fostering dialogue, and supporting artists' and
            activists' archiving needs
          </li>
          <li>
            Working hand-in-hand with and connecting local, national, and
            transnational art practices, activist projects, and conversations
            centered on forced migration issues
          </li>
        </ul>
        <h4 class="about-content-subheader">how to participate</h4>
        <p>
          <span>Submit your artwork or activist project to the archive.</span>
          <br />
          Click the Submit Your Work menu tab to submit materials easily (no
          registration necessary) and for more information about submitting to
          the archive. if you are submitting more than one item and want to
          group your items into a collection or need help to submit your
          material(s), contact us: theamplificationproject@gmail.com
          <br />
          <br />
          <span>Comment on art and activist projects in the archive.</span>
          <br />
          Create an account or login (in the top right of the menu).
          <br />
          <br />
          <span
            >Join our Collective Advisory Group and help manage the
            archive.</span
          >
          <br />
          For more information, contact us: theamplificationproject@gmail.com
        </p>
      </div>
      <div class="about-content-team" v-else></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      mainBody: true,
    };
  },
  methods: {
    showArchive: function () {
      // Toggle content
      this.mainBody = true;
      // Set color + decoration
      document.getElementsByClassName("about-nav-archive")[0].style.color =
        "#298A7E";
      document.getElementsByClassName("about-nav-team")[0].style.color =
        "black";
      document.getElementsByClassName(
        "about-nav-archive"
      )[0].style.textDecoration = "underline";
      document.getElementsByClassName(
        "about-nav-team"
      )[0].style.textDecoration = "none";
    },
    showTeam: function () {
      // Toggle content
      this.mainBody = false;
      // Set color + decoration
      document.getElementsByClassName("about-nav-team")[0].style.color =
        "#298A7E";
      document.getElementsByClassName("about-nav-archive")[0].style.color =
        "black";
      document.getElementsByClassName(
        "about-nav-team"
      )[0].style.textDecoration = "underline";
      document.getElementsByClassName(
        "about-nav-archive"
      )[0].style.textDecoration = "none";
    },
  },
  mounted() {
    this.showArchive();
  },
};
</script>

<style scoped lang="scss">
.about {
  // Container
  background: $bg-color;
  width: 100%;
  // Spacing
  padding: 0 clamp(3rem, -1.8rem + 19.2vw, 15rem);

  .about-header {
    // Sizing
    width: 100%;
    // Typography
    text-align: center;
    font-size: $header-font-size;
    // Spacing
    margin-top: $title-margin;
    margin-bottom: 2rem;
  }

  .about-nav {
    // Flexbox for alignment
    display: flex;
    justify-content: center;
    // Spacing
    margin-bottom: 2.5rem;

    button {
      // Remove default button styling
      border: none;
      background: transparent;
      // Typography
      font-family: $main-font;
      text-transform: uppercase;
      font-size: $subheader-font-size;
      // Clickable
      cursor: pointer;
      // Spacing
      margin: 0 2.5rem;
      // Transition
      transition: all 0.5s ease;
    }
  }

  .about-content {
    // Flexbox for alignment
    display: flex;
    align-items: center;
    flex-direction: column;
    // Spacing
    margin-bottom: 4rem;

    .about-content-subheader {
      // Typography
      text-transform: uppercase;
      font-size: $subheader-font-size;
      font-family: $main-font;
      color: black;
      // Spacing
      margin-bottom: 2rem;
    }

    .about-content-archive {
      // Typography
      font-family: $alt-font;
      font-size: $body-font-size;
      line-height: 1.6;
      // Flexbox for alignment
      display: flex;
      flex-direction: column;
      align-items: center;

      ul {
        // Spacing
        padding: 1rem 0;

        li {
          // Spacing
          margin: 0.5rem 0;
        }
      }

      span {
        font-weight: $bold;
      }
    }
  }
}
</style>
