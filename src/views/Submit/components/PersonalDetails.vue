<template>
  <div id="personal-details">
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
    </div>
    <div class="section-header">
      <p>{{ creatorType }} name(s)</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field grouped-field" v-for="i in numCreators" :key="i">
      <div class="input-fields">
        <input
          placeholder="First name"
          v-model="submissionData.creator.firstNames[i - 1]"
          :disabled="disabled"
        />
        <input
          placeholder="Last name"
          v-model="submissionData.creator.lastNames[i - 1]"
          :disabled="disabled"
        />
      </div>
      <i
        class="fas fa-times-circle"
        v-if="!disabled && i > 1"
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
    <div class="section-header" id="contributor-header">
      <p>Contributor name(s)</p>
    </div>
    <div
      class="section-field grouped-field"
      v-for="i in numContributors"
      :key="i"
    >
      <div class="input-fields">
        <input
          placeholder="First name"
          v-model="submissionData.contributor.firstNames[i - 1]"
          :disabled="disabled"
        />
        <input
          placeholder="Last name"
          v-model="submissionData.contributor.lastNames[i - 1]"
          :disabled="disabled"
        />
      </div>
      <i
        class="fas fa-info-circle"
        v-if="i === 1 && !disabled"
        @click="handleTooltip(0)"
        ><Tooltip :open="tooltipStates[0]" :message="tooltipMessages[0]"
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
    <div class="section-header" id="statement-header">
      <p>{{ creatorType }} biography</p>
    </div>
    <div class="section-field textarea-field">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.creator.bio"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>{{ creatorType }} website</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Website URL"
        v-model="submissionData.creator.website"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>{{ creatorType }} Facebook page</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Facebook link"
        v-model="submissionData.creator.facebook"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>{{ creatorType }} Twitter</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Twitter link"
        v-model="submissionData.creator.twitter"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>{{ creatorType }} Instagram</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Instagram link"
        v-model="submissionData.creator.insta"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>Contributor biography</p>
    </div>
    <div class="section-field textarea-field">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.contributor.bio"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>Contributor website</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Website URL"
        v-model="submissionData.contributor.website"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>Contributor Facebook page</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Facebook link"
        v-model="submissionData.contributor.facebook"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>Contributor Twitter</p>
    </div>
    <div class="section-field">
      <input
        placeholder="Twitter link"
        v-model="submissionData.contributor.twitter"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>Contributor Instagram</p>
    </div>
    <div class="section-field">
      <input
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
      creatorType: "Artist"
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
  },
  mounted() {
    if (this.fileType === 0) this.creatorType = "Author";
  }
};
</script>

<style lang="scss" scoped>
#personal-details {
  #contributor-header {
    // Spacing
    margin-top: 48px;
  }

  #statement-header {
    // Spacing
    margin-top: 48px;
  }
}

input {
  // Sizing
  width: 90%;
}
</style>