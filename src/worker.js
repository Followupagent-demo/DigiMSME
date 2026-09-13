/*
 * AsliKaam Worker — serves the static site (env.ASSETS, unchanged) and
 * adds one dynamic feature: "Market Pulse", a short tip posted every
 * 6 hours by a free, open-weight LLM (via Groq's free-tier API).
 *
 * Deliberately scoped to be safe unattended: the system prompt forbids
 * invented statistics, prices, client names, or testimonials — only
 * generic, evergreen small-business advice from a fixed topic pool.
 * Every post is labeled "auto-generated" on the page itself. This is
 * NOT a substitute for the hand-researched, sourced posts in /blogs/ —
 * it's a clearly separate, clearly labeled feed, so nothing here can
 * be mistaken for a verified claim.
 *
 * Needs, set outside this file (see README):
 *   - env.GROQ_API_KEY      — Secrets Store binding (wrangler.toml),
 *                             an object with an async .get() — NOT a
 *                             plain string, unlike a classic Worker
 *                             secret. Always read it via
 *                             (await env.GROQ_API_KEY.get()).
 *   - env.MARKET_PULSE      — KV namespace binding (wrangler.toml)
 */

const TOPIC_POOL = [
  "why a Google Business Profile without photos loses walk-ins",
  "the cost of a WhatsApp message left unanswered for 2 hours",
  "why 'let me check and get back to you' loses price-sensitive customers",
  "what a missed-call auto-reply actually needs to say",
  "why festive-season response speed matters more than festive-season discounts",
  "the difference between a website that exists and a website that gets found",
  "why repeat customers deserve a faster reply than new ones, not a slower one",
  "what to automate first when you only have time to automate one thing",
  "why an unpaid invoice needs a reminder schedule, not a memory",
  "how a booking confirmation message prevents no-shows",
  "why reviews need a reply, not just a read",
  "what 'agentic' actually means for a small business, in plain terms",
  "why a stockout should trigger a message, not a shrug",
  "the real cost of a slow quote in a price-sensitive category",
  "why WhatsApp catalogs work better than a PDF price list",
  "what a customer decides in the first 15 seconds on your Google listing",
  "why referral follow-ups get forgotten and what that costs",
  "the gap between 'we have a website' and 'our website generates leads'",
  "why a fixed reply template beats no reply at all",
  "what small businesses get wrong about needing a mobile app before a WhatsApp flow",
];

function pickTopic() {
  const idx = Math.floor((Date.now() / (1000 * 60 * 60 * 6)) % TOPIC_POOL.length);
  return TOPIC_POOL[idx];
}

async function generatePost(env) {
  const topic = pickTopic();
  const system = `You write short, plain-language business tips for Indian MSME (small business) owners, for AsliKaam's "Market Pulse" feed.
Hard rules:
- Never invent a statistic, percentage, price, client name, testimonial, or "study shows" claim. If you'd need a real source to say it, don't say it.
- Plain, concrete, spoken language — no marketing jargon, no metaphors like "leaks" or "compounds".
- 90-140 words. One short paragraph, maybe two.
- End with one practical, doable suggestion, not a sales pitch.
- Do not mention AsliKaam, pricing, or tell the reader to buy anything.`;
  const user = `Write today's tip about: ${topic}`;

  const groqKey = await env.GROQ_API_KEY.get();
  const res = await fetch("https://api.groq.com/openai/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${groqKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: "llama-3.3-70b-versatile",
      messages: [
        { role: "system", content: system },
        { role: "user", content: user },
      ],
      temperature: 0.6,
      max_tokens: 260,
    }),
  });

  if (!res.ok) {
    throw new Error(`Groq API error ${res.status}: ${await res.text()}`);
  }
  const data = await res.json();
  const body = data.choices?.[0]?.message?.content?.trim();
  if (!body) throw new Error("Groq returned no content");

  const now = new Date();
  const key = `post:${now.toISOString()}`;
  const post = { topic, body, date: now.toISOString() };
  await env.MARKET_PULSE.put(key, JSON.stringify(post));

  const indexRaw = await env.MARKET_PULSE.get("index");
  const index = indexRaw ? JSON.parse(indexRaw) : [];
  index.unshift(key);
  await env.MARKET_PULSE.put("index", JSON.stringify(index.slice(0, 60)));
}

