import en from './languagues/en';
import vi from './languagues/vi';
export default defineI18nConfig(() => ({
  legacy: false,
  locales: ['en', 'vi'],
  locale: 'en',
  messages: {
    en,
    vi
  }
}));