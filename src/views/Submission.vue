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
        :fileType="submissionData.fileData.fileType"
      />
    </div>
    <div class="page" v-if="curPage === 2 || curPage === 4">
      <ContributionBasics
        :submissionData="submissionData.contributionData"
        :disabled="curPage === 4"
        :fileType="submissionData.fileData.fileType"
      />
    </div>
    <div class="page" v-if="curPage === 3 || curPage === 4">
      <ContributionDetails
        :submissionData="submissionData.contributionData"
        :disabled="curPage === 4"
        :fileType="submissionData.fileData.fileType"
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
    <div id="submit-error" v-if="error">Please fill in all required fields!</div>
    <div id="nav-buttons">
      <button v-if="curPage > 0" @click="handleNavClick(-1)">Back</button>
      <button v-if="curPage < pages.length - 1" @click="handleNavClick(1)">
        Next
      </button>
      <button v-else @click="handleSubmit">Submit</button>
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
      // Page labels
      pages: [
        "File Upload",
        "Personal Details",
        "Contribution Basics",
        "Contribution Details",
        "Review & Submit",
      ],
      // Page state
      curPage: 0,
      error: false,
      testing: false,
      // Checkboxes on review page
      checkboxes: {
        publish: false,
        private: false,
        agreement: false,
      },
      // Form data
      submissionData: {
        fileData: {
          files: [],
          fileType: null,
        },
        personalData: {
          email: "",
          creator: {
            firstNames: [],
            lastNames: [],
            bio: "",
            website: "",
            facebook: "",
            twitter: "",
            insta: "",
          },
          contributor: {
            firstNames: [],
            lastNames: [],
            bio: "",
            website: "",
            facebook: "",
            twitter: "",
            insta: "",
          },
        },
        contributionData: {
          title: "",
          completionYear: "",
          language: "",
          city: "",
          country: "",
          location: null,
          description: "",
          size: "",
          mediums: "",
          duration: "",
          rights: "",
          tags: [],
        },
      },
    };
  },
  methods: {
    handleSubmit: function () {
      alert("This feature needs to be implemented still");
    },
    // File type select functions
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
    // Page navigation functions
    handleBarClick: function (i) {
      // Handle page scroll
      this.curPage = i;
      window.scrollTo(0, 0);
    },
    handleNavClick: function (inc) {
      // Check and set error
      if (!this.testing && inc === 1 && !this.handleFormValidation()) {
        this.error = true;
        return;
      }
      this.error = false;
      this.curPage += inc;
      window.scrollTo(0, 0);
    },
    handleFormValidation: function () {
      // Validate file upload page
      if (this.curPage === 0) {
        let obj = this.submissionData.fileData;
        return obj.files.length > 0 && obj.fileType !== null;
        // Validate personal info page
      } else if (this.curPage === 1) {
        let obj = this.submissionData.personalData;
        return obj.email !== "" && obj.creator.firstNames.length > 0;
      } else if (this.curPage === 2) {
        let obj = this.submissionData.contributionData;
        return (
          obj.title !== "" && obj.completionYear !== "" && obj.location !== null
        );
      } else if (this.curPage === 3) {
        let obj = this.submissionData.contributionData;
        return obj.rights !== "" && obj.tags.length > 0;
      } else
        console.log("An invalid page was accessed in handleFormValidation()");
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
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  justify-content: center;

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
    margin: 48px auto 0 auto;
    // Sizing
    width: 80%;

    .fa-info-circle {
      // Clickable
      cursor: pointer;
      // Icon styling
      color: $accent-teal;
      font-size: $subheader-font-size;
      // Spacing
      margin-left: 10px;
      // Positioning for tooltips
      position: relative;
    }

    .section-header {
      // Flexbox for layout
      display: flex;
      align-items: center;
      // Sizing
      max-width: 640px;

      p {
        // Typography
        font-size: $subheader-font-size;
        font-weight: bold;
      }

      .fa-asterisk {
        // Icon styling
        color: red;
        font-size: calc(clamp(0.4rem, 0.28rem + 0.48vw, 0.7rem));
        // Spacing
        margin-left: 4px;
        margin-bottom: 16px;
      }
    }

    .section-field {
      // Flexbox for layout
      display: flex;
      align-items: center;
      // Spacing
      margin-top: 20px;
      margin-bottom: 48px;
      // Sizing
      width: min(400px, 100%);

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
      margin-bottom: 16px;
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
          font-size: $subheader-font-size;
          // Spacing
          margin-right: 12px;
        }

        p {
          // Typography
          font-family: $alt-font;
          font-size: $body-font-size;
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
      margin-left: 10px;
    }
  }

  #checkboxes {
    // Centering
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

  #submit-error {
    // Typography
    color: red;
    font-size: 20px;
    // Spacing
    margin-top: 36px;
    // Centering
    text-align: center;
  }

  #nav-buttons {
    // Flexbox for centering
    display: flex;
    justify-content: center;

    button {
      // Spacing
      margin: 48px;
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

// Smaller layouts
@media screen and (max-width: 767px) {
  .submission {
    .fa-info-circle {
      // Hide tooltips
      display: none;
    }

    .page {
      .textarea-field {
        // Resize
        width: 100%;
      }
    }
  }
}
</style>