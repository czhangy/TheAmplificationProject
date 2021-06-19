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
      <div class="about-content-team" v-else>
        <h4 class="about-content-subheader">collective advisory group</h4>
        <div class="about-content-team-panel">
          <img src="@/assets/img/test-grey.jpg" alt="Image Here" />
          <div>
            <h5>elizabeth shoshany anderson</h5>
            <h6>Founding Member</h6>
            <p>
              Assistant Curator at the Madison Museum of Contemporary Art, and
              the Lead Curator of Arts + Literature Laboratory, a
              community-driven contemporary non-profit arts organization. She
              also works to organize exhibitions for the Bubbler program through
              the City of Madison Public Library. Before joining MMoCA, Shoshany
              Anderson was Curator of Exhibitions and Collections at the Miller
              Art Museum in Sturgeon Bay, Wisconsin. Shoshany Anderson was
              previously based in London, where she held a Curatorial Internship
              at the Tate Modern. Additionally, she has served as a juror and
              guest curator on numerous panels and programs. Shoshany Anderson
              received her MA in Curating the Art Museum from the Courtauld
              Institute of Art in London, and a BA in Art History and Jewish
              Studies from the University of Wisconsin-Madison.
            </p>
          </div>
        </div>
        <div class="about-content-team-panel">
          <img src="@/assets/img/test-grey.jpg" alt="Image Here" />
          <div>
            <h5>kathy carbone</h5>
            <h6>Project Director, Archivist, Founding Member</h6>
            <p>
              Postdoctoral Scholar and Lecturer in the Department of Information
              Studies at the University of California, Los Angeles (UCLA).
              Before joining UCLA, she was the Institute Archivist and
              Performing Arts Librarian for over a decade at the California
              Institute of the Arts (CalArts) and a modern dancer and
              choreographer for more than 20 years. Carbone holds a Ph.D. in
              Information Studies from UCLA, an MLIS from Kent State University,
              and an MA in Dance and Music, and a BFA in Dance from Ohio
              University. Carbone’s interests broadly focus on intersections
              between archives, contemporary art, and activism, with particular
              emphasis on documenting and preserving art practice driven by
              human rights and social justice agendas and using archives as
              strategies and tools for expressive resistance and community
              building.
            </p>
          </div>
        </div>
        <div class="about-content-team-panel">
          <img src="@/assets/img/test-grey.jpg" alt="Image Here" />
          <div>
            <h5>vukašin nedeljković</h5>
            <h6>Founding Member</h6>
            <p>
              Vukašin holds a Masters in Visual Arts Practice at Dunlaoghaire
              Institute of Arts, Design and Technology. He has exhibited both
              nationally and internationally. His recent contributions include
              Reiterating Asylum Archive: Documenting Direct Provision in
              Ireland, (2018) and Asylum Archive: An Archive of Asylum and
              Direct Provision in Ireland, (2016-2017). He was awarded an Arts
              and Activism bursary from Arts Council in 2018/2019 and has
              recently published the monograph, Asylum Archive. He is currently
              writing a book with Dr. Ronit Lentin on Direct Provision,
              entitled, Disavowing Asylum: Documenting Ireland’s Asylum
              Industrial Complex. Vukašin Nedeljković initiated the
              multidisciplinary project Asylum Archive.
            </p>
          </div>
        </div>
        <div class="about-content-team-footer">
          <div class="about-content-team-card">
            <img src="@/assets/img/test-grey.jpg" alt="Image Here" />
            <h5>Pinar Öğrenci</h5>
            <h6>Founding Member</h6>
            <p>Artist and writer (Istanbul and Berlin).</p>
          </div>
          <div class="about-content-team-card">
            <img src="@/assets/img/test-grey.jpg" alt="Image Here" />
            <h5>Habibah (Biba) Sheikh</h5>
            <h6>Founding Member</h6>
            <p>Theater artist, curator, and activist (Detroit).</p>
          </div>
          <div class="about-content-team-card">
            <img src="@/assets/img/test-grey.jpg" alt="Image Here" />
            <h5>Nick Schwieterman</h5>
            <h6>Founding Member</h6>
            <p>PhD student in information studies (Los Angeles).</p>
          </div>
        </div>
      </div>
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
      transition: all 0.3s ease;
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

    .about-content-team {
      // Typography
      font-family: $alt-font;
      // Flexbox for alignment
      display: flex;
      flex-direction: column;
      align-items: center;

      .about-content-team-panel {
        // Flexbox for layout
        display: flex;
        justify-content: center;
        align-items: center;
        // Spacing
        margin-bottom: 2rem;
        // Typography
        line-height: 1.6;
      }

      .about-content-team-footer {
        // Flexbox for layout
        display: flex;
        justify-content: center;
        // Spacing
        margin: 2rem 0;

        .about-content-team-card {
          // Typography
          text-align: center;
          // Flexbox for alignment
          display: flex;
          justify-content: center;
          align-items: center;
          flex-direction: column;
          // Spacing
          margin: 0 1rem;

          img {
            // Resize
            width: 40%;
            // Remove margin
            margin-right: 0;
            // Spacing
            margin-bottom: 1rem;
          }
        }
      }

      img {
        // Shape to circle
        border-radius: 50%;
        // Sizing
        width: 15%;
        height: auto;
        // Teal border
        border: 3px solid $accent-teal;
        // Spacing
        margin-right: 4rem;
      }

      h5 {
        // Typography
        font-family: $main-font;
        text-transform: uppercase;
        font-size: 1.2rem;
      }

      h6 {
        // Typography
        color: $font-color;
        font-style: italic;
        font-size: $caption-font-size;
        font-weight: $normal;
      }
    }
  }
}

// Media queries
// Mobile layout
@media screen and (max-width: $mobile) {
  .about {
    .about-content {
      .about-content-team {
        .about-content-team-footer {
          // Change from row display to column
          flex-direction: column;
          // Remove excess spacing
          margin-bottom: 0;

          .about-content-team-card {
            // Spacing
            margin-bottom: 2rem;
            img {
              // Resize
              width: 60%;
            }
          }
        }
      }
    }
  }
}
</style>
