<template>
  <div id="contribution-details">
    <div class="section-header">
      <p>Describe the work</p>
    </div>
    <div class="section-field textarea-field">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.description"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipStates[0]" :message="tooltipMessages[0]"
      /></i>
    </div>
    <div class="section-header" v-if="fileType === 1">
      <p>Size of work</p>
    </div>
    <div class="section-field" v-if="fileType === 1">
      <input
        placeholder="H x W x D"
        v-model="submissionData.size"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(1)"
        ><Tooltip :open="tooltipStates[1]" :message="tooltipMessages[1]"
      /></i>
    </div>
    <div class="section-header" v-if="fileType === 1">
      <p>Mediums</p>
    </div>
    <div class="section-field" v-if="fileType === 1">
      <input
        placeholder="Enter medium type"
        v-model="submissionData.mediums"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(2)"
        ><Tooltip :open="tooltipStates[2]" :message="tooltipMessages[2]"
      /></i>
    </div>
    <div class="section-header" v-if="fileType === 2 || fileType === 3">
      <p>Duration of the work</p>
    </div>
    <div class="section-field" v-if="fileType === 2 || fileType === 3">
      <input
        placeholder="Enter duration"
        v-model="submissionData.duration"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(3)"
        ><Tooltip :open="tooltipStates[3]" :message="tooltipMessages[3]"
      /></i>
    </div>
    <div class="section-header">
      <p>Copyright</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field">
      <input
        placeholder="Enter rights"
        v-model="submissionData.rights"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(4)"
        ><Tooltip :open="tooltipStates[4]" :message="tooltipMessages[4]"
      /></i>
    </div>
    <div class="section-header">
      <p>Tags or keywords</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field grouped-field" v-for="i in numTags" :key="i">
      <input
        placeholder="Enter descriptive term"
        v-model="submissionData.tags[i - 1]"
        :disabled="disabled"
      />
      <i
        class="fas fa-info-circle"
        v-if="i === 1 && !disabled"
        @click="handleTooltip(5)"
        ><Tooltip :open="tooltipStates[5]" :message="tooltipMessages[5]"
      /></i>
      <i
        class="fas fa-times-circle"
        v-else-if="!disabled"
        @click="handleNumTags(-1, i - 1)"
      ></i>
    </div>
    <div
      class="add-container"
      v-if="numTags < 3 && !disabled"
      @click="handleNumTags(1)"
    >
      <div class="add-button">
        <i class="fas fa-plus-circle"></i>
        <p>Add another tag</p>
      </div>
    </div>
  </div>
</template>

<script>
// Import local components
import Tooltip from "@/components/Submission/Tooltip";

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
    // Styling function
    handleDropdownStyling: function () {
      document.getElementsByTagName("select")[0].style.color = "black";
    },
  },
};
</script>

<style lang="scss" scoped>
#contribution-details {
  input,
  select {
    // Sizing
    width: 50%;
  }

  select {
    // Typography
    color: grey;

    option {
      // Typography
      color: black;
    }
  }

  #medium-header {
    // Spacing
    margin-top: 48px;
  }
}
</style>