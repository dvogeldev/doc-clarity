---
audience: human
standard: ISO-24495-1
slug: stewardshipbridge-website-readme
title: Stewardship Bridge website README
readers: a developer who maintains this site and must preview, deploy, or edit it after one read
purpose: preview the site on your computer, deploy it, and know where the words, design, and example come from
clarity-exceptions:
---

# Preview, deploy, and edit the Stewardship Bridge website

This repo holds the public landing page for [stewardshipbridge.com](https://stewardshipbridge.com/). It's a static site — plain HTML, CSS, and images in `public/` — served by a small Cloudflare Worker.

## What's in the repo

- `public/` — the site itself: `index.html`, `styles.css`, and images in `public/assets/`
- `worker.js` — sends `www.stewardshipbridge.com` visitors to `stewardshipbridge.com`, then serves the files in `public/`
- `wrangler.jsonc` — the Cloudflare Worker configuration

## How to preview the site on your computer

```bash
python3 -m http.server 4173 -d public
```

Then open http://127.0.0.1:4173/

## How to deploy the site

```bash
wrangler deploy
```

That command deploys `public/` as the `stewardshipbridge-website` Worker. It runs on the `stewardshipbridge.org` Cloudflare account, on two custom domains: `stewardshipbridge.com` and `www.stewardshipbridge.com`. The `www` domain redirects to the first.

## Where the words and design come from

**The copy** comes from the brand guide and the brand voice guide.

**The page structure** comes from the October 2026 website-visuals research. That research calls for large type, one primary action, and a static how-it-works diagram written in real text. It rules out stock photos and autoplay video.

**The layout** follows the Lovable preview: the tagline is the headline, an illustration sits beside it, and how-it-works is three cards at `#how`.

**The content order** follows the product pipeline in `~/projects/stewardshipbridge`. Bylaws, minutes, and public statements come first. Human-led interviews come last. Then come pages that a person reviews.

**The colors and type** match brand tokens v0.1:

- Forest Green `#425C46`
- Terracotta `#D77456` (graphics only)
- Terracotta Deep `#A75A43` (links)
- Cream `#FEF7EF`
- Fonts: Nunito and Source Sans 3

Body text is 18px so board members can read it comfortably.

## The example on the page is not a client

The procedure shown on the page is labeled as an example. It is not a client.

## Where conversation requests go

Send conversation requests to `hello@stewardshipbridge.com`.
