<template>
  <div id="support">
    <div id="support-banner">
      <p id="support-header">Donate to the Amplification Project</p>
      <p id="support-banner-text">
        All gifts to The Amplification Project are meaningful, no matter how big
        or small. 100% of your donation goes directly to the mission of The
        Amplification Project.
        <br />
        <br />
        Currently, your donation counts towards the development and improvement
        of The Amplification Project's website.
        <br />
        <br />
        <span id="support-banner-text-small">
          The Amplification Project is in affiliation with
          <a
            id="support-banner-link"
            href="https://saveourplanet.org/"
            target="_blank"
            >Social and Environmental Entrepreneurs (SEE)</a
          >, a non-profit public charity exempt from federal income tax under
          Section 501(c)(3) of the Internal Revenue Code. Donations to The
          Amplification Project are tax-deductible through SEE (EIN
          #95-4116679).
        </span>
      </p>
      <div id="support-nav">
        <button class="support-nav-button" @click="handlePageNav(0)">
          Donate Online
        </button>
        <button class="support-nav-button" @click="handlePageNav(1)">
          Donate by Check
        </button>
      </div>
    </div>
    <div id="support-content">
      <form id="support-form" v-if="!altPage" @submit.prevent="handleSubmit">
        <p class="support-form-text">
          <strong>Make a Donation:</strong>
          <br />
          <br />
          Would you like to make a monthly or a one-time donation?
          <span class="asterisk">*</span>
        </p>
        <div class="dono-buttons">
          <button
            class="freq-buttons dono-button"
            @click="handleDonoButton(0)"
          >
            Monthly
          </button>
          <button
            class="freq-buttons dono-button"
            @click="handleDonoButton(1)"
          >
            One-Time
          </button>
        </div>
        <p class="support-form-text">
          Choose an amount:
          <span class="asterisk">*</span>
        </p>
        <div class="dono-buttons">
          <button class="dono-button" @click="handleDonoButton(2)">
            $5
          </button>
          <button class="dono-button" @click="handleDonoButton(3)">
            $10
          </button>
          <button class="dono-button" @click="handleDonoButton(4)">
            $25
          </button>
          <button class="dono-button" @click="handleDonoButton(5)">
            $100
          </button>
          <input
            class="dono-button"
            type="number"
            placeholder="Custom"
            v-model="res.donoAmnt"
            @click="handleDonoButton(6)"
          />
        </div>
        <strong class="support-form-text"
          >Please tell us about yourself:</strong
        >
        <div id="personal-info">
          <div class="personal-info-field">
            <label for="support-first-name">
              First Name: <span class="asterisk">*</span>
            </label>
            <input id="support-first-name" v-model="res.firstName" />
          </div>
          <div class="personal-info-field">
            <label for="support-last-name">
              Last Name: <span class="asterisk">*</span>
            </label>
            <input id="support-last-name" v-model="res.lastName" />
          </div>
          <div class="personal-info-field">
            <label for="support-email">
              Email: <span class="asterisk">*</span>
            </label>
            <input id="support-email" v-model="res.email" />
          </div>
        </div>
        <input id="dono-submit-button" type="submit" value="Continue" />
      </form>
      <div id="support-check" v-else>
        <p class="support-text">
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
          <span>Thank you for your donation to The Amplification Project!</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Support",
  data() {
    return {
      altPage: null,
      res: {
        donoFreq: null,
        donoAmnt: "",
        firstName: "",
        lastName: "",
        email: "",
      },
    };
  },
  methods: {
    // Navigation functions
    handlePageNav: function (ind) {
      // Set page state
      this.altPage = ind === 1;
      // Set underline
      let arr = document.getElementsByClassName("support-nav-button");
      for (let i = 0; i < arr.length; i++)
        if (i === ind) arr[i].classList.add("nav-active");
        else arr[i].classList.remove("nav-active");
    },
    // Button styling function
    handleDonoButton: function (ind) {
      let arr = document.getElementsByClassName("dono-button");
      // Style frequency buttons
      if (ind < 2) {
        for (let i = 0; i < 2; i++) {
          if (i === ind) arr[i].classList.add("button-active");
          else arr[i].classList.remove("button-active");
        }
        // FIX ME
        this.res.donoFreq = true;
        // Style amount buttons
      } else {
        for (let i = 2; i < 7; i++) {
          if (i === ind) arr[i].classList.add("button-active");
          else arr[i].classList.remove("button-active");
        }
        // FIX ME
        this.res.donoAmnt = true;
      }
    },
    // Form submission function
    handleSubmit() {
      console.log(this.res);
    },
  },
  mounted() {
    // Set initial page styling
    this.handlePageNav(0);
  },
};
</script>

