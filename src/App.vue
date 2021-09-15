<template>
  <Navbar />
  <router-view />
  <Footer />
</template>

<script>
// Import nav components
import Navbar from "@/components/nav/Navbar";
import Footer from "@/components/nav/Footer";

export default {
  name: "App",
  components: {
    Navbar,
    Footer,
  },
};
</script>


<style lang="scss">
// Import fonts
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,400;0,700;1,400&display=swap");

#app {
  font-family: Inter, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #333;
  background: #fffefe;
  height: auto;
  width: 100vw;
  position: relative;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  outline: none;
}

html {
  height: auto;
  overflow-y: auto;

  // Custom scrollbar
  &::-webkit-scrollbar {
    width: 7px;
    position: relative;

    &-track {
      cursor: pointer;
    }

    &-thumb {
      background: #aaa;
      border-radius: 12px;

      &:hover {
        background: #999;
      }
    }
  }
}

body {
  // Fix scrollTo
  height: auto;
  overflow-x: hidden;
  // Set font
  font-family: Inter;
}
</style>
