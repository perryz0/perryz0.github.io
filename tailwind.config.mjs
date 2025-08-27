// tailwind.config.mjs
/** @type {import('tailwindcss').Config} */
import typography from "@tailwindcss/typography";
export default {
  content: ["./src/**/*.{astro,html,md,mdx,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "var(--ink)",
        smoke: "var(--smoke)",
        slate: "var(--slate)",
        mist: "var(--mist)",
        cyan: "var(--cyan)",
        violet: "var(--violet)",
      },
      boxShadow: {
        aura: "0 10px 40px -10px rgba(92,225,230,.25)",
      },
    },
  },
  plugins: [typography],
};
