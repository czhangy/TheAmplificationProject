<template>
  <div id="map-page"></div>
</template>

<script>
export default {
  name: "MapPage",
  props: {
    query: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
#map-page {
}
</style>