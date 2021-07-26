<template>
  <div>
    <div class="section-header">
      <p>Image title</p>
    </div>
    <div class="section-field">
      <input placeholder="Image title" v-model="submissionData.title" />
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
    <div class="section-header">
      <p>
        Title of collection, set, or series this image is part of (inside or
        outside of The Amplification Project)
      </p>
    </div>
    <div class="section-field">
      <input
        placeholder="Title of collection, set, or series"
        v-model="submissionData.set"
      />
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
    <div class="section-header">
      <p>Date of creation</p>
    </div>
    <div class="section-field">
      <Datepicker
        v-model="submissionData.date"
        inputFormat="MM/dd/yyyy"
        :style="{
          width: '10rem',
          padding: '0.5rem',
          fontFamily: 'Open Sans',
        }"
      />
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
    <div class="section-header">
      <p>Language</p>
    </div>
    <div class="section-field">
      <input placeholder="Language" v-model="submissionData.language" />
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
    <div class="section-header">
      <p>City and country image was made in</p>
    </div>
    <div class="section-field">
      <div class="input-fields">
        <input placeholder="City" v-model="submissionData.city" />
        <input placeholder="Country" v-model="submissionData.country" />
      </div>
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
    <div class="section-header">
      <p>Exhibit information (if applicable)</p>
    </div>
    <div v-for="i in numExhibits" :key="i" :style="{ marginBottom: '1rem' }">
      <div class="section-field" :style="{ marginBottom: '1rem' }">
        <div class="input-fields">
          <input placeholder="City" v-model="submissionData.exhibitCities[i]" />
          <input
            placeholder="Country"
            v-model="submissionData.exhibitCountries[i]"
          />
        </div>
        <i
          class="fas fa-info-circle"
          v-if="i === 1"
          @click="handleUnfinished"
        ></i>
      </div>
      <div class="section-field" :style="{ marginBottom: '1rem' }">
        <input placeholder="Language" v-model="submissionData.language" />
        <i
          class="fas fa-info-circle"
          v-if="i === 1"
          @click="handleUnfinished"
        ></i>
      </div>
      <div class="section-field" :style="{ marginBottom: '1rem' }">
        <div class="date-inputs">
          <Datepicker
            v-model="submissionData.exhibitStartDates[i]"
            inputFormat="MM/dd/yyyy"
            :style="{
              width: '10rem',
              padding: '0.5rem',
              fontFamily: 'Open Sans',
            }"
          />
          <p>-</p>
          <Datepicker
            v-model="submissionData.exhibitEndDates[i]"
            inputFormat="MM/dd/yyyy"
            :style="{
              width: '10rem',
              padding: '0.5rem',
              fontFamily: 'Open Sans',
            }"
          />
        </div>
        <i
          class="fas fa-info-circle"
          v-if="i === 1"
          @click="handleUnfinished"
        ></i>
      </div>
    </div>
    <div class="container" @click="handleNumExhibits(1)">
      <div class="add-button" v-if="numExhibits < 5">
        <i class="fas fa-plus-circle"></i>
        <p>Add another exhibit</p>
      </div>
    </div>
    <div class="section-header">
      <p>Find a geographic location for the image</p>
    </div>
    <div class="section-field" :style="{ width: '30rem' }">
      <input
        placeholder="Search by city, state, country, or continent"
        v-model="submissionData.location"
        :style="{ width: '70%' }"
      />
      <button @click="handleLocationSearch">Find</button>
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
  </div>
</template>

<script>
// Import global components
import Datepicker from "vue3-datepicker";

export default {
  name: "ContributionDetails",
  components: {
    Datepicker,
  },
  props: {
    submissionData: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      numExhibits: 1,
    };
  },
  methods: {
    handleNumExhibits: function (inc, ind) {
      this.numExhibits += inc;
      // Update remaining fields accordingly
      if (inc === -1) {
        this.submissionData.exhibitCities.splice(ind, 1);
        this.submissionData.exhibitCountries.splice(ind, 1);
        this.submissionData.exhibitVenues.splice(ind, 1);
        this.submissionData.exhibitStartDates.splice(ind, 1);
        this.submissionData.exhibitEndDates.splice(ind, 1);
      }
    },
    handleLocationSearch: function () {
      alert("This feature has not been implemented yet");
    },
  },
};
</script>

<style lang="scss" scoped>
.section-header {
  // Flexbox for layout
  display: flex;
  align-items: center;
  // Sizing
  width: 40rem;

  p {
    // Typography
    font-size: $subheader-font-size;
  }
}

.section-field {
  // Variables for Datepicker
  --vdp-hover-bg-color: #8abbac;
  --vdp-selected-bg-color: #298a7e;
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  align-items: center;
  // Spacing
  margin-top: 1rem;
  margin-bottom: 3rem;
  // Sizing
  width: 25rem;

  input {
    // Sizing
    width: 90%;
    // Typography
    font-family: $alt-font;
    // Inner spacing
    padding: 0.5rem;
  }

  p {
    // Spacing
    margin: 0 0.5rem;
  }

  button {
    // Typography
    font-family: $alt-font;
    font-weight: $bold;
    font-size: 1rem;
    color: white;
    text-align: center;
    // Button styling
    background: $accent-dark-teal;
    padding: 0.7rem 1.5rem;
    border-radius: 10px;
    // Smooth hover animation
    transition: all 0.2s ease;
    // Remove default button styling
    border: none;
    // Clickable
    cursor: pointer;
  }

  .input-fields {
    // Sizing
    width: 90%;
    // Flexbox for layout
    display: flex;
    align-items: center;
    justify-content: space-between;

    input {
      // Sizing
      width: 48%;
    }
  }

  .date-inputs {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;
    // Sizing
    width: 90%;
  }
}

.fa-info-circle {
  // Clickable
  cursor: pointer;
  // Icon styling
  color: $accent-teal;
  font-size: $subheader-font-size;
  // Spacing
  margin-left: 0.6rem;
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

// Sticky hover
@media (hover: hover) {
  button {
    &:hover {
      transform: scale(1.05);
    }
  }
}
</style>