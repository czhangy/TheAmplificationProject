<template>
  <div id="artists-page">
    <div id="artists-page-header">
      <p id="artists-page-count">Showing 103 items</p>
      <Pagination
        ref="header-pagination"
        :maxPage="maxPage"
        :onClick="handlePagination"
      />
    </div>
    <div id="artists-page-content">
      <div
        class="content-container"
        v-for="i in 12"
        :key="i"
        @click="onClick(test)"
      >
        <div class="content-overlay">
          <p>NAME, ARTIST</p>
        </div>
      </div>
    </div>
    <Pagination
      id="artists-nav"
      ref="footer-pagination"
      :maxPage="maxPage"
      :onClick="handlePagination"
    />
  </div>
</template>

<script>
// Import local components
import Pagination from "./Pagination.vue";

export default {
  name: "ArtistsPage",
  components: {
    Pagination,
  },
  props: {
    filter: {
      type: String,
      required: true,
    },
    sortBy: {
      type: String,
      required: true,
    },
    query: {
      type: String,
      required: true,
    },
    onClick: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      curPage: 0,
      maxPage: 10,
      contents: [],
      test: {
        name: "Artist Name",
        bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut imperdiet egestas turpis quis congue. Vestibulum eget lacus laoreet, convallis nisl in, dictum urna. In molestie, quam in euismod commodo, mi est fringilla erat, facilisis iaculis eros justo et dolor. Integer ac ornare libero. Maecenas iaculis quis quam et sollicitudin. In posuere mauris",
      },
    };
  },
  methods: {
    // Nav function
    handlePagination: function (page) {
      // Check if new page is within bounds
      if (page >= 0 && page < this.maxPage) {
        this.curPage = page;
        this.$refs["header-pagination"].handleBounds(this.curPage);
        this.$refs["footer-pagination"].handleBounds(this.curPage);
      }
      // Scroll to top
      window.scrollTo(0, 0);
    },
  },
};
</script>

<style lang="scss" scoped>
#artists-page {
  // Spacing
  margin-top: 48px;
  margin-bottom: 64px;
  // Positioning
  position: relative;

  #artists-page-header {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;

    #artists-page-count {
      // Typography
      font-size: 1.5rem;
      font-weight: bold;
    }
  }

  #artists-page-content {
    // Sizing
    width: 100%;
    // Spacing
    margin: 48px 0;
    // Grid for layout
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 20px;

    .content-container {
      // Sizing
      width: 100%;
      height: 40vh;
      background: red;
      // Positioning for children
      position: relative;
      // Clickable
      cursor: pointer;

      .content-overlay {
        // Positioning
        position: absolute;
        bottom: 0;
        // Overlay effect
        background: rgba(0, 0, 0, 0.6);
        // Typography
        color: white;
        font-size: 1.5rem;
        font-weight: bold;
        // Sizing
        width: 100%;
        // Spacing
        padding: 24px 15px;
      }
    }
  }

  #artists-nav {
    // Positioning
    position: absolute;
    right: 0;
  }
}
</style>