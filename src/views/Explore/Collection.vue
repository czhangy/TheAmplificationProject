<template>
  <div id="collection">
    <button id="collection-back-button" @click="onBack">← Back</button>
    <div id="collection-banner">
      <strong id="collection-name">{{ collection.name }}</strong>
      <p id="collection-desc">
        {{ collection.desc }}
      </p>
    </div>
    <div id="collection-works">
      <div id="collection-works-content">
        <div
          class="content-container"
          v-for="i in limit"
          :key="i"
          @click="onClick('placeholder')"
        >
          <HoverPanel header="Lorem ipsum" />
        </div>
      </div>
      <button id="load-more-button" @click="handleLoadMore">Load More</button>
    </div>
  </div>
</template>

<script>
// Import global components
import HoverPanel from "@/components/global/HoverPanel.vue";

export default {
  name: "Collection",
  components: {
    HoverPanel,
  },
  props: {
    collection: {
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
      limit: 9,
    };
  },
  methods: {
    handleLoadMore: function () {
      this.limit += 9;
    },
  },
};
</script>

<style lang="scss" scoped>
#collection {
  // Positioning for children
  position: relative;
  // Sizing
  min-height: 100vh;

  #collection-back-button {
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

  #collection-banner {
    // Flexbox for display
    display: flex;
    justify-content: center;
    align-items: center;
    // Sizing
    width: 100%;
    // Inner spacing
    padding: 128px 64px;
    // Shadow for separation
    box-shadow: inset 0 -5px 5px -5px $box-shadow;

    #collection-name {
      // Typography
      font-size: 2rem;
      color: $accent-teal;
      // Spacing
      margin-right: 96px;
      // Display
      display: block;
    }

    #collection-desc {
      // Typography
      font-size: 1rem;
      font-family: $alt-font;
      // Sizing
      max-width: 60%;
    }
  }

  #collection-works {
    // Inner spacing
    padding: 48px 64px;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    align-items: center;

    #collection-works-content {
      // Sizing
      width: 100%;
      // Spacing
      margin: 48px 0;
      // Grid for layout
      display: grid;
      grid-template-columns: 1fr 1fr 1fr;
      gap: 15px;

      .content-container {
        // Sizing
        width: 100%;
        height: 40vh;
        background: red;
      }
    }

    #load-more-button {
      // Button styling
      border-radius: 10px;
      background: $accent-teal;
      padding: 12px 24px;
      // Remove default styling
      border: none;
      // Typography
      font-size: 1.5rem;
      font-family: $main-font;
      color: white;
      // Clickable
      cursor: pointer;
      // Centering
      margin: 0 auto;
    }
  }
}

// Handle sticky hover
@media (hover: hover) {
  #collection > #collection-works > #load-more-button {
    &:hover {
      background: $accent-light-teal;
    }
  }
}
</style>