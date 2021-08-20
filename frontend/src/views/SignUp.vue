<template>
  <div class="signup">
    <h2>Sign Up</h2>
    <div class="signup-form">
      <div class="form-field-row">
        <div class="form-field">
          <label>Username</label>
          <input v-model="username" />
        </div>
        <div class="form-field">
          <label>Email</label>
          <input v-model="email" />
        </div>
      </div>
      <div class="form-field-row">
        <div class="form-field">
          <label>Password</label>
          <input type="password" v-model="password" />
        </div>
        <div class="form-field">
          <label>Confirm Password</label>
          <input type="password" v-model="confirmPassword" />
        </div>
      </div>
      <div class="form-field-row">
        <div class="captcha"></div>
        <button @click="handleRegister">Register</button>
      </div>
    </div>
    <p>
      Already have an account? <router-link to="/login">Log In</router-link>
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
    handleRegister: function () {
      alert(
        `The handleLogin() function in Login.vue must still be implemented, but here's the data stored in the component for testing:\n
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
.signup {
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

  .signup-form {
    // Sizing
    width: max(50vw, 300px);
    // Spacing
    margin-top: 4rem;
    // Flexbox for centering
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    .form-field-row {
      // Flexbox for layout
      display: flex;
      justify-content: space-between;
      align-items: center;
      // Sizing
      width: 100%;

      .form-field {
        // Sizing
        width: 40%;

        label {
          // Typography
          font-size: $subheader-font-size;
          // Align left
          width: 100%;
          text-align: left;
        }

        input {
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

      .captcha {
        height: 5rem;
        width: 40%;
        background: grey;
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

// Smaller layout
@media screen and (max-width: 1024px) {
  .signup {
    .signup-form {
      .form-field-row {
        flex-direction: column;
        .form-field {
          width: 80%;
        }
        .captcha {
          margin-bottom: 2rem;
          width: 80%;
        }
      }
    }
  }
}

// Sticky hover
@media (hover: hover) {
  .signup {
    .signup-form {
      .form-field-row {
        button {
          transition: transform 0.2s ease;
          &:hover {
            transform: scale(1.05);
          }
        }
      }
    }
  }
}
</style>