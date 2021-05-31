<template>
  <div class="footer">
    <div class="footer-text">
      <div class="footer-links">
        <router-link to="/about" class="footer-link"> About </router-link>
        |
        <router-link to="/termsandconditions" class="footer-link">
          Terms and Conditions
        </router-link>
      </div>
      Powered by <a href="https://omeka.org/" target="_blank">Omeka</a> | Site
      Hosted by
      <a href="https://reclaimhosting.com/" target="_blank">Reclaim Hosting</a>
      | 2019 - 2021
    </div>
    <div class="footer-socials">
      <a
        class="fa fa-twitter"
        href="https://twitter.com/AmplifiProject"
        target="_blank"
        aria-hidden="true"
      ></a>
      <a class="fa fa-envelope-o" aria-hidden="true"></a>
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
};
</script>

<style scoped lang="scss">
.footer {
  // Sizing
  width: 100%;
  height: 8rem;
  // Bar styling
  background: $accent-light-grey;
  // Spacing
  padding: 0 3rem;
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

    .footer-links {
      .footer-link {
        // Remove effects of router link
        text-decoration: none;
        color: $accent-teal;
      }
    }

    a {
      // Remove effects of anchor tag
      text-decoration: none;
      // Color styling
      color: $accent-teal;
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
      margin: 0 1rem;
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
  .footer {
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
</style>