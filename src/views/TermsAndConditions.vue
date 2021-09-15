<template>
  <div id="terms-and-conditions">
    <p id="terms-and-conditions-header">Terms and Conditions</p>
    <p id="terms-and-conditions-subheader">
      The Amplification Project: Digital Archive for Forced Migration,
      Contemporary Art, and Action (henceforth, “The Amplification Project”) is
      a non-commercial community-led participatory public digital archive for
      preserving and sharing art and activist projects inspired, influenced, or
      affected by forced migration, comprising people working on behalf of or
      for the archive and includes, for these terms and conditions, any
      associated social media platforms.
      <br />
      <br />
      The Amplification Project uses Omeka, an open-source web publishing
      information management system that enables contributors to upload,
      preserve, and share text, video, image, and audio files. Reclaim Hosting
      hosts our website and stores our files on servers in San Francisco, CA,
      and New York City, NY, USA.
      <br />
      <br />
      The Amplification Project is in affiliation with Social and Environmental
      Entrepreneurs (SEE), a non-profit charity exempt from federal income tax
      under Section 501(c)(3) of the Internal Revenue Code.
    </p>
    <div id="terms-and-conditions-content">
      <em id="terms-and-conditions-list-header">
        By submitting content to The Amplification Project, the following
        conditions apply:
      </em>
      <ol id="terms-and-conditions-list">
        <li class="terms-and-conditions-entry">
          You must provide accurate and complete information when you create an
          account. You are solely responsible for any and all activity that
          occurs on your account and must notify us
          (theamplificationproject@gmail.com) immediately of any breach of
          security, unauthorized use of or activity on your account.
        </li>
        <li class="terms-and-conditions-entry">
          In pursuance of The Amplification Project’s stated purpose, you can
          upload, store, and display image, video, audio, and textual files of
          art and activism inspired, influenced, or affected by forced
          migration.
        </li>
        <li class="terms-and-conditions-entry">
          Certain material cannot be uploaded, stored, and displayed on The
          Amplification Project for copyright reasons. We, therefore, ask that
          the following not be uploaded without clear permission from all
          relevant copyright owners, representatives, and/or licensees:
          <ul class="terms-and-conditions-sublist">
            <li class="terms-and-conditions-subentry">
              Recordings that you know or have reason to believe have been made
              available commercially and continue to be commercially available
              or for which a commercial license can be reasonably obtained;
            </li>
            <li class="terms-and-conditions-subentry">
              Widely-distributed commercial films, either in whole or in part;
              and
            </li>
            <li class="terms-and-conditions-subentry">
              Artworks that you know or have reason to believe were made
              available as part of a commercial publication and for which a
              commercial license can be reasonably obtained.
            </li>
          </ul>
        </li>
        <li class="terms-and-conditions-entry">
          The following material is not acceptable for upload under any
          circumstances:
          <ul class="terms-and-conditions-sublist">
            <li class="terms-and-conditions-subentry">{{ " " }}Material that is clearly confidential in nature;</li>
            <li class="terms-and-conditions-subentry">
              Material the publication of which would contravene United States
              criminal laws; and,
            </li>
            <li class="terms-and-conditions-subentry">
              Material that is defamatory or harmful towards another person or
              group.
            </li>
          </ul>
        </li>
        <li class="terms-and-conditions-entry">
          The Amplification Project maintains the right to reject any submission
          for upload based on the above criteria or on any other reasonable
          basis.
        </li>
        <li class="terms-and-conditions-entry">
          Upon receipt of a genuine (or apparently genuine) claim that material
          on The Amplification Project is infringing copyright or violating
          another legal requirement, The Amplification Project will remove the
          material immediately and, if required, will contact the uploader of
          said material to examine the situation further.
        </li>
        <li class="terms-and-conditions-entry">
          If you own the copyright in the material you are uploading, you agree
          to allow The Amplification Project to make copies of that material
          (e.g., thumbnail images) pursuant to The Amplification Project’s
          stated purpose, in perpetuity and in all media formats.
        </li>
        <li class="terms-and-conditions-entry">
          If you do not own the copyright in the material you are uploading, you
          will include in the contribution form all copyright information and
          other relevant information related to the material, to the best of
          your knowledge.
        </li>
        <li class="terms-and-conditions-entry">
          The Amplification Project is committed to handling contributions
          respectfully and ethically. If you believe that another person has
          made your work available on this site in a way that constitutes
          copyright infringement or has violated your moral or intellectual
          property rights in some way, please contact us at
          theamplificationproject@gmail.com. To ensure a prompt response to your
          request, please include a) a detailed description of the material(s)
          in question, including the URL, and b) your reason(s) for wanting it
          removed, including additional details that were not provided as part
          of the original submission. We will review the request upon receipt
          and, if validated, we will immediately remove the relevant material.
          We're also happy to work with rights holders if they wish to modify
          the presentation of their materials or to learn more about the
          project.
        </li>
        <li class="terms-and-conditions-entry">
          You will also allow other users of The Amplification Project to make
          use of the material for non-commercial research, private study,
          education, criticism, or review under the terms of a CC BY-NC-ND 4.0
          Creative Commons License, including to make the work available through
          social media.
        </li>
        <li class="terms-and-conditions-entry">
          You agree not to use any part of The Amplification Project for any
          commercial uses without prior written consent.
        </li>
        <li class="terms-and-conditions-entry">
          By uploading material to The Amplification Project, you guarantee that
          the material is acceptable pursuant to the present terms and
          conditions.
        </li>
        <li class="terms-and-conditions-entry">
          You will also hold harmless The Amplification Project for any errors,
          omissions, or misstatements you make in submitting or describing
          material you upload to The Amplification Project.
        </li>
        <li class="terms-and-conditions-entry">
          The Amplification Project reserves the right to modify the present
          terms and conditions in keeping with The Amplification Project’s
          stated purpose. As an uploader of material to The Amplification
          Project, you agree to be bound by any and all such modified terms and
          conditions.
        </li>
        <li class="terms-and-conditions-entry">
          The Amplification Project is operated out of Los Angeles, California,
          USA, and any activities relating to The Amplification Project will be
          governed by United States law.
        </li>
      </ol>
    </div>
  </div>
