# AsliKaam — V1

Digital Partner of MSMEs Automation. Static site, generated from `data.py` + `build.py` into `site/` — no build step needed at deploy time.

## What's in V1

- **Home** (`/`) — cinematic pinned-scroll story: Pain → Fix → Growth → Reveal (industry picker) → Payoff.
- **Industries** (`/industries/`) — 15 verticals (the original 11 + Retail/Kirana, Automobile Showroom, Building Materials/Tiles Showroom, Wholesale Distributor). Each has a leak-map, a **tap-to-select use-case chip row** (primary story + its mapped secondary automation modules, each with its own before/after preview and Proven/Proposed badge), solution bullets, and — where we have solid sourcing — an "Industry Context" citation card linking to a real external report (never a link to a competing consumer app). **No pricing appears here or anywhere except `/pricing/`** — CTAs link to Demos/Pricing instead of showing a number.
- **Retail/Kirana is the flagship vertical**: the pain point is losing home-bound orders to quick-commerce apps because there's no ordering channel tied to real inventory — grounded in real 2026 market data (kirana closures, wallet-share shift to Blinkit/Zepto/Instamart).
- **MODULES** (`data.py`) — 15 reusable automation add-ons, mapped to relevant industries in `INDUSTRY_MODULES`. Single source of truth reused across Industries pages, Demos, Pricing, and Agentic Use Cases. Covers: Invoice + Payment Reminders, Payment Reconciliation, Booking Confirmation + No-Show Reminder, Claim/Document Auto-Email Dispatch, Review Request + AI-Drafted Reply, Stock Check-and-Reserve, Reorder/Repeat-Purchase Nudge, Lead Qualification + Scoring, FAQ + Objection-Handling, Negative Review Alert + Recovery, Abandoned-Inquiry Win-Back, AI Local-SEO Content Agent, Missed-Call Instant Win-Back, AI Quotation Drafting, Competitor Price-Watch Alert.
  - Each module has two independent fields: **`effort`** (`"quick"` ~2 days or `"advanced"` ~1-2 weeks) — this is **internal planning only, never rendered on the site**, it's how we scope our own delivery, not a promise to a visitor. And **`agentic`** (`True`/`False`) — this **is** customer-facing: it's whether the automation needs real AI judgment (scoring, drafting, negotiating) or is simple deterministic rules/templates. The site groups and labels everything by `agentic`, never by `effort`.
