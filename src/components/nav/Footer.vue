<template>
  <!-- Footer.vue is a nav component that appears at the bottom of each page -->
  <div id="footer">
    <div id="footer-text">
      Powered by
      <a class="footer-link" href="https://omeka.org/" target="_blank">Omeka</a>
      | Site Hosted by
      <a class="footer-link" href="https://reclaimhosting.com/" target="_blank"
        >Reclaim Hosting</a
      >
      | 2019 - 2021
    </div>
    <form id="footer-mailing-list" @submit.prevent="handleSubscribe">
      <strong class="mailing-list-text">Join Our Mailing List!</strong>
      <div id="mailing-list-fields">
        <label class="mailing-list-label" for="footer-name">Name:</label>
        <input id="footer-name" class="mailing-list-field" v-model="name" />
        <label class="mailing-list-label" for="email-name">Email:</label>
        <input id="email-name" class="mailing-list-field" v-model="email" />
      </div>
      <input id="subscribe-button" type="submit" value="Subscribe!" />
    </form>
    <div id="footer-socials">
      <a
        class="footer-social-link fa fa-twitter"
        href="https://twitter.com/AmplifiProject"
        target="_blank"
        aria-hidden="true"
      />
      <a
        class="footer-social-link fa fa-facebook-f"
        href="https://www.facebook.com/TheAmplificationProject/"
        target="_blank"
      />
      <a
        class="footer-social-link fa fa-instagram"
        href="https://www.instagram.com/theamplificationproject/"
        target="_blank"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer",
  data() {
    return {
      name: "",
      email: "",
    };
  },
  methods: {
    // Submission function
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
};
</script>

<style scoped lang="scss">
#footer {
  // Sizing
  width: 100%;
  // Bar styling
  background: $accent-light-grey;
  // Spacing
  padding: 48px;
  // Flexbox for layout
  display: flex;
  justify-content: space-between;
  align-items: center;

  #footer-text {
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
  }

  #footer-mailing-list {
    // Typography
    font-family: $alt-font;
    color: $font-color;
    font-size: $caption-font-size;
    // Spacing
    line-height: 2;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    align-items: flex-start;

    #mailing-list-fields {
      // Flexbox for layout
      display: flex;
      align-items: center;

      .mailing-list-field {
        // Typography
        font-family: $alt-font;
        color: $font-color;
        font-size: $caption-font-size;
      }

      .mailing-list-label {
        // Spacing
        margin: 0 8px;

        &:first-child {
          // Remove spacing
          margin-left: 0;
        }
      }
    }

    #subscribe-button {
      // Typography
      font-family: $alt-font;
      font-size: 1rem;
      color: $accent-teal;
      // Spacing
      margin-top: 8px;
      // Button sizing
      border-radius: 20px;
      border: 1px solid $accent-teal;
      padding: 8px 32px;
      // Clickable
      cursor: pointer;
    }
  }

  #footer-socials {
    // Icon centering
    text-align: center;
    // Icon sizing
    font-size: 1.25rem;

    .footer-social-link {
      // Icon centering
      line-height: 40px;
      // Icon sizing
      height: 40px;
      width: 40px;
      // Color icon
      color: $accent-teal;
      // Clickable
      cursor: pointer;
      // Spacing
      margin: 8px 16px;
      // Border
      border: 1px solid $accent-teal;
      border-radius: 100%;
      // Remove effects of anchor
      text-decoration: none;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #footer {
    #footer-mailing-list > #subscribe-button:hover {
      // Animate
      background: $accent-teal;
      color: $accent-light-grey;
    }

    #footer-socials > .footer-social-link:hover {
      // Animate
      background: $accent-teal;
      color: $accent-light-grey;
    }
  }
}

// Mobile layout
@media screen and (max-width: 1439px) {
  #footer > #footer-mailing-list {
    // Respace
    margin: 0 32px;
    // Center
    align-items: center;

    #mailing-list-fields {
      // Column layout
      flex-direction: column;
      align-items: flex-start;

      .mailing-list-label {
        // Remove spacing
        margin: 0;
      }
    }

    #subscribe-button {
      // Respace
      margin-top: 16px;
    }
  }
}

@media screen and (max-width: 1023px) {
  #footer {
    // Column layout
    flex-direction: column;
    height: auto;
    padding: 48px 16px;

    #footer-text {
      // Realign
      text-align: center;
      margin-bottom: 16px;
    }

    #footer-mailing-list {
      // Respace
      margin-bottom: 32px;
    }
  }
}
</style>