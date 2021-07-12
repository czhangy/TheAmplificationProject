<template>
  <div class="accordion">
    <div class="accordion-entry" v-for="(panel, i) in panelContent" :key="i">
      <div class="accordion-panel">
        <p>{{ panel.title }}</p>
        <i
          class="fa fa-chevron-down"
          aria-hidden="true"
          v-if="!accordionOpen[i]"
          @click="handleAccordionClick(i)"
        ></i>
        <i
          class="fa fa-chevron-up"
          aria-hidden="true"
          v-else
          @click="handleAccordionClick(i)"
        ></i>
      </div>
      <p class="panel-body" v-if="accordionOpen[i]">{{ panel.body }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Accordion",
  props: {
    panelContent: {
      type: Array,
      default: [],
    },
  },
  data() {
    return {
      accordionOpen: [],
    };
  },
  mounted() {
    for (let i = 0; i < this.panelContent.length; i++)
      this.accordionOpen[i] = false;
  },
  methods: {
    handleAccordionClick(i) {
      this.accordionOpen[i] = !this.accordionOpen[i];
    },
  },
};
</script>

<style lang="scss" scoped>
.accordion {
  // Container border
  border: 2px solid lightgrey;
  border-bottom: none;
  // Typography
  font-family: $alt-font;
  font-size: $body-font-size;
  // Sizing
  width: 100%;

  .accordion-entry {
    // Border
    border-bottom: 2px solid lightgrey;

    .accordion-panel {
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;
      // Spacing
      padding: 1rem 2rem;

      i {
        // Icon styling
        color: $accent-teal;
        font-size: 1.2rem;
        // Clickable
        cursor: pointer;
        // Spacing
        margin-left: 1rem;
      }
    }

    .panel-body {
      // Typography
      font-style: italic;
      // Border
      border-top: 2px solid lightgrey;
      // Background
      background: lighten(lightgrey, 10);
      // Spacing
      padding: 1rem 2rem;
    }
  }
}
</style>