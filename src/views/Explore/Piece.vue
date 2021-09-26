<template>
  <div id="piece">
    <button id="piece-back-button" @click="onBack">← Back</button>
    <div id="piece-tabs">
      <div class="piece-tab" @click="handleTabNav(0)">About</div>
      <div class="piece-tab" @click="handleTabNav(1)">Metadata</div>
    </div>
    <div id="piece-info">
      <div id="piece-about">
        <strong id="piece-name">{{ piece.name }}</strong>
        <em id="piece-artist">{{ piece.artist }}</em>
        <p id="piece-desc" v-if="curPage === 0">
          {{ piece.desc }}
        </p>
        <div id="piece-metadata" v-if="curPage === 1">
          <div
            class="piece-metadata-field"
            v-for="(field, i) in metadata"
            :key="i"
          >
            <label>{{ field }}</label>
            <p class="piece-metadata-value">{{ piece[field] }}</p>
          </div>
        </div>
      </div>
      <div id="piece-map-container" />
      <div id="piece-tags">
        <div class="piece-tag" v-for="(tag, i) in piece.tags" :key="i">
          {{ tag }}
        </div>
      </div>
    </div>
    <div class="placeholder" />
  </div>
</template>

<script>
// Import external stylesheets
import "leaflet/dist/leaflet.css";

// Import global libraries
import L from "leaflet";

export default {
  name: "Piece",
  props: {
    piece: {
      type: Object,
      required: true,
    },
    onBack: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      curPage: 0,
      center: this.piece.location,
      map: null,
      marker: null,
    };
  },
  methods: {
    // Map functions
    handleLeafletSetup: function () {
      // Set map object
      this.map = L.map("piece-map-container").setView(this.center, 9);
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
      // Disable interactivity
      this.map.dragging.disable();
      this.map.zoomControl.remove();
      this.map.scrollWheelZoom.disable();
      // Get marker
      this.handleMarkerSetup();
    },
    handleMarkerSetup: function () {
      // Fix icon
      const defaultIcon = new L.icon({
        iconUrl: require("leaflet/dist/images/marker-icon.png"),
        iconSize: [16, 24],
        iconAnchor: [10, 25],
        popupAnchor: [0, -2],
      });
      // Set marker to center
      L.marker(this.center, {
        icon: defaultIcon,
      }).addTo(this.map);
    },
    // Nav functions
    handleTabNav: function (page) {
      this.curPage = page;
      // Update styling
      this.handleTabStyling();
    },
    handleTabStyling: function () {
      let arr = document.getElementsByClassName("piece-tab");
      for (let i = 0; i < arr.length; i++) {
        // Set active tag
        if (this.curPage === i) arr[i].classList.add("active");
        else arr[i].classList.remove("active");
      }
    },
  },
  computed: {
    metadata: function () {
      let fields = [
        "format",
        "insta",
        "contributor",
        "medium",
        "size",
        "year",
        "rights",
      ];
      return fields.filter((field) => this.piece[field] != null);
    },
  },
  mounted() {
    // Set up map
    this.handleLeafletSetup();
    // Style tabs
    this.handleTabStyling();
  },
};
</script>

<style lang="scss" scoped>
#piece {
  // Inner spacing
  padding: 128px 10%;
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  // Positioning for children
  position: relative;

  #piece-back-button {
    // Remove default styling
    background: none;
    border: none;
    // Positioning
    position: absolute;
    top: 32px;
    left: 32px;
    // Clickable
    cursor: pointer;
    // Typography
    color: $accent-teal;
    font-size: 1.2rem;
    font-family: $alt-font;
  }

  #piece-tabs {
    // Sizing
    width: 5%;
    // Flexbox for alignment
    display: flex;
    flex-direction: column;
    align-items: flex-end;

    .piece-tab {
      // Rotate text
      writing-mode: vertical-lr;
      transform: rotate(-180deg);
      -webkit-transform: rotate(-180deg);
      -moz-transform: rotate(-180deg);
      // Border
      border: 2px solid $accent-teal;
      border-left: none;
      border-radius: 0 8px 8px 0;
      // Spacing
      margin-top: 8px;
      // Typography
      font-size: 1.2rem;
      font-family: $alt-font;
      color: $accent-teal;
      // Inner spacing
      padding: 16px 8px;
      // Clickable
      cursor: pointer;
    }

    .active {
      // Active colors
      color: white;
      background: $accent-teal;
    }
  }

  #piece-info {
    // Positioning for children
    position: relative;
    // Sizing
    width: 40%;
    // Inner spacing
    padding: 32px;
    // Separation from background
    box-shadow: 0 0 5px $box-shadow;
    clip-path: inset(-5px 0px -5px -5px);

    #piece-about {
      #piece-name {
        // Typography
        font-size: 1.7rem;
        font-weight: bold;
      }

      #piece-artist {
        // Typography
        font-size: 1.2rem;
        font-family: $alt-font;
        // Layout
        display: block;
        // Spacing
        margin-bottom: 32px;
      }

      #piece-desc {
        // Typography
        font-size: 1rem;
        font-family: $alt-font;
      }

      #piece-metadata {
        .piece-metadata-field {
          // Spacing
          margin-bottom: 8px;
          // Typography
          font-size: 1rem;
          // Flexbox for layout
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
          // Sizing
          width: 100%;

          &:last-child {
            // Remove spacing
            margin-bottom: 0;
          }

          label {
            // Typography
            color: grey;
            letter-spacing: 0.05em;
            font-family: $alt-font;
            text-transform: uppercase;
            // Spacing
            margin-bottom: 8px;
            // Sizing
            width: 40%;
            // Alignment
            text-align: right;
          }

          .piece-metadata-value {
            // Typography
            font-family: $alt-font;
            font-weight: bold;
            // Sizing
            width: 50%;
          }
        }
      }
    }

    #piece-map-container {
      // Sizing
      height: 30vh;
      width: 100%;
      // Remove overlap
      z-index: 0;
      // Spacing
      margin: 32px 0;
    }

    #piece-tags {
      // Flexbox for layout
      display: flex;
      align-items: center;
      flex-wrap: wrap;

      .piece-tag {
        // Prevent wrap
        white-space: nowrap;
        // Tag styling
        border: 1px solid $accent-teal;
        border-radius: 4px;
        // Typography
        font-size: 0.8rem;
        color: $accent-teal;
        font-family: $alt-font;
        font-weight: bold;
        // Spacing
        margin-right: 8px;
        margin-bottom: 4px;
        // Inner spacing
        padding: 4px 8px;
      }
    }
  }

  .placeholder {
    background: grey;
    width: 55%;
    // Separation from background
    box-shadow: 0 0 5px $box-shadow;
    clip-path: inset(-5px -5px -5px 0px);
  }
}

// Sticky hover
@media (hover: hover) {
  #piece > #piece-tabs > .piece-tab:hover {
    // Animate
    background: $accent-light-teal;
    color: white;
    border: 2px solid $accent-light-teal;
  }
}
</style>