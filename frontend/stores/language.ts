// stores/language.js
import { defineStore } from 'pinia'

interface LanguageState {
  currentLang: {
    name: string;
    code: string;
  };
}

export const useLanguageStore = defineStore('language', {
  state: (): LanguageState => ({
    currentLang: {
      name: "English (US)",
      code: "en",
    }
  }),
  actions: {
    setLanguage(lang: { name: string; code: string }) {
      this.$state.currentLang = lang;
    }
  },
  getters: {
    getCurrentLang(): { name: string; code: string } {
      return this.currentLang;
    }
  }
})