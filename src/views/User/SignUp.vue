<template>
  <div id="sign-up">
    <p id="sign-up-header">Sign Up</p>
    <form id="sign-up-form" @submit.prevent="handleSignUp">
      <div class="form-row">
        <div class="form-entry">
          <label for="sign-up-username">Username</label>
          <input id="sign-up-username" class="form-field" v-model="username" />
        </div>
        <div class="form-entry">
          <label for="sign-up-email">Email</label>
          <input id="sign-up-email" class="form-field" v-model="email" />
        </div>
      </div>
      <div class="form-row">
        <div class="form-entry">
          <label for="sign-up-password">Password</label>
          <input
            id="sign-up-password"
            class="form-field"
            type="password"
            v-model="password"
          />
        </div>
        <div class="form-entry">
          <label for="sign-up-confirm-password">Confirm Password</label>
          <input
            id="sign-up-confirm-password"
            class="form-field"
            type="password"
            v-model="confirmPassword"
          />
        </div>
      </div>
      <div class="form-row">
        <div id="captcha"></div>
        <input id="sign-up-button" type="submit" value="Sign Up" />
      </div>
    </form>
    <p id="login-redirect">
      Already have an account?
      <router-link id="login-link" to="/login">Log In</router-link>
    </p>
  </div>
</template>

<script>
export default {
  name: "SignUp",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
    };
  },
  methods: {
    handleSignUp: function () {
      alert(
        `The handleSignUp() function in Login.vue must still be implemented, but here's the data stored in the component for testing:\n
        username = "${this.username}"
        email = "${this.email}"
        password = "${this.password}"
        confirmPassword = "${this.confirmPassword}"`
      );
      this.username = "";
      this.email = "";
      this.password = "";
      this.confirmPassword = "";
    },
  },
};
</script>

<style scoped lang="scss">
#sign-up {
  // Sizing
  width: 100%;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  align-items: center;
  // Spacing
  padding: 1rem;

  #sign-up-header {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    font-family: $main-font;
    font-weight: bold;
    // Spacing
    margin-top: $title-margin;
  }

  #sign-up-form {
    // Sizing
    width: max(50vw, 300px);
    // Spacing
    margin-top: 4rem;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .form-row {
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;
      // Sizing
      width: 100%;

      .form-entry {
        // Sizing
        width: 40%;

        label {
          // Typography
          font-size: $subheader-font-size;
          font-weight: bold;
          // Align left
          width: 100%;
          text-align: left;
        }

        .form-field {
          // Sizing
          width: 100%;
          // Typography
          font-size: $subheader-font-size;
          font-family: $alt-font;
          // Outer spacing
          margin-top: 1rem;
          margin-bottom: 2rem;
          // Inner spacing
          padding: 0.25rem 0.5rem;
          // Box styling
          border: 2px solid lightgrey;
          border-radius: 5px;
        }
      }

      #captcha {
        height: 5rem;
        width: 40%;
        background: grey;
      }

      #sign-up-button {
        // Remove default styling
        border: none;
        // Button styling
        background: $accent-teal;
        padding: 0.6rem 1.5rem;
        border-radius: 5px;
        // Typography
        font-family: $main-font;
        font-size: $body-font-size;
        color: white;
        // Clickable
        cursor: pointer;
      }
    }
  }

  #login-redirect {
    // Spacing
    margin: 48px 0;
    // Typography
    font-size: $body-font-size;
    font-family: $alt-font;

    #login-link {
      // Clear default styling
      text-decoration: none;
      // Typography
      color: $accent-teal;
    }
  }
}

// Smaller layout
@media screen and (max-width: 1023px) {
  #sign-up > #sign-up-form > .form-row {
    // Column layout
    flex-direction: column;

    .form-entry {
      // Resize
      width: 80%;
    }

    #captcha {
      // Respace
      margin-bottom: 2rem;
      // Resize
      width: 80%;
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #sign-up {
    #sign-up-form > .form-row > #sign-up-button {
      &:hover {
        // Animate
        background: $accent-light-teal;
      }
    }

    #login-redirect > #login-link {
      &:hover {
        // Animate
        color: $accent-light-teal;
      }
    }
  }
}
</style>