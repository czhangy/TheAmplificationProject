<template>
  <div>
    <div class="section-header">
      <p>Email</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field">
      <input
        placeholder="Your email"
        v-model="submissionData.email"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipState[0]"
      /></i>
    </div>
    <div class="section-header">
      <p>Name(s) of contributor(s)</p>
    </div>
    <div
      class="section-field grouped-field"
      v-for="i in numContributors"
      :key="i"
    >
      <div class="input-fields">
        <input
          placeholder="First name"
          v-model="submissionData.contributorFirstNames[i - 1]"
          :disabled="disabled"
        />
        <input
          placeholder="Last name"
          v-model="submissionData.contributorLastNames[i - 1]"
          :disabled="disabled"
        />
      </div>
      <i
        class="fas fa-info-circle"
        v-if="i === 1 && !disabled"
        @click="handleTooltip(1)"
        ><Tooltip :open="tooltipState[1]"
      /></i>
      <i
        class="fas fa-times-circle"
        v-else-if="!disabled"
        @click="handleNumContributors(-1, i - 1)"
      ></i>
    </div>
    <div
      class="add-container"
      v-if="numContributors < 5 && !disabled"
      @click="handleNumContributors(1)"
    >
      <div class="add-button">
        <i class="fas fa-plus-circle"></i>
        <p>Add another contributor</p>
      </div>
    </div>
    <div class="section-header" id="creator-header">
      <p>Name(s) of creator(s)</p>
    </div>
    <div
      class="section-field grouped-field"
      v-for="i in numCreators"
      :key="i"
    >
      <div class="input-fields">
        <input
          placeholder="First name"
          v-model="submissionData.creatorFirstNames[i - 1]"
          :disabled="disabled"
        />
        <input
          placeholder="Last name"
          v-model="submissionData.creatorLastNames[i - 1]"
          :disabled="disabled"
        />
      </div>
      <i
        class="fas fa-info-circle"
        v-if="i === 1 && !disabled"
        @click="handleTooltip(2)"
        ><Tooltip :open="tooltipState[2]"
      /></i>
      <i
        class="fas fa-times-circle"
        v-else-if="!disabled"
        @click="handleNumCreators(-1, i - 1)"
      ></i>
    </div>
    <div
      class="add-container"
      v-if="numCreators < 5 && !disabled"
      @click="handleNumCreators(1)"
    >
      <div class="add-button">
        <i class="fas fa-plus-circle"></i>
        <p>Add another creator</p>
      </div>
    </div>
    <div class="section-header" id="statement-header">
      <p>
        Artist statements and/or biographies of creator(s) and contributor(s)
      </p>
    </div>
    <div class="section-field textarea-field">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.statements"
        :disabled="disabled"
      />
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(3)"
        ><Tooltip :open="tooltipState[3]"
      /></i>
    </div>
  </div>
</template>

<script>
// Import local components
import Tooltip from "@/components/Submission/Tooltip";

export default {
  name: "PersonalDetails",
  components: {
    Tooltip,
  },
  data() {
    return {
      tooltipState: [false, false, false, false],
      numContributors: 1,
      numCreators: 1,
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
    handleNumContributors: function (inc, ind) {
      this.numContributors += inc;
      // Update remaining fields accordingly
      if (inc === -1) {
        this.submissionData.contributorFirstNames.splice(ind, 1);
        this.submissionData.contributorLastNames.splice(ind, 1);
      }
    },
    handleNumCreators: function (inc, ind) {
      this.numCreators += inc;
      // Update remaining fields accordingly
      if (inc === -1) {
        this.submissionData.contributorFirstNames.splice(ind, 1);
        this.submissionData.contributorLastNames.splice(ind, 1);
      }
    },
  },
};
</script>

<style lang="scss" scoped>
input {
  // Sizing
  width: 90%;
}

#creator-header {
  // Spacing
  margin-top: 3rem;
}

#statement-header {
  // Spacing
  margin-top: 3rem;
}
</style>