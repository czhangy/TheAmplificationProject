<template>
  <div id="page-not-found">
    <p id="page-not-found-text">Uh oh! That page doesn't exist!</p>
    <router-link id="page-not-found-link" to="/">Return to Home</router-link>
  </div>
</template>

<script>
export default {
  name: "PageNotFound",
};
</script>

<style lang="scss" scoped>
#page-not-found {
  // Sizing
  min-height: 100vh;
  width: 100%;
  // Inner spacing
  padding: 80px;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  #page-not-found-text {
    // Typography
    font-size: 4rem;
    font-weight: bold;
  }

  #page-not-found-link {
    // Remove default styling
    text-decoration: none;
    // Centering
    margin: 80px auto;
    display: block;
    // Typography
    color: white;
    font-size: 2rem;
    // Button styling
    background: $accent-teal;
    border-radius: 10px;
    padding: 16px 24px;
  }
}

// Sticky hover
@media (hover: hover) {
  #page-not-found > #page-not-found-link:hover {
    // Animate
    background: $accent-light-teal;
  }
}
</style>