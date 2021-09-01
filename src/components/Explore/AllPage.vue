<template>
  <div id="all-page">
    <div id="all-page-header">
      <p>Showing 103 items</p>
      <Pagination
        ref="header-pagination"
        :maxPage="maxPage"
        :onClick="handlePagination"
      />
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
// Import local components
import Pagination from "./Pagination.vue";

export default {
  name: "AllPage",
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
  },
  data() {
    return {
      curPage: 0,
      maxPage: 5,
      contents: [],
    };
  },
  methods: {
    // Nav function
    handlePagination: function (page) {
      // Check if new page is within bounds
      if (page >= 0 && page < this.maxPage) {
        this.curPage = page;
        this.$refs["header-pagination"].handleDisplay(this.curPage);
        this.$refs["footer-pagination"].handleDisplay(this.curPage);
      }
      console.log(this.curPage);
    },
  },
};
</script>

<style lang="scss" scoped>
#all-page {
  // Spacing
  margin: 48px 0;
  // Positioning
  position: relative;

  #all-page-header {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;

    p {
      // Typography
      font-size: 1.5rem;
    }
  }

  #footer-nav {
    // Positioning
    position: absolute;
    right: 0;
  }
}
</style>