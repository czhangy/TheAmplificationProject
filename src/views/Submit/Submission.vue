<template>
  <div id="submission">
    <ProgressBar
      :labels="pages"
      :curPage="curPage"
      :maxPage="maxPage"
      :onClick="handleBubbleNav"
    />
    <FileUpload
      :submissionData="submissionData.fileData"
      :onClick="handleTypeSelect"
      :onUpload="handleFileSelect"
      :disabled="isReview"
      v-if="isFileUpload || isReview"
    />
    <PersonalDetails
      :submissionData="submissionData.personalData"
      :disabled="isReview"
      :fileType="submissionData.fileData.fileType"
      v-if="isPersonalDetails || isReview"
    />
    <ContributionBasics
      :submissionData="submissionData.contributionData"
      :disabled="isReview"
      :fileType="submissionData.fileData.fileType"
      v-if="isContributionBasics || isReview"
    />
    <ContributionDetails
      :submissionData="submissionData.contributionData"
      :disabled="isReview"
      :fileType="submissionData.fileData.fileType"
      v-if="isContributionDetails || isReview"
    />
    <div id="checkboxes" v-if="isReview">
      <div class="checkbox-field">
        <input
          id="publish-checkbox"
          class="checkbox"
          type="checkbox"
          v-model="checkboxes.publish"
        />
        <label class="checkbox-label" for="publish"
          >Publish my contribution on the web.</label
        >
      </div>
      <div class="checkbox-field">
        <input
          id="private"
          class="checkbox"
          type="checkbox"
          v-model="checkboxes.private"
        />
        <label class="checkbox-label" for="private"
          >Keep identity private.</label
        >
      </div>
      <div class="checkbox-field">
        <input
          id="agreement"
          class="checkbox"
          type="checkbox"
          v-model="checkboxes.agreement"
        />
        <label class="checkbox-label" for="agreement"
          >I agree to the
          <router-link class="checkbox-link" to="/termsandconditions"
            >Terms and Conditions</router-link
          >.</label
        >
      </div>
    </div>
    <p id="submit-error" v-if="error">Please fill in all required fields!</p>
    <div id="nav-buttons">
      <button
        class="nav-button"
        v-if="curPage > 0"
        @click="handleButtonNav(-1)"
      >
        Back
      </button>
      <button
        class="nav-button"
        v-if="curPage < pages.length - 1"
        @click="handleButtonNav(1)"
      >
        Next
      </button>
      <button class="nav-button" v-else @click="handleSubmit">Submit</button>
    </div>
  </div>
</template>

<script>
// Import global library
import Swal from "sweetalert2";

// Import local components
import ProgressBar from "./components/ProgressBar";
import FileUpload from "./components/FileUpload";
import PersonalDetails from "./components/PersonalDetails";
import ContributionBasics from "./components/ContributionBasics";
import ContributionDetails from "./components/ContributionDetails";

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
      maxPage: 0,
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
          collection: "",
          tags: [],
        },
      },
      fileContents: "",
    };
  },
  methods: {
    // Submission function
    handleSubmit: function () {
      // Alert about submission status
      Swal.fire({
        title: "Success!",
        text: "Your submission has been uploaded",
        icon: "success",
        confirmButtonColor: "#298A7E",
      })
        // Redirect to home page
        .then(this.$router.push({ path: "/" }));
    },
    // File type select functions
    handleTypeSelect: function (type) {
      // Disable select on summary page
      if (!this.isReview) {
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
    handleFileSelect: function (contents) {
      // Pass file contents from FileUpload
      this.fileContents = contents;
    },
    // Page navigation functions
    handleButtonNav: function (inc) {
      // Show error message if form incomplete
      if (inc === 1 && !this.handleFormValidation()) this.error = true;
      else {
        // Remove error
        this.error = false;
        // Move to next page
        this.curPage += inc;
        this.maxPage = Math.max(this.maxPage, this.curPage);
        // Scroll to top
        window.scrollTo(0, 0);
      }
    },
    handleBubbleNav: function (page) {
      // Check if page is in bounds
      if (page > this.maxPage) return;
      // Set curPage to clicked page
      this.curPage = page;
      // Scroll to top
      window.scrollTo(0, 0);
    },
    handleFormValidation: function () {
      // Breakpoint for testing
      if (this.testing) return true;
      // Validate file upload page
      if (this.isFileUpload) {
        let obj = this.submissionData.fileData;
        return obj.files.length > 0 && obj.fileType !== null;
        // Validate personal info page
      } else if (this.isPersonalDetails) {
        let obj = this.submissionData.personalData;
        return obj.email !== "" && obj.creator.firstNames.length > 0;
        // Validate contribution basics page
      } else if (this.isContributionBasics) {
        let obj = this.submissionData.contributionData;
        return (
          obj.title !== "" && obj.completionYear !== "" && obj.location !== null
        );
      } else if (this.isContributionDetails) {
        // Validate contribution details page
        let obj = this.submissionData.contributionData;
        return (
          obj.description !== "" && obj.rights !== "" && obj.tags.length > 0
        );
        // Lol
      } else
        console.log("An invalid page was accessed in handleFormValidation()");
    },
  },
  computed: {
    isFileUpload() {
      return this.curPage === 0;
    },
    isPersonalDetails() {
      return this.curPage === 1;
    },
    isContributionBasics() {
      return this.curPage === 2;
    },
    isContributionDetails() {
      return this.curPage === 3;
    },
    isReview() {
      return this.curPage === 4;
    },
  },
  updated() {
    // Keep icon styling constant between pages
    if (this.isFileUpload || this.isReview) this.handleIconStyling();
  },
};
</script>

<style lang="scss" scoped>
#submission {
  // Sizing
  width: 100%;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  justify-content: center;

  #checkboxes {
    // Centering
    margin: 0 auto;
    // Spacing
    margin-top: 32px;

    .checkbox-field {
      // Flexbox for alignment
      display: flex;
      align-items: center;
      // Spacing
      margin-bottom: 16px;

      .checkbox {
        // Spacing
        margin-right: 30px;
        // Sizing
        height: 24px;
        width: 24px;
      }

      .checkbox-label {
        // Typography
        font-size: $subheader-font-size;
        font-family: $alt-font;

        .checkbox-link {
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
    font-weight: bold;
    // Spacing
    margin-top: 36px;
    // Centering
    text-align: center;
  }

  #nav-buttons {
    // Flexbox for centering
    display: flex;
    justify-content: center;

    .nav-button {
      // Spacing
      margin: 48px;
      // Button styling
      padding: 0.625rem 2rem;
      background: $accent-teal;
      border-radius: 10px;
      // Typography
      font-family: $alt-font;
      font-weight: $bold;
      color: white;
      text-align: center;
      font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
      // Remove default button styling
      border: none;
      // Clickable
      cursor: pointer;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #submission > #nav-buttons > .nav-button:hover {
    // Animate
    background: $accent-dark-teal;
  }
}
</style>