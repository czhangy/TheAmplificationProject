<template>
  <div id="file-upload">
    <div class="section-header">
      <p class="section-header-text">Select item contribution type</p>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div id="media-icons">
      <div class="media-icon" @click="onClick(0)">
        <i id="text-icon" class="icon fas fa-file-alt" />
        <label class="label" for="text-icon">Text</label>
      </div>
      <div class="media-icon" @click="onClick(1)">
        <i id="image-icon" class="icon fas fa-image" />
        <label class="label" for="image-icon">Image</label>
      </div>
      <div class="media-icon" @click="onClick(2)">
        <i id="video-icon" class="icon fas fa-video" />
        <label class="label" for="video-icon">Video</label>
      </div>
      <div class="media-icon" @click="onClick(3)">
        <i id="audio-icon" class="icon fas fa-volume-up" />
        <label class="label" for="audio-icon">Audio</label>
      </div>
    </div>
    <div class="section-header">
      <p class="section-header-text">File Upload</p>
      <i class="asterisk fas fa-asterisk" />
    </div>
    <div id="file-upload-area" v-if="maxFiles > submissionData.files.length">
      <p class="drag-and-drop-text">
        Drag & drop your files here<br />
        <br />
        OR
        <br />
        <br />
      </p>
      <label id="file-upload-button">
        <input type="file" @change="handleFileSelect" />
        Choose File
      </label>
    </div>
    <ul id="file-list">
      <li class="file-entry" v-for="(file, i) in submissionData.files" :key="i">
        <p class="file-name">{{ file.name }}</p>
        <i
          class="file-delete-button fa fa-times"
          v-if="!disabled"
          aria-hidden="true"
          @click="handleFileRemove(i)"
        />
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "FileUpload",
  props: {
    submissionData: {
      type: Object,
      required: true,
    },
    onClick: {
      type: Function,
      required: true,
    },
    onUpload: {
      type: Function,
      required: true,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    maxFiles: {
      type: Number,
      default: 1,
    },
  },
  methods: {
    // Icon styling method
    handleIconStyling: function () {
      if (this.disabled)
        document.getElementsByClassName("media-icon").forEach((icon) => {
          icon.classList.remove("pointer");
        });
      else
        document.getElementsByClassName("media-icon").forEach((icon) => {
          icon.classList.add("pointer");
        });
    },
    // Drag and drop methods
    handleDropAreaInit: function () {
      if (!this.disabled) {
        // Select area for drag and drop
        let dropArea = document.getElementById("file-upload-area");
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
    handleDropAreaRemove: function () {
      if (!this.disabled) {
        let dropArea = document.getElementById("file-upload-area");
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
      // Remove from submission data
      this.submissionData.files.splice(ind, 1);
    },
  },
  mounted() {
    // Handle pointer cursor on icons
    this.handleIconStyling();
    if (this.submissionData.files.length === 0)
      // Set up drag and drop
      this.handleDropAreaInit();
  },
  beforeUnmount() {
    if (this.submissionData.files.length === 0)
      // Clean up drag and drop
      this.handleDropAreaRemove();
  },
};
</script>

<style lang="scss" scoped>
#file-upload {
  // Spacing + centering
  margin: 48px auto 0 auto;
  // Sizing
  width: 80%;

  .section-header {
    // Flexbox for layout
    display: flex;
    align-items: center;
    // Sizing
    max-width: 640px;

    .section-header-text {
      // Typography
      font-size: $subheader-font-size;
      font-weight: bold;
    }

    .asterisk {
      // Icon styling
      color: red;
      font-size: calc(clamp(0.4rem, 0.28rem + 0.48vw, 0.7rem));
      // Spacing
      margin-left: 4px;
      margin-bottom: 16px;
    }
  }

  #media-icons {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    align-items: center;
    // Centering + spacing
    margin: calc(clamp(2.5rem, 1.5rem + 4vw, 5rem)) auto;
    // Sizing
    width: 80%;

    .media-icon {
      // Flexbox for centering
      display: flex;
      flex-direction: column;
      align-items: center;

      &.pointer {
        // Clickable
        cursor: pointer;
      }

      .icon {
        // Spacing
        margin-bottom: 16px;
        // Icon styling
        color: grey;
        font-size: calc(clamp(3rem, 2.2rem + 3.2vw, 5rem));
      }

      .label {
        // Typography
        font-size: $body-font-size;
        font-weight: bold;
      }
    }
  }

  #file-upload-area {
    // Sizing
    width: 90%;
    // Box styling
    border: 1px dashed gray;
    // Centering + spacing
    margin: calc(clamp(2.5rem, 1.5rem + 4vw, 5rem)) auto 0 auto;
    // Flexbox for layout
    display: flex;
    flex-direction: column;
    align-items: center;
    // Typography
    font-size: $subheader-font-size;
    color: lightgrey;
    // Container spacing
    padding: 96px 0;

    .drag-and-drop-text {
      // Alignment
      text-align: center;
    }

    #file-upload-button {
      // Container spacing
      padding: 8px 16px;
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

  #file-list {
    // Sizing
    width: 90%;
    // Centering + spacing
    margin: 0 auto;
    // Remove bullet points
    list-style: none;

    .file-entry {
      // Container spacing
      padding: 32px;
      // Style container
      background: lighten(lightgrey, 10);
      border: 2px solid lightgrey;
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;
      // Spacing
      margin-top: 32px;

      .file-name {
        // Typography
        font-size: $subheader-font-size;
        font-family: $alt-font;
        font-weight: normal;
      }

      .file-delete-button {
        // Icon sizing
        font-size: 2rem;
        // Clickable
        cursor: pointer;
      }
    }
  }
}

// Handle sticky hover
@media (hover: hover) {
  #file-upload > #file-upload-area > #file-upload-button:hover {
    // Animate
    background: $accent-dark-teal;
  }
}

// Smaller layouts
@media screen and (max-width: 767px) {
  #file-upload > #media-icons {
    // Resize
    width: 100%;
  }
}
</style>