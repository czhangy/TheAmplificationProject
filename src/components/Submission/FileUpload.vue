<template>
  <div>
    <div class="section-header">
      <p>Select item contribution type</p>
      <i class="fas fa-asterisk"></i>
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
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
      <i class="fas fa-info-circle" @click="handleUnfinished"></i>
    </div>
    <div class="file-upload">
      <p>Drag & drop your files here</p>
      <span>OR</span>
      <button @click="handleUnfinished">Choose File</button>
    </div>
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
  },
  methods: {
    handleUnfinished: function () {
      alert("This feature needs to be implemented still");
    },
  },
};
</script>

<style lang="scss" scoped>
.fa-info-circle {
  // Clickable
  cursor: pointer;
  // Icon styling
  color: $accent-teal;
  font-size: $subheader-font-size;
  // Spacing
  margin-left: 0.6rem;
}

.section-header {
  // Flexbox for layout
  display: flex;
  align-items: center;

  p {
    // Typography
    font-size: $subheader-font-size;
  }

  .fa-asterisk {
    // Icon styling
    color: red;
    font-size: 0.7rem;
    // Spacing
    margin-left: 0.3rem;
    margin-bottom: 1rem;
  }
}

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
    // Clickable
    cursor: pointer;

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

// Sticky hover
@media (hover: hover) {
  button {
    &:hover {
      transform: scale(1.05);
    }
  }

  .media-icon {
    &:hover {
      i,
      p {
        transform: scale(1.1);
      }
    }
  }
}
</style>