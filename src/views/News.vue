<template>
  <div id="news">
    <p id="news-header">News</p>
    <div id="news-search">
      <i
        id="news-search-icon"
        class="fa fa-search"
        aria-hidden="true"
        @click="handleSearch"
      ></i>
      <input id="news-search-bar" v-model="query" placeholder="Search..." />
    </div>
    <div id="news-articles">
      <div id="main-article">
        <img src="@/assets/img/News/news1.png" />
        <div class="article-caption">
          <p class="caption-timestamp">{{ articles[0].timestamp }}</p>
          <p class="caption-title">{{ articles[0].title }}</p>
        </div>
      </div>
      <div id="reg-articles-container">
        <div
          class="reg-article"
          v-for="(article, i) in articles.slice(1)"
          :key="i"
        ></div>
      </div>
    </div>
    <div id="news-nav">
      <button id="more-articles-button" @click="handleMore">
        More Articles →
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "News",
  data() {
    return {
      query: "",
      articles: [
        {
          src: "news1",
          timestamp: "March 5, 2021",
          title: "100 items in the archive!",
        },
        {},
        {},
        {},
        {},
        {},
        {},
      ],
    };
  },
  methods: {
    // Search functions
    handleSearchSetup: function () {
      // Get reference to self
      const self = this;
      // Check for enter presses
      document
        .getElementById("news-search-bar")
        .addEventListener("keydown", function (e) {
          if (e.code === "Enter") self.handleSearch();
        });
    },
    handleSearch: function () {
      alert(
        `The handleSearch() function in News.vue must still be implemented, but here's the data stored in the component for testing:\n
        query = "${this.query}"`
      );
      this.query = "";
    },
    handleSearchCleanUp: function () {
      const self = this;
      document
        .getElementById("search-field")
        .removeEventListener("keydown", function (e) {
          if (e.code == "Enter") self.handleSearch();
        });
    },
    // Nav function
    handleMore: function () {
      alert(
        "The handleRedirect() function in News.vue must still be implemented, along with the page that should be redirected to."
      );
    },
  },
  mounted() {
    // Set up search bar
    this.handleSearchSetup();
  },
  beforeUnmount() {
    // Clean up
    this.handleSearchCleanUp();
  },
};
</script>

<style scoped lang="scss">
#news {
  // Container
  background: $bg-color;
  // Spacing
  padding: 0 calc(clamp(3rem, -9rem + 21.333vw, 15rem));

  #news-header {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    font-weight: bold;
    // Spacing
    margin-top: $title-margin;
  }

  #news-search {
    // Flexbox for layout
    display: flex;
    justify-content: center;
    align-items: center;
    // Spacing
    margin: 2rem 0;

    #news-search-icon {
      // Color
      color: $accent-teal;
      // Sizing
      font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
      // Clickable
      cursor: pointer;
    }

    #news-search-bar {
      // Sizing
      width: 90%;
      // Typography
      font-family: $alt-font;
      font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
      // Inner spacing
      padding: 8px 16px;
      // Outer spacing
      margin-left: 16px;
    }
  }

  #news-articles {
    // Flexbox for layout
    display: flex;
    justify-content: center;
    // Show number of articles based on screen size
    max-height: 35rem;
    overflow-y: hidden;

    img {
      width: 100%;
    }

    #main-article {
      // Sizing
      height: calc(clamp(21rem, 9.8rem + 44.8vw, 35rem));
      width: calc(clamp(18rem, 8.4rem + 38.4vw, 30rem));
      // Positioning for caption
      position: relative;
      // Clickable
      cursor: pointer;
    }

    #reg-articles-container {
      // Grid for layout
      display: grid;
      grid-gap: 1rem;
      grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
      // Sizing
      width: calc(100% - 35rem);
      // Spacing
      margin-left: 1rem;

      .reg-article {
        height: 17rem;
        background: red;
        // Clickable
        cursor: pointer;
      }
    }

    .article-caption {
      // Overlay effect
      background: rgba(0, 0, 0, 0.6);
      position: absolute;
      // Positioning in element
      bottom: 0;
      // Sizing
      width: 100%;
      // Typography
      color: white;
      // Spacing
      padding: 1rem;

      .caption-timestamp {
        // Typography
        font-family: $alt-font;
      }

      .caption-title {
        // Typography
        text-transform: uppercase;
        font-size: $header-font-size;
      }
    }
  }

  #news-nav {
    // Flexbox for layout
    display: flex;
    justify-content: flex-end;
    // Spacing
    margin-top: 32px;
    margin-bottom: 80px;

    #more-articles-button {
      // Remove button styling
      border: none;
      background: none;
      // Clickable
      cursor: pointer;
      // Typography
      font-family: $alt-font;
      color: $accent-teal;
      font-size: calc(clamp(1rem, 0.1rem + 1.6vw, 1.2rem));
    }
  }
}

// Mobile layout
@media screen and (max-width: 900px) {
  #news > #news-articles {
    // Column layout
    flex-direction: column;
    align-items: center;
    max-height: none;

    #reg-articles-container {
      // Column layout
      margin-left: 0;
      margin-top: 2rem;
      grid-template-columns: 1fr;
      width: calc(clamp(18rem, 8.4rem + 38.4vw, 30rem));
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #news {
    #news-search > #news-search-icon {
      &:hover {
        // Animate
        color: $accent-light-teal;
      }
    }
    
    #news-articles > #main-article,
    #reg-articles-container > .reg-article {
      // Smooth animation
      transition: transform 0.2s ease;

      &:hover {
        // Animate
        transform: scale(1.02);
      }
    }

    #news-nav > #more-articles-button {
      &:hover {
        // Animate
        color: $accent-light-teal;
      }
    }
  }
}
</style>