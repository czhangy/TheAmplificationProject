<template>
  <div id="explore">
    <div id="explore-nav">
      <button class="nav-button" @click="handlePageNav(0)">ALL</button>
      <button class="nav-button" @click="handlePageNav(1)">ARTIST</button>
      <button class="nav-button" @click="handlePageNav(2)">MAP</button>
    </div>
    <div id="explore-search">
      <i class="fas fa-search"></i>
      <input placeholder="Search..." v-model="query" />
    </div>
    <div id="explore-filters" v-if="curPage !== 2">
      <div class="filter-field">
        <label for="filter-dropdown">FILTER BY</label>
        <select id="filter-dropdown" v-model="filter">
          <option value="" disabled>MEDIUM</option>
          <option>TEXT</option>
          <option>IMAGE</option>
          <option>VIDEO</option>
          <option>AUDIO</option>
        </select>
      </div>
      <div class="filter-field">
        <label for="sort-dropdown">SORT BY</label>
        <select id="sort-dropdown" v-model="sortBy">
          <option>YEAR ASCENDING</option>
          <option>YEAR DESCENDING</option>
          <option>TITLE A → Z</option>
          <option>TITLE Z → A</option>
          <option>LAST NAME A → Z</option>
          <option>LAST NAME Z → A</option>
        </select>
      </div>
    </div>
    <AllPage
      :filter="filter"
      :sortBy="sortBy"
      :query="query"
      v-if="curPage === 0"
    />
    <ArtistsPage
      :filter="filter"
      :sortBy="sortBy"
      :query="query"
      v-if="curPage === 1"
    />
    <MapPage :query="query" v-if="curPage === 2" />
  </div>
</template>

<script>
// Import local components
import AllPage from "@/components/Explore/AllPage.vue";
import ArtistsPage from "@/components/Explore/ArtistsPage.vue";
import MapPage from "@/components/Explore/MapPage.vue";

export default {
  name: "Explore",
  components: {
    AllPage,
    ArtistsPage,
    MapPage,
  },
  data() {
    return {
      curPage: null,
      filter: "",
      sortBy: "YEAR DESCENDING",
      query: "",
    };
  },
  methods: {
    // Navigation function
    handlePageNav: function (page) {
      // Return out
      if (page === this.curPage) return;
      // Set page
      this.curPage = page;
      // Handle nav button styling
      let arr = document.getElementsByClassName("nav-button");
      for (let i = 0; i < 3; i++) {
        if (i === this.curPage) arr[i].classList.add("active");
        else arr[i].classList.remove("active");
      }
    },
  },
  mounted() {
    // Init page state
    this.handlePageNav(0);
  },
};
</script>

<style scoped lang="scss">
#explore {
  // Inner spacing
  padding: 48px 96px;

  #explore-nav {
    // Spacing
    margin-bottom: 32px;
    // Flexbox for centering
    display: flex;
    justify-content: center;
    align-items: flex-start;

    button {
      // Remove default styling
      background: none;
      border: none;
      // Spacing
      margin: 0 48px;
      // Clickable
      cursor: pointer;
      // Typography
      color: black;
      font-family: $main-font;
      font-size: 1.5rem;
    }

    .active {
      // Typography
      color: $accent-teal;
      // Underline
      border-bottom: 3px solid $accent-teal;
      // Inner spacing
      padding-bottom: 4px;
    }
  }

  #explore-search {
    // Flexbox for centering
    display: flex;
    justify-content: center;
    align-items: center;
    // Centering
    margin: 0 auto;
    // Spacing
    margin-bottom: 24px;
    // Sizing
    width: calc(min(100%, 1000px));

    .fa-search {
      // Icon styling
      margin-right: 16px;
      color: $accent-teal;
      // Sizing
      font-size: 1.5rem;
    }

    input {
      // Typography
      font-size: 1.25rem;
      font-family: $alt-font;
      // Inner spacing
      padding: 8px 16px;
      // Sizing
      width: 98%;
    }
  }

  #explore-filters {
    // Flexbox for layout
    display: flex;
    justify-content: space-between;
    // Centering
    margin: 0 auto;
    // Inner spacing
    padding: 0 48px;
    // Sizing
    width: calc(min(100%, 1000px));

    .filter-field {
      // Flexbox for alignment
      display: flex;
      align-items: center;

      label {
        // Typography
        font-size: 1.25rem;
        // Spacing
        margin-right: 24px;
      }

      select {
        // Typography
        font-size: 1.25rem;
        color: #9d9d9d;
        // Inner spacing
        padding: 8px 16px;
        // Box styling
        border: 1px solid #9d9d9d;
      }

      #filter-dropdown {
        // Typography
        font-family: $main-font;
      }

      #sort-dropdown {
        // Typography
        font-family: $alt-font;
      }
    }
  }
}
</style>