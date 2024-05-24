export const plugins = [
  require('tailwindcss/nesting'),
  require('tailwindcss'),
  require("postcss-prefix-selector")({
    prefix: '.parent-class', // you can change this whatever you want
  })
];
