<template>
  <!-- HoverPanel.vue is a global component that creates a container which, when hovered over by the user, pops up an overlay containing
       information defined by the props -->
  <div class="hover-panel">
    <div class="hover-panel-overlay">
      <p class="hover-panel-header">
        {{ header }}
      </p>
      <p class="hover-panel-subheader">
        {{ subheader }}
      </p>
      <br />
      <p class="hover-panel-content">
        {{ content }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "HoverPanel",
  props: {
    header: {
      type: String,
      default: "Insert title here",
    },
    subheader: {
      type: String,
      default: "Insert subheader here",
    },
    content: {
      type: String,
      default: "Insert content here",
    },
  },
};
</script>

<style scoped lang="scss">
.hover-panel {
  // Sizing
  height: 100%;
  width: 100%;
  // Clickable
  cursor: pointer;

  .hover-panel-overlay {
    // Sizing
    height: 100%;
    width: 100%;
    // Overlay effect
    background: rgba(0, 0, 0, 0.6);
    // Spacing
    padding: 16px;
    // Set hidden
    visibility: hidden;
    color: white;

    .hover-panel-header {
      // Typography
      font-size: $header-font-size;
      font-weight: bold;
    }

    .hover-panel-subheader {
      // Typography
      font-family: $alt-font;
      font-size: $body-font-size;
    }

    .hover-panel-content {
      // Typography
      font-family: $alt-font;
      font-size: $caption-font-size;
      // Cut off text
      text-overflow: ellipsis;
      // Allow for newlines
      white-space: pre;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  .hover-panel {
    &:hover .hover-panel-overlay {
      // Show
      visibility: visible;
    }
  }
}
</style>