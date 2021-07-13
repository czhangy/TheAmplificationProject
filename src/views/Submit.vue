<template>
  <div class="submit">
    <h2>Submit Your Work</h2>
    <p class="submit-subheader">
      Read the archive’s submission guide to learn more about our submission
      process, how to interact with materials, and other important information.
    </p>
    <Accordion :panelContent="panelContent" />
    <router-link to="/submission">I'm ready to submit</router-link>
  </div>
</template>

<script>
import Accordion from "@/components/Accordion";

export default {
  name: "Submit",
  components: {
    Accordion,
  },
  data() {
    return {
      panelContent: [
        {
          title: "What does it mean to contribute to the archive?",
          body: "Filler text",
        },
        {
          title: "What kinds of media are accepted?",
          body: "Filler text",
        },
        {
          title: "How do I submit materials?",
          body: "Filler text",
        },
        {
          title: "Who creates the description and presentation of materials?",
          body: "Filler text",
        },
        {
          title:
            "Who reviews the submission, and when should I expect approval?",
          body: "Filler text",
        },
        {
          title: "What if I want my materials removed?",
          body: "Filler text",
        },
        {
          title: "How do I comment on materials?",
          body: "Filler text",
        },
        {
          title: "Are there any rules and restrictions to the archive?",
          body: "Filler text",
        },
      ],
    };
  },
};
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap");

.submit {
  // Sizing
  width: 100%;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  align-items: center;
  // Spacing
  padding: 1rem calc(clamp(2rem, -3.143rem + 20.571vw, 20rem));

  h2 {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    // Spacing
    margin-top: $title-margin;
  }

  .submit-subheader {
    // Spacing
    margin: 3rem 0;
    // Typography
    font-weight: normal;
    font-size: $subheader-font-size;
  }

  a {
    // Button styling
    background: $accent-dark-teal;
    padding: 0.625rem 1rem;
    border-radius: 10px;
    // Typography
    font-family: $alt-font;
    font-weight: $bold;
    font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
    color: white;
    // Remove effects of router link
    text-decoration: none;
    // Smooth hover animation
    transition: transform 0.2s ease;
    // Spacing
    margin: 2rem 0;
  }
}

// Sticky hover
@media (hover: hover) {
  a {
    &:hover {
      transform: scale(1.05);
    }
  }
}
</style>