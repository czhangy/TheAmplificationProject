<template>
  <div class="footer">
    <div class="footer-text">
      <div class="footer-links">
        <router-link to="/about" class="footer-link"> About </router-link>
        |
        <router-link to="/" class="footer-link">
          Terms and Conditions
        </router-link>
      </div>
      Powered by Omeka | Site Hosted by Reclaim Hosting | 2019 - 2021
    </div>
    <div class="footer-socials">
      <i class="fa fa-twitter" aria-hidden="true"></i>
      <i class="fa fa-envelope-o" aria-hidden="true"></i>
      <i class="fab fa-facebook-f"></i>
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
        color: $font-color;
      }
    }
  }

  .footer-socials {
    // Icon centering
      text-align: center;
      // Icon sizing
      font-size: 1.25rem;

    .fa-twitter {
      // Icon centering
      line-height: 2.5rem;
      // Icon sizing
      height: 2.5rem;
      width: 2.5rem;
      // Outline
      color: transparent;
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: $accent-teal;
      // Border
      border: 1px solid $accent-teal;
      border-radius: 100%;
      // Clickable
      cursor: pointer;
      // Spacing
      margin: 0 1rem;
    }
    .fa-envelope-o {
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
    }
    .fa-facebook-f {
      // Icon centering
      line-height: 2.25rem;
      // Icon sizing
      height: 2.5rem;
      width: 2.5rem;
      // Outline
      color: transparent;
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: $accent-teal;
      // Border
      border: 1px solid $accent-teal;
      border-radius: 100%;
      // Clickable
      cursor: pointer;
      // Spacing
      margin: 0 1rem;
    }
  }
}
</style>