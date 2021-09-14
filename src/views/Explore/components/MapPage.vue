<template>
  <div id="map-page">
    <div id="map-container"></div>
  </div>
</template>

<script>
// Import external stylesheets
import "leaflet/dist/leaflet.css";

// Import global library
import L from "leaflet";

export default {
  name: "MapPage",
  props: {
    query: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      // Map variables
      center: [34.0522, -118.24],
      map: null,
    };
  },
  methods: {
    handleLeafletSetup: function () {
      // Set map object
      this.map = L.map("map-container").setView(this.center, 3);
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
    },
  },
  mounted() {
    this.handleLeafletSetup();
  }
};
</script>

<style lang="scss" scoped>
#map-page {
  // Spacing
  margin: 64px 0;

  #map-container {
    // Sizing
    height: 70vh;
    width: 100%;
    // Place below content
    z-index: 0;
  }
}
</style>