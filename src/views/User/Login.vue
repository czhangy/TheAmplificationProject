<template>
  <div id="login">
    <p id="login-header">Login</p>
    <form id="login-form" @submit.prevent="handleLogin">
      <label class="form-field-label" for="login-username">Username</label>
      <input id="login-username" class="form-field" v-model="username" />
      <div id="password-header">
        <label class="form-field-label" for="login-password">Password</label>
        <button id="forgot-password-button" @click="handleForgotPasswordReq">
          Forgot password?
        </button>
      </div>
      <input
        id="login-password"
        class="form-field"
        type="password"
        v-model="password"
      />
      <div id="form-footer">
        <div id="remember-me">
          <input id="remember-me-checkbox" type="checkbox" v-model="remember" />
          <label for="remember-me-checkbox">Remember me</label>
        </div>
        <input id="login-button" type="submit" value="Login" />
      </div>
      <p id="sign-up-redirect">
        New user?
        <router-link id="sign-up-link" to="/signup">Sign Up</router-link>
      </p>
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      remember: false,
      username: "",
      password: "",
    };
  },
  methods: {
    handleForgotPasswordReq: function () {
      alert(
        `The handleForgotPasswordReq() function in Login.vue must still be implemented, but here's the data stored in the component for testing:\n
        remember = "${this.remember}"
        username = "${this.username}"
        password = "${this.password}"`
      );
    },
    handleLogin: function () {
      alert(
        `The handleLogin() function in Login.vue must still be implemented, but here's the data stored in the component for testing:\n
        remember = "${this.remember}"
        username = "${this.username}"
        password = "${this.password}"`
      );
      this.username = "";
      this.password = "";
    },
  },
};
</script>

<style scoped lang="scss">
#login {
  // Sizing
  width: 100%;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  align-items: center;
  // Spacing
  padding: 1rem;

  #login-header {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    font-weight: bold;
    // Spacing
    margin-top: $title-margin;
  }

  #login-form {
    // Sizing
    width: max(30vw, 300px);
    // Spacing
    margin-top: 64px;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .form-field-label {
      // Typography
      font-size: $subheader-font-size;
      font-weight: bold;
      // Align left
      width: 100%;
      text-align: left;
      // Spacing
      margin-bottom: 1rem;
    }

    .form-field {
      // Sizing
      width: 100%;
      // Typography
      font-size: $subheader-font-size;
      font-family: $alt-font;
      // Outer spacing
      margin-bottom: 32px;
      // Inner spacing
      padding: 0.25rem 0.5rem;
      // Box styling
      border: 2px solid lightgrey;
      border-radius: 5px;
    }

    #password-header {
      // Sizing
      width: 100%;
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;

      #forgot-password-button {
        // Remove default styling
        background: none;
        border: none;
        // Clickable
        cursor: pointer;
        // Stop text wrap
        white-space: nowrap;
        // Typography
        font-family: $alt-font;
        color: $accent-teal;
        font-size: $body-font-size;
        // Spacing
        margin-bottom: 16px;
        // Alignment
        text-align: right;
      }
    }

    #form-footer {
      // Sizing
      width: 100%;
      // Flexbox for layout
      display: flex;
      justify-content: space-between;

      #remember-me {
        // Flexbox for layout
        display: flex;
        justify-content: flex-start;
        align-items: center;
        // Sizing
        width: 50%;

        #remember-me-checkbox {
          // Spacing
          margin-right: 8px;
          // Sizing
          height: 1.5rem;
          width: 1.5rem;
          // Clickable
          cursor: pointer;
        }

        label {
          // Typography
          font-size: $body-font-size;
          font-family: $alt-font;
        }
      }

      #login-button {
        // Remove default styling
        border: none;
        // Button styling
        background: $accent-teal;
        padding: 0.6rem 1.5rem;
        border-radius: 5px;
        // Typography
        font-family: $main-font;
        font-size: $body-font-size;
        font-weight: bold;
        color: white;
        // Clickable
        cursor: pointer;
      }
    }

    #sign-up-redirect {
      // Spacing
      margin: 48px 0;
      // Typography
      font-size: $body-font-size;
      font-family: $alt-font;

      #sign-up-link {
        // Clear default styling
        text-decoration: none;
        // Typography
        color: $accent-teal;
      }
    }
  }
}

// Sticky hover
@media (hover: hover) {
  #login > #login-form {
    #password-header > #forgot-password-button:hover {
      // Animate
      color: $accent-light-teal;
    }

    #form-footer > #login-button:hover {
      // Animate
      background: $accent-light-teal;
    }

    #sign-up-redirect > #sign-up-link:hover {
      color: $accent-light-teal;
    }
  }
}
</style>