<template>
  <div id="contribution-details">
    <div class="section-header">
      <label class="section-label" for="description-field"
        >Describe the work</label
      >
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container textarea">
      <textarea
        id="description-field"
        class="input-field textarea"
        placeholder="Type here..."
        v-model="submissionData.description"
        :disabled="disabled"
      />
      <i
        class="tooltip-button fas fa-info-circle"
        v-if="!disabled"
        @click="handleTooltip(0)"
        ><Tooltip :open="tooltipStates[0]" :message="tooltipMessages[0]"
      /></i>
    </div>
    <div class="section-header" v-if="isImage">
      <label class="section-label" for="size-field">Size of work</label>
    </div>
    <div class="field-container" v-if="isImage">
      <input
        id="size-field"
        class="input-field"
        placeholder="H x W x D"
        v-model="submissionData.size"
        :disabled="disabled"
      />
      <i
        class="tooltip-button fas fa-info-circle"
        v-if="!disabled"
        @click="handleTooltip(1)"
        ><Tooltip :open="tooltipStates[1]" :message="tooltipMessages[1]"
      /></i>
    </div>
    <div class="section-header" v-if="isImage">
      <label class="section-label" for="medium-field">Mediums</label>
    </div>
    <div class="field-container" v-if="isImage">
      <input
        id="medium-field"
        class="input-field"
        placeholder="Enter medium type"
        v-model="submissionData.mediums"
        :disabled="disabled"
      />
      <i
        class="tooltip-button fas fa-info-circle"
        v-if="!disabled"
        @click="handleTooltip(2)"
        ><Tooltip :open="tooltipStates[2]" :message="tooltipMessages[2]"
      /></i>
    </div>
    <div class="section-header" v-if="isVideo || isAudio">
      <label class="section-label" for="duration-field"
        >Duration of the work</label
      >
    </div>
    <div class="field-container" v-if="isVideo || isAudio">
      <input
        id="duration-field"
        class="input-field"
        placeholder="Enter duration"
        v-model="submissionData.duration"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(3)"
        ><Tooltip :open="tooltipStates[3]" :message="tooltipMessages[3]"
      /></i>
    </div>
    <div class="section-header">
      <label class="section-label" for="collection-field">
        Is this item part of a collection? If so, put collection title here:
      </label>
    </div>
    <div class="field-container">
      <input
        id="collection-field"
        class="input-field"
        placeholder="Enter collection name"
        v-model="submissionData.collection"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="rights-field">Copyright</label>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container">
      <input
        id="rights-field"
        class="input-field"
        placeholder="Enter rights"
        v-model="submissionData.rights"
        :disabled="disabled"
      />
      <i
        class="tooltip-button fas fa-info-circle"
        v-if="!disabled"
        @click="handleTooltip(4)"
        ><Tooltip :open="tooltipStates[4]" :message="tooltipMessages[4]"
      /></i>
    </div>
    <div class="section-header">
      <label class="section-label">Tags or keywords</label>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container grouped" v-for="i in numTags" :key="i">
      <input
        class="input-field"
        placeholder="Enter descriptive term"
        v-model="submissionData.tags[i - 1]"
        :disabled="disabled"
      />
      <i
        class="tooltip-button fas fa-info-circle"
        v-if="i === 1 && !disabled"
        @click="handleTooltip(5)"
        ><Tooltip :open="tooltipStates[5]" :message="tooltipMessages[5]"
      /></i>
      <i
        class="delete-field-button fas fa-times-circle"
        v-else-if="!disabled"
        @click="handleNumTags(-1, i - 1)"
      />
    </div>
    <div
      class="add-field-container"
      v-if="numTags < 3 && !disabled"
      @click="handleNumTags(1)"
    >
      <div class="add-field-button">
        <i class="add-field-icon fas fa-plus-circle"></i>
        <label class="add-field-label">Add another tag</label>
      </div>
    </div>
  </div>
</template>

<script>
// Import local components
import Tooltip from "./Tooltip";

export default {
  name: "ContributionDetails",
  components: {
    Tooltip,
  },
  data() {
    return {
      // Data variables
      numTags: 1,
      // Tooltip variables
      tooltipStates: [false, false, false, false, false, false],
      tooltipMessages: [
        "Anything you would like to mention about the work – subject, theme, comments about and interpretation of it, how/why you created it, etc.",
        "Outer size of the paper, canvas, or other material that is the base of an artwork",
        "Oil on linen, mixed media, wood, acrylic, etc.",
        "Hours, minutes, seconds",
        "Information about the copyright status and the rights holder for the work. Can also include a link to a website containing more rights and/or contact information",
        "One to three words that describe, interpret, or provide details about the work",
      ],
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
    // Data handling function
    handleNumTags: function (inc, ind) {
      this.numTags += inc;
      // Update remaining fields accordingly
      if (inc === -1) this.submissionData.tags.splice(ind, 1);
    },
  },
  computed: {
    isImage() {
      return this.fileType === 1;
    },
    isVideo() {
      return this.fileType === 2;
    },
    isAudio() {
      return this.fileType === 3;
    },
  },
};
</script>

<style lang="scss" scoped>
#contribution-details {
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

    &.textarea {
      // Adjust sizing
      width: 80%;
    }

    &.grouped {
      // Adjust spacing
      margin-bottom: 16px;
    }

    .input-field {
      // Typography
      font-family: $alt-font;
      // Inner spacing
      padding: 0.5rem;
      // Sizing
      width: 50%;

      &.textarea {
        // Adjust sizing
        width: 90%;
        height: 10rem;
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
  #contribution-details > .field-container {
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