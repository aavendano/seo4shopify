/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./editor/templates/editor/**/*.html",
    'node_modules/preline/dist/*.js'
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('preline/plugin')
  ],
}