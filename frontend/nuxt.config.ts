// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: false },
  modules: [
    '@nuxt/ui',
    '@pinia/nuxt',
    '@vesp/nuxt-fontawesome',
    // '@nuxtjs/toast'
    'nuxt-vue3-google-signin',
    "@nuxtjs/i18n",
  ],

  vite: {
    vue: {
      template: {
        transformAssetUrls,
      },
    },
    define: {
      "process.env.DEBUG": false,
    },
  },
  nitro: {
    serveStatic: true,
  },
  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },
  css: [
    '~/assets/css/main.css',
    '@fortawesome/fontawesome-svg-core/styles.css'
  ],
  components: true,
  colorMode: {
    preference: 'light'
  },
  googleSignIn: {
    clientId: '512422882432-jh7q8uj4dtkhl7l55r99au4nf15tnut8.apps.googleusercontent.com',
  },
  i18n: {
    vueI18n: './localization/i18n.config.ts'
  }

})