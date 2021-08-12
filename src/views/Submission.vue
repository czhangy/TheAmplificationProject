<template>
  <div class="submission">
    <ProgressBar
      :pages="pages"
      :active="curPage"
      :onClick="handleBarClick"
      :key="curPage"
    />
    <div class="page" v-if="curPage === 0 || curPage === 4">
      <FileUpload
        :submissionData="submissionData.fileData"
        :onClick="handleTypeSelect"
        :disabled="curPage === 4"
      />
    </div>
    <div class="page" v-if="curPage === 1 || curPage === 4">
      <PersonalDetails
        :submissionData="submissionData.personalData"
        :disabled="curPage === 4"
      />
    </div>
    <div class="page" v-if="curPage === 2 || curPage === 4">
      <ContributionBasics
        :submissionData="submissionData.imageData"
        :disabled="curPage === 4"
      />
    </div>
    <div class="page" v-if="curPage === 3 || curPage === 4">
      <ContributionDetails
        :submissionData="submissionData.contributionData"
        :disabled="curPage === 4"
      />
    </div>
    <div id="checkboxes" v-if="curPage === 4">
      <div class="field">
        <input type="checkbox" id="publish" v-model="checkboxes.publish" />
        <label for="publish">Publish my contribution on the web.</label>
      </div>
      <div class="field">
        <input type="checkbox" id="private" v-model="checkboxes.private" />
        <label for="private">Keep identity private.</label>
      </div>
      <div class="field">
        <input type="checkbox" id="agreement" v-model="checkboxes.agreement" />
        <label for="agreement"
          >I agree to the
          <router-link to="/termsandconditions"
            >Terms and Conditions.</router-link
          ></label
        >
      </div>
    </div>
    <div id="nav-buttons">
      <button v-if="curPage > 0" @click="handleNavClick(-1)">Back</button>
      <button v-if="curPage < pages.length - 1" @click="handleNavClick(1)">
        Next
      </button>
      <button v-else @click="handleUnfinished">Submit</button>
    </div>
  </div>
</template>

<script>
// Import local components
import ProgressBar from "@/components/Submission/ProgressBar";
import FileUpload from "@/components/Submission/FileUpload";
import PersonalDetails from "@/components/Submission/PersonalDetails";
import ContributionBasics from "@/components/Submission/ContributionBasics";
import ContributionDetails from "@/components/Submission/ContributionDetails";

export default {
  name: "Submission",
  components: {
    ProgressBar,
    FileUpload,
    PersonalDetails,
    ContributionBasics,
    ContributionDetails,
  },
  data() {
    return {
      pages: [
        "File Upload",
        "Personal Details",
        "Contribution Basics",
        "Contribution Details",
        "Review & Submit",
      ],
      curPage: 0,
      checkboxes: {
        publish: false,
        private: false,
        agreement: false,
      },
      submissionData: {
        fileData: {
          files: [],
          fileType: null,
        },
        personalData: {
          email: null,
          contributorFirstNames: [],
          contributorLastNames: [],
          creatorFirstNames: [],
          creatorLastNames: [],
          statements: null,
        },
        imageData: {
          title: null,
          set: null,
          date: null,
          language: null,
          city: null,
          country: null,
          exhibitCities: [],
          exhibitCountries: [],
          exhibitVenues: [],
          exhibitStartDates: [],
          exhibitEndDates: [],
          location: null,
        },
        contributionData: {
          description: null,
          tags: [],
          medium: null,
          format: "",
          rights: null,
        },
      },
    };
  },
  methods: {
    handleUnfinished: function () {
      alert("This feature needs to be implemented still");
    },
    handleTypeSelect: function (type) {
      // Disable select on summary page
      if (this.curPage !== 4) {
        this.submissionData.fileData.fileType = type;
        this.handleIconStyling();
      }
    },
    handleIconStyling: function () {
      let arr = document.getElementsByClassName("icon");
      // Set icon colors based on selection
      for (let i = 0; i < arr.length; i++)
        arr[i].style.color =
          i === this.submissionData.fileData.fileType ? "#298A7E" : "grey";
    },
    handleBarClick: function (i) {
      // Handle page scroll
      this.curPage = i;
      window.scrollTo(0, 0);
    },
    handleNavClick: function (inc) {
      this.curPage += inc;
      window.scrollTo(0, 0);
    },
  },
  updated() {
    // Keep icon styling constant between pages 0 and 4
    if (this.curPage === 0 || this.curPage === 4) this.handleIconStyling();
  },
};
</script>

