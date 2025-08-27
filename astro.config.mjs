// astro.config.mjs
import tailwind from "@astrojs/tailwind";
import mdx from "@astrojs/mdx";
export default {
  integrations: [tailwind({ applyBaseStyles: false }), mdx()],
};
