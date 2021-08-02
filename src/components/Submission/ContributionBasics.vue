<template>
  <div>
    <div class="section-header">
      <p>Image title</p>
    </div>
    <div class="section-field">
      <input placeholder="Image title" v-model="submissionData.title" />
      <i class="fas fa-info-circle" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipState[0]"
      /></i>
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
      <i class="fas fa-info-circle" @click="handleTooltip(1)"
        ><Tooltip :open="tooltipState[1]"
      /></i>
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
      <i class="fas fa-info-circle" @click="handleTooltip(2)"
        ><Tooltip :message="tooltipMessage[2]" :open="tooltipState[2]"
      /></i>
    </div>
    <div class="section-header">
      <p>Language</p>
    </div>
    <div class="section-field">
      <input placeholder="Language" v-model="submissionData.language" />
      <i class="fas fa-info-circle" @click="handleTooltip(3)"
        ><Tooltip :open="tooltipState[3]"
      /></i>
    </div>
    <div class="section-header">
      <p>City and country image was made in</p>
    </div>
    <div class="section-field">
      <div class="input-fields">
        <input placeholder="City" v-model="submissionData.city" />
        <input placeholder="Country" v-model="submissionData.country" />
      </div>
      <i class="fas fa-info-circle" @click="handleTooltip(4)"
        ><Tooltip :open="tooltipState[4]"
      /></i>
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
        <i class="fas fa-info-circle" v-if="i === 1" @click="handleTooltip(5)"
          ><Tooltip :open="tooltipState[5]"
        /></i>
      </div>
      <div class="section-field" :style="{ marginBottom: '1rem' }">
        <input placeholder="Language" v-model="submissionData.language" />
        <i class="fas fa-info-circle" v-if="i === 1" @click="handleTooltip(6)"
          ><Tooltip :open="tooltipState[6]"
        /></i>
      </div>
      <div class="section-field" :style="{ marginBottom: '1rem' }">
        <div class="date-inputs">
          <Datepicker
            v-model="submissionData.exhibitStartDates[i - 1]"
            inputFormat="MM/dd/yyyy"
            :style="{
              width: '10rem',
              padding: '0.5rem',
              fontFamily: 'Open Sans',
            }"
          />
          <p>-</p>
          <Datepicker
            v-model="submissionData.exhibitEndDates[i - 1]"
            inputFormat="MM/dd/yyyy"
            :style="{
              width: '10rem',
              padding: '0.5rem',
              fontFamily: 'Open Sans',
            }"
          />
        </div>
        <i class="fas fa-info-circle" v-if="i === 1" @click="handleTooltip(7)"
          ><Tooltip :open="tooltipState[7]"
        /></i>
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
    <div
      class="section-field"
      :style="{ width: '30rem', justifyContent: 'space-between' }"
    >
      <input
        placeholder="Search by city, state, country, or continent"
        v-model="submissionData.location"
        :style="{ width: '70%' }"
      />
      <button @click="handleLocationSearch">Find</button>
      <i class="fas fa-info-circle" @click="handleTooltip(8)"
        ><Tooltip :message="tooltipMessage[8]" :open="tooltipState[8]"
      /></i>
    </div>
  </div>
</template>

<script>
// Import global components
import Datepicker from "vue3-datepicker";

// Import local components
import Tooltip from "@/components/Submission/Tooltip";

export default {
  name: "ContributionBasics",
  components: {
    Datepicker,
    Tooltip,
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
      tooltipMessage: [
        null,
        null,
        "Give the date that the original work was created. For multi-day projects, give whatever date you feel is best.",
        null,
        null,
        null,
        null,
        null,
        "Give the location where the work was originally created.",
      ],
      tooltipState: [
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
        false,
      ],
    };
  },
  methods: {
    handleTooltip: function (ind) {
      this.tooltipState[ind] = !this.tooltipState[ind];
    },
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
.section-field {
  // Variables for Datepicker
  --vdp-hover-bg-color: #8abbac;
  --vdp-selected-bg-color: #298a7e;

  input {
    // Sizing
    width: 90%;
  }

  p {
    // Spacing
    margin: 0 0.5rem;
  }

  button {
    // Typography
    font-size: 1rem;
    // Button styling
    padding: 0.7rem 1.5rem;
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
</style>