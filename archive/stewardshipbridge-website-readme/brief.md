---
slug: stewardshipbridge-website-readme
title: Stewardship Bridge website README
audiences: human
ste-human: no
climb-to: writing
readers: a developer who maintains this site and must preview, deploy, or edit it after one read
purpose: preview the site on their computer, deploy it, and know where the words, design, and example come from
---

# Brief - one topic for one run

## Source

The repo `stewardshipbridge-website` holds the public landing page for https://stewardshipbridge.com/.

It is a static site: plain HTML, CSS, and images in `public/`. A small Cloudflare Worker serves the files.

- `public/` — the site: `index.html`, `styles.css`, images in `public/assets/`
- `worker.js` — redirects `www.stewardshipbridge.com` to `stewardshipbridge.com`, then serves `public/`
- `wrangler.jsonc` — the Cloudflare Worker configuration

Preview on your computer:

```bash
python3 -m http.server 4173 -d public
```

Open http://127.0.0.1:4173/

Deploy:

```bash
wrangler deploy
```

This deploys `public/` as the `stewardshipbridge-website` Worker to the `stewardshipbridge.org` Cloudflare account. It serves two custom domains: `stewardshipbridge.com` and `www.stewardshipbridge.com` (which redirects to the first).

Copy comes from the brand guide and the brand voice guide.

Page structure comes from the October 2026 website-visuals research: large type, one primary action, a static how-it-works diagram written in real text, and no stock photos or autoplay video.

Layout follows the Lovable preview: the tagline is the headline, an illustration sits beside it, and how-it-works is three cards at `#how`.

Content order follows the product pipeline from `~/projects/stewardshipbridge`: bylaws, minutes, and public statements first; human-led interviews last; then pages a person reviews.

Colors and type match brand tokens v0.1:

- Forest Green `#425C46`
- Terracotta `#D77456` (graphics only)
- Terracotta Deep `#A75A43` (links)
- Cream `#FEF7EF`
- Fonts: Nunito and Source Sans 3

Body text is 18px so board members can read it comfortably.

The procedure shown on the page is labeled as an example. It is not a client.

Conversation requests go to `hello@stewardshipbridge.com`.

## Task

After one read the reader can:

1. Preview the site on their computer.
2. Deploy the site with `wrangler deploy`.
3. Say where the copy, the page structure, the layout, and the design tokens come from.
4. Know the procedure on the page is an example, not a client.
5. Know the contact address for conversation requests.

## Keep

Keep these technical names as written: `stewardshipbridge.com`, `www.stewardshipbridge.com`, `stewardshipbridge.org`, `hello@stewardshipbridge.com`, file names (`public/`, `worker.js`, `wrangler.jsonc`, `index.html`, `styles.css`, `public/assets/`), the commands, color names and hex values, `Nunito`, `Source Sans 3`, `Lovable`, `wrangler`, `Cloudflare Worker`. Do not drop the 18px body-text reason.
