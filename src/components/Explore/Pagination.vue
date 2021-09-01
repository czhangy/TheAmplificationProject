<template>
  <div class="pagination">
    <button @click="onClick(curPage - 1)">&lt;</button>
    <button id="lower-limit" class="hide" @click="onClick(0)">{{ 1 }}</button>
    <p id="leading-break" class="hide">···</p>
    <button v-for="(page, i) in bounds" :key="i" @click="onClick(page - 1)">
      {{ page }}
    </button>
    <p id="trailing-break">···</p>
    <button id="upper-limit" @click="onClick(maxPage - 1)">
      {{ maxPage }}
    </button>
    <button @click="onClick(curPage + 1)">></button>
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
    handleDisplay: function (page) {
      // Set page
      this.curPage = page;
      // Reset bounds
      this.bounds = [];
      // Full pagination should be visible
      if (this.maxPage <= 5) {
        // Set bounds
        for (let i = 0; i < this.maxPage; i++)
          this.bounds.push(this.curPage + i + 1);
        // Hide trailing elements
        document
          .querySelectorAll("#trailing-break")
          .forEach((el) => el.classList.add("hide"));
        document
          .querySelectorAll("#upper-limit")
          .forEach((el) => el.classList.add("hide"));
      } else for (let i = 0; i < 3; i++) this.bounds.push(this.curPage + i + 1);
    },
    // Nav styling function
    handleNavStyling: function () {
      let arr = document.getElementsByTagName("button");
      for (let i = 1; i < arr.length - 1; i++) {
        if (i - 1 === this.curPage) {
          arr[i].classList.add("active");
          console.log(i);
        }
      }
    },
  },
  mounted() {
    // Init styling + display
    this.handleDisplay(0);
  },
};
</script>

<style lang="scss" scoped>
.pagination {
  // Flexbox for layout
  display: flex;
  align-items: center;

  button {
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