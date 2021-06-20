<template>
  <div>
    <div class="support-banner">
      <h1>Donate to the Amplification Project</h1>
      <p>
        All gifts to The Amplification Project are meaningful, no matter how big
        or small. Your contributions help us to realize our mission to preserve,
        share, and amplify art and activism inspired, influenced, and affected
        by forced migration.
        <br />
        <br />
        Currently, your donation counts towards the development and improvement
        of The Amplification Project's website.
        <br />
        <br />
        The Amplification Project is in affiliation with Social and
        Environmental Entrepreneurs (SEE), a non-profit public charity exempt
        from federal income tax under Section 501(c)(3) of the Internal Revenue
        Code. Donations to The Amplification Project are tax-deductible through
        SEE (EIN #95-4116679).
      </p>
      <div class="support-nav">
        <button id="donate-online-button" @click="setOnlinePage">
          Donate Online
        </button>
        <button id="donate-check-button" @click="setCheckPage">
          Donate by Check
        </button>
      </div>
    </div>
    <div class="support-content">
      <div class="support-form">
        <div class="support-form-online" v-if="!altPage">
          <p>
            <span>Make a Donation:</span>
            <br />
            <br />
            Would you like to make a monthly or a one-time donation?
            <span class="asterisk">*</span>
          </p>
          <div class="dono-freq-buttons">
            <button>Monthly</button>
            <button>One-Time</button>
          </div>
        </div>
        <div v-else>
          <p>
            Please make checks payable to Social and Environmental Entrepreneurs
            (SEE) with The Amplification Project written in the memo section.
            Checks can be mailed to:
            <br />
            <br />
            Social and Environmental Entrepreneurs
            <br />
            23532 Calabasas Road Suite A
            <br />
            Calabasas, CA 91302
            <br />
            Tel: 818-225-9150
            <br />
            <br />
            <span
              >Thank you for your donation to The Amplification Project!</span
            >
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Support",
  data() {
    return {
      altPage: false,
    };
  },
  methods: {
    setOnlinePage: function () {
      this.altPage = false;
      // Set underline
      document.getElementById("donate-online-button").style.borderBottom =
        "5px solid white";
      document.getElementById("donate-check-button").style.borderBottom =
        "none";
    },
    setCheckPage: function () {
      this.altPage = true;
      // Set underline
      document.getElementById("donate-online-button").style.borderBottom =
        "none";
      document.getElementById("donate-check-button").style.borderBottom =
        "5px solid white";
    },
  },
};
</script>

<style scoped lang="scss">
.support-banner {
  // Typography
  color: white;
  // Background
  background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)),
    url("../assets/img/Support/support1.png");
  background-size: cover;
  // Flexbox for layout
  display: flex;
  flex-direction: column;
  justify-content: center;
  // Spacing
  padding: calc(clamp(2.5rem, 1.5rem + 4vw, 5rem))
    calc(clamp(2rem, -1.2rem + 12.8vw, 10rem));

  h1 {
    // Centering
    text-align: center;
    // Typography
    font-size: calc(clamp(2rem, 1.2rem + 3.2vw, 4rem));
    // Spacing
    margin-bottom: 3rem;
  }

  p {
    // Typography
    font-family: $alt-font;
    font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
    // Spacing
    margin-bottom: calc(clamp(3rem, 1.8rem + 4.8vw, 6rem));
  }

  .support-nav {
    // Flexbox for layout
    display: flex;
    justify-content: space-evenly;

    #donate-online-button {
      // Default state of page
      border-bottom: 5px solid white;
    }

    button {
      // Remove default button styling
      border: none;
      background: transparent;
      // Clickable
      cursor: pointer;
      // Typography
      color: white;
      font-size: calc(clamp(1.3rem, 1.02rem + 1.12vw, 2rem));
      font-family: $main-font;
      // Spacing the underline
      padding-bottom: 1rem;
    }
  }
}

.support-content {
  // Flexbox for alignment
  display: flex;
  justify-content: center;
  // Spacing
  padding: 5rem 0;

  .support-form {
    // Typography
    font-family: $alt-font;
    font-size: 1.2rem;
    // Make border box
    border: 1px solid $accent-teal;
    // Size border box
    padding: 3rem clamp(2rem, -1.2rem + 12.8vw, 5rem);

    span {
      // Bold selected lines
      font-weight: $bold;
    }

    .asterisk {
      // Asterisk color
      color: darken(red, 10);
    }

    .dono-freq-buttons {
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      // Spacing
      margin-top: 1rem;
      margin-bottom: 3rem;

      button {
        // Typography
        font-family: $alt-font;
        font-size: 1.2rem;
        // Button sizing
        padding: 0.5rem 8rem;
      }
    }
  }
}

// Media queries
// Sticky hover
@media (hover: hover) {
  .support-banner {
    .support-nav {
      button {
        // Set animation
        transition: transform 0.2s ease;
        &:hover {
          transform: scale(1.05);
        }
      }
    }
  }
}
</style>