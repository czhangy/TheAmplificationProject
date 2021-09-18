<template>
  <div id="submit">
    <p id="submit-header">Submit Your Work</p>
    <p id="submit-instructions">
      Read the archive’s submission guide to learn more about our submission
      process, how to interact with materials, and other important information.
    </p>
    <div id="submit-accordion">
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>What does it mean to contribute to the archive?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[0]"
            @click="handleAccordionClick(0)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(0)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[0]">
          We are an independent, community-led, participatory digital archive,
          and by contributing to the archive, you are making your item(s)
          available to users of the site and helping advance a more diverse and
          inclusive story of border crossing, asylum, refuge, and belonging.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>What kinds of things are accepted?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[1]"
            @click="handleAccordionClick(1)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(1)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[1]">
          We welcome digital files of visual, performing, and literary art that
          you created—drawings; paintings; photography; sculpture; poetry and
          spoken-word; fiction and non-fiction stories, essays, and reflections;
          graphic novels; dance, music, and theater works; performance art; and
          other content that narrates or contemplates lived or observed
          experiences of exile, crossing borders, seeking asylum, detention and
          refugee camps, and refugeehood. We also welcome your comments on the
          archive's content.
          <br />
          <br />
          As we are a public archive, please do not submit materials or comments
          that are confidential, offensive, defamatory towards another person or
          group, or that may put individuals/communities at risk of any harm.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>How do I submit my item(s)? Do I need to create an account?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[2]"
            @click="handleAccordionClick(2)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(2)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[2]">
          You do not need to create an account to submit your item(s). Simply
          click “I’m ready to submit” at the bottom of this page and follow the
          prompts, which include agreeing to our
          <router-link to="/termsandconditions"
            >Terms and Conditions</router-link
          >. But, creating an account allows you to see what items you have
          contributed, viewed, and/or commented on.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>Who describes my item(s)?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[3]"
            @click="handleAccordionClick(3)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(3)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[3]">
          You create all descriptions for your item(s) and have complete
          authority over the description of your work. How much you want to
          describe your item(s) is up to you, and we will not change your
          descriptive information without first asking your permission. We're
          also happy to work with you if you wish to change how your work is
          presented on the site.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>Who reviews the submission, and when should I expect approval?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[4]"
            @click="handleAccordionClick(4)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(4)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[4]">
          Members of the Amplification Project's Collective Advisory Group
          review all submissions (items and comments) before being publicly
          available on the site. Please give us 3-5 days to review and publish
          your item(s) and/or comments. If we have any questions about your
          submission we will be in touch.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>What if I want my materials removed?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[5]"
            @click="handleAccordionClick(5)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(5)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[5]">
          Please contact us (theamplificationproject@gmail.com) and we will
          remove your item(s).
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>
            What if someone has made my work available on your site without my
            permission?
          </p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[6]"
            @click="handleAccordionClick(6)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(6)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[6]">
          If you believe that another person has made your work available on
          this site against your wishes or in a way that constitutes copyright
          infringement or violates your moral or intellectual property rights,
          don’t hesitate to contact us (theamplificationproject@gmail.com) and
          we will remove the material immediately.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>How do I comment on materials in the archive?</p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[7]"
            @click="handleAccordionClick(7)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(7)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[7]">
          To comment on materials in the archive, go to “SIGN UP” (top right of
          our site) and follow the prompts to create an account.
        </p>
      </div>
      <div class="submit-accordion-entry">
        <div class="submit-accordion-panel">
          <p>
            Are there any rules and restrictions to contributing to the archive?
          </p>
          <i
            class="fa fa-chevron-down"
            aria-hidden="true"
            v-if="!accordionOpen[8]"
            @click="handleAccordionClick(8)"
          ></i>
          <i
            class="fa fa-chevron-up"
            aria-hidden="true"
            v-else
            @click="handleAccordionClick(8)"
          ></i>
        </div>
        <p class="panel-body" v-if="accordionOpen[8]">
          Please read our
          <router-link to="/termsandconditions"
            >Terms and Conditions.</router-link
          >
        </p>
      </div>
    </div>
    <p id="t-and-c-warning">
      Please read our
      <router-link to="/termsandconditions">Terms and Conditions</router-link>
      before submitting
    </p>
    <router-link id="ready-to-submit" to="/submission"
      >I'm ready to submit</router-link
    >
  </div>
</template>

<script>
export default {
  name: "Submit",
  data() {
    return {
      accordionOpen: [],
    };
  },
  mounted() {
    for (let i = 0; i < 9; i++) this.accordionOpen[i] = false;
  },
  methods: {
    handleAccordionClick(i) {
      this.accordionOpen[i] = !this.accordionOpen[i];
    },
  },
};
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap");

#submit {
  // Sizing
  width: 100%;
  // Flexbox for centering
  display: flex;
  flex-direction: column;
  align-items: center;
  // Spacing
  padding: 16px calc(clamp(2rem, -3.143rem + 20.571vw, 20rem));

  #submit-header {
    // Typography
    text-align: center;
    font-size: $header-font-size;
    font-weight: bold;
    // Spacing
    margin-top: $title-margin;
  }

  #submit-instructions {
    // Spacing
    margin: 48px 0;
    // Typography
    font-weight: normal;
    font-size: $subheader-font-size;
  }

  a {
    // Remove effects of router link
    text-decoration: none;
    // Typography
    color: $accent-teal;
  }

  #submit-accordion {
    // Container border
    border: 2px solid lightgrey;
    border-bottom: none;
    // Typography
    font-family: $alt-font;
    font-size: $body-font-size;
    // Sizing
    width: 100%;

    p {
      // Typography
      font-size: $body-font-size;
    }

    .submit-accordion-entry {
      // Border
      border-bottom: 2px solid lightgrey;

      .submit-accordion-panel {
        // Flexbox for layout
        display: flex;
        justify-content: space-between;
        align-items: center;
        // Spacing
        padding: 1rem 2rem;

        i {
          // Icon styling
          color: $accent-teal;
          font-size: 1.2rem;
          // Clickable
          cursor: pointer;
          // Spacing
          margin-left: 1rem;
        }
      }

      .panel-body {
        // Typography
        font-style: italic;
        // Border
        border-top: 2px solid lightgrey;
        // Background
        background: lighten(lightgrey, 10);
        // Spacing
        padding: 1rem 2rem;
      }
    }
  }

  #t-and-c-warning {
    // Spacing
    margin-top: 32px;
    // Typography
    font-size: $subheader-font-size;
  }

  #ready-to-submit {
    // Button styling
    background: $accent-teal;
    padding: 10px 16px;
    border-radius: 10px;
    // Typography
    font-family: $alt-font;
    font-weight: $bold;
    font-size: calc(clamp(0.8rem, 0.64rem + 0.64vw, 1.2rem));
    color: white;
    // Spacing
    margin: 32px 0;
  }
}

// Sticky hover
@media (hover: hover) {
  #submit > #ready-to-submit {
    &:hover {
      background: $accent-dark-teal;
    }
  }
}
</style>