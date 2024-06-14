<script lang="ts" setup>
import {mdiArrowTopRight} from '@mdi/js'
import BaseIcon from '~/components/BaseIcon.vue';
import image from '@/assets/images/travel_bg.jpg'
import { ref, onMounted, onUnmounted } from 'vue';

definePageMeta({
  layout: 'default'
})

// definePageMeta({
//     middleware: 'auth' 
// })


const sentences = ref<string[]>([
  'Find exciting travel destinations for adventurous trip',
  'Suggest serene travel spots for couples seeking tranquility.',
  "Recommend culturally enriching destinations for exploration."
]);

const typedSentences = ref<string[]>(Array(sentences.value.length).fill(''));
let currentState = 'typing';



const typeAndErase = (index: number) => {
  let currentIndex = index;
  let interval = setInterval(() => {
    if (currentState === 'typing') {
      if (typedSentences.value[currentIndex] !== sentences.value[currentIndex]) {
        typedSentences.value[currentIndex] = sentences.value[currentIndex].slice(0, typedSentences.value[currentIndex].length + 1);
      } else {
        currentState = 'erasing';
        clearInterval(interval);
        setTimeout(() => {
          typeAndErase(currentIndex);
        }, 100);
      }
    } else if (currentState === 'erasing') {
      if (typedSentences.value[currentIndex].length > 0) {
        typedSentences.value[currentIndex] = typedSentences.value[currentIndex].slice(0, -1);
      } else {
        currentState = 'typing';
        clearInterval(interval);
        let nextIndex = (currentIndex + 1) % sentences.value.length;
        typeAndErase(nextIndex);
      }
    }
  }, 100);
};

onMounted(() => {
  sentences.value.forEach((sentence, index) => {
    typedSentences.value[index] = "";
    setTimeout(() => {
      typeAndErase(index);
    }, index * 100000);
  });
});

const faqItems = ref([
  {
    id: 1,
    question: "What makes Heros different from other travel search platforms?",
    answer: "Unlike standard booking engines, we offer a conversational interface that adapts and engages with your unique preferences. By aligning our interests and technology with the traveler, we enable a more comprehensive, and personalized search experience.",
    isOpen: false
  },
  {
    id: 2,
    question: "What is your return policy?",
    answer: "Our return policy allows returns for items within 30 days of delivery. Please contact us for further details.",
    isOpen: false
  },
  {
    id: 3,
    question: "How do I track my order?",
    answer: "Once your order has shipped, you will receive an email with tracking information. You can also track your order by logging into your account on our website.",
    isOpen: false
  },
  {
    id: 4,
    question: "Do you offer international shipping?",
    answer: "Yes, we offer international shipping to most countries. Shipping rates and delivery times may vary depending on your location.",
    isOpen: false
  },
  {
    id: 5,
    question: "What payment methods do you accept?",
    answer: "We accept all major credit cards, PayPal, and Apple Pay for online purchases.",
    isOpen: false
  },
  {
    id: 6,
    question: "Can I cancel my order?",
    answer: "Orders can be canceled within 24 hours of purchase. Please contact us as soon as possible if you need to cancel your order.",
    isOpen: false
  },
  {
    id: 7,
    question: "Do you offer gift wrapping?",
    answer: "Yes, we offer gift wrapping services for an additional fee. You can select this option during checkout.",
    isOpen: false
  },
  {
    id: 8,
    question: "How do I return an item?",
    answer: "To return an item, please contact our customer service team to initiate the return process. We will provide you with further instructions.",
    isOpen: false
  },

  // Add more FAQ items here in the same format
]);

const toggleFaq = (index: number) => {
  faqItems.value[index].isOpen = !faqItems.value[index].isOpen;
};

</script>

