<template>
  <div id="all-page">
    <div id="all-page-header">
      <p id="all-page-count">Showing 103 items</p>
      <Pagination
        ref="header-pagination"
        :maxPage="maxPage"
        :onClick="handlePagination"
      />
    </div>
    <div id="all-page-content">
      <div
        class="content-container"
        v-for="i in 12"
        :key="i"
        @click="onClick(test)"
      >
        <HoverPanel header="Lorem ipsum" />
      </div>
    </div>
    <Pagination
      id="footer-nav"
      ref="footer-pagination"
      :maxPage="maxPage"
      :onClick="handlePagination"
    />
  </div>
</template>

<script>
// Import global components
import HoverPanel from "@/components/global/HoverPanel.vue";

// Import local components
import Pagination from "./Pagination.vue";

export default {
  name: "AllPage",
  components: {
    HoverPanel,
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
        name: "Piece Name",
        artist: "Artist Name",
        desc: "Suspendisse augue erat, venenatis ut ante ornare, pretium rutrum magna. Donec accumsan erat felis, non egestas nibh mattis convallis. Curabitur dolor orci, lobortis sed pretium et, porta id velit. Pellentesque vehicula sem leo. Maecenas cursus, est eu laoreet",
        format: "Text",
        contributor: "N/A",
        medium: "Pencil on paper",
        size: "40 x 40 in.",
        year: "2019",
        rights: "Rights reserved",
        location: {
          lat: 34,
          lng: -118,
        },
        tags: ["Tag 1", "Tag 2", "Tag 3", "Tag 4", "Tag 5", "Tag 6"],
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
#all-page {
  // Spacing
  margin-top: 48px;
  margin-bottom: 64px;
  // Positioning
  position: relative;

  #all-page-header {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;

    #all-page-count {
      // Typography
      font-size: 1.5rem;
      font-weight: bold;
    }
  }

  #all-page-content {
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
    }
  }

  #footer-nav {
    // Positioning
    position: absolute;
    right: 0;
  }
}
</style>