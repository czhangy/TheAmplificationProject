<template>
  <div class="pagination">
    <button class="pagination-nav" @click="onClick(curPage - 1)">&lt;</button>
    <button
      class="pagination-nav"
      v-for="(page, i) in bounds"
      :key="i"
      @click="onClick(page - 1)"
    >
      <p v-if="handleStyling(i)" class="active">{{ page }}</p>
      <p v-else>{{ page }}</p>
    </button>
    <button class="pagination-nav" @click="onClick(curPage + 1)">></button>
  </div>
</template>

<script>
export default {
  name: "Pagination",
  props: {
    maxPage: {
      type: Number,
      required: true,
    },
    onClick: {
      type: Function,
      required: true,
    },
  },
  data() {
    return {
      bounds: [],
      curPage: null,
    };
  },
  methods: {
    // Pagination display function
    handleBounds: function (page) {
      // Set page
      this.curPage = page;
      // Reset bounds
      this.bounds = [];
      // Full range of bounds is within valid pages
      if (this.curPage + 5 <= this.maxPage)
        for (let i = 0; i < 5; i++) this.bounds.push(this.curPage + i + 1);
      // Show last 5 pages
      else for (let i = 4; i >= 0; i--) this.bounds.push(this.maxPage - i);
    },
    // Nav styling function
    handleStyling: function (i) {
      // Default display --> first page is active
      if (this.curPage + 5 <= this.maxPage) return i === 0;
      // Last 5 pages display
      else return i === 5 - (this.maxPage - this.curPage);
    },
  },
  created() {
    // Init styling + display
    this.handleBounds(0);
  },
};
</script>

<style lang="scss" scoped>
.pagination {
  // Flexbox for layout
  display: flex;
  align-items: center;

  .pagination-nav {
    // Remove default styling
    background: none;
    border: none;
    // Clickable
    cursor: pointer;
    // Spacing
    margin: 0 4px;
    // Typography
    font-size: 1rem;
    font-family: $alt-font;
    font-weight: bold;
  }

  p {
    // Typography
    font-size: 1.2rem;
    // Spacing
    margin: 0 4px;
  }

  .active {
    // Typography
    color: $accent-teal;
  }

  .hide {
    // Hide from view
    display: none;
  }
}
</style>