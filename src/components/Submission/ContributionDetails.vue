<template>
  <div>
    <div class="section-header">
      <p>Image description</p>
    </div>
    <div class="section-field textarea-field">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.description"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipState[0]"
      /></i>
    </div>
    <div class="section-header">
      <p>Keywords/Tags that describe, identify, or interpret the image</p>
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
        @click="handleTooltip(1)"
        ><Tooltip :open="tooltipState[1]"
      /></i>
      <i
        class="fas fa-times-circle"
        v-else-if="!disabled"
        @click="handleNumTags(-1, i - 1)"
      ></i>
    </div>
    <div
      class="add-container"
      v-if="numTags < 5 && !disabled"
      @click="handleNumTags(1)"
    >
      <div class="add-button">
        <i class="fas fa-plus-circle"></i>
        <p>Add another tag</p>
      </div>
    </div>
    <div class="section-header" id="medium-header">
      <p>Medium of original work</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Enter medium type"
        v-model="submissionData.medium"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(2)"
        ><Tooltip :open="tooltipState[2]"
      /></i>
    </div>
    <div class="section-header">
      <p>File format</p>
    </div>
    <div class="section-field">
      <select
        v-model="submissionData.format"
        @change="handleDropdownStyling"
        :disabled="disabled"
      >
        <option disabled value="">Select file format</option>
        <option>JPG</option>
        <option>PNG</option>
        <option>JPEG</option>
      </select>
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(3)"
        ><Tooltip :open="tooltipState[3]"
      /></i>
    </div>
    <div class="section-header">
      <p>Rights</p>
    </div>
    <div class="section-field textarea-field">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.rights"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(4)"
        ><Tooltip :open="tooltipState[4]"
      /></i>
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
      numTags: 1,
      tooltipState: [false, false, false, false, false],
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
  },
  methods: {
    handleTooltip: function (ind) {
      this.tooltipState[ind] = !this.tooltipState[ind];
    },
    handleNumTags: function (inc, ind) {
      this.numTags += inc;
      // Update remaining fields accordingly
      if (inc === -1) this.submissionData.tags.splice(ind, 1);
    },
    handleDropdownStyling: function () {
      document.getElementsByTagName("select")[0].style.color = "black";
    },
  },
};
</script>

<style lang="scss" scoped>
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
  margin-top: 3rem;
}
</style>