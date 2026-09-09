import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Production builds use the custom domain. Environment variables remain useful
// if the site is previewed elsewhere in the future.
const site = process.env.SITE_URL || 'https://huaye410.site';
const base = process.env.BASE_PATH || '/';

export default defineConfig({
  site,
  base,
  output: 'static',
  trailingSlash: 'always',
  integrations: [sitemap()],
});
