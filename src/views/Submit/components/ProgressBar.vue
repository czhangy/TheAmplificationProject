<template>
  <div id="progress-bar">
    <div class="bubble-container" v-for="(label, i) in labels" :key="i">
      <div class="bubble" @click="onClick(i)">
        {{ i + 1 }}
        <label class="label">{{ label }}</label>
      </div>
      <hr class="line" v-if="i !== labels.length - 1" />
    </div>
  </div>
</template>

<script>
export default {
  name: "ProgressBar",
  props: {
    labels: {
      type: Array,
      default: [],
    },
    curPage: {
      type: Number,
      default: 0,
    },
    maxPage: {
      type: Number,
      default: 0,
    },
    onClick: {
      type: Function,
      required: true,
    },
  },
  methods: {
    // Styling function
    handleStyling: function () {
      let bubbles = document.getElementsByClassName("bubble");
      let labels = document.getElementsByClassName("label");
      let lines = document.getElementsByClassName("line");
      // Style bubbles and labels
      for (let i = 0; i < bubbles.length; i++) {
        if (i > this.maxPage) {
          bubbles[i].classList.remove("active");
          labels[i].classList.remove("active");
        } else {
          bubbles[i].classList.add("active");
          labels[i].classList.add("active");
        }
      }
      // Style transition lines
      for (let i = 0; i < lines.length; i++) {
        if (i >= this.maxPage) lines[i].classList.remove("active");
        else lines[i].classList.add("active");
      }
    },
  },
  mounted() {
    // Initialize styling
    this.handleStyling();
  },
  updated() {
    // Update styling on page nav
    this.handleStyling();
  },
};
</script>

<style lang="scss" scoped>
#progress-bar {
  // Centering
  margin: 0 auto;
  // Flexbox for layout + centering
  display: flex;
  justify-content: center;
  // Spacing
  margin: 60px 0;
  // Variable
  --default: #8f8f8f;

  .bubble-container {
    // Centering
    display: flex;
    justify-content: center;
    align-items: center;

    .bubble {
      // Sizing
      height: 64px;
      width: 64px;
      // Shaping
      border-radius: 50%;
      // Centering
      line-height: 64px;
      text-align: center;
      // Typography
      font-family: $alt-font;
      font-size: 2rem;
      color: var(--default);
      // Spacing
      margin: 0 6px;
      // Positioning
      position: relative;
      // Bubble styling
      border: 1px solid var(--default);

      &.active {
        // Bubble styling
        background: $accent-teal;
        // Typography
        color: white;
        // Clickable
        cursor: pointer;
        // Remove border
        border: none;
      }

      .label {
        // Typography
        font-size: 18px;
        color: var(--default);
        white-space: nowrap;
        // Positioning
        position: absolute;
        top: 64px;
        left: calc(-50% - 24px);
        width: 175px;
        // Centering
        text-align: center;

        &.active {
          // Typography
          color: $accent-teal;
        }
      }
    }

    .line {
      // Bar styling
      background: var(--default);
      // Sizing
      height: 2px;
      width: 10vw;
      border: none;

      &.active {
        // Bar styling
        background: $accent-teal;
      }
    }
  }
}

// Smaller layouts
@media screen and (max-width: 1023px) {
  #progress-bar {
    // Respace to account for hidden text
    margin-bottom: 24px;

    .bubble-container {
      .bubble {
        // Resize
        height: 60px;
        width: 60px;
        line-height: 60px;
        // Resize font
        font-size: 1.4rem;

        .label {
          // Hide text on smaller layouts
          display: none;
        }
      }
    }
  }
}

@media screen and (max-width: 767px) {
  #progress-bar {
    // Respace to account for hidden text
    margin-bottom: 24px;

    .bubble-container {
      .bubble {
        // Resize
        height: 40px;
        width: 40px;
        line-height: 40px;
        // Resize font
        font-size: 1.2rem;
      }

      .line {
        // Resize
        width: 5vw;
      }
    }
  }
}
</style>