<template>
  <div id="contribution-basics">
    <div class="section-header">
      <p>Title of work</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field">
      <input
        placeholder="Enter title"
        v-model="submissionData.title"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>Year work completed</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field">
      <input
        placeholder="YYYY"
        v-model="submissionData.completionYear"
        :disabled="disabled"
      />
    </div>
    <div class="section-header" v-if="fileType === 0">
      <p>Language of work</p>
    </div>
    <div class="section-field" v-if="fileType === 0">
      <input
        placeholder="Enter language"
        v-model="submissionData.language"
        :disabled="disabled"
      />
    </div>
    <div class="section-header">
      <p>City and country where you created the work</p>
      <i class="fas fa-asterisk"></i>
    </div>
    <div class="section-field" id="location-field">
      <div class="input-fields">
        <input
          placeholder="Enter city"
          v-model="submissionData.city"
          :disabled="disabled"
        />
        <input
          placeholder="Enter country"
          v-model="submissionData.country"
          :disabled="disabled"
        />
        <button @click="handleLocationSearch">Find</button>
      </div>
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipStates[0]" :message="tooltipMessages[0]"
      /></i>
    </div>
    <div id="map-container"></div>
  </div>
</template>

<script>
// Import external stylesheets
import "leaflet/dist/leaflet.css";

// Import global libraries
import L from "leaflet";
import axios from "axios";

// Import local components
import Tooltip from "@/components/Submission/Tooltip";

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
      axios
        // Query LocationStack API for forward geocoding
        .get(
          `http://api.positionstack.com/v1/forward?access_key=${
            process.env.VUE_APP_POSITIONSTACK_ACCESS_TOKEN
          }&query=${
            this.submissionData.city + " " + this.submissionData.country
          }`
        )
        .then((res) => {
          // Fix icon
          const defaultIcon = new L.icon({
            iconUrl: require("leaflet/dist/images/marker-icon.png"),
            iconSize: [16, 24],
            iconAnchor: [10, 25],
            popupAnchor: [0, -2],
          });
          // Clear existing marker
          if (this.marker !== null) this.map.removeLayer(this.marker);
          // Add marker to clicked location
          this.marker = L.marker(
            [res.data.data[0].latitude, res.data.data[0].longitude],
            {
              icon: defaultIcon,
            }
          ).addTo(this.map);
          // Pan to location
          this.map.flyTo([res.data.data[0].latitude, res.data.data[0].longitude])
        });
    },
    handleLeafletSetup: function () {
      let self = this;
      // Set map object
      this.map = L.map("map-container").setView(this.center, 13);
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
      // Add click handler
      this.map.addEventListener("click", function (e) {
        self.handleMarker(e);
      });
    },
    handleMarker: function (e) {
      // Fix icon
      const defaultIcon = new L.icon({
        iconUrl: require("leaflet/dist/images/marker-icon.png"),
        iconSize: [16, 24],
        iconAnchor: [10, 25],
        popupAnchor: [0, -2],
      });
      // Clear existing marker
      if (this.marker !== null) this.map.removeLayer(this.marker);
      // Add marker to clicked location
      this.marker = L.marker([e.latlng.lat, e.latlng.lng], {
        icon: defaultIcon,
      }).addTo(this.map);
      // Save location
      this.submissionData.location = [e.latlng.lat, e.latlng.lng];
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
  #location-field {
    // Spacing
    justify-content: space-between;
    margin-bottom: 24px;
    // Sizing
    width: max(40%, 350px);

    input {
      // Spacing
      margin-right: 16px;
    }

    button {
      // Button styling
      padding: 10px 16px;
    }
  }

  #map-container {
    // Sizing
    height: 50vh;
    width: 100%;
  }
}

input {
  // Sizing
  width: 90%;
}
</style>