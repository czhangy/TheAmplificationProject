<template>
  <div id="contribution-basics">
    <div class="section-header">
      <label class="section-label" for="title-field">Title of work</label>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container">
      <input
        id="title-field"
        class="input-field"
        placeholder="Enter title"
        v-model="submissionData.title"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label" for="year-field">Year work completed</label>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div class="field-container">
      <input
        id="year-field"
        class="input-field"
        placeholder="YYYY"
        v-model="submissionData.completionYear"
        :disabled="disabled"
      />
    </div>
    <div class="section-header" v-if="isText">
      <label class="section-label" for="language-field">Language of work</label>
    </div>
    <div class="field-container" v-if="isText">
      <input
        id="language-field"
        class="input-field"
        placeholder="Enter language"
        v-model="submissionData.language"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <label class="section-label"
        >City and country where you created the work</label
      >
      <i class="asterisk fas fa-asterisk" />
    </div>
    <!-- <div class="field-container grouped">
      <div class="multi-input">
        <input
          class="input-field"
          placeholder="Enter city"
          v-model="submissionData.city"
          :disabled="disabled"
        />
        <input
          class="input-field"
          placeholder="Enter country"
          v-model="submissionData.country"
          :disabled="disabled"
        />
        <button
          id="location-search-button"
          @click="handleLocationSearch"
          v-if="!disabled"
        >
          Find
        </button>
      </div>
      <i class="tooltip-button fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipStates[0]" :message="tooltipMessages[0]"
      /></i>
    </div> -->
    <div id="map-container" />
  </div>
</template>

<script>
// Import external stylesheets
import "leaflet/dist/leaflet.css";

// Import global libraries
import L from "leaflet";
// import axios from "axios";

// Import local components
import Tooltip from "./Tooltip";

export default {
  name: "ContributionBasics",
  components: {
    Tooltip,
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
  data() {
    return {
      // Tooltip variables
      tooltipMessages: ["Locate on the map where you created the work"],
      tooltipStates: [false],
      // Map variables
      center: [34.0522, -118.24],
      map: null,
      marker: null,
    };
  },
  methods: {
    // Tooltip toggle function
    handleTooltip: function (ind) {
      this.tooltipStates[ind] = !this.tooltipStates[ind];
    },
    // Map functions
    handleLocationSearch: async function () {
      alert("This feature is under development!");
      return;
      // axios
      //   // Query LocationStack API for forward geocoding
      //   .get(
      //     `http://api.positionstack.com/v1/forward?access_key=${
      //       process.env.VUE_APP_POSITIONSTACK_ACCESS_TOKEN
      //     }&query=${
      //       this.submissionData.city + " " + this.submissionData.country
      //     }`
      //   )
      //   .then((res) => {
      //     let coords = [res.data.data[0].latitude, res.data.data[0].longitude];
      //     // Set marker to location
      //     this.handleSetMarker(coords[0], coords[1]);
      //     // Pan to location
      //     this.map.flyTo(coords);
      //     // Set location
      //     this.submissionData.location = coords;
      //   });
    },
    handleLeafletSetup: function () {
      let center =
        this.submissionData.location === null
          ? this.center
          : this.submissionData.location;
      // Set map object
      this.map = L.map("map-container").setView(center, 13);
      // Leaflet initialization
      L.tileLayer(
        "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}",
        {
          attribution:
            'Map data (c) <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery (c) <a href="https://www.mapbox.com/">Mapbox</a>',
          maxZoom: 18,
          id: "mapbox/streets-v11",
          accessToken: process.env.VUE_APP_MAPBOX_ACCESS_TOKEN,
        }
      ).addTo(this.map);
      this.handleMapState();
    },
    handleMapState: function () {
      // Get reference to self
      const self = this;
      // Add marker onto map if location exists already
      if (this.submissionData.location !== null)
        this.handleSetMarker(
          this.submissionData.location[0],
          this.submissionData.location[1]
        );
      // Disable interactivity on review page
      if (this.disabled) {
        this.map.dragging.disable();
        this.map.zoomControl.remove();
        this.map.scrollWheelZoom.disable();
      }
      // Add click handler
      else
        this.map.addEventListener("click", function (e) {
          self.handleMarkerClick(e);
        });
    },
    // Marker functions
    handleSetMarker: function (lat, long) {
      // Fix icon
      const defaultIcon = new L.icon({
        iconUrl: require("leaflet/dist/images/marker-icon.png"),
        iconSize: [16, 24],
        iconAnchor: [10, 25],
        popupAnchor: [0, -2],
      });
      // Remove existing marker
      if (this.marker !== null) this.map.removeLayer(this.marker);
      // Set marker
      this.marker = L.marker([lat, long], {
        icon: defaultIcon,
      }).addTo(this.map);
      // Save location
      this.submissionData.location = [lat, long];
    },
    handleMarkerClick: function (e) {
      // Pass event to handler
      this.handleSetMarker(e.latlng.lat, e.latlng.lng);
    },
  },
  computed: {
    isText() {
      return this.fileType === 0;
    },
  },
  mounted() {
    // Set up map
    this.handleLeafletSetup();
  },
};
</script>

<style lang="scss" scoped>
#contribution-basics {
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

    &.grouped {
      // Spacing
      justify-content: space-between;
      margin-bottom: 24px;
      // Sizing
      width: max(40%, 350px);
    }

    .input-field {
      // Typography
      font-family: $alt-font;
      // Inner spacing
      padding: 0.5rem;
      // Sizing
      width: 90%;
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
        // Spacing
        margin-right: 16px;
      }

      #location-search-button {
        // Button styling
        padding: 10px 16px;
        background: $accent-teal;
        border-radius: 10px;
        // Typography
        font-family: $alt-font;
        font-weight: $bold;
        color: white;
        text-align: center;
        // Remove default button styling
        border: none;
        // Clickable
        cursor: pointer;
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
  }

  #map-container {
    // Sizing
    height: 50vh;
    width: 100%;
    // Place below content
    z-index: 0;
    // Spacing
    margin-top: 20px;
  }
}

// Sticky hover
@media (hover: hover) {
  #contribution-basics
    > .field-container
    > .multi-input
    > #location-search-button:hover {
    // Animate
    background: $accent-dark-teal;
  }
}

// Smaller layout
@media screen and (max-width: 767px) {
  #contribution-basics > .field-container > .tooltip-button {
    // Hide
    display: none;
  }
}
</style>