<template>
  <!-- <Navbar /> -->
  <NuxtLayout>
    <div class="page-wrapper-2">
      <div class="main-section-2">
        <div class="w-layout-grid _1-2-grid">
          <div class="content-wrap">
            <div class="subheader cta-color">Bold Voyage Heros</div>
            <div class="spacer-xs"></div>
            <h1 class="h1-3">The Smarter Way to Travel</h1>
            <div class="spacer-xs"></div>
            <p class="paragraph-11">BVHs redefines travel planning with precision and personalization at its core.
              Experience bespoke itineraries crafted to your preferences, powered by advanced semantic search.</p>
            <div class="spacer-l"></div>
            <div class="form-horizontal">
              <div class="input-large typed-animation">
                <div id="typed-words" class="typed-words">
                  <span v-for="(sentence, index) in sentences" :key="index">{{ typedSentences[index] }}</span>
                </div>

              </div><a href="/chatbot" class="button-16 in-horizontal-form w-button">Try it!</a>
            </div>
            <div class="spacer-xs"></div>
            <div class="small-feature-wrap">
              <div class="icon-secondary w-embed"><svg width="420" height="420" viewBox="0 0 24 24" fill="none"
                  xmlns="http://www.w3.org/2000/svg">
                  <path
                    d="M10.0002 15.172L19.1922 5.979L20.6072 7.393L10.0002 18L3.63623 11.636L5.05023 10.222L10.0002 15.172Z"
                    fill="currentColor"></path>
                </svg>
              </div>
              <div class="small-feature-label">Join <strong>thousands</strong> of travelers from 150+ countries!</div>
            </div>
          </div>
          <div class="hero-bg-image">
            <img :src="image" style="width:500px; height:460px">
            <div class="large-inverse-icon w-embed">
              <svg width="420" height="420" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M2 9.00011H5V21.0001H2C1.73478 21.0001 1.48043 20.8948 1.29289 20.7072C1.10536 20.5197 1 20.2653 1 20.0001V10.0001C1 9.7349 1.10536 9.48054 1.29289 9.293C1.48043 9.10547 1.73478 9.00011 2 9.00011V9.00011ZM7.293 7.70711L13.693 1.30711C13.7781 1.22181 13.8911 1.17008 14.0112 1.16144C14.1314 1.15281 14.2506 1.18785 14.347 1.26011L15.2 1.90011C15.4369 2.07796 15.6158 2.32196 15.7143 2.60137C15.8127 2.88077 15.8262 3.18306 15.753 3.47011L14.6 8.00011H21C21.5304 8.00011 22.0391 8.21083 22.4142 8.5859C22.7893 8.96097 23 9.46968 23 10.0001V12.1041C23.0003 12.3655 22.9493 12.6244 22.85 12.8661L19.755 20.3811C19.6795 20.5643 19.5513 20.721 19.3866 20.8312C19.2219 20.9414 19.0282 21.0002 18.83 21.0001H8C7.73478 21.0001 7.48043 20.8948 7.29289 20.7072C7.10536 20.5197 7 20.2653 7 20.0001V8.41411C7.00006 8.14892 7.10545 7.8946 7.293 7.70711Z"
                  fill="currentColor"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
    <section
      class="Homepage_section__hp0I_ Homepage_section_column__5YD3p BucketListSection_bucketList__section__kmFFL">
      <div class="BucketListSection_container">
        <div class="BucketListSection_textWrapper__XDzjj">
          <h2 class="SectionTitle_sectionTitle__i5qvD BucketListSection_title__lQfYg">Your travel bucketlist starts here
          </h2>
          <h3 class="SectionDescription_sectionDescription__iNgJ2">
            <a class="BucketListSection_bucketList__subtitleRA__VMMyq" href="/roamaround">Roam Around</a> is now
            OhTravel.
            Share where you're headed, and I'll craft an itinerary just for you.
          </h3>
        </div>
        <div class="SearchInput_input_wrapper">
          <input placeholder="Where to?" class="SearchInput_input__zM_0J" value="">
          <button class="SearchInput_button SearchInput_disabled">
            <!-- <img alt="search" loading="lazy" width="22" height="20" decoding="async" data-nimg="1"
              src="https://justasklayla.com/_next/static/media/search.c379aeab.svg" style="color: transparent;"> -->
              <BaseIcon :path="mdiArrowTopRight"/>
          </button>
        </div>
        <div class="BucketListSection_cards">
          <div class="Card_wrapper__yopvl Card_wrapperHover__9jHB0">
            <div class="Card_container__dYkWR">
              <div class="Card_videoWrapper__Jpvu1">
                <video class="Card_video__WzswZ" src="@/assets/videos/dest1.mp4" preload="none" autoplay loop
                  playsinline></video>
              </div>
              <div class="Card_bottom">
                <div class="Card_info">
                  <span class="Card_destination">Saigon Cao Dai Temple</span>
                  <span class="Card_date__Pudsn">Jun 2-Jun 6</span>
                </div>
                <button
                  class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium Card_button__1LjEC css-1ujsas3"
                  tabindex="0" type="button">Explore<span class="MuiTouchRipple-root css-w0pj6f"></span></button>
              </div>
            </div>
          </div>
          <!-- More cards go here -->
          <div class="Card_wrapper__yopvl Card_wrapperHover__9jHB0">
            <div class="Card_container__dYkWR">
              <div class="Card_videoWrapper__Jpvu1">
                <video class="Card_video__WzswZ" src="@/assets/videos/dest2.mp4" preload="none" autoplay loop
                  playsinline></video>
              </div>
              <div class="Card_bottom">
                <div class="Card_info">
                  <span class="Card_destination">Son Bac Valley</span>
                  <span class="Card_date__Pudsn">Jun 2-Jun 6</span>
                </div>
                <button
                  class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium Card_button__1LjEC css-1ujsas3"
                  tabindex="0" type="button">Explore<span class="MuiTouchRipple-root css-w0pj6f"></span></button>
              </div>
            </div>
          </div>
          <!-- More cards go here -->
          <div class="Card_wrapper__yopvl Card_wrapperHover__9jHB0">
            <div class="Card_container__dYkWR">
              <div class="Card_videoWrapper__Jpvu1">
                <video class="Card_video__WzswZ" src="@/assets/videos/dest3.mp4" preload="none" autoplay loop
                  playsinline
                  poster="https://cdn.dev.beautifuldestinations.app/207d31fa-a78a-4c48-a310-769f3c34a828/midThumbnail.jpg"></video>
              </div>
              <div class="Card_bottom">
                <div class="Card_info">
                  <span class="Card_destination">The Road at Night time</span>
                  <span class="Card_date__Pudsn">Jun 2-Jun 6</span>
                </div>
                <button
                  class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium Card_button__1LjEC css-1ujsas3"
                  tabindex="0" type="button">Explore<span class="MuiTouchRipple-root css-w0pj6f"></span></button>
              </div>
            </div>
          </div>

          <div class="Card_wrapper__yopvl Card_wrapperHover__9jHB0">
            <div class="Card_container__dYkWR">
              <div class="Card_videoWrapper__Jpvu1">
                <video class="Card_video__WzswZ" src="@/assets/videos/dest4.mp4" preload="none" autoplay loop
                  playsinline></video>
              </div>
              <div class="Card_bottom">
                <div class="Card_info">
                  <span class="Card_destination">Nha Trang Beach</span>
                  <span class="Card_date__Pudsn">Jun 2-Jun 6</span>
                </div>
                <button
                  class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium Card_button__1LjEC css-1ujsas3"
                  tabindex="0" type="button">Explore<span class="MuiTouchRipple-root css-w0pj6f"></span></button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>


    <!-- <section class="Homepage_section__hp0I_ Homepage_section_column__5YD3p">
    <div class="DescriptionSection_descriptionArea__xOFkj">
      <div class="DescriptionSection_descriptionArea__textWrapper__TXYYF">
        <h2 class="SectionTitle_sectionTitle__i5qvD DescriptionSection_descriptionArea__title__VrQzg">We see an big
          opportunity to deliver a superior experience for discovering and planning your next vacation. Our aim is to
          offer increasingly reliable, user-centric products for travelers worldwide.</h2>>
        <a target="_blank" href="/about">
          <button
            class="MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-root MuiButton-text MuiButton-textPrimary MuiButton-sizeMedium MuiButton-textSizeMedium Button_button__QHarr css-1ujsas3"
            tabindex="0" type="button">About us<span class="MuiTouchRipple-root css-w0pj6f"></span></button>
        </a>
      </div>
      <div class="DescriptionSection_descriptionArea__imageWrapper__CivCM">
        <iframe class="DescriptionSection_descriptionArea__video__AP04U" src="https://www.youtube.com/embed/iy53wPnNCYU"
          title="Đi Để Trở Về - Soobin Hoàng Sơn | Official Music Video" frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture;"
          referrerpolicy="strict-origin-when-cross-origin" allowfullscreen=""></iframe>
      </div>
    </div>
  </section> -->
    <!-- About us -->
    <div class="main-section-2">
      <div class="main-container-2">
        <div class="w-layout-grid _1-2-grid">
          <div class="content-wrap">
            <h2 class="h2">Built by travelers, for travelers.</h2>
            <div class="spacer-m"></div>
            <p class="paragraph-11">We see an big opportunity to deliver a superior experience for discovering and
              planning your next vacation. Our aim is to offer increasingly reliable, user-centric products for
              travelers
              worldwide.</p>
            <div class="spacer-l"></div><a href="/about" class="button-2">About us</a>
          </div><img
            src="https://assets-global.website-files.com/6241fae88cb0b11a61c12ba5/64a8d65b7dba1d15886f4ac5_FS%20Bora%20Bora.jpeg"
            loading="lazy" id="w-node-d598884f-1d19-2366-1050-61c2e001b8ba-eee4a83f" sizes="90vw" alt=""
            srcset="https://assets-global.website-files.com/6241fae88cb0b11a61c12ba5/64a8d65b7dba1d15886f4ac5_FS%20Bora%20Bora-p-500.jpeg 500w, https://assets-global.website-files.com/6241fae88cb0b11a61c12ba5/64a8d65b7dba1d15886f4ac5_FS%20Bora%20Bora-p-800.jpeg 800w, https://assets-global.website-files.com/6241fae88cb0b11a61c12ba5/64a8d65b7dba1d15886f4ac5_FS%20Bora%20Bora-p-1080.jpeg 1080w, https://assets-global.website-files.com/6241fae88cb0b11a61c12ba5/64a8d65b7dba1d15886f4ac5_FS%20Bora%20Bora.jpeg 1530w"
            class="hero-image-2">
        </div>
      </div>
    </div>

    <!-- Prices -->

    <div class="main-section-2">
      <div class="main-container-2">
        <div class="content-wrap-center">
          <div
            style="opacity: 1; transform: translate3d(0px, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg); transform-style: preserve-3d;"
            class="content-wrap-center max-width-800">
            <h2 class="h2">Memberships for Travelers and Agencies</h2>
            <div class="spacer-xs"></div>
            <p class="paragraph-11">Explore our full <a href="/pricing" class="link">membership</a> plans.</p>
          </div>
          <div class="spacer-xxl"></div>
          <div class="w-layout-grid _1-3-grid">
            <div id="w-node-d598884f-1d19-2366-1050-61c2e001b8c9-eee4a83f"
              data-w-id="d598884f-1d19-2366-1050-61c2e001b8c9"
              style="opacity: 1; transform: translate3d(0px, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg); transform-style: preserve-3d;"
              class="card-outer">
              <div class="card-inner">
                <h3 class="h3">Personal</h3>
                <div class="spacer-xs"></div>
                <p class="paragraph-11"><strong>Free</strong></p>
                <p class="paragraph-11">Create a free account to get limited access to our platform and become part of
                  our
                  growing community.</p>
                <div class="spacer-m"></div><a href="/sign-up" class="button-2">Sign up</a>
              </div>
            </div>
            <div
              style="opacity: 1; transform: translate3d(0px, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg); transform-style: preserve-3d;"
              class="card-outer">
              <div class="card-inner">
                <h3 class="h3">Premium</h3>
                <div class="spacer-xs"></div>
                <p class="paragraph-11"><strong>$9.99 / month</strong></p>
                <p class="paragraph-11">Upgrade to unlock full access to our platform tools and exclusive membership
                  benefits.</p>
                <div class="spacer-m"></div><a href="/pricing" class="button-2">Learn More</a>
              </div>
            </div>
            <div
              style="opacity: 1; transform: translate3d(0px, 0px, 0px) scale3d(1, 1, 1) rotateX(0deg) rotateY(0deg) rotateZ(0deg) skew(0deg, 0deg); transform-style: preserve-3d;"
              class="card-outer">
              <div class="card-inner">
                <h3 class="h3">Professional</h3>
                <div class="spacer-xs"></div>
                <p class="paragraph-11"><strong>$49 / month</strong></p>
                <p class="paragraph-11">For advisors and agencies looking to step-up their planning and operational
                  efficiency.</p>
                <div class="spacer-m"></div><a href="/pricing" class="button-2">7-Day Trial</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- FAQs -->

    <div class="main-section-2">
      <div class="main-container-2">
        <div class="content-wrap">
          <h2 class="h2">Have a question?</h2>
          <div class="spacer-xs"></div>
          <p class="paragraph-11">Don't hesitate to <nuxt-link to="/contact" class="link">contact us</nuxt-link> for any
            other questions or support.</p>
        </div>
        <div class="spacer-xxl"></div>
        <div class="_2-4-grid vertical-mobile">
          <div v-for="(faq, index) in faqItems" :key="index">
            <div class="accordion-wrap">
              <div class="faq-item">
                <a href="#" class="faq-question w-inline-block" @click.prevent="toggleFaq(index)">
                  <div>{{ faq.question }}</div>
                  <div class="p-m-wrap">
                    <div class="minus"></div>
                    <div class="plus"></div>
                  </div>
                </a>
                <div class="faq-answer" :style="{ height: faq.isOpen ? 'auto' : '0px' }">
                  <p class="faq-p">{{ faq.answer }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </NuxtLayout>
</template>

<style lang="scss" scoped>
@import url("@/assets/css/home.scss");

p {
  margin-top: 0;
  margin-bottom: 10px;
}

.main-section-2 {
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 100px 5%;
  display: flex;
}

.main-container-2 {
  width: 100%;
  max-width: 1100px;
}

._1-2-grid {
  grid-column-gap: 40px;
  grid-row-gap: 40px;
  grid-template-rows: auto;
  align-items: center;
}

.w-layout-grid {
  grid-row-gap: 16px;
  grid-column-gap: 16px;
  grid-template-rows: auto auto;
  grid-template-columns: 1fr 1fr;
  grid-auto-columns: 1fr;
  display: grid;
}

.content-wrap {
  flex-direction: column;
  align-items: flex-start;
  display: flex;
}

.h2 {
  color: #000;
  margin-top: 0;
  margin-bottom: 0;
  font-size: 45px;
  font-weight: 600;
  line-height: 1.1;
}

.spacer-m {
  width: 100%;
  height: 20px;
}

.paragraph-11 {
  opacity: .9;
  color: #000;
  font-size: 16px;
  font-weight: 300;
  line-height: 1.5;
}

.spacer-l {
  width: 100%;
  height: 30px;
}

img {
  vertical-align: middle;
  max-width: 100%;
  display: inline-block;
}

.hero-image-2 {
  height: auto;
  border-radius: 10px;
  width: 100%;
  box-shadow: 21px 21px 30px -10px rgba(29, 1, 80, .1);
}

@media screen and (max-width: 991px) {
  ._1-2-grid {
    flex-direction: column;
    align-items: flex-start;
    display: flex;
  }
}

// About us

.content-wrap-center {
  text-align: center;
  flex-direction: column;
  align-items: center;
  display: flex;
}

._1-3-grid {
  grid-column-gap: 40px;
  grid-row-gap: 40px;
  grid-template-rows: auto auto;
  grid-template-columns: 1fr 1fr 1fr;
  grid-auto-columns: 1fr;
  width: 100%;
  display: grid;
}

.card-inner {
  text-align: left;
  flex-direction: column;
  align-items: flex-start;
  padding: 25px;
  display: flex;
}

.h3 {
  color: #000;
  margin-top: 0;
  margin-bottom: 0;
  font-size: 30px;
  font-weight: 600;
}

.paragraph-11 {
  opacity: .9;
  color: #000;
  font-size: 16px;
  font-weight: 300;
  line-height: 1.5;
}


.button-2 {
  color: #434de7;
  border-radius: 10px;
  height: 50px;
  padding: 15px 35px;
  font-size: 15px;
  font-weight: 500;
  box-shadow: 0 10px 20px -3px rgba(29, 1, 80, .1);
  background-color: #fff;
  border: 2px solid #434de7;
  padding-top: 13px;
  padding-left: 25px;
  padding-right: 25px;
}

//FAQs
._2-4-grid {
  grid-column-gap: 16px;
  grid-row-gap: 16px;
  grid-template-rows: auto auto auto auto;
  grid-template-columns: 1fr 1fr;
  grid-auto-columns: 1fr;
  grid-auto-flow: column;
  align-content: start;
  min-height: 150px;
  margin-top: 0;
  margin-bottom: 0;
  display: grid;
}

.accordion-wrap {
  border: 1px solid #f2f3ff;
  border-radius: 10px;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  max-width: 800px;
  display: flex;
  overflow: hidden;
  box-shadow: 0 10px 30px -10px rgba(29, 1, 80, .1);
}

.faq-item {
  background-color: #fff;
  border-radius: 0;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  max-width: none;
  display: flex;
}

.faq-question {
  color: #000;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 20px;
  font-size: 16px;
  font-weight: 600;
  text-decoration: none;
  display: flex;
}

.p-m-wrap {
  justify-content: center;
  align-items: center;
  width: 15px;
  height: 15px;
  display: flex;
  position: relative;
}

.minus {
  background-color: #000;
  border-radius: 20px;
  width: 100%;
  height: 3px;
  position: absolute;
}

.plus {
  background-color: #000;
  border-radius: 20px;
  width: 3px;
  height: 100%;
  position: absolute;
}

.faq-answer {
  text-align: left;
  border-bottom: 1px #cfcfcf;
  width: 100%;
  overflow: hidden;
}

.faq-p {
  color: #000;
  margin-bottom: 20px;
  margin-left: 20px;
  margin-right: 20px;
}

.link {
  font-weight: 400;
}

@media screen and (max-width: 479px) {
  ._2-4-grid.vertical-mobile {
    grid-auto-flow: row;
  }
}


$card-width: 260px;

.BucketListSection_cards {
  display: flex;
  align-items: stretch;
  gap: 16px;
  max-width: calc(#{$card-width}* 4 + 3* 16px + 20px);
  width: 100%;
  padding: 10px;
  overflow-x: auto;
}

.BucketListSection_container {
  width: 100%;
  padding: 0 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  --card-width: 260px;
}

.BucketListSection_textWrapper__XDzjj {
  @media (min-width: 1024px) {
    margin-bottom: 60px;
  }
}

.SearchInput_input_wrapper {
  position: relative;
  max-width: 406px;
  width: 100%;
}

.SearchInput_input__zM_0J {
  align-items: center;
  background: #fff;
  border-radius: 46px;
  margin-bottom: 32px;
  padding: 17px 64px 17px 23px;
  width: 100%;
  height: 68px;
  font-family: Montserrat;
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 20px;
  border: 2px solid #dfe0e1;
  box-shadow: 0 12px 32px 0 #0000001f;
  outline: none;
}

.SearchInput_button {
  display: flex;
  justify-content: center;
  align-items: center;
  position: absolute;
  right: 12px;
  margin-bottom: 5px;
  margin-top: 5px;
  cursor: pointer;
  border-radius: 100px;
  width: 44px;
  height: 44px;
  top: 6px;
  font-weight: 700;
  font-size: 6px;
  line-height: 12.6px;
  color: #fff;
  border: none;
  transition: all .3s;
  background-color: #21bcbe;
}

img {
  width: 22px;
  aspect-ratio: auto 22 / 20;
  height: 20px;
}

.SearchInput_input_wrapper {
  position: relative;
  max-width: 406px;
  width: 100%;
}


.BucketListSection_container {
  width: 100%;
  padding: 0 150px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.BucketListSection_cards {
  display: flex;
  align-items: stretch;
  gap: 16px;
  max-width: calc(var(--card-width)* 4 + 3* 16px + 20px);
  width: 100%;
  padding: 10px;
  overflow-x: auto;
}

.Card_videoWrapper__Jpvu1 {
  position: relative;
  width: 100%;
  height: 260px;
  overflow: hidden;
  border-radius: 12px 12px 0 0;
}

.Card_wrapper__yopvl {
  width: 260px;
  border-radius: 16px;
  cursor: pointer;
  transition: box-shadow .5s;
  background-color: #fff;
}


.Homepage_container__lpxw5 {
  min-height: 100svh;
  overflow: hidden;
  background-color: #fff;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  --iframe-navbar-height: 48px;
}

.BucketListSection_title__lQfYg {
  margin-bottom: 24px;
}

.SectionTitle_sectionTitle__i5qvD {
  @media (min-width: 1024px) {
    line-height: 64px;
    font-size: 56px;
    margin-bottom: 60px;
  }
}

.SectionTitle_sectionTitle__i5qvD {
  @media (min-width: 768px) {
    line-height: 36px;
    font-size: 44px;
    margin-bottom: 36px;
  }
}

.Card_container__dYkWR {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 260px;
  height: 100%;
  justify-content: space-between;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, .06);
  border-radius: 12px;
}

.Card_info {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.Card_button__1LjEC {
  margin-top: 16px !important;
  width: 100% !important;
  background: #f6f6f6 !important;
  border-radius: 10px !important;
  padding: 14px !important;
  font-weight: 700 !important;
  font-family: Montserrat, "sans-serif" !important;
  font-size: 14px !important;
  line-height: 14px !important;
  text-align: center !important;
  text-transform: none !important;
  color: #000 !important;
}

.Card_destination {
  font-size: 18px;
  font-weight: 600;
  line-height: 18px;
  letter-spacing: -.02em;
  text-align: left;
  color: #002c6a;
}

.Card_bottom {
  width: 100%;
  padding: 16px;
}

// Section 2: 
.Homepage_section__hp0I_ {
  display: flex;
  margin-block: 30px;
  width: 100%;
  padding-inline: 30px;
}


.Homepage_container__lpxw5 {
  min-height: 100svh;
  overflow: hidden;
  background-color: #fff;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  --iframe-navbar-height: 48px;
}

.Homepage_section_column__5YD3p {
  flex-direction: column;
}

.Homepage_section__hp0I_ {
  @media (min-width: 1024px) {
    margin-block: 70px;
  }

  @media (min-width: 768px) {
    margin-block: 50px;
  }
}

.DescriptionSection_descriptionArea__xOFkj {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  width: 100%;
  gap: 56px;
}

.DescriptionSection_descriptionArea__xOFkj {
  @media (min-width: 768px) {
    display: flex;
    flex-direction: row;
  }
}

.DescriptionSection_descriptionArea__textWrapper__TXYYF {
  @media (min-width: 768px) {
    align-items: flex-start;
  }
}

.DescriptionSection_descriptionArea__title__VrQzg {
  @media (min-width: 768px) {
    text-align: left;
  }
}

.DescriptionSection_descriptionArea__title__VrQzg {
  margin-bottom: 32px;
  text-align: center;
}

.SectionTitle_sectionTitle__i5qvD {
  @media (min-width: 1024px) {
    line-height: 64px;
    font-size: 56px;
    margin-bottom: 60px;
  }
}

.SectionTitle_sectionTitle__i5qvD {
  @media (min-width: 768px) {
    line-height: 36px;
    font-size: 44px;
    margin-bottom: 36px;
  }
}

.SectionTitle_sectionTitle__i5qvD {
  margin-bottom: 24px;
  font-family: Montserrat, "sans-serif";
  font-weight: 700;
  font-size: 32px;
  text-align: center;
  color: #002c6a;
}

.DescriptionSection_descriptionArea__description__FyNwS {
  margin-bottom: 48px;
  font-family: Montserrat, "sans-serif";
  font-weight: 500;
  font-size: 18px;
  line-height: 28px;
  color: #002c6a;
}

.DescriptionSection_descriptionArea__textWrapper__TXYYF {
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  max-width: 626px;
  width: 100%;
  text-align: left;
}

a {
  color: inherit;
  text-decoration: none;
}

.Button_button__QHarr {
  background: #000 !important;
  border-radius: 14px !important;
  padding: 16px 24px !important;
  height: 56px !important;
  font-weight: 700 !important;
  font-family: Montserrat, "sans-serif" !important;
  font-size: 16px !important;
  line-height: 24px !important;
  text-align: center !important;
  text-transform: none !important;
  color: #fff !important;
}
</style>
