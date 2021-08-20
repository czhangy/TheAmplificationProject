<template>
  <div class="login">
    <h2>Login</h2>
    <div class="login-form">
      <label>Username</label>
      <input v-model="username" />
      <div class="form-header">
        <label>Password</label>
        <button @click="handleForgotPasswordReq">Forgot password?</button>
      </div>
      <input type="password" v-model="password" />
      <div class="form-footer">
        <div class="remember-me-check">
          <input type="checkbox" v-model="remember" />
          <label>Remember me</label>
        </div>
        <button @click="handleLogin">Login</button>
      </div>
      <p>New user? <router-link to="/signup">Sign Up</router-link></p>
    </div>
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
.login {
  // Sizing
  width: 100%;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  align-items: center;
  // Spacing
  padding: 1rem;

  h2 {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    // Spacing
    margin-top: $title-margin;
  }

  .login-form {
    // Sizing
    width: max(20vw, 300px);
    // Spacing
    margin-top: 4rem;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    label {
      // Typography
      font-size: $subheader-font-size;
      // Align left
      width: 100%;
      text-align: left;
      // Spacing
      margin-bottom: 1rem;
    }

    input {
      // Sizing
      width: 100%;
      // Typography
      font-size: $subheader-font-size;
      font-family: $alt-font;
      // Outer spacing
      margin-bottom: 2rem;
      // Inner spacing
      padding: 0.25rem 0.5rem;
      // Box styling
      border: 2px solid lightgrey;
      border-radius: 5px;
    }

    .form-header {
      // Sizing
      width: 100%;
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;

      button {
        // Remove default styling
        background: none;
        border: none;
        // Clickable
        cursor: pointer;
        // Sizing
        width: 11rem;
        // Typography
        font-family: $alt-font;
        color: $accent-teal;
        font-size: $body-font-size;
        // Spacing
        margin-bottom: 1rem;
        // Flush right
        text-align: right;
      }
    }

    .form-footer {
      // Sizing
      width: 100%;
      // Flexbox for layout
      display: flex;
      justify-content: space-between;

      .remember-me-check {
        // Flexbox for layout
        display: flex;
        justify-content: flex-start;
        align-items: center;
        // Sizing
        width: 50%;

        input {
          // Clear styling
          margin-bottom: 0;
          // Spacing
          margin-right: 0.5rem;
          // Sizing
          height: 1.5rem;
          width: 1.5rem;
        }

        label {
          // Clear margins
          margin-bottom: 0;
          // Typography
          font-size: $body-font-size;
          font-family: $alt-font;
        }
      }

      button {
        // Remove default styling
        border: none;
        // Button styling
        background: $accent-teal;
        padding: 0.6rem 1.5rem;
        border-radius: 10px;
        // Typography
        font-family: $main-font;
        font-size: $body-font-size;
        color: white;
        // Shadow
        box-shadow: 0 2px 4px $box-shadow;
        // Clickable
        cursor: pointer;
      }
    }

    p {
      // Spacing
      margin: 3rem 0;
      // Typography
      font-size: $body-font-size;
      font-family: $alt-font;

      a {
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
  .login {
    .login-form {
      .form-header {
        button {
          &:hover {
            color: $accent-light-teal;
          }
        }
      }
      .form-footer {
        button {
          transition: transform 0.2s ease;
          &:hover {
            transform: scale(1.05);
          }
        }
      }
      p {
        a {
          &:hover {
            color: $accent-light-teal;
          }
        }
      }
    }
  }
}
</style>