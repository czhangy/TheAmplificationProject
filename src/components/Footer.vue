<template>
  <div id="footer">
    <div class="footer-text">
      Powered by <a href="https://omeka.org/" target="_blank">Omeka</a> | Site
      Hosted by
      <a href="https://reclaimhosting.com/" target="_blank">Reclaim Hosting</a>
      | 2019 - 2021
    </div>
    <div class="footer-mailing-list">
      <p>Join Our Mailing List!</p>
      <div class="mailing-list-fields">
        <label for="name">Name:</label>
        <input v-model="name" id="name" />
        <label for="email">Email:</label>
        <input v-model="email" id="email" />
      </div>
      <button @click="handleSubscribe">Subscribe!</button>
    </div>
    <div class="footer-socials">
      <a
        class="fa fa-twitter"
        href="https://twitter.com/AmplifiProject"
        target="_blank"
        aria-hidden="true"
      ></a>
      <a
        href="https://www.facebook.com/TheAmplificationProject/"
        target="_blank"
        class="fa fa-facebook-f"
      ></a>
      <a
        href="https://www.instagram.com/theamplificationproject/"
        target="_blank"
        class="fa fa-instagram"
      ></a>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  methods: {
    handleSubscribe: function () {
      alert(
        `The handleSubscribe() function in News.vue must still be implemented, but here's the data stored in the component for testing:\n
        name = "${this.name}"
        email = "${this.email}"`
      );
      this.name = "";
      this.email = "";
    },
  },
  data() {
    return {
      name: "",
      email: "",
    };
  },
};
</script>

<style scoped lang="scss">
#footer {
  // Sizing
  width: 100%;
  // Bar styling
  background: $accent-light-grey;
  // Spacing
  padding: 3rem;
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  align-items: center;

  .footer-text {
    // Typography
    font-family: $alt-font;
    color: $font-color;
    font-size: $caption-font-size;
    // Spacing
    line-height: 2;
    font-weight: $normal;

    .footer-link {
      // Remove effects of router link
      text-decoration: none;
      color: $accent-teal;
    }

    a {
      // Remove effects of anchor tag
      text-decoration: none;
      // Color styling
      color: $accent-teal;
    }
  }

  .footer-mailing-list {
    // Typography
    font-family: $alt-font;
    color: $font-color;
    font-size: $caption-font-size;
    // Spacing
    line-height: 2;
    display: flex;
    flex-direction: column;
    align-items: flex-start;

    .mailing-list-fields {
      // Flexbox for layout
      display: flex;
      align-items: center;

      input {
        // Typography
        font-family: $alt-font;
        color: $font-color;
        font-size: $caption-font-size;
      }

      label {
        // Spacing
        margin: 0 0.5rem;
      }
    }

    button {
      // Typography
      font-family: $alt-font;
      font-size: 1rem;
      color: $accent-teal;
      // Spacing
      margin-top: 0.5rem;
      // Button sizing
      border-radius: 20px;
      border: 1px solid $accent-teal;
      padding: 0.5rem 2rem;
      // Clickable
      cursor: pointer;
    }
  }

  .footer-socials {
    // Icon centering
    text-align: center;
    // Icon sizing
    font-size: 1.25rem;

    .fa {
      // Icon centering
      line-height: 2.5rem;
      // Icon sizing
      height: 2.5rem;
      width: 2.5rem;
      // Color icon
      color: $accent-teal;
      // Clickable
      cursor: pointer;
      // Spacing
      margin: 0.5rem 1rem;
      // Border
      border: 1px solid $accent-teal;
      border-radius: 100%;
      // Remove effects of anchor
      text-decoration: none;
    }
  }
}

// Media queries
// Sticky hover
@media (hover: hover) {
  #footer {
    .footer-mailing-list {
      button {
        transition: transform 0.2s ease;
        &:hover {
          background: $accent-teal;
          color: $accent-light-grey;
          transform: scale(1.05);
        }
      }
    }
    .footer-socials {
      .fa {
        &:hover {
          background: $accent-teal;
          color: $accent-light-grey;
        }
      }
    }
  }
}

// Mobile layout
@media screen and (max-width: 1300px) {
  #footer > .footer-mailing-list {
    margin: 0 2rem;
    .mailing-list-fields {
      flex-direction: column;
      align-items: flex-start;
      label {
        margin: 0;
      }
    }
    button {
      margin-top: 1rem;
    }
  }
}

@media screen and (max-width: 900px) {
  #footer {
    flex-direction: column;
    height: auto;
    padding: 3rem 1rem;

    .footer-text {
      text-align: center;
      margin-bottom: 1rem;
    }
    .footer-mailing-list {
      margin-bottom: 2rem;
    }
  }
}
</style>