<template>
  <div id="collections-page">
    <div id="collections-page-header">
      <p id="collections-page-count">Showing 103 items</p>
      <Pagination
        ref="header-pagination"
        :maxPage="maxPage"
        :onClick="handlePagination"
      />
    </div>
    <div id="collections-page-content">
      <div
        class="content-container"
        v-for="i in 12"
        :key="i"
        @click="onClick(test)"
      >
        <div class="content-overlay"></div>
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
  name: "CollectionsPage",
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
          name: "Collection Name",
          desc: "Collection Description",
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
#collections-page {
  // Spacing
  margin-top: 48px;
  margin-bottom: 64px;
  // Positioning
  position: relative;

  #collections-page-header {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;

    #collections-page-count {
      // Typography
      font-size: 1.5rem;
      font-weight: bold;
    }
  }

  #collections-page-content {
    // Sizing
    width: 100%;
    // Spacing
    margin: 48px 0;
    // Grid for layout
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 60px;

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
        // Sizing
        width: 100%;
        height: 40vh;
        background: blue;
        // Positioning
        position: absolute;
        left: 16px;
        top: 16px;
      }
    }
  }

  #collections-nav {
    // Positioning
    position: absolute;
    right: 0;
  }
}
</style>