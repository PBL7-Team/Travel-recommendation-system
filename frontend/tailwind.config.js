/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./components/**/*.{js,vue,ts}",
    "./layouts/**/*.{html,js,vue,ts}",
    "./pages/**/*.{html,js,vue,ts}",
    "./plugins/**/*.{js,ts}",
    "./configs/**/*.{js,ts}", // Áp dụng cho các tệp trong configs
    "./app.vue",
    "./error.vue",
  ],
  theme: {
    extend: {
      colors: {
        blue: {
          500: '#3b82f6',
          950: '#17275c',
        },
        purple: '#7e5bef',
        pink: '#ff49db',
        orange: '#ff7849',
        green: '#13ce66',
        yellow: '#ffc82c',
        'gray-dark': '#273444',
        gray: '#8492a6',
        'gray-light': '#d3dce6',
      },
      boxShadow: {
        'custom-shadow': '0 20px 30px -10px rgba(29, 1, 80, .1)',
      },
    },
  },
  plugins: [],
}
