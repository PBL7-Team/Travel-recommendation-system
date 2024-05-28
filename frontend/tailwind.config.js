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
  colors: {
    'blue': '#1fb6ff',
    'purple': '#7e5bef',
    'pink': '#ff49db',
    'orange': '#ff7849',
    'green': '#13ce66',
    'yellow': '#ffc82c',
    'gray-dark': '#273444',
    'gray': '#8492a6',
    'gray-light': '#d3dce6',
  },
  plugins: [],
}