</template>

<script>
export default {
  name: "TermsAndConditions",
};
</script>

<style scoped lang="scss">
#terms-and-conditions {
  // Container
  background: $bg-color;
  width: 100%;
  // Spacing
  padding: 0 calc(clamp(3rem, -1.800rem + 19.200vw, 15rem));

  #terms-and-conditions-header {
    // Sizing
    width: 100%;
    // Typography
    text-align: center;
    font-size: $header-font-size;
    font-weight: bold;
    // Spacing
    margin-top: $title-margin;
    margin-bottom: 32px;
  }

  #terms-and-conditions-subheader {
    // Typography
    font-size: $caption-font-size;
    font-family: $alt-font;
    color: black;
  }

  #terms-and-conditions-content {
    // Spacing
    margin: 32px 0;
    // Typography
    font-family: $alt-font;
    // Typography
    font-size: $caption-font-size;

    #terms-and-conditions-list-header {
      // Typography
      color: $accent-teal;
      font-weight: $bold;
      // Spacing
      margin-bottom: 32px;
      display: block;
    }

    #terms-and-conditions-list {
      // Init counter
      list-style: none;
      counter-reset: item;
      // Spacing
      margin-bottom: 5rem;

      .terms-and-conditions-entry {
        // Increment counter
        counter-increment: item;
        // Spacing
        margin-bottom: 1.25rem;
        line-height: 1.6;

        &:before {
          // Labelling
          content: counter(item) ".";
          // Typography
          color: $accent-teal;
          font-weight: bold;
        }

        .terms-and-conditions-sublist {
          .terms-and-conditions-subentry {
            // Bullets
            list-style: none;
            counter-reset: item;
            // Indent
            margin-left: 2rem;
            // Spacing
            margin-top: 1rem;

            &:before {
              // Custom bullet
              content: "•";
              color: $accent-teal;
              // Sizing
              font-size: 0.9rem;
              // Spacing
              margin-right: 0.3rem;
            }
          }
        }
      }
    }
  }
}
</style>