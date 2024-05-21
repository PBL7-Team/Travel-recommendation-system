/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.{html,js,vue,ts}",
    "./pages/**/*.{html,js,vue,ts}",
    "./plugins/**/*.{js,ts}",
    "./configs/**/*.{js,ts}",  // Add this to apply colors
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

