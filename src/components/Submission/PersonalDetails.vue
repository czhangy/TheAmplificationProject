<template>
  <div>
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
    <div
      class="section-field"
      v-for="i in numContributors"
      :key="i"
      :style="{ marginBottom: '1rem' }"
    >
      <div class="input-fields">
        <input
          placeholder="First name"
          v-model="submissionData.contributorFirstNames[i]"
        />
        <input
          placeholder="Last name"
          v-model="submissionData.contributorLastNames[i]"
        />
      </div>
      <i
        class="fas fa-info-circle"
        v-if="i === 1"
        @click="handleUnfinished"
      ></i>
      <i
        class="fas fa-times-circle"
        v-else
        @click="handleNumContributors(-1, i)"
      ></i>
    </div>
    <div
      class="container"
      v-if="numContributors < 5"
      @click="handleNumContributors(1)"
    >
      <div class="add-button">
        <i class="fas fa-plus-circle"></i>
        <p>Add another contributor</p>
      </div>
    </div>
    <div class="section-header">
      <p>Name(s) of creator(s)</p>
    </div>
    <div
      class="section-field"
      v-for="i in numCreators"
      :key="i"
      :style="{ marginBottom: '1rem' }"
    >
      <div class="input-fields">
        <input
          placeholder="First name"
          v-model="submissionData.creatorFirstNames[i]"
        />
        <input
          placeholder="Last name"
          v-model="submissionData.creatorLastNames[i]"
        />
      </div>
      <i
        class="fas fa-info-circle"
        v-if="i === 1"
        @click="handleUnfinished"
      ></i>
      <i class="fas fa-times-circle" v-else @click="handleNumCreators(-1, i)"></i>
    </div>
    <div class="container" @click="handleNumCreators(1)">
      <div class="add-button" v-if="numCreators < 5">
        <i class="fas fa-plus-circle"></i>
        <p>Add another creator</p>
      </div>
    </div>
    <div class="section-header">
      <p>
        Artist statements and/or biographies of creator(s) and contributor(s)
      </p>
    </div>
    <div class="section-field" :style="{ width: '100%' }">
      <textarea
        placeholder="Type here..."
        v-model="submissionData.statements"
      />
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
  </div>
</template>

<script>
export default {
  name: "PersonalDetails",
  props: {
    submissionData: {
      type: Object,
      required: true,
    },
  },
  methods: {
    handleUnfinished: function () {
      alert("This feature needs to be implemented still");
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
  data() {
    return {
      numContributors: 1,
      numCreators: 1,
    };
  },
};
</script>

<style lang="scss" scoped>
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

.section-field {
  // Flexbox for layout
  display: flex;
  align-items: center;
  // Spacing
  margin-top: 1rem;
  margin-bottom: 3rem;
  // Sizing
  width: 25rem;

  input,
  textarea {
    // Typography
    font-family: $alt-font;
    // Inner spacing
    padding: 0.5rem;
  }

  input {
    // Sizing
    width: 100%;
  }

  textarea {
    // Sizing
    width: 90%;
    height: 10rem;
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

  .fa-times-circle {
    // Clickable
    cursor: pointer;
    // Icon styling
    color: red;
    font-size: $subheader-font-size;
    // Spacing
    margin-left: 0.6rem;
  }
}

.container {
  // Limit width
  display: inline-block;
  // Clickable
  cursor: pointer;
  // Spacing
  margin-bottom: 3rem;

  .add-button {
    // Typography
    color: $accent-teal;
    // Flexbox for alignment
    display: flex;
    justify-content: flex-start;
    align-items: center;

    .fa-plus-circle {
      // Icon sizing
      font-size: 1.5rem;
      // Spacing
      margin-right: 0.7rem;
    }

    p {
      // Typography
      font-family: $alt-font;
    }
  }
}
</style>