<template>
  <div>
    <div class="section-header">
      <p>Select item contribution type</p>
      <i class="fas fa-asterisk"></i>
      <i class="fas fa-info-circle" v-if="!disabled" @click="handleTooltip(0)"
        ><Tooltip :open="tooltipState[0]"
      /></i>
    </div>
    <div id="media-icons">
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
    <div id="file-upload" v-if="!disabled">
      <p>Drag & drop your files here</p>
      <span>OR</span>
      <label>
        <input type="file" @change="handleFileSelect" />
        Choose File
      </label>
    </div>
    <ul>
      <li v-for="(file, i) in submissionData.files" :key="i">
        <p>{{ file.name }}</p>
        <i
          class="fa fa-times"
          v-if="!disabled"
          aria-hidden="true"
          @click="handleFileRemove(i)"
        ></i>
      </li>
    </ul>
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
      files: [],
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
  mounted() {
    // Handle icon cursor
    if (this.disabled)
      document.getElementsByClassName("media-icon").forEach((icon) => {
        icon.classList.remove("pointer");
      });
    else
      document.getElementsByClassName("media-icon").forEach((icon) => {
        icon.classList.add("pointer");
      });
    // Set up drag and drop
    if (!this.disabled) {
      // Select area for drag and drop
      let dropArea = document.getElementById("file-upload");
      // Prevent defaults on target events
      ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
        dropArea.addEventListener(eventName, this.preventDefaults, false);
      });
      // Highlight during drag and drop process
      ["dragenter", "dragover"].forEach((eventName) => {
        dropArea.addEventListener(
          eventName,
          () => dropArea.classList.add("highlighted"),
          false
        );
      });
      ["dragleave", "drop"].forEach((eventName) => {
        dropArea.addEventListener(
          eventName,
          () => dropArea.classList.remove("highlighted"),
          false
        );
      });
      // Handle the drop action
      dropArea.addEventListener("drop", this.handleFileSelect, false);
    }
  },
  beforeUnmount() {
    // Clean up drag and drop
    if (!this.disabled) {
      let dropArea = document.getElementById('file-upload');
      ["dragenter", "dragover", "dragleave", "drop"].forEach((eventName) => {
        dropArea.removeEventListener(eventName, this.preventDefaults, false);
      });
      ["dragenter", "dragover"].forEach((eventName) => {
        dropArea.removeEventListener(
          eventName,
          () => dropArea.classList.add("highlighted"),
          false
        );
      });
      ["dragleave", "drop"].forEach((eventName) => {
        dropArea.removeEventListener(
          eventName,
          () => dropArea.classList.remove("highlighted"),
          false
        );
      });
      dropArea.removeEventListener("drop", this.handleFileSelect, false);
    }
  },
  methods: {
    handleTooltip: function (ind) {
      this.tooltipState[ind] = !this.tooltipState[ind];
    },
    // File select methods
    handleFileSelect: function (e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.submissionData.files.push(files[0]);
    },
    preventDefaults: function (e) {
      // Prevent event's default behaviors
      e.preventDefault();
      // Stop events from bubbling higher than necessary
      e.stopPropagation();
    },
    handleFileRemove: function (ind) {
      this.submissionData.files.splice(ind, 1);
    },
  },
};
</script>

<style lang="scss" scoped>
#media-icons {
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

#file-upload {
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

  label {
    // Container spacing
    padding: 0.5rem 1rem;
    // Typography
    font-family: $alt-font;
    font-weight: bold;
    // Clickable
    cursor: pointer;
    // Button styling
    background: $accent-teal;
    color: white;
    border-radius: 5px;

    input[type="file"] {
      // Hide default button
      display: none;
    }
  }
}

.highlighted {
  // Color background fror drag hover
  background: lighten(lightgrey, 10);
}

ul {
  // Sizing
  width: 90%;
  // Centering + spacing
  margin: 0 auto;
  // Remove bullet points
  list-style: none;

  li {
    // Container spacing
    padding: 2rem;
    // Style container
    background: lighten(lightgrey, 10);
    border: 2px solid lightgrey;
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;
    // Spacing
    margin-top: 2rem;

    p {
      // Typography
      font-size: $subheader-font-size;
      font-family: $alt-font;
      font-weight: normal;
    }

    .fa-times {
      // Icon sizing
      font-size: 2rem;
      // Clickable
      cursor: pointer;
    }
  }
}

// Handle sticky hover
@media (hover: hover) {
  #file-upload > label {
    &:hover {
      // Animate
      background: $accent-dark-teal;
    }
  }
}
</style>