<style scoped lang="scss">
#support {
  #support-banner {
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

    #support-header {
      // Centering
      text-align: center;
      // Typography
      font-size: calc(clamp(2rem, 1.2rem + 3.2vw, 4rem));
      // Spacing
      margin-bottom: 3rem;
    }

    #support-banner-text {
      // Typography
      font-family: $alt-font;
      font-size: calc(clamp(1rem, 0.8rem + 0.8vw, 1.5rem));
      // Spacing
      margin-bottom: calc(clamp(3rem, 1.8rem + 4.8vw, 6rem));

      #support-banner-text-small {
        // Typography
        font-size: calc(clamp(0.9rem, 0.76rem + 0.56vw, 1.25rem));

        #support-banner-link {
          // Remove default styling
          color: white;
        }
      }
    }

    #support-nav {
      // Flexbox for layout
      display: flex;
      justify-content: space-evenly;
      align-items: flex-start;

      .support-nav-button {
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
        padding-bottom: 16px;
      }

      .nav-active {
        // Underline
        border-bottom: 5px solid white;
      }
    }
  }

  #support-content {
    // Flexbox for alignment
    display: flex;
    justify-content: center;
    // Spacing
    padding: 80px 0;

    #support-form {
      // Typography
      font-family: $alt-font;
      font-size: 1.2rem;
      // Make border box
      border: 1px solid $accent-teal;
      // Size border box
      padding: 3rem clamp(2rem, -1.2rem + 12.8vw, 5rem);

      .asterisk {
        // Asterisk color
        color: darken(red, 10);
      }

      .dono-buttons {
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        // Spacing
        margin-top: 16px;
        margin-bottom: 48px;

        .dono-button {
          // Typography
          font-family: $alt-font;
          font-size: 1.2rem;
          color: black;
          // Button sizing
          width: 17.5%;
          padding: 16px 0;
          // Remove default button styling
          background: transparent;
          // Shape button
          border-radius: 10px;
          border: 1px solid black;
          // Centering
          text-align: center;
          // Hide arrows
          -moz-appearance: textfield;
          // Clickable
          cursor: pointer;
        }

        .freq-buttons {
          // Sizing
          width: 45%;
        }

        input::-webkit-outer-spin-button,
        input::-webkit-inner-spin-button {
          // Hide arrows
          -webkit-appearance: none;
          margin: 0;
        }

        .button-active {
          // Button styling
          border: none;
          background: $accent-teal;
          color: white;

          &::placeholder {
            // Restyle placeholder text
            color: white;
          }
        }
      }

      #personal-info {
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        // Spacing
        margin-top: 16px;

        .personal-info-field {
          // Sizing
          width: max(300px, 45%);
          margin-bottom: 32px;

          input {
            // Typography
            font-family: $alt-font;
            font-size: 1.2rem;
            // Spacing
            margin-top: 8px;
            padding: 8px;
            // Border styling
            border: none;
            border-bottom: 1px solid grey;
            // Sizing
            width: 100%;

            &:focus {
              // Highlight bar
              border-bottom: 2px solid $accent-teal;
            }
          }
        }
      }

      #dono-submit-button {
        // Button styling
        background: $accent-teal;
        border: none;
        padding: 16px 32px;
        border-radius: 5px;
        // Typography
        font-family: $alt-font;
        font-size: 1.2rem;
        font-weight: bold;
        color: white;
        // Clickable
        cursor: pointer;
        // Centering
        margin: 0 auto;
        display: block;
      }
    }

    #support-check {
      // Typography
      font-family: $alt-font;
      font-size: 1.2rem;
      // Make border box
      border: 1px solid $accent-teal;
      // Size border box
      padding: 3rem clamp(2rem, -1.2rem + 12.8vw, 5rem);
      max-width: 70%;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #support > #support-content > #support-form {
    .dono-button {
      // Smooth animation
      transition: transform 0.2s ease;

      &:hover {
        // Animate
        transform: scale(1.05);
      }
    }

    #dono-submit-button {
      &:hover {
        // Animate
        background: $accent-light-teal;
      }
    }
  }
}
</style>