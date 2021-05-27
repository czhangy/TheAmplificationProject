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
      <i class="far fa-envelope"></i>
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
    .fa-twitter .fa-facebook-f {
        font-size: 3rem;
      color: transparent;
      -webkit-text-stroke-width: 1px;
      -webkit-text-stroke-color: red;
    }
  }
}
</style>