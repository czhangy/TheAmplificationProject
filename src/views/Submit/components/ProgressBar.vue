<template>
  <div id="progress-bar">
    <div class="step" v-for="(label, i) in labels" :key="i">
      <div class="container">
        <div class="bubble default-bubble" v-if="maxPage < i">
          {{ i + 1 }}
          <label class="label">{{ label }}</label>
        </div>
        <div class="bubble active-bubble" v-else @click="onClick(i)">
          {{ i + 1 }}
          <label class="active-label">{{ label }}</label>
        </div>
      </div>
      <hr class="bar" v-if="i !== labels.length - 1 && maxPage <= i" />
      <hr class="active-bar" v-else-if="i !== labels.length - 1" />
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
    // Nav function
    handleCircleClick(i) {
      // Don't let the user advance to future pages before completing current ones
      if (i > this.active) return;
      this.onClick(i);
    },
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

  .step {
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
      // Spacing
      margin: 0 6px;
      // Positioning
      position: relative;

      label {
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
      }

      .active-label {
        // Typography
        color: $accent-teal;
      }
    }

    .default-bubble {
      // Bubble styling
      border: 1px solid var(--default);
      // Typography
      color: var(--default);
    }

    .active-bubble {
      // Bubble styling
      background: $accent-teal;
      // Typography
      color: white;
      // Clickable
      cursor: pointer;
    }

    hr {
      // Bar styling
      background: var(--default);
      // Sizing
      height: 2px;
      width: 10vw;
      border: none;
    }

    .active-bar {
      // Bar styling
      background: $accent-teal;
    }
  }
}

// Smaller layouts
@media screen and (max-width: 1023px) {
  #progress-bar {
    // Respace to account for hidden text
    margin-bottom: 24px;

    .step {
      .bubble {
        // Resize
        height: 40px;
        width: 40px;
        line-height: 40px;
        // Resize font
        font-size: 1.2rem;

        label {
          // Hide text on smaller layouts
          display: none;
        }
      }

      hr {
        // Resize
        width: 5vw;
      }
    }
  }
}
</style>