/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './apps/**/templates/**/*.html',
    './apps/**/forms.py',
    './front/components/**/*.jsx',

  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
