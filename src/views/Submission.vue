<template>
  <div class="submission">
    <ProgressBar
      :pages="pages"
      :active="curPage"
      :onClick="handleBarClick"
      :key="curPage"
    />
    <div class="page" v-if="curPage === 0">
      <div class="section-header">
        <p>Select item contribution type</p>
        <i class="fas fa-asterisk"></i>
        <i class="fas fa-info-circle" @click="handleUnfinished"></i>
      </div>
      <div class="media-icons">
        <div class="media-icon" @click="handleTypeSelect(0)">
          <i class="fas icon fa-file-alt"></i>
          <p>Text</p>
        </div>
        <div class="media-icon" @click="handleTypeSelect(1)">
          <i class="fas icon fa-image"></i>
          <p>Image</p>
        </div>
        <div class="media-icon" @click="handleTypeSelect(2)">
          <i class="fas icon fa-video"></i>
          <p>Video</p>
        </div>
        <div class="media-icon" @click="handleTypeSelect(3)">
          <i class="fas icon fa-volume-up"></i>
          <p>Audio</p>
        </div>
        <div class="media-icon" @click="handleTypeSelect(4)">
          <i class="fas icon fa-calendar-alt"></i>
          <p>Event</p>
        </div>
      </div>
      <div class="section-header">
        <p>File Upload</p>
        <i class="fas fa-asterisk"></i>
        <i class="fas fa-info-circle" @click="handleUnfinished"></i>
      </div>
      <div class="file-upload">
        <p>Drag & drop your files here</p>
        <span>OR</span>
        <button @click="handleUnfinished">Choose File</button>
      </div>
    </div>
    <div class="page" v-if="curPage === 1">
      <div class="section-header">
        <p>Email</p>
        <i class="fas fa-asterisk"></i>
      </div>
      <div class="section-field">
        <input placeholder="Your email" v-model="submissionData.email" />
        <i class="fas fa-info-circle" @click="handleUnfinished"></i>
      </div>
      <div class="section-header">
        <p>Name(s) of contributor(s)</p>
      </div>
      <div class="section-field">
        <div class="input-fields" v-for="i in numContributors" :key="i">
          <input placeholder="First name" v-model="submissionData.contributorFirstNames[i]" />
          <input placeholder="Last name" v-model="submissionData.contributorLastNames[i]" />
        </div>
        <i class="fas fa-info-circle" @click="handleUnfinished"></i>
      </div>
      <div class="section-header">
        <p>Name(s) of creator(s)</p>
      </div>
      <div class="section-field">
        <div class="input-fields" v-for="i in numCreators" :key="i">
          <input placeholder="First name" v-model="submissionData.creatorFirstNames[i]" />
          <input placeholder="Last name" v-model="submissionData.creatorLastNames[i]" />
        </div>
        <i class="fas fa-info-circle" @click="handleUnfinished"></i>
      </div>
      <div class="section-header">
        <p>
          Artist statements and/or biographies of creator(s) and contributor(s)
        </p>
      </div>
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
import ProgressBar from "@/components/ProgressBar";

export default {
  name: "Submission",
  components: {
    ProgressBar,
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
      numContributors: 1,
      numCreators: 1,
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
      let arr = document.getElementsByClassName("icon");
      for (let i = 0; i < arr.length; i++)
        arr[i].style.color = i === type ? "#298A7E" : "grey";
    },
    handleBarClick: function (i) {
      this.curPage = i;
    },
    handleNavClick: function (inc) {
      this.curPage += inc;
    },
  },
};
</script>

<style lang="scss" scoped>
.submission {
  width: 100%;

  .page {
    // Spacing + centering
    margin: 8rem auto 0 auto;
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
    }

    .section-header {
      // Flexbox for layout
      display: flex;
      align-items: center;

      p {
        // Typography
        font-size: $subheader-font-size;
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

    .media-icons {
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;
      // Centering + spacing
      margin: 5rem auto;
      // Clickable
      cursor: pointer;
      // Sizing
      width: 80%;

      .media-icon {
        // Flexbox for centering
        display: flex;
        flex-direction: column;
        align-items: center;

        i {
          // Spacing
          margin-bottom: 1rem;
          // Icon styling
          color: grey;
          font-size: 5rem;
        }

        p {
          // Typography
          font-size: $body-font-size;
        }
      }
    }

    .file-upload {
      // Sizing
      width: 90%;
      // Box styling
      border: 1px dashed gray;
      // Centering + spacing
      margin: 5rem auto 0 auto;
      // Flexbox for layout
      display: flex;
      flex-direction: column;
      align-items: center;
      // Typography
      font-size: $subheader-font-size;
      color: lightgrey;
      // Container spacing
      padding: 6rem 0;

      span {
        // Spacing
        margin: 3rem 0;
      }

      button {
        // Border styling
        border: 1px solid lightgrey;
        // Container spacing
        padding: 0.5rem 1rem;
        // Typography
        font-family: $alt-font;
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

      input {
        // Typography
        font-family: $alt-font;
        // Inner spacing
        padding: 0.5rem;
        // Sizing
        width: 100%;
      }

      .input-fields {
        // Sizing
        width: 100%;
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