<template>
  <div id="personal-details">
    <div class="section-header">
      <label class="section-label" for="email-field">Email</label>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container">
      <input
        id="email-field"
        class="input-field"
        placeholder="Your email"
        v-model="submissionData.email"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label">{{ creatorType }} name(s)</label>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container grouped" v-for="i in numCreators" :key="i">
      <div class="multi-input">
        <input
          class="input-field"
          placeholder="First name"
          v-model="submissionData.creator.firstNames[i - 1]"
          :disabled="disabled"
        />
        <input
          class="input-field"
          placeholder="Last name"
          v-model="submissionData.creator.lastNames[i - 1]"
          :disabled="disabled"
        />
      </div>
      <i
        class="delete-field-button fas fa-times-circle"
        v-if="!disabled && i > 1"
        @click="handleNumCreators(-1, i - 1)"
      />
    </div>
    <div
      class="add-field-container"
      v-if="numCreators < 5 && !disabled"
      @click="handleNumCreators(1)"
    >
      <div class="add-field-button">
        <i class="add-field-icon fas fa-plus-circle" />
        <label class="add-field-label">Add another creator</label>
      </div>
    </div>
    <div class="section-header spaced">
      <label class="section-label">Contributor name(s)</label>
    </div>
    <div class="field-container grouped" v-for="i in numContributors" :key="i">
      <div class="multi-input">
        <input
          class="input-field"
          placeholder="First name"
          v-model="submissionData.contributor.firstNames[i - 1]"
          :disabled="disabled"
        />
        <input
          class="input-field"
          placeholder="Last name"
          v-model="submissionData.contributor.lastNames[i - 1]"
          :disabled="disabled"
        />
      </div>
      <i
        class="tooltip-button fas fa-info-circle"
        v-if="i === 1 && !disabled"
        @click="handleTooltip(0)"
        ><Tooltip :open="tooltipStates[0]" :message="tooltipMessages[0]"
      /></i>
      <i
        class="delete-field-button fas fa-times-circle"
        v-else-if="!disabled"
        @click="handleNumContributors(-1, i - 1)"
      />
    </div>
    <div
      class="add-field-container"
      v-if="numContributors < 5 && !disabled"
      @click="handleNumContributors(1)"
    >
      <div class="add-field-button">
        <i class="add-field-icon fas fa-plus-circle" />
        <label class="add-field-label">Add another contributor</label>
      </div>
    </div>
    <div class="section-header spaced">
      <label class="section-label" for="creator-bio-field"
        >{{ creatorType }} biography</label
      >
    </div>
    <div class="field-container textarea">
      <textarea
        id="creator-bio-field"
        class="input-field textarea"
        placeholder="Type here..."
        v-model="submissionData.creator.bio"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="creator-site-field"
        >{{ creatorType }} website</label
      >
    </div>
    <div class="field-container">
      <input
        id="creator-site-field"
        class="input-field"
        placeholder="Website URL"
        v-model="submissionData.creator.website"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="creator-facebook-field"
        >{{ creatorType }} Facebook page</label
      >
    </div>
    <div class="field-container">
      <input
        id="creator-facebook-field"
        class="input-field"
        placeholder="Facebook link"
        v-model="submissionData.creator.facebook"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="creator-twitter-field"
        >{{ creatorType }} Twitter</label
      >
    </div>
    <div class="field-container">
      <input
        id="creator-twitter-field"
        class="input-field"
        placeholder="Twitter link"
        v-model="submissionData.creator.twitter"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="creator-instagram-field"
        >{{ creatorType }} Instagram</label
      >
    </div>
    <div class="field-container">
      <input
        id="creator-instagram-field"
        class="input-field"
        placeholder="Instagram link"
        v-model="submissionData.creator.insta"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="contributor-bio-field"
        >Contributor biography</label
      >
    </div>
    <div class="field-container textarea">
      <textarea
        id="contributor-bio-field"
        class="input-field textarea"
        placeholder="Type here..."
        v-model="submissionData.contributor.bio"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="contributor-site-field"
        >Contributor website</label
      >
    </div>
    <div class="field-container">
      <input
        id="contributor-site-field"
        class="input-field"
        placeholder="Website URL"
        v-model="submissionData.contributor.website"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="contributor-facebook-field"
        >Contributor Facebook page</label
      >
    </div>
    <div class="field-container">
      <input
        id="contributor-facebook-field"
        class="input-field"
        placeholder="Facebook link"
        v-model="submissionData.contributor.facebook"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="contributor-twitter-field"
        >Contributor Twitter</label
      >
    </div>
    <div class="field-container">
      <input
        id="contributor-twitter-field"
        class="input-field"
        placeholder="Twitter link"
        v-model="submissionData.contributor.twitter"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="contributor-instagram-field"
        >Contributor Instagram</label
      >
    </div>
    <div class="field-container">
      <input
        id="contributor-instagram-field"
        class="input-field"
        placeholder="Instagram link"
        v-model="submissionData.contributor.insta"
        :disabled="disabled"
      />
    </div>
  </div>
