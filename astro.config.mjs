// astro.config.mjs
import tailwind from "@astrojs/tailwind";
import mdx from "@astrojs/mdx";

export default {
  trailingSlash: "always",
  site: "https://perryz0.github.io",
  base: "/",
  integrations: [tailwind({ applyBaseStyles: false }), mdx()],
};