<style lang="scss">
.submission {
  // Sizing
  width: 100%;

  button {
    // Button styling
    background: $accent-teal;
    border-radius: 10px;
    // Typography
    font-family: $alt-font;
    font-weight: $bold;
    color: white;
    text-align: center;
    // Remove default button styling
    border: none;
    // Clickable
    cursor: pointer;
  }

  .page {
    // Spacing + centering
    margin: 3rem auto 0 auto;
    // Sizing
    width: 80%;

    .fa-info-circle {
      // Clickable
      cursor: pointer;
      // Icon styling
      color: $accent-teal;
      font-size: $subheader-font-size;
      // Spacing
      margin-left: 0.6rem;
      // Positioning for tooltips
      position: relative;
    }

    .section-header {
      // Flexbox for layout
      display: flex;
      align-items: center;
      // Sizing
      max-width: 40rem;

      p {
        // Typography
        font-size: $subheader-font-size;
        font-weight: bold;
      }

      .fa-asterisk {
        // Icon styling
        color: red;
        font-size: 0.7rem;
        // Spacing
        margin-left: 0.3rem;
        margin-bottom: 1rem;
      }
    }

    .section-field {
      // Flexbox for layout
      display: flex;
      align-items: center;
      // Spacing
      margin-top: 1rem;
      margin-bottom: 3rem;
      // Sizing
      width: 25rem;

      input,
      textarea,
      select {
        // Typography
        font-family: $alt-font;
        // Inner spacing
        padding: 0.5rem;
      }

      textarea {
        // Sizing
        width: 90%;
        height: 10rem;
      }

      .input-fields {
        // Sizing
        width: 90%;
        // Flexbox for layout
        display: flex;
        align-items: center;
        justify-content: space-between;

        input {
          // Sizing
          width: 48%;
        }
      }
    }

    .textarea-field {
      // Overwrite sizing
      width: 80%;
    }

    .grouped-field {
      // Spacing
      margin-bottom: 1rem;
    }

    .add-container {
      // Limit width
      display: inline-block;
      // Clickable
      cursor: pointer;

      .add-button {
        // Typography
        color: $accent-teal;
        // Flexbox for alignment
        display: flex;
        justify-content: flex-start;
        align-items: center;

        .fa-plus-circle {
          // Icon sizing
          font-size: 1.5rem;
          // Spacing
          margin-right: 0.7rem;
        }

        p {
          // Typography
          font-family: $alt-font;
        }
      }
    }

    .fa-times-circle {
      // Clickable
      cursor: pointer;
      // Icon styling
      color: red;
      font-size: $subheader-font-size;
      // Spacing
      margin-left: 0.6rem;
    }
  }

  #checkboxes {
    width: 500px;
    // Sizing
    margin: 0 auto;
    // Spacing
    margin-top: 32px;

    .field {
      // Flexbox for alignment
      display: flex;
      align-items: center;
      // Spacing
      margin-bottom: 16px;

      input[type="checkbox"] {
        // Spacing
        margin-right: 30px;
        // Sizing
        height: 24px;
        width: 24px;
      }

      label {
        // Typography
        font-size: $subheader-font-size;
        font-family: $alt-font;

        a {
          // Typography
          color: $accent-teal;
          text-decoration: none;
        }
      }

      &:last-child {
        // Remove spacing on bottom
        margin: 0;
      }
    }
  }

  #nav-buttons {
    // Flexbox for centering
    display: flex;
    justify-content: center;

    button {
      // Spacing
      margin: 3rem;
      // Button styling
      padding: 0.625rem 2rem;
      // Typography
      font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
    }
  }
}

.pointer {
  // Clickable
  cursor: pointer;
}

// Sticky hover
@media (hover: hover) {
  button {
    &:hover {
      // Animate
      background: $accent-dark-teal;
    }
  }
}
</style>