<template>
  <div class="terms-and-conditions">
    <div class="terms-and-conditions-header">Terms and Conditions</div>
  </div>
</template>

<script>
export default {
  name: "TermsAndConditions",
};
</script>

<style scoped lang="scss">
.terms-and-conditions {
  background: $bg-color;
  width: 100%;

  .terms-and-conditions-header {
      // Sizing
      width: 100%;
      // Typography
      text-align: center;
      font-size: $header-font-size;
      // Spacing
      margin: 2rem;
  }
}
</style>