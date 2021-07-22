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
        :submissionData="submissionData"
        :onClick="handleTypeSelect"
      />
    </div>
    <div class="page" v-if="curPage === 1 || curPage === 4">
      <PersonalDetails :submissionData="submissionData" />
    </div>
    <div class="nav-buttons">
      <button v-if="curPage > 0" @click="handleNavClick(-1)">Back</button>
      <button v-if="curPage < pages.length - 1" @click="handleNavClick(1)">
        Next
      </button>
    </div>
  </div>
</template>

<script>
import ProgressBar from "@/components/Submission/ProgressBar";
import FileUpload from "@/components/Submission/FileUpload";
import PersonalDetails from "@/components/Submission/PersonalDetails";

export default {
  name: "Submission",
  components: {
    ProgressBar,
    FileUpload,
    PersonalDetails,
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
      submissionData: {
        submissionType: null,
        email: null,
        contributorFirstNames: [],
        contributorLastNames: [],
        creatorFirstNames: [],
        creatorLastNames: [],
        statements: null,
      },
    };
  },
  methods: {
    handleUnfinished: function () {
      alert("This feature needs to be implemented still");
    },
    handleTypeSelect: function (type) {
      this.submissionData.submissionType = type;
      this.handleIconStyling();
    },
    handleIconStyling: function () {
      let arr = document.getElementsByClassName("icon");
      // Set icon colors based on selection
      for (let i = 0; i < arr.length; i++)
        arr[i].style.color =
          i === this.submissionData.submissionType ? "#298A7E" : "grey";
    },
    handleBarClick: function (i) {
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

<style lang="scss" scoped>
.submission {
  width: 100%;

  .page {
    // Spacing + centering
    margin: 3rem auto 0 auto;
    // Sizing
    width: 80%;
  }

  .nav-buttons {
    // Flexbox for centering
    display: flex;
    justify-content: center;

    button {
      // Spacing
      margin: 3rem;
      // Button styling
      background: $accent-dark-teal;
      padding: 0.625rem 2rem;
      border-radius: 10px;
      // Typography
      font-family: $alt-font;
      font-weight: $bold;
      font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
      color: white;
      text-align: center;
      // Smooth hover animation
      transition: all 0.2s ease;
      // Remove default button styling
      border: none;
      // Clickable
      cursor: pointer;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  button {
    &:hover {
      transform: scale(1.05);
    }
  }

  .media-icon {
    &:hover {
      i,
      p {
        transform: scale(1.1);
      }
    }
  }
}
</style>