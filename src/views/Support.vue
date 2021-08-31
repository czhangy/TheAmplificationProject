<template>
  <div id="support">
    <div id="support-banner">
      <h1>Donate to the Amplification Project</h1>
      <p>
        All gifts to The Amplification Project are meaningful, no matter how big
        or small. 100% of your donation goes directly to the mission of The
        Amplification Project.
        <br />
        <br />
        Currently, your donation counts towards the development and improvement
        of The Amplification Project's website.
        <br />
        <br />
        <span>
          The Amplification Project is in affiliation with
          <a href="https://saveourplanet.org/" target="_blank"
            >Social and Environmental Entrepreneurs (SEE)</a
          >, a non-profit public charity exempt from federal income tax under
          Section 501(c)(3) of the Internal Revenue Code. Donations to The
          Amplification Project are tax-deductible through SEE (EIN
          #95-4116679).
        </span>
      </p>
      <div id="support-nav">
        <button id="donate-online-button" @click="setOnlinePage">
          Donate Online
        </button>
        <button id="donate-check-button" @click="setCheckPage">
          Donate by Check
        </button>
      </div>
    </div>
    <div id="support-content">
      <div id="support-form">
        <form v-if="!altPage" @submit.prevent="handleSubmit">
          <p>
            <span>Make a Donation:</span>
            <br />
            <br />
            Would you like to make a monthly or a one-time donation?
            <span class="asterisk">*</span>
          </p>
          <div class="dono-buttons">
            <button class="freq-buttons dono-button" @click="handleButton(0)">
              Monthly
            </button>
            <button class="freq-buttons dono-button" @click="handleButton(1)">
              One-Time
            </button>
          </div>
          <p>
            Choose an amount:
            <span class="asterisk">*</span>
          </p>
          <div class="dono-buttons">
            <button @click="handleButton(2)">$5</button>
            <button @click="handleButton(3)">$10</button>
            <button @click="handleButton(4)">$25</button>
            <button @click="handleButton(5)">$100</button>
            <input type="number" placeholder="Custom" v-model="res.donoAmnt" />
          </div>
          <p><span>Please tell us about yourself:</span></p>
          <div id="personal-info">
            <div class="personal-info-field">
              <div class="personal-info-label">
                <p>First Name: <span class="asterisk">*</span></p>
              </div>
              <input v-model="res.firstName" />
            </div>
            <div class="personal-info-field">
              <div class="personal-info-label">
                <p>Last Name: <span class="asterisk">*</span></p>
              </div>
              <input v-model="res.lastName" />
            </div>
            <div class="personal-info-field">
              <div class="personal-info-label">
                <p>Email: <span class="asterisk">*</span></p>
              </div>
              <input v-model="res.email" />
            </div>
          </div>
          <input type="submit" value="Continue" />
        </form>
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
    // Custom dono function
    openCustomAmountModal: function () {
      alert("This feature is being implemented still");
    },
    // Button styling function
    handleButton: function (i) {
      let arr = document.getElementsByClassName("dono-button");
      if (i < 2) {
        for (let j = 0; j < 2; j++) {
          arr[j].style.background = i === j ? "#298A7E" : "none";
          arr[j].style.color = i === j ? "white" : "black";
          arr[j].style.border = i === j ? "none" : "1px solid black";
        }
        // FIX ME
        this.res.donoFreq = true;
      } else {
        for (let j = 2; j < 7; j++) {
          arr[j].style.background = i === j ? "#298A7E" : "none";
          arr[j].style.color = i === j ? "white" : "black";
          arr[j].style.border = i === j ? "none" : "1px solid black";
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

      span {
        // Typography
        font-size: calc(clamp(0.9rem, 0.76rem + 0.56vw, 1.25rem));

        a {
          // Remove default a tag styling
          color: white;
        }
      }
    }

    #support-nav {
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
        padding-bottom: 16px;
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

      span {
        // Bold selected lines
        font-weight: $bold;
      }

      .asterisk {
        // Asterisk color
        color: darken(red, 10);
      }

      .dono-buttons {
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        // Spacing
        margin-top: 1rem;
        margin-bottom: 3rem;

        button,
        input {
          // Typography
          font-family: $alt-font;
          font-size: 1.2rem;
          // Button sizing
          width: 17.5%;
          padding: 1rem 0;
          // Remove default button styling
          background: transparent;
          // Shape button
          border-radius: 10px;
          border: 1px solid black;
          // Centering
          text-align: center;
          // Hide arrows
          -moz-appearance: textfield;
        }

        button {
          // Clickable
          cursor: pointer;
        }

        input::-webkit-outer-spin-button,
        input::-webkit-inner-spin-button {
          // Hide arrows
          -webkit-appearance: none;
          margin: 0;
        }

        .freq-buttons {
          // Sizing
          width: 45%;
        }
      }

      #personal-info {
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
        // Spacing
        margin-top: 1rem;

        .personal-info-field {
          // Sizing
          width: max(300px, 45%);
          margin-bottom: 2rem;

          .personal-info-label {
            // Flexbox for layout
            display: flex;
          }

          input {
            // Typography
            font-family: $alt-font;
            font-size: 1.2rem;
            // Spacing
            margin-top: 0.5rem;
            padding: 0.5rem;
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

      input[type="submit"] {
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
  }
}

// Sticky hover
@media (hover: hover) {
  button {
    // Smooth animation
    transition: transform 0.2s ease;

    &:hover {
      // Animate
      transform: scale(1.05);
    }
  }

  #support {
    #support-content {
      #support-form {
        input[type="submit"] {
          &:hover {
            // Animate
            background: $accent-light-teal;
          }
        }
      }
    }
  }
}
</style>