function slugify(key) {
  return key.replace("post:", "").replace(/[:.]/g, "-").toLowerCase();
}

function pageShell(title, bodyHtml) {
  return `<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>${title} — Market Pulse — AsliKaam</title>
<link rel="stylesheet" href="/assets/css/style.css">
</head><body>
<nav class="site-nav"><div class="container"><a class="brand" href="/"><span class="dot"></span>AsliKaam</a>
<ul class="nav-links"><li><a href="/blogs/">Blogs</a></li><li><a href="/">Home</a></li></ul></div></nav>
<section class="page-hero"><div class="container">
<div class="eyebrow">⚡ Market Pulse</div>
<h1>${title}</h1>
<p class="lead">A short tip, auto-generated every 6 hours by an open-weight LLM — evergreen advice only, no invented numbers or claims. Not a substitute for the sourced posts in <a href="/blogs/" style="color:var(--accent);">Blogs</a>.</p>
</div></section>
<section class="section-pad-sm"><div class="container">${bodyHtml}</div></section>
</body></html>`;
}

async function renderIndex(env) {
  const indexRaw = await env.MARKET_PULSE.get("index");
  const keys = indexRaw ? JSON.parse(indexRaw) : [];
  if (!keys.length) {
    return new Response(pageShell("Market Pulse", "<p class=\"lead\">First post lands within 6 hours.</p>"), { headers: { "content-type": "text/html;charset=utf-8" } });
  }
  const posts = await Promise.all(keys.slice(0, 20).map(k => env.MARKET_PULSE.get(k)));
  const cards = posts.filter(Boolean).map((raw, i) => {
    const p = JSON.parse(raw);
    const slug = slugify(keys[i]);
    const d = new Date(p.date).toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric" });
    return `<div class="card" style="margin-bottom:16px;"><div style="font-size:0.78rem;color:var(--muted);margin-bottom:8px;">${d}</div>
    <p class="lead" style="margin:0;"><a href="/blogs/market-pulse/${slug}/" style="color:var(--fg);">${p.body.slice(0, 160)}${p.body.length > 160 ? "…" : ""}</a></p></div>`;
  }).join("");
  return new Response(pageShell("Market Pulse", cards), { headers: { "content-type": "text/html;charset=utf-8" } });
}

async function renderPost(env, slug) {
  const indexRaw = await env.MARKET_PULSE.get("index");
  const keys = indexRaw ? JSON.parse(indexRaw) : [];
  const key = keys.find(k => slugify(k) === slug);
  if (!key) return new Response("Not found", { status: 404 });
  const raw = await env.MARKET_PULSE.get(key);
  if (!raw) return new Response("Not found", { status: 404 });
  const p = JSON.parse(raw);
  const d = new Date(p.date).toLocaleDateString("en-IN", { day: "numeric", month: "short", year: "numeric", hour: "2-digit", minute: "2-digit" });
  const html = `<div style="font-size:0.78rem;color:var(--muted);margin-bottom:14px;">${d}</div><p class="lead">${p.body}</p>
  <p style="margin-top:24px;"><a href="/blogs/market-pulse/" style="color:var(--accent);">← All Market Pulse posts</a></p>`;
  return new Response(pageShell(p.topic, html), { headers: { "content-type": "text/html;charset=utf-8" } });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    if (url.pathname === "/blogs/market-pulse/" || url.pathname === "/blogs/market-pulse") {
      return renderIndex(env);
    }
    const m = url.pathname.match(/^\/blogs\/market-pulse\/([a-z0-9-]+)\/?$/);
    if (m) {
      return renderPost(env, m[1]);
    }
    return env.ASSETS.fetch(request);
  },

  async scheduled(event, env, ctx) {
    ctx.waitUntil(generatePost(env));
  },
};
