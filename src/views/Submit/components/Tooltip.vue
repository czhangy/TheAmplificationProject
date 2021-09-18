<template>
  <div class="tooltip" v-if="open">
    <div class="tooltip-arrow" />
    <div class="tooltip-body">
      <p class="tooltip-content">{{ message }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Tooltip",
  props: {
    message: {
      type: String,
      default: "This is a tooltip.",
    },
    open: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style lang="scss" scoped>
.tooltip {
  // Flexbox for layout
  display: flex;
  align-items: center;
  // Positioning
  position: absolute;
  top: 50%;
  left: 32px;
  transform: translate(0, -50%);

  .tooltip-arrow {
    // Make triangle
    border-top: 10px solid transparent;
    border-bottom: 10px solid transparent;
    border-right: 10px solid lighten(lightgrey, 10);
  }

  .tooltip-body {
    // Sizing
    width: 240px;
    // Color styling
    background: lighten(lightgrey, 10);
    // Container shaping
    border-radius: 5px;
    // Inner spacing
    padding: 16px;

    .tooltip-content {
      // Typography
      font-family: $alt-font;
      color: $font-color;
      font-size: $body-font-size;
      font-weight: normal;
      // Spacing
      line-height: 1.4;
    }
  }
}
</style>