- **NEGOTIATION_AGENT** (`data.py`) — the flagship "Instant-Response + Negotiation Agent" story, now the full funnel: found via a complete Google Business Profile (posts/website/WhatsApp button beat the listings that get skipped) → enquiry → pre-drafted qualifying reply → quote → negotiation (asks for a competitor's name/quote, matches within limits) → payment-link close → follow-up + referral for repeat orders. 7 narrative scenes + payoff = 8 total, its own cinematic demo (`/demos/module-negotiation-agent.html`), top billing on Agentic Use Cases. Verified with zero layout issues at phone/tablet/laptop widths.
- **Demos** (`/demos/`) — 31 standalone pages (15 industries + 15 modules + the flagship), each with the *full* pinned cinematic sequence. The index has a **live search box** and **tap-to-filter industry chips**.
- **Pricing** (`/pricing/`) — the only page with prices. Go Digital / Growth / Expansion packs + a Custom Pack configurator that leads with an **industry picker**: choosing one auto-checks its relevant modules and shows a "Recommended for X" note. The live summary + "Send Enquiry on WhatsApp" button build a prefilled WhatsApp message including the industry and every selection — no invented add-on pricing.
- **Agentic Use Cases** (`/agentic-use-cases/`) — leads with the flagship negotiation-agent banner, then all 15 modules grouped as **"⚙️ Non-Agentic Automations"** (simple, rule-based) and **"🤖 Agentic Automations"** (needs real AI judgment) — no day/week estimates, no prices, each links to its own demo.
- **Blogs** and **Free Tools** — stub "Coming in V2" pages (as scoped: full blog content + Hindi/Marathi land in V2).
- Global UI: persistent WhatsApp float button + mobile sticky Call/WhatsApp bar.

### On the "citation" fields in `data.py`

Only 5 industries (`export-trading`, `hospital`, `gym-fitness-chain`, `ca-legal-firm`, `retail-store`) currently have a `citation` — a real, checked external source backing the pain-point narrative. The rest intentionally have none rather than a fabricated one. Add more by following the same `{"stat", "source", "url"}` shape once you've verified a source for that vertical — the honesty rule applies to citations exactly as it does to the Proven/Proposed badges.

### Real-screen component system

Every demo (Home, the flagship, all 15 industries, all 15 modules) renders actual platform mockups instead of narrated placeholder text — built in `build.py`:
- `search_results_screen()` — a Maps/Search results list with named competitors, ratings, and complete-vs-incomplete profile tags. Home's opening scene cycles through 5 industries (Electrician/Gym/Event Planner/Hospital/Retail) every 2.2s via `assets_src/js/home-rotator.js`, in sync across its two scenes — so no visitor sees only a field that isn't theirs.
- `chat_screen()` — a WhatsApp conversation with a real header (avatar, contact name, live status). Every industry and module has its own distinct customer name (see `CUSTOMER_NAMES` / `MODULE_CONTACT_NAMES` in `build.py`).
- `lead_notification_screen()` — a platform-native inbound-lead card (IndiaMART RFQ, 99acres, Instagram DM, a missed call) for industries whose pain narrative is about a specific discovery platform, not Maps.
- `payment_screen()` — a pay sheet (Pending → Paid), visually distinct from chat.

`DISCOVERY_OVERRIDES` in `build.py` maps 8 industries (hospital, ca-legal-firm → search; export-trading, real-estate-developer, b2b-manufacturer, private-school, wedding-planner-banquet, building-materials-showroom → lead notification) to the platform their *existing* pain copy already describes — reusing that copy as the screen's content, not inventing new text. The other 7 industries (coaching-institute, diagnostic-lab, gym-fitness-chain, interior-designer, retail-store, automobile-showroom, wholesale-distributor) keep their pain scene as a headered chat, because their story genuinely isn't about being found. Don't force every industry through the same visual — match the screen to what the copy already says.

## Before going live

Replace the placeholder contact details in **`assets_src/js/config.js`**:
```js
whatsappNumber: "911234567890", // real WhatsApp Business number, no + or spaces
phoneNumber: "+911234567890",   // real business line
```
Then re-run `python3 build.py` to bake the new numbers into the generated pages (the nav/footer WhatsApp links are baked at build time; the floating button and mobile bar read `config.js` at runtime).

## Editing content

All industry copy, pricing packs, and configurator options live in **`data.py`** — one place, no HTML editing needed. After changing it:

```bash
python3 build.py
```

This regenerates `site/` from scratch (deletes and rebuilds it) and copies `assets_src/` into `site/assets/`. Never hand-edit files inside `site/` directly — they'll be overwritten on the next build.

## Local preview

```bash
cd site && python3 -m http.server 8000
```

## Cloudflare Pages deploy (free tier)

**Option A — direct upload (fastest):** Cloudflare dashboard → Workers & Pages → Create → Pages → Upload assets → drag in the contents of `site/` (or this zip). No build command needed — it's already static output.

**Option B — connect a git repo:** push this project to GitHub, then in Cloudflare Pages set:
- Build command: `python3 build.py`
- Build output directory: `site`
- Root directory: `/`

### Free-tier optimizations already built in
- Zero build step required — pure static HTML/CSS/JS, so Pages serves it instantly with no build minutes spent.
- `_headers` sets `immutable` caching on `/assets/*` (hits Cloudflare's edge cache hard) and basic security headers on every page.
- No external fonts, no icon-font/CDN requests — only GSAP + ScrollTrigger load from a CDN (cdnjs), and even that has a hard 3-second timeout with a full non-JS fallback (see below), so nothing blocks first paint.
- All 30+ pages are pre-rendered HTML (good Core Web Vitals / SEO out of the box, no client-side routing/hydration cost).

## Cinematic scroll: how the fallback works

`assets_src/js/gsap-loader.js` loads GSAP + ScrollTrigger from cdnjs with a **3-second timeout**. If the CDN is slow, blocked, or errors out, the page falls back to the plain stacked/non-pinned layout — scenes fade in via `IntersectionObserver` as the user scrolls normally. This is a real fallback, not just a manifest claim: it was verified by intercepting and aborting all `cdnjs.cloudflare.com` requests in a headless browser and confirming (a) the page never applies `.js-pin-active`, (b) every scene still becomes visible on scroll, (c) the page remains naturally scrollable, and (d) zero console errors. GSAP's own `pin` is the only pinning mechanism used — CSS `position: sticky` is never combined with it, so there's no double-pin risk.

Test it yourself with the CDN blocked: open DevTools → Network → block `cdnjs.cloudflare.com`, then reload.

## V2 scope (not in this build)

- 66 blog posts (6 per industry) with regulator/brand citations
- Hindi + Marathi translations, hreflang tags, translated slugs
- Free Tools calculators (EMI, BMI, GST, landed-cost, etc.)
- Flipping industries from Proposed → Proven as real pilots land
