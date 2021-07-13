<template>
  <div class="submission">
    <ProgressBar
      :pages="pages"
      :active="curPage"
      :onClick="handleBarClick"
      :key="curPage"
    />
    <div class="nav-buttons">
      <button v-if="curPage > 0" @click="handleNavClick(-1)">Back</button>
      <button v-if="curPage < pages.length - 1" @click="handleNavClick(1)">Next</button>
    </div>
  </div>
</template>

<script>
import ProgressBar from "@/components/ProgressBar";

export default {
  name: "Submission",
  components: {
    ProgressBar,
  },
  data() {
    return {
      pages: [
        "File Upload",
        "Personal Details",
        "Contribution Basics",
        "Contribution Details",
        "Review & Submit",
      ],
      curPage: 0,
    };
  },
  methods: {
    handleBarClick(i) {
      this.curPage = i;
    },
    handleNavClick(inc) {
      this.curPage += inc;
    },
  },
};
</script>

<style lang="scss" scoped>
.submission {
  width: 100%;

  .nav-buttons {
    // Flexbox for centering
    display: flex;
    justify-content: center;

    button {
      // Spacing
      margin: 3rem;
      // Button styling
      background: $accent-dark-teal;
      padding: 0.625rem 2rem;
      border-radius: 10px;
      // Typography
      font-family: $alt-font;
      font-weight: $bold;
      font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
      color: white;
      text-align: center;
      // Smooth hover animation
      transition: all 0.2s ease;
      // Remove default button styling
      border: none;
      // Clickable
      cursor: pointer;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  button {
    &:hover {
      transform: scale(1.05);
    }
  }
}
</style>