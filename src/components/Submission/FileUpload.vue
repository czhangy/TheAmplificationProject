<template>
  <div>
    <div class="section-header">
      <p>Select item contribution type</p>
      <i class="fas fa-asterisk"></i>
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipState[0]"
      /></i>
    </div>
    <div class="media-icons">
      <div class="media-icon" @click="onClick(0)">
        <i class="fas icon fa-file-alt"></i>
        <p>Text</p>
      </div>
      <div class="media-icon" @click="onClick(1)">
        <i class="fas icon fa-image"></i>
        <p>Image</p>
      </div>
      <div class="media-icon" @click="onClick(2)">
        <i class="fas icon fa-video"></i>
        <p>Video</p>
      </div>
      <div class="media-icon" @click="onClick(3)">
        <i class="fas icon fa-volume-up"></i>
        <p>Audio</p>
      </div>
      <div class="media-icon" @click="onClick(4)">
        <i class="fas icon fa-calendar-alt"></i>
        <p>Event</p>
      </div>
    </div>
    <div class="section-header">
      <p>File Upload</p>
      <i class="fas fa-asterisk"></i>
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(1)"
        ><Tooltip :open="tooltipState[1]"
      /></i>
    </div>
    <div class="file-upload">
      <p>Drag & drop your files here</p>
      <span>OR</span>
      <button @click="handleUnfinished">Choose File</button>
    </div>
  </div>
</template>

<script>
// Import local components
import Tooltip from "@/components/Submission/Tooltip";

export default {
  name: "FileUpload",
  components: {
    Tooltip,
  },
  data() {
    return {
      tooltipState: [false, false],
    };
  },
  props: {
    submissionData: {
      type: Object,
      required: true,
    },
    onClick: {
      type: Function,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {
    handleTooltip: function (ind) {
      this.tooltipState[ind] = !this.tooltipState[ind];
    },
  },
};
</script>

<style lang="scss" scoped>
.media-icons {
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  align-items: center;
  // Centering + spacing
  margin: 5rem auto;
  // Sizing
  width: 80%;

  .media-icon {
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    align-items: center;

    i {
      // Spacing
      margin-bottom: 1rem;
      // Icon styling
      color: grey;
      font-size: 5rem;
    }

    p {
      // Typography
      font-size: $body-font-size;
      font-weight: bold;
    }
  }
}

.file-upload {
  // Sizing
  width: 90%;
  // Box styling
  border: 1px dashed gray;
  // Centering + spacing
  margin: 5rem auto 0 auto;
  // Flexbox for layout
  display: flex;
  flex-direction: column;
  align-items: center;
  // Typography
  font-size: $subheader-font-size;
  color: lightgrey;
  // Container spacing
  padding: 6rem 0;

  span {
    // Spacing
    margin: 3rem 0;
  }

  button {
    // Border styling
    border: 1px solid lightgrey;
    // Container spacing
    padding: 0.5rem 1rem;
    // Typography
    font-family: $alt-font;
    // Clickable
    cursor: pointer;
  }
}
</style>