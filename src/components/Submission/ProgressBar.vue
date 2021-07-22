<template>
  <div class="bar">
    <div class="page" v-for="(page, i) in pages" :key="i">
      <div class="page-circle" @click="handleCircleClick(i)">
        {{ i + 1 }}
      </div>
      <div class="page-label">
        {{ page }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ProgressBar",
  props: {
    pages: {
      type: Array,
      default: [],
    },
    active: {
      type: Number,
      default: 0,
    },
    onClick: {
        type: Function,
        required: true,
    },
  },
  mounted() {
    // Set styling for each bubble
    let arr = document.getElementsByClassName("page-circle");
    for (let i = 0; i < this.pages.length; i++) {
      if (i > this.active) return;
      else if (i === this.active) {
        arr[i].style.background = "#298A7E";
        arr[i].style.color = "white";
      } else {
        arr[i].style.background = "lighten(lightgrey, 10)";
        arr[i].style.color = "#333";
        arr[i].style.cursor = "pointer";
        arr[i].style.border = "3px solid #298A7E";
      }
    }
  },
  methods: {
    handleCircleClick(i) {
      // Don't let the user advance to future pages before completing current ones
      if (i > this.active) return;
      this.onClick(i);
    },
  },
};
</script>

<style lang="scss" scoped>
.bar {
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  align-items: center;
  // Spacing
  margin: 3rem auto 6rem auto;
  width: 80%;

  .page {
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    align-items: center;
    // Spacing
    margin: 0;

    .page-circle {
      // Background
      background: lighten(lightgrey, 10);
      // Flexbox for centering
      display: flex;
      justify-content: center;
      align-items: center;
      // Shaping
      border-radius: 50%;
      // Sizing
      height: 4rem;
      width: 4rem;
      // Typography
      font-family: $alt-font;
      font-size: $subheader-font-size;
      // Spacing
      margin-bottom: 1rem;
    }

    .page-label {
      // Typography
      font-family: $alt-font;
    }
  }
}
</style>