<template>
  <div id="artist">
    <button id="artist-back-button" @click="onBack">← Back</button>
    <div id="artist-banner">
      <strong id="artist-name">{{ artist.name }}</strong>
      <p id="artist-bio">
        {{ artist.bio }}
      </p>
    </div>
    <div id="artist-featured">
      <strong id="artist-featured-title">Featured Work</strong>
      <div id="artist-featured-work">
        <div class="placeholder" />
        <div id="artist-featured-text">
          <strong id="artist-featured-title">Featured Work Title</strong>
          <p id="artist-featured-desc">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam
            posuere purus id rhoncus tempor. Vestibulum tincidunt ante ac dolor
            accumsan mollis. Mauris sit amet convallis justo. Pellentesque
            sollicitudin lacinia augue, et fringilla metus tempor nec.
            Pellentesque porttitor est nec quam blandit, in tincidunt ante
            convallis. Donec nec arcu odio. Cras consequat, nulla sed viverra
            consequat, urna enim tincidunt enim, ut sagittis dui neque ut
            ligula. Duis ullamcorper lectus dolor, et lacinia sem interdum non.
            Etiam ac elit viverra, euismod risus ac, porttitor ligula. Sed nec
            lacus sed lacus venenatis facilisis. Ut varius placerat faucibus. In
            id nisl eu arcu tristique rutrum nec sed ante. Vivamus vel lectus
            rhoncus, cursus risus a, cursus ante. Nullam pretium neque vitae
            risus porta iaculis. Nulla et tempor nisl.
          </p>
        </div>
      </div>
    </div>
    <div id="artist-all-work">
      <strong id="artist-all-title">All Works</strong>
      <div id="artist-content">
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
  name: "Artist",
  components: {
    HoverPanel,
  },
  props: {
    artist: {
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
#artist {
  // Positioning for children
  position: relative;

  #artist-back-button {
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

  #artist-banner {
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

    #artist-name {
      // Typography
      font-size: 2rem;
      color: $accent-teal;
      // Spacing
      margin-right: 96px;
      // Display
      display: block;
    }

    #artist-bio {
      // Typography
      font-size: 1rem;
      font-family: $alt-font;
      // Sizing
      max-width: 60%;
    }
  }

  #artist-featured {
    // Inner spacing
    padding: 48px 64px;
    // Sizing
    width: 100%;
    // Shadow for separation
    box-shadow: 0 0 5px $box-shadow;

    #artist-featured-title {
      // Typography
      font-size: 1.7rem;
      // Spacing
      display: block;
      margin-bottom: 16px;
    }

    #artist-featured-work {
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;
      // Sizing
      width: 100%;

      .placeholder {
        // Sizing
        width: 60%;
        height: 40vw;
        background: grey;
      }

      #artist-featured-text {
        // Sizing
        width: 35%;
        // Typography
        font-family: $alt-font;
      }
    }
  }

  #artist-all-work {
    // Inner spacing
    padding: 48px 64px;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    align-items: center;

    #artist-all-title {
      // Typography
      font-size: 1.7rem;
      // Spacing
      display: block;
      margin-bottom: 16px;
      // Alignment
      width: 100%;
    }

    #artist-content {
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
  #artist > #artist-all-work > #load-more-button {
    &:hover {
      background: $accent-light-teal;
    }
  }
}
</style>