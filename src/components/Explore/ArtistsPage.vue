<template>
  <div id="artists-page"></div>
</template>

<script>
export default {
  name: "ArtistsPage",
  props: {
    filter: {
      type: String,
      required: true,
    },
    sortBy: {
      type: String,
      required: true,
    },
    query: {
      type: String,
      required: true,
    },
  },
};
</script>

<style lang="scss" scoped>
#artists-page {
}
</style>