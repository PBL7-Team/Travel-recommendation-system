// https://nuxt.com/docs/api/configuration/nuxt-config
import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'
export default defineNuxtConfig({
  ssr: false,
  devtools: { enabled: false },
  runtimeConfig: {
    public: {
      apiUrl: process.env.NUXT_API_URL
    }
  },
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
    // server: {
    //   proxy: {
    //     "/backend": {
    //       target: "https://singular-joey-normally.ngrok-free.app/",
    //       changeOrigin: true,
    //     },
    //   },
    // }
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
    clientId: process.env.GOOGLE_SIGNIN_CLIENT_ID||'512422882432-jh7q8uj4dtkhl7l55r99au4nf15tnut8.apps.googleusercontent.com',
  },
  i18n: {
    vueI18n: './localization/i18n.config.ts'
  }

})