</template>

<script>
// Import local components
import Tooltip from "./Tooltip";

export default {
  name: "PersonalDetails",
  components: {
    Tooltip,
  },
  data() {
    return {
      // Tooltip variables
      tooltipStates: [false],
      tooltipMessages: [
        "Person(s) or organization(s) who have made significant contributions to the work",
      ],
      // Data variables
      numContributors: 1,
      numCreators: 1,
      // Wording
      creatorType: null,
    };
  },
  props: {
    submissionData: {
      type: Object,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    fileType: {
      type: Number,
      required: true,
    },
  },
  methods: {
    // Tooltip toggle function
    handleTooltip: function (ind) {
      this.tooltipStates[ind] = !this.tooltipStates[ind];
    },
    // Field management functions
    handleNumContributors: function (inc, ind) {
      this.numContributors += inc;
      // Update remaining fields accordingly
      if (inc === -1) {
        this.submissionData.contributor.firstNames.splice(ind, 1);
        this.submissionData.contributor.lastNames.splice(ind, 1);
      }
    },
    handleNumCreators: function (inc, ind) {
      this.numCreators += inc;
      // Update remaining fields accordingly
      if (inc === -1) {
        this.submissionData.creator.firstNames.splice(ind, 1);
        this.submissionData.creator.lastNames.splice(ind, 1);
      }
    },
    // Creator type setter function
    handleCreatorType: function () {
      // Set creator type based on selected file type
      this.creatorType = this.fileType === 0 ? "Author" : "Artist";
    },
  },
  mounted() {
    // Set creator type
    this.handleCreatorType();
  },
};
</script>

<style lang="scss" scoped>
#personal-details {
  // Spacing + centering
  margin: 48px auto 0 auto;
  // Sizing
  width: 80%;

  .section-header {
    // Flexbox for layout
    display: flex;
    align-items: center;
    // Sizing
    max-width: 640px;

    &.spaced {
      // Extra spacing for fields below add-field-containers
      margin-top: 48px;
    }

    .section-label {
      // Typography
      font-size: $subheader-font-size;
      font-weight: bold;
    }

    .asterisk {
      // Icon styling
      color: red;
      font-size: calc(clamp(0.4rem, 0.28rem + 0.48vw, 0.7rem));
      // Spacing
      margin-left: 4px;
      margin-bottom: 16px;
    }
  }

  .field-container {
    // Flexbox for layout
    display: flex;
    align-items: center;
    // Spacing
    margin-top: 20px;
    margin-bottom: 48px;
    // Sizing
    width: min(400px, 100%);

    &.grouped {
      // Adjust spacing
      margin-bottom: 16px;
    }

    &.textarea {
      // Adjust sizing
      width: 80%;
    }

    .input-field {
      // Typography
      font-family: $alt-font;
      // Inner spacing
      padding: 0.5rem;
      // Sizing
      width: 90%;

      &.textarea {
        // Adjust sizing
        width: 90%;
        height: 10rem;
      }
    }

    .multi-input {
      // Sizing
      width: 90%;
      // Flexbox for layout
      display: flex;
      align-items: center;
      justify-content: space-between;

      .input-field {
        // Resize field
        width: 48%;
      }
    }

    .tooltip-button {
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

    .delete-field-button {
      // Clickable
      cursor: pointer;
      // Icon styling
      color: red;
      font-size: $subheader-font-size;
      // Spacing
      margin-left: 10px;
    }
  }

  .add-field-container {
    // Limit width
    display: inline-block;
    // Clickable
    cursor: pointer;

    .add-field-button {
      // Typography
      color: $accent-teal;
      // Flexbox for alignment
      display: flex;
      justify-content: flex-start;
      align-items: center;

      .add-field-icon {
        // Icon sizing
        font-size: $subheader-font-size;
        // Spacing
        margin-right: 12px;
      }

      .add-field-label {
        // Typography
        font-family: $alt-font;
        font-size: $body-font-size;
        // Override default cursor
        cursor: pointer;
      }
    }
  }
}

// Smaller layout
@media screen and (max-width: 767px) {
  #personal-details > .field-container {
    &.textarea {
      // Resize
      width: 100%;
    }

    .tooltip-button {
      // Hide
      display: none;
    }
  }
}
</style>