<template>
  <div class="news">
    <h2 class="news-header">News</h2>
    <div class="search-bar">
      <i class="fa fa-search" aria-hidden="true" @click="handleSearch"></i>
      <input id="search-field" v-model="query" placeholder="Search..." />
    </div>
    <div class="articles">
      <div class="main-article">
        <img src="@/assets/img/News/news1.png" />
        <div class="caption">
          <p>{{ articles[0].timestamp }}</p>
          <h5>{{ articles[0].title }}</h5>
        </div>
      </div>
      <div class="reg-articles">
        <div
          class="reg-article"
          v-for="article in articles.slice(1)"
          :key="article"
        ></div>
      </div>
    </div>
    <div class="links">
      <button @click="handleRedirect">More Articles →</button>
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
    handleSearch: function () {
      alert(
        `The handleSearch() function in News.vue must still be implemented, but here's the data stored in the component for testing:\n
        query = "${this.query}"`
      );
      this.query = "";
    },
    handleRedirect: function () {
      alert(
        "The handleRedirect() function in News.vue must still be implemented, along with the page that should be redirected to."
      );
    },
  },
  mounted() {
    const self = this;
    document
      .getElementById("search-field")
      .addEventListener("keydown", function (e) {
        if (e.code == "Enter") self.handleSearch();
      });
  },
  beforeUnmount() {
    const self = this;
    document
      .getElementById("search-field")
      .removeEventListener("keydown", function (e) {
        if (e.code == "Enter") self.handleSearch();
      });
  },
};
</script>

<style scoped lang="scss">
.news {
  // Container
  background: $bg-color;
  // Spacing
  padding: 0 calc(clamp(3rem, -9rem + 21.333vw, 15rem));

  .news-header {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    // Spacing
    margin-top: $title-margin;
  }

  .search-bar {
    // Flexbox for layout
    display: flex;
    justify-content: center;
    align-items: center;
    // Spacing
    margin: 2rem 0;

    .fa-search {
      // Color
      color: $accent-teal;
      // Sizing
      font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
      // Clickable
      cursor: pointer;
    }

    input {
      // Sizing
      width: 90%;
      // Typography
      font-family: $alt-font;
      font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
      // Inner spacing
      padding: 0.2rem 0.5rem;
      // Outer spacing
      margin-left: 1rem;
    }
  }

  .articles {
    // Flexbox for layout
    display: flex;
    justify-content: center;
    // Show number of articles based on screen size
    max-height: 35rem;
    overflow-y: hidden;

    img {
      width: 100%;
    }

    .main-article {
      // Sizing
      height: calc(clamp(21rem, 9.8rem + 44.8vw, 35rem));
      width: calc(clamp(18rem, 8.4rem + 38.4vw, 30rem));
      // Positioning for caption
      position: relative;
    }

    .reg-articles {
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
      }
    }

    .caption {
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

      p {
        // Typography
        font-family: $alt-font;
      }

      h5,
      h6 {
        // Typography
        text-transform: uppercase;
      }

      h5 {
        // Typography
        font-size: $header-font-size;
      }

      h6 {
        // Typography
        font-size: $subheader-font-size;
      }
    }
  }

  .links {
    // Flexbox for layout
    display: flex;
    justify-content: flex-end;
    // Spacing
    margin-top: 2rem;
    margin-bottom: 5rem;

    button {
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

// Media queries
// Mobile layout
@media screen and (max-width: 900px) {
  .news {
    .articles {
      flex-direction: column;
      align-items: center;
      max-height: none;
      .reg-articles {
        margin-left: 0;
        margin-top: 2rem;
        grid-template-columns: 1fr;
        width: calc(clamp(18rem, 8.4rem + 38.4vw, 30rem));
      }
    }
  }
}

// Sticky hover
@media (hover: hover) {
  .main-article,
  .reg-article {
    transition: transform 0.2s ease;
    cursor: pointer;
    &:hover {
      transform: scale(1.05);
    }
  }
}
</style>