#!/usr/bin/env python3
"""Generates the AsliKaam V1 static site into ./site/.
Pure static output — no build step required at deploy time, so the
output directory can be uploaded to Cloudflare Pages (or any static host)
as-is. Re-run this script and re-zip whenever data.py or templates below change.
"""
import json
import os
import shutil
from data import (
    BRAND, TAGLINE, NAV, INDUSTRIES, PRICING_PACKS,
    CUSTOM_HAVE, CUSTOM_ADDONS,
    MODULES, INDUSTRY_MODULES, NEGOTIATION_AGENT, BLOG_POSTS, FREE_TOOLS,
)

INDUSTRY_BY_SLUG = {i["slug"]: i for i in INDUSTRIES}
MODULE_BY_ID = {m["id"]: m for m in MODULES}

# A distinct realistic customer name per industry, for chat_screen headers.
CUSTOMER_NAMES = {
    "export-trading": "Michael Chen",
    "hospital": "Sunita Patil",
    "coaching-institute": "Ananya Reddy",
    "real-estate-developer": "Karan Mehta",
    "b2b-manufacturer": "Deepak Agarwal",
    "private-school": "Priya Joshi",
    "diagnostic-lab": "Rajesh Kulkarni",
    "wedding-planner-banquet": "Neha Kapoor",
    "gym-fitness-chain": "Rohit Verma",
    "ca-legal-firm": "Vivek Malhotra",
    "interior-designer": "Kavya Iyer",
    "retail-store": "Ganesh Pawar",
    "automobile-showroom": "Siddharth Rao",
    "building-materials-showroom": "Imran Sheikh",
    "wholesale-distributor": "Manoj Gupta",
}

# For industries whose pain narrative is *already* about a specific discovery
# platform (buried in a portal, not found on Maps, a missed call), the pain
# scene's existing chat copy is reused verbatim as that platform's real
# screen instead of a WhatsApp bubble — no new copy, just the true visual.
DISCOVERY_OVERRIDES = {
    "hospital": {"kind": "search", "query": "hospital near Wakad",
        "results": [
            {"name": "Sanjeevani Multispecialty", "rating": 4.3, "reviews": 260, "distance": "0.9 km", "complete": True},
            {"name": "Your Wakad Branch", "rating": 3.8, "reviews": 6, "distance": "0.5 km", "complete": False},
            {"name": "City Care Hospital", "rating": 4.0, "reviews": 140, "distance": "1.7 km", "complete": True},
        ], "winner_idx": 0},
    "ca-legal-firm": {"kind": "search", "query": "CA near me",
        "results": [
            {"name": "Desai & Associates", "rating": 4.5, "reviews": 88, "distance": "1.0 km", "complete": True},
            {"name": "Your Firm", "rating": 4.0, "reviews": 9, "distance": "0.6 km", "complete": False},
            {"name": "Kulkarni Tax Consultants", "rating": 4.1, "reviews": 52, "distance": "1.4 km", "complete": True},
        ], "winner_idx": 0},
    "export-trading": {"kind": "lead", "source": "IndiaMART", "icon": "📦",
        "from_name": "Michael Chen — Chen Trading Co.", "meta": "Bulk RFQ · 500 units",
        "message": "Hi, interested in your product. Can you share price + sample?", "handled": False},
    "real-estate-developer": {"kind": "lead", "source": "99acres", "icon": "🏢",
        "from_name": "Karan Mehta", "meta": "2BHK enquiry · Ready-to-move",
        "message": "Interested in the 2BHK. Send details?", "handled": False},
    "b2b-manufacturer": {"kind": "lead", "source": "IndiaMART RFQ", "icon": "🏭",
        "from_name": "Deepak Agarwal — Agarwal Traders", "meta": "Urgent · 5000 units",
        "message": "Need a quote for 5000 units, urgent.", "handled": False},
    "private-school": {"kind": "lead", "source": "Phone", "icon": "📞",
        "from_name": "Priya Joshi", "meta": "Missed call ×3 · admission week",
        "message": "Calling about Grade 2 admission...", "handled": False},
    "wedding-planner-banquet": {"kind": "lead", "source": "Instagram DM", "icon": "📸",
        "from_name": "Neha & Arjun Kapoor", "meta": "300 guests · Dec 14",
        "message": "Loved your work! Available for Dec 14 wedding, 300 guests?", "handled": False},
    "building-materials-showroom": {"kind": "lead", "source": "IndiaMART", "icon": "🧱",
        "from_name": "Imran Sheikh — Site Contractor", "meta": "2000 sqft · urgent",
        "message": "Need tile samples + quote for a 2000 sqft site, urgent.", "handled": False},
}


def discovery_visual(slug):
    """Render the discovery-platform override for this industry's pain
    scene, or None if it should stay a plain chat (its pain isn't about
    being found — forcing a search screen there would be off-story)."""
    o = DISCOVERY_OVERRIDES.get(slug)
    if not o:
        return None
    if o["kind"] == "search":
        return search_results_screen(o["query"], o["results"], o["winner_idx"])
    return lead_notification_screen(o["source"], o["icon"], o["from_name"], o["meta"], o["message"], o["handled"])


def tier_label(mod, full=False):
    """Customer-facing classification — Agentic (needs AI judgment) vs
    Non-Agentic (deterministic rules/templates). Deliberately no
    day/week estimates here: those are internal planning numbers, not
    a promise made to a visitor."""
    if mod["agentic"]:
        return "🤖 Agentic Automation" if full else "Agentic"
    return "⚙️ Non-Agentic Automation" if full else "Non-Agentic"

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")
ASSETS_SRC = os.path.join(ROOT, "assets_src")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def write(path, html):
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


def head(title, description, canonical="/"):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:type" content="website">
<link rel="icon" href="data:,">
<link rel="stylesheet" href="/assets/css/style.css">
</head>
<body>
"""


def foot():
    return f"""<footer class="site-footer">
  <div class="container">
    <div>© {BRAND} — {TAGLINE}</div>
  </div>
</footer>
<script src="/assets/js/config.js"></script>
<script src="/assets/js/gsap-loader.js"></script>
<script src="/assets/js/cinematic.js"></script>
<script src="/assets/js/global-ui.js"></script>
<script src="/assets/js/use-case-switcher.js"></script>
<script src="/assets/js/home-rotator.js"></script>
</body>
</html>
"""


def nav(active):
    links = ""
    for label, href in NAV:
        current = ' aria-current="page"' if href == active else ""
        links += f'<li><a href="{href}"{current}>{label}</a></li>'
    wa_href = "https://wa.me/911234567890?text=Hi!%20I'd%20like%20to%20know%20more%20about%20AsliKaam."
    return f"""<nav class="site-nav">
  <div class="container">
    <a class="brand" href="/"><span class="dot"></span>{BRAND}</a>
    <ul class="nav-links">{links}</ul>
    <a class="nav-cta" href="{wa_href}" target="_blank" rel="noopener">WhatsApp Us</a>
  </div>
</nav>
"""


def badge(kind):
    if kind == "proven":
        return '<span class="badge badge-proven">Proven</span>'
    return '<span class="badge badge-proposed">Proposed approach</span>'


def chat_mock(lines):
    out = '<div class="chat-mock">'
    for kind, text in lines:
        out += f'<div class="chat-bubble {kind}">{esc(text)}</div>'
    out += "</div>"
    return out


def chat_screen(contact, status, lines):
    """A chat_mock with a real conversation header — avatar initial, contact
    name, and a live status line (Online / Typing…) — reads as an actual
    open chat, not a floating stack of bubbles."""
    initial = contact[0].upper() if contact else "?"
    return f"""<div class="chat-screen">
      <div class="chat-screen-header">
        <span class="cs-avatar">{esc(initial)}</span>
        <div>
          <div class="cs-name">{esc(contact)}</div>
          <div class="cs-status">{esc(status)}</div>
        </div>
      </div>
      {chat_mock(lines)}
    </div>"""


def search_results_screen(query, results, winner_idx):
    """results: list of {name, rating, reviews, distance, complete: bool}.
    The winner gets tapped/highlighted; incomplete listings read as skipped."""
    cards = ""
    for i, r in enumerate(results):
        is_winner = i == winner_idx
        is_skipped = not r["complete"] and not is_winner
        cls = "result-card"
        if is_winner:
            cls += " is-winner"
        elif is_skipped:
            cls += " is-skipped"
        initial = r["name"][0].upper()
        stars = "★" * round(r["rating"]) + "☆" * (5 - round(r["rating"]))
        tap_badge = '<span class="rc-tap-badge">👆 Tapped</span>' if is_winner else ""
        if r["complete"]:
            tags = '<div class="rc-tags"><span class="rc-tag">Website</span><span class="rc-tag">Posts</span><span class="rc-tag">WhatsApp</span></div>'
        else:
            tags = '<div class="rc-meta rc-missing">No website · no posts · no way to message</div>'
        cards += f"""<div class="{cls}">
          {tap_badge}
          <span class="rc-avatar">{esc(initial)}</span>
          <div class="rc-body">
            <div class="rc-name">{esc(r['name'])}</div>
            <div class="rc-meta">{stars} {r['rating']} ({r['reviews']}) · {esc(r['distance'])}</div>
            {tags}
          </div>
        </div>"""
    return f"""<div class="search-screen">
      <div class="search-bar"><span class="sb-icon">🔍</span> {esc(query)}</div>
      <div class="result-list">{cards}</div>
    </div>"""


def rotating_search_screen(presets, use_fixed):
    """Cycles through several industries' search results every ~2.2s (see
    home-rotator.js) so no single visitor sees only a field that isn't
    theirs — each preset has its own realistic names, not a swapped word."""
    slides = ""
    for i, p in enumerate(presets):
        results = p["fixed"] if use_fixed else p["broken"]
        winner = p["winner_fixed"] if use_fixed else p["winner_broken"]
        hidden_attr = "" if i == 0 else " hidden"
        slides += (f'<div class="rotation-slide" data-rot="{i}"{hidden_attr}>'
                   f'{search_results_screen(p["query"], results, winner)}</div>')
    return f'<div class="rotation-wrap">{slides}</div>'


def lead_notification_screen(source, icon, from_name, meta, message, handled):
    """A platform-native inquiry notification — IndiaMART RFQ, Instagram
    DM, a property portal lead — for industries whose real discovery
    moment isn't a Maps/Search result."""
    cls = "is-handled" if handled else "is-unread"
    status_line = f'<div class="ln-meta" style="margin-top:8px; color:var(--accent); font-weight:700;">✓ Replied</div>' if handled else \
                  f'<div class="ln-meta" style="margin-top:8px; color:var(--danger); font-weight:700;">● Unread</div>'
    return f"""<div class="lead-notif {cls}">
      <div class="ln-source"><span class="ln-icon">{icon}</span> New lead from {esc(source)}</div>
      <div class="ln-card">
        <div class="ln-from">{esc(from_name)}</div>
        <div class="ln-meta">{esc(meta)}</div>
        <div class="ln-message">{esc(message)}</div>
        {status_line}
      </div>
    </div>"""


def payment_screen(business, amount, paid):
    status_cls = "is-paid" if paid else "is-pending"
    status_text = "✓ Paid" if paid else "⏳ Pending"
    btn_text = "Paid via UPI ✓" if paid else "Pay via UPI"
    return f"""<div class="payment-screen {status_cls}">
      <div class="ps-label">Payment request from</div>
      <div class="ps-business">{esc(business)}</div>
      <div class="ps-amount">{esc(amount)}</div>
      <div class="ps-btn">{btn_text}</div>
      <span class="ps-status">{status_text}</span>
    </div>"""


def scene(stage, kind, extra_body="", contact=None, status="Online"):
    """kind: 'chat' for pain/fix stages, 'stat' for growth, or raw html via extra_body.
    Pass contact= to render 'chat' as a real headered chat_screen instead of
    a bare chat_mock — used wherever a customer name adds realism."""
    accent = stage.get("accent", "")
    body = ""
    if kind == "chat":
        body = chat_screen(contact, status, stage["chat"]) if contact else chat_mock(stage["chat"])
    elif kind == "stat":
        body = f"""<div class="stat-panel">
          <div class="stat-row">
            <span class="stat-from">{esc(stage['stat_from'])}</span>
            <span class="stat-arrow">→</span>
            <span class="stat-to">{esc(stage['stat_to'])}</span>
          </div>
          <div class="stat-label">{esc(stage['stat_label'])}</div>
        </div>"""
    else:
        body = extra_body

    return f"""<div class="scene" data-accent="{accent}">
      <div class="container scene-grid">
        <div class="scene-copy">
          <span class="eyebrow">{esc(stage['eyebrow'])}</span>
          <h2>{stage['title']}</h2>
          <p>{esc(stage['body'])}</p>
        </div>
        <div class="scene-visual">{body}</div>
      </div>
    </div>"""


def picker_scene(stage_eyebrow="The Reveal", stage_title="See your own leak, live", stage_body="Pick your industry — the demo adapts to your exact mechanism."):
    chips = ""
    for ind in INDUSTRIES:
        chips += f"""<a class="picker-chip" href="/demos/{ind['slug']}.html">
          <span class="icon">{ind['icon']}</span>{ind['name']}
        </a>"""
    return f"""<div class="scene" data-accent="reveal">
      <div class="container">
        <div class="scene-copy center" style="margin: 0 auto 32px; max-width:640px;">
          <span class="eyebrow">{stage_eyebrow}</span>
          <h2>{stage_title}</h2>
          <p style="margin:0 auto;">{stage_body}</p>
        </div>
        <div class="picker-grid">{chips}</div>
      </div>
    </div>"""


def payoff_scene():
    return f"""<div class="scene" data-accent="payoff">
      <div class="container">
        <div class="scene-copy center" style="margin:0 auto;">
          <span class="eyebrow">The Payoff</span>
          <h2>One fix. Then it compounds.</h2>
          <p style="margin:0 auto 24px;">See the exact mechanism for your industry, then talk to us on WhatsApp.</p>
          <div class="row-cta center" style="justify-content:center;">
            <a class="btn btn-primary" href="/industries/">Explore Industries</a>
            <a class="btn btn-ghost" href="/pricing/">See Pricing</a>
          </div>
        </div>
      </div>
    </div>"""


def cinematic_wrap(scenes_html, n_scenes, extra_class=""):
    dots = "".join('<span class="dot"></span>' for _ in range(n_scenes))
    return f"""<section class="cinematic-wrap {extra_class}">
  <div class="cinematic-pin">
    {''.join(scenes_html)}
  </div>
  <div class="scene-dots">{dots}</div>
  <p class="container fallback-note" style="padding:16px 24px; color:var(--muted); font-size:0.8rem;">Scroll to move through each step.</p>
</section>
"""


# ---------------------------------------------------------------- HOME
def build_home():
    """The full customer journey, framed as four numbered Loss Points —
    search, enquiry, negotiation, payment — each shown broken (red) then
    covered (green) with a real screen, not a narrated placeholder.
    The point: a business can lose the same customer at any one of these
    four steps to a competitor who covers the whole journey."""
    def preset(query, biz, others, biz_row):
        """others: 3 competitor dicts. biz_row: the featured business's
        rating/reviews/distance — it appears incomplete in 'broken' and
        complete in 'fixed', at the same position among the same competitors."""
        def build(complete_biz):
            row = {**biz_row, "name": biz, "complete": complete_biz}
            listing = [others[0], row, others[1], others[2]]
            winner = 0 if not complete_biz else 1
            return listing, winner
        broken, w_broken = build(False)
        fixed, w_fixed = build(True)
        return {"query": query, "broken": broken, "fixed": fixed, "winner_broken": w_broken, "winner_fixed": w_fixed}

    # One preset per industry we actually target (matches data.py's INDUSTRIES
    # order) — every visitor sees their own field flash by within ~30s,
    # not just a handful of generic examples.
    search_presets = [
        preset("garment exporter near Tirupur", "Sri Balaji Exports",  # export-trading
            [{"name": "Tirupur Fashion Exports", "rating": 4.5, "reviews": 180, "distance": "1.4 km", "complete": True},
             {"name": "Classic Knitwear Exports", "rating": 4.1, "reviews": 64, "distance": "2.0 km", "complete": True},
             {"name": "New Era Garments", "rating": 3.6, "reviews": 11, "distance": "1.7 km", "complete": False}],
            {"rating": 3.8, "reviews": 9, "distance": "0.9 km"}),
        preset("multispecialty hospital near Hinjewadi", "Hinjewadi Care Hospital",  # hospital
            [{"name": "Lifeline Multispecialty", "rating": 4.5, "reviews": 420, "distance": "1.1 km", "complete": True},
             {"name": "Sunrise Care Hospital", "rating": 4.2, "reviews": 180, "distance": "2.3 km", "complete": True},
             {"name": "Om Hospital", "rating": 3.5, "reviews": 30, "distance": "1.9 km", "complete": False}],
            {"rating": 3.8, "reviews": 25, "distance": "0.7 km"}),
        preset("NEET coaching near me", "Vidya NEET Academy",  # coaching-institute
            [{"name": "Brilliant Career Institute", "rating": 4.6, "reviews": 260, "distance": "1.0 km", "complete": True},
             {"name": "Pinnacle Coaching Classes", "rating": 4.2, "reviews": 88, "distance": "1.6 km", "complete": True},
             {"name": "Bright Future Classes", "rating": 3.5, "reviews": 12, "distance": "2.1 km", "complete": False}],
            {"rating": 3.9, "reviews": 16, "distance": "0.8 km"}),
        preset("2BHK flats near Baner", "Skyline Residency",  # real-estate-developer
            [{"name": "Horizon Developers", "rating": 4.4, "reviews": 140, "distance": "1.3 km", "complete": True},
             {"name": "Greenfield Properties", "rating": 4.0, "reviews": 70, "distance": "1.9 km", "complete": True},
             {"name": "Om Constructions", "rating": 3.4, "reviews": 10, "distance": "2.2 km", "complete": False}],
            {"rating": 3.7, "reviews": 13, "distance": "0.6 km"}),
        preset("auto parts manufacturer near me", "Precision Auto Components",  # b2b-manufacturer
            [{"name": "Apex Auto Ancillaries", "rating": 4.5, "reviews": 190, "distance": "1.5 km", "complete": True},
             {"name": "Reliable Engineering Works", "rating": 4.1, "reviews": 76, "distance": "2.0 km", "complete": True},
             {"name": "New India Auto Parts", "rating": 3.6, "reviews": 14, "distance": "1.8 km", "complete": False}],
            {"rating": 3.8, "reviews": 11, "distance": "1.0 km"}),
        preset("CBSE school near me", "Bright Minds CBSE School",  # private-school
            [{"name": "Green Valley Public School", "rating": 4.6, "reviews": 310, "distance": "1.2 km", "complete": True},
             {"name": "National Public School", "rating": 4.2, "reviews": 145, "distance": "1.8 km", "complete": True},
             {"name": "Sunrise Public School", "rating": 3.5, "reviews": 22, "distance": "2.0 km", "complete": False}],
            {"rating": 3.9, "reviews": 19, "distance": "0.7 km"}),
        preset("blood test home collection near me", "Wellness Diagnostics",  # diagnostic-lab
            [{"name": "Prime Diagnostic Center", "rating": 4.5, "reviews": 230, "distance": "0.9 km", "complete": True},
             {"name": "Accurate Path Labs", "rating": 4.1, "reviews": 90, "distance": "1.5 km", "complete": True},
             {"name": "City Diagnostic Center", "rating": 3.5, "reviews": 17, "distance": "1.9 km", "complete": False}],
            {"rating": 3.7, "reviews": 15, "distance": "0.5 km"}),
        preset("wedding planner near me", "Forever After Events",  # wedding-planner-banquet
            [{"name": "Celebrations Co.", "rating": 4.8, "reviews": 150, "distance": "1.5 km", "complete": True},
             {"name": "Royal Occasions", "rating": 4.3, "reviews": 75, "distance": "2.0 km", "complete": True},
             {"name": "Starlight Events", "rating": 3.6, "reviews": 9, "distance": "1.3 km", "complete": False}],
            {"rating": 3.9, "reviews": 18, "distance": "0.9 km"}),
        preset("gym near Baner", "Fitzone Gym",  # gym-fitness-chain
            [{"name": "PowerHouse Fitness", "rating": 4.7, "reviews": 340, "distance": "1.0 km", "complete": True},
             {"name": "Iron Paradise", "rating": 4.2, "reviews": 95, "distance": "1.8 km", "complete": True},
             {"name": "City Gym", "rating": 3.4, "reviews": 15, "distance": "2.2 km", "complete": False}],
            {"rating": 4.0, "reviews": 20, "distance": "0.6 km"}),
        preset("income tax consultant near me", "Mehta Tax Consultants",  # ca-legal-firm
            [{"name": "Precision Tax Advisors", "rating": 4.6, "reviews": 120, "distance": "1.1 km", "complete": True},
             {"name": "Trust Tax Consultants", "rating": 4.2, "reviews": 58, "distance": "1.7 km", "complete": True},
             {"name": "Sharma & Co", "rating": 3.6, "reviews": 9, "distance": "1.4 km", "complete": False}],
            {"rating": 3.9, "reviews": 12, "distance": "0.8 km"}),
        preset("interior designer near me", "Casa Interiors",  # interior-designer
            [{"name": "Urban Design Studio", "rating": 4.7, "reviews": 165, "distance": "1.3 km", "complete": True},
             {"name": "Elegant Spaces Interiors", "rating": 4.2, "reviews": 82, "distance": "1.9 km", "complete": True},
             {"name": "Modern Nest Interiors", "rating": 3.5, "reviews": 13, "distance": "2.1 km", "complete": False}],
            {"rating": 3.8, "reviews": 10, "distance": "0.7 km"}),
        preset("grocery store near me", "Patil Kirana",  # retail-store
            [{"name": "Sharma General Store", "rating": 4.4, "reviews": 95, "distance": "0.5 km", "complete": True},
             {"name": "Fresh Mart", "rating": 4.1, "reviews": 60, "distance": "1.0 km", "complete": True},
             {"name": "City Grocers", "rating": 3.6, "reviews": 20, "distance": "1.4 km", "complete": False}],
            {"rating": 3.7, "reviews": 14, "distance": "0.3 km"}),
        preset("car showroom near me", "Deccan Motors",  # automobile-showroom
            [{"name": "City Auto Gallery", "rating": 4.5, "reviews": 210, "distance": "1.4 km", "complete": True},
             {"name": "Premier Car World", "rating": 4.1, "reviews": 88, "distance": "2.0 km", "complete": True},
             {"name": "Highway Auto Hub", "rating": 3.5, "reviews": 16, "distance": "1.8 km", "complete": False}],
            {"rating": 3.8, "reviews": 14, "distance": "0.9 km"}),
        preset("tiles showroom near me", "Shree Tiles Gallery",  # building-materials-showroom
            [{"name": "Elegant Tiles Showroom", "rating": 4.5, "reviews": 175, "distance": "1.2 km", "complete": True},
             {"name": "Classic Ceramics Store", "rating": 4.1, "reviews": 70, "distance": "1.8 km", "complete": True},
             {"name": "New Bharat Sanitaryware", "rating": 3.6, "reviews": 12, "distance": "1.6 km", "complete": False}],
            {"rating": 3.9, "reviews": 11, "distance": "0.6 km"}),
        preset("electrical wholesale distributor near me", "Ganpati Electricals Wholesale",  # wholesale-distributor
            [{"name": "Prime Electrical Distributors", "rating": 4.5, "reviews": 155, "distance": "1.3 km", "complete": True},
             {"name": "City Electric Traders", "rating": 4.1, "reviews": 64, "distance": "1.9 km", "complete": True},
             {"name": "Metro Electrical Supplies", "rating": 3.5, "reviews": 10, "distance": "1.7 km", "complete": False}],
            {"rating": 3.8, "reviews": 13, "distance": "0.8 km"}),
    ]

    scenes = [
        scene({
            "eyebrow": "Loss Point #1 — Search", "title": "Found, but skipped",
            "body": "A thin profile: no photos, no posts, no website. A customer searching nearby scrolls straight past it without a second thought.",
            "accent": "red",
        }, "raw", extra_body=rotating_search_screen(search_presets, use_fixed=False)),
        scene({
            "eyebrow": "Covered", "title": "Same business. Now it's the one that gets tapped.",
            "body": "Photos, posts, a website link, a WhatsApp button — a complete profile is the difference between being found and being chosen.",
            "accent": "green",
        }, "raw", extra_body=rotating_search_screen(search_presets, use_fixed=True)),

        scene({
            "eyebrow": "Loss Point #2 — Enquiry", "title": "The enquiry goes quiet",
            "body": "A real question, waiting. While it waits, the customer is already messaging two other electricians.",
            "chat": [
                ("in", "Hi, do you do electrical panel upgrades?"),
                ("meta", "Seen · no reply · 2 hours"),
            ],
            "accent": "red",
        }, "raw", extra_body=chat_screen("Rohan Sharma", "Last seen 2 hours ago", [
            ("in", "Hi, do you do electrical panel upgrades?"),
            ("meta", "Seen · no reply · 2 hours"),
        ])),
        scene({
            "eyebrow": "Covered", "title": "Instant reply, and the right follow-up",
            "body": "Not just \"thanks for reaching out\" — a question that moves the conversation toward a real quote.",
            "accent": "green",
        }, "raw", extra_body=chat_screen("Rohan Sharma", "Online", [
            ("in", "Hi, do you do electrical panel upgrades?"),
            ("out", "Yes! Could you share your panel's current capacity?"),
            ("in", "It's a 5kW panel, want to upgrade to 8kW."),
        ])),

        scene({
            "eyebrow": "Loss Point #3 — Negotiation", "title": "No quote, no negotiation, no deal",
            "body": "Asked for a price, given a shrug. The customer doesn't wait around for a number.",
            "accent": "red",
        }, "raw", extra_body=chat_screen("Rohan Sharma", "Typing…", [
            ("in", "So what's the cost?"),
            ("meta", "No clear answer given"),
            ("in", "Ok, let me check elsewhere."),
        ])),
        scene({
            "eyebrow": "Covered", "title": "Quoted, matched, and booked — same conversation",
            "body": "A real quote, and when they've got a better offer, it gets matched instead of losing the deal outright.",
            "accent": "green",
        }, "raw", extra_body=chat_screen("Rohan Sharma", "Online", [
            ("out", "Upgrade to 8kW: ₹6,200 all-inclusive, done in a day."),
            ("in", "Got a quote for ₹5,000 elsewhere, can you match?"),
            ("out", "We'll match ₹5,000 — plus a 1-year warranty. Book it?"),
            ("in", "Yes, book it."),
        ])),

        scene({
            "eyebrow": "Loss Point #4 — Payment", "title": "\"I'll pay after the work\" — and then they don't",
            "body": "The job's done. The payment isn't. Now it's three awkward follow-up messages instead of a closed deal.",
            "accent": "red",
        }, "raw", extra_body=chat_screen("Rohan Sharma", "Online", [
            ("in", "I'll just pay you in cash after the work."),
            ("meta", "Work done · payment \"forgotten\" · 3 follow-ups needed"),
        ])),
        scene({
            "eyebrow": "Covered", "title": "A link, paid before the technician leaves",
            "body": "People commit to a payment link faster than they commit out loud — and it's done before anyone has to ask twice.",
            "accent": "green",
        }, "raw", extra_body=payment_screen("Patel Electric Works", "₹5,000", paid=True)),

        picker_scene(
            stage_title="One journey. Every point covered.",
            stage_body="Four places a customer can be lost — search, enquiry, negotiation, payment. Pick your industry to see the exact version of this for your business.",
        ),
        payoff_scene(),
    ]
    body = nav("/") + cinematic_wrap(scenes, len(scenes)) + f"""
<section class="section-pad">
  <div class="container">
    <div class="eyebrow">Why AsliKaam</div>
    <h2>A studio, not a SaaS</h2>
    <p class="lead">Few clients, real work delivered end-to-end — website, Google presence, WhatsApp-driven client handling — built and personally run by us. We tap the money already flowing through your existing website and marketing spend, instead of inventing new demand.</p>
    <div class="row-cta">
      <a class="btn btn-primary" href="/industries/">Find your industry</a>
      <a class="btn btn-ghost" href="/agentic-use-cases/">Can AI actually increase sales?</a>
    </div>
  </div>
</section>
""" + foot()
    write("index.html", head(f"{BRAND} — {TAGLINE}",
        "AsliKaam is the digital partner for MSMEs: website, Google presence, and WhatsApp-driven client handling, built end-to-end.") + body)


# ---------------------------------------------------------------- INDUSTRIES
def build_industries_index():
    cards = ""
    for ind in INDUSTRIES:
        cards += f"""<a class="card industry-card" href="/industries/{ind['slug']}.html">
          <span class="icon" style="font-size:28px;">{ind['icon']}</span>
          {badge(ind['badge'])}
          <h3>{ind['name']}</h3>
          <p>{esc(ind['use_case'])}</p>
          <div class="starts-at">Explore →</div>
        </a>"""
    body = nav("/industries/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Industries</div>
    <h1>{len(INDUSTRIES)} businesses. {len(INDUSTRIES)} exact leaks.</h1>
    <p class="lead">Every page is labeled honestly: {badge('proven')} means a real pilot has run. {badge('proposed')} means it's our diagnosed fix, not yet delivered there.</p>
  </div>
</section>
<section class="section-pad-sm">
  <div class="container">
    <div class="grid grid-3">{cards}</div>
  </div>
</section>
""" + foot()
    write("industries/index.html", head(f"Industries — {BRAND}",
        "Eleven MSME verticals, each with its exact lead-leak mapped and the fix that closes it.", "/industries/") + body)


def use_case_panel(key, pain, fix, visible=False, badge_kind=None, contact=None):
    hidden_attr = "" if visible else " hidden"
    badge_html = f'<div style="margin-bottom:14px;">{badge(badge_kind)}</div>' if badge_kind else ""
    pain_visual = chat_screen(contact, "Seen 2 hrs ago", pain["chat"]) if contact else chat_mock(pain["chat"])
    fix_visual = chat_screen(contact, "Online", fix["chat"]) if contact else chat_mock(fix["chat"])
    return f"""<div class="use-case-panel" data-usecase="{key}"{hidden_attr}>
  {badge_html}
  <div class="grid grid-2" style="align-items:start;">
    <div>
      <span class="eyebrow">Today</span>
      <h3 style="margin-bottom:10px;">{pain['title']}</h3>
      {pain_visual}
    </div>
    <div>
      <span class="eyebrow">With AsliKaam</span>
      <h3 style="margin-bottom:10px;">{fix['title']}</h3>
      {fix_visual}
    </div>
  </div>
</div>"""


def static_preview(ind):
    """A lightweight, non-pinned before/after preview for Industry pages,
    switchable via dropdown between the primary use case and its mapped
    secondary automation modules. The full pinned cinematic sequence
    belongs on the Demos page only — embedding it here too would force a
    ~300vh scroll-jack detour through a mostly-static info page."""
    module_ids = INDUSTRY_MODULES.get(ind["slug"], [])
    contact = CUSTOMER_NAMES.get(ind["slug"], "Customer")
    chips = f'<button type="button" class="use-case-chip is-active" data-usecase="primary">{esc(ind["name"])} — {esc(ind["solution"])}</button>'
    panels = use_case_panel("primary", ind["pain"], ind["fix"], visible=True, contact=contact)
    for mid in module_ids:
        mod = MODULE_BY_ID[mid]
        chips += f'<button type="button" class="use-case-chip" data-usecase="{mid}">{esc(mod["name"])} <span class="chip-tier">{tier_label(mod)}</span></button>'
        panels += use_case_panel(mid, mod["pain"], mod["fix"], badge_kind=mod["badge"], contact=contact)

    if not module_ids:
        return f"""<section class="section-pad-sm">
  <div class="container">{panels}</div>
</section>"""

    return f"""<section class="section-pad-sm">
  <div class="container">
    <div class="eyebrow">See it in action</div>
    <h2>Pick a use case</h2>
    <p class="lead" style="margin-bottom:18px;">Each one has its own working demo — tap to switch. 👇</p>
    <div class="use-case-chip-row" role="tablist" aria-label="Choose a use case to preview">{chips}</div>
    <div class="use-case-panels mt-32">{panels}</div>
  </div>
</section>"""


def industry_citation(ind):
    """External validation — a real, neutral industry report or news
    analysis, never a link to the competing consumer app itself. Only
    rendered where we actually have solid sourcing (see data.py)."""
    c = ind.get("citation")
    if not c:
        return ""
    return f"""<section class="section-pad-sm" style="padding-top:0;">
  <div class="container">
    <div class="card" style="border-left:3px solid var(--accent);">
      <div class="eyebrow">Why this matters right now</div>
      <p class="lead" style="margin:0 0 10px;">{esc(c['stat'])}</p>
      <a href="{c['url']}" target="_blank" rel="noopener" style="font-size:0.85rem; color:var(--accent); font-weight:600;">— {esc(c['source'])} ↗</a>
    </div>
  </div>
</section>"""


def build_industry_page(ind):
    bullets = "".join(f"<li>{esc(b)}</li>" for b in ind["solution_bullets"])
    body = nav("/industries/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Industries / {ind['name']}</div>
    {badge(ind['badge'])}
    <h1 style="margin-top:14px;">{ind['name']}</h1>
    <p class="lead">{esc(ind['use_case'])}</p>
  </div>
</section>

<section class="section-pad-sm">
  <div class="container">
    <h2>Where the lead actually leaks</h2>
    <div class="leak-map">
      <div class="leak-node"><h4>Inquiry comes in</h4><p>Customer reaches out, ready to buy.</p></div>
      <span class="leak-arrow">→</span>
      <div class="leak-node leak-point"><h4>{esc(ind['leak_label'])}</h4><p>This is the exact point it's lost today.</p></div>
      <span class="leak-arrow">→</span>
      <div class="leak-node"><h4>Lost to a competitor</h4><p>The customer buys somewhere else.</p></div>
    </div>
  </div>
</section>

{industry_citation(ind)}

{static_preview(ind)}

<section class="section-pad">
  <div class="container">
    <div class="grid grid-2" style="align-items:start;">
      <div>
        <h2>Our solution</h2>
        <p class="lead">{esc(ind['solution'])}</p>
        <ul class="stack" style="list-style:none; padding:0;">{bullets}</ul>
      </div>
      <div class="card">
        <div class="eyebrow">Ready to see it live?</div>
        <p class="lead" style="margin:10px 0 20px;">Watch the full mechanism in action, or head straight to pricing.</p>
        <div class="stack">
          <a class="btn btn-primary btn-block" href="/demos/{ind['slug']}.html">Watch the full demo</a>
          <a class="btn btn-ghost btn-block" href="/pricing/">See pricing</a>
        </div>
      </div>
    </div>
  </div>
</section>
""" + foot()
    write(f"industries/{ind['slug']}.html", head(f"{ind['name']} — {BRAND}",
        ind["use_case"], f"/industries/{ind['slug']}.html") + body)


# ---------------------------------------------------------------- DEMOS
def build_demos_index():
    all_slugs = " ".join(i["slug"] for i in INDUSTRIES)
    na_search = esc(f"{NEGOTIATION_AGENT['name']} {NEGOTIATION_AGENT['blurb']} negotiation price match".lower())
    cards = f"""<a class="card industry-card demo-card" href="/demos/module-{NEGOTIATION_AGENT['id']}.html"
         data-search="{na_search}" data-industries="{all_slugs}">
      <span class="icon" style="font-size:28px;">🏆</span>
      <h3>{esc(NEGOTIATION_AGENT['name'])} <span class="badge badge-proposed" style="font-size:0.65rem;">Flagship</span></h3>
      <p>{esc(NEGOTIATION_AGENT['blurb'])}</p>
      <div class="starts-at effort-tag">🤖 Agentic</div>
    </a>"""
    for ind in INDUSTRIES:
        search_text = esc(f"{ind['name']} {ind['leak_label']} {ind['use_case']}".lower())
        cards += f"""<a class="card industry-card demo-card" href="/demos/{ind['slug']}.html"
             data-search="{search_text}" data-industries="{ind['slug']}">
          <span class="icon" style="font-size:28px;">{ind['icon']}</span>
          <h3>{ind['name']}</h3>
          <p>{esc(ind['use_case'])}</p>
          <div class="starts-at">Watch the fix →</div>
        </a>"""
    for mod in MODULES:
        search_text = esc(f"{mod['name']} {mod['blurb']}".lower())
        cards += f"""<a class="card industry-card demo-card" href="/demos/module-{mod['id']}.html"
             data-search="{search_text}" data-industries="{' '.join(mod['industries'])}">
          <span class="icon" style="font-size:28px;">{'🤖' if mod['agentic'] else '⚙️'}</span>
          <h3>{esc(mod['name'])}</h3>
          <p>{esc(mod['blurb'])}</p>
          <div class="starts-at effort-tag">{tier_label(mod)}</div>
        </a>"""

    filter_chips = '<button class="demos-filter-chip is-active" data-slug="">All</button>'
    for ind in INDUSTRIES:
        filter_chips += f'<button class="demos-filter-chip" data-slug="{ind["slug"]}">{ind["icon"]} {ind["name"]}</button>'

    body = nav("/demos/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Demos</div>
    <h1>See the exact mechanism, live</h1>
    <p class="lead">The same cinematic scroll from the homepage, run all the way through — one per industry, plus every reusable automation module.</p>
  </div>
</section>
<section class="section-pad-sm">
  <div class="container">
    <div class="demos-toolbar">
      <input type="text" class="demos-search" id="demos-search" placeholder="Search demos… e.g. invoice, booking, kirana">
      <div class="demos-filters" id="demos-filters">{filter_chips}</div>
    </div>
    <div class="grid grid-3" id="demos-grid">{cards}</div>
  </div>
</section>
""" + foot()
    write("demos/index.html", head(f"Demos — {BRAND}",
        "Standalone interactive demos — one per industry plus every automation module, each showing the exact fix in action.", "/demos/") + body)
    global DEMOS_FILTER_NEEDED
    DEMOS_FILTER_NEEDED = True


def build_demo_page(ind):
    contact = CUSTOMER_NAMES.get(ind["slug"], "Customer")
    pain_override = discovery_visual(ind["slug"])
    pain_scene = scene(ind["pain"], "raw", extra_body=pain_override) if pain_override \
        else scene(ind["pain"], "chat", contact=contact, status="Seen 2 hrs ago")
    scenes = [
        pain_scene,
        scene(ind["fix"], "chat", contact=contact, status="Online"),
        scene(ind["growth"], "stat"),
        payoff_scene(),
    ]
    body = nav("/demos/") + f"""
<section class="page-hero section-pad-sm">
  <div class="container">
    <div class="eyebrow">Demo / {ind['name']}</div>
    <h1>{ind['name']}: the fix, end to end</h1>
    <p class="lead">{esc(ind['use_case'])}</p>
  </div>
</section>
{cinematic_wrap(scenes, len(scenes))}
<section class="section-pad-sm">
  <div class="container center">
    <a class="btn btn-primary" href="/industries/{ind['slug']}.html">Read the full breakdown</a>
  </div>
</section>
""" + foot()
    write(f"demos/{ind['slug']}.html", head(f"{ind['name']} Demo — {BRAND}",
        f"Live demo: {ind['use_case']}", f"/demos/{ind['slug']}.html") + body)


def deployment_modes_section():
    """Not AI-or-nothing: three ways to actually run the negotiation flow,
    from zero-AI button flow to fully autonomous within set limits."""
    modes = [
        ("⚙️", "Pre-set Only", "A fixed button/quick-reply flow — \"Yes, book\" / \"Need a different price\" / \"Just browsing.\" No AI, no open-ended negotiation. Cheapest and fastest to ship."),
        ("🔔", "Hybrid — Alert Me", "Pre-set replies handle the everyday questions. The moment a customer pushes on price or names a competitor, you get a WhatsApp alert — \"Serious customer, wants to negotiate\" — and decide whether to step in or let the agent proceed."),
        ("🤖", "Full Agentic", "The agent handles the whole negotiation on its own, matching within the price limits you set in advance — no owner involvement unless it's outside those limits."),
    ]
    cards = "".join(f"""<div class="card">
      <div style="font-size:1.6rem;">{icon}</div>
      <h3 style="margin:8px 0 6px;">{name}</h3>
      <p class="lead" style="font-size:0.88rem;">{esc(desc)}</p>
    </div>""" for icon, name, desc in modes)
    return f"""<section class="section-pad-sm">
  <div class="container">
    <div class="eyebrow">Not AI-or-nothing</div>
    <h2>Three ways to run this</h2>
    <p class="lead">Agentic AI costs very little to run (a few paise to a rupee or two per conversation on an efficient model) — the real reason to pick a lighter mode isn't cost, it's control. Choose per client.</p>
    <div class="grid grid-3 mt-32">{cards}</div>
  </div>
</section>"""


def build_negotiation_agent_demo():
    """The flagship story: independent narrative scenes (not a pain/fix
    pair), each using a real screen — search results, a headered chat,
    or a payment sheet — matched to what's actually happening at that step."""
    scenes = []
    for stage in NEGOTIATION_AGENT["stages"]:
        k = stage["kind"]
        if k == "search":
            scenes.append(scene(stage, "raw", extra_body=search_results_screen(
                stage["query"], stage["results"], stage["winner_idx"])))
        elif k == "chat_screen":
            scenes.append(scene(stage, "raw", extra_body=chat_screen(
                stage["contact"], stage["status"], stage["chat"])))
        elif k == "payment":
            scenes.append(scene(stage, "raw", extra_body=payment_screen(
                stage["business"], stage["amount"], stage["paid"])))
        else:
            scenes.append(scene(stage, "stat"))
    scenes.append(payoff_scene())
    body = nav("/demos/") + f"""
<section class="page-hero section-pad-sm">
  <div class="container">
    <div class="eyebrow">Flagship Demo</div>
    {badge(NEGOTIATION_AGENT["badge"])}
    <h1 style="margin-top:14px;">{esc(NEGOTIATION_AGENT['name'])}</h1>
    <p class="lead">{esc(NEGOTIATION_AGENT['blurb'])}</p>
  </div>
</section>
{cinematic_wrap(scenes, len(scenes))}
{deployment_modes_section()}
<section class="section-pad-sm">
  <div class="container center">
    <a class="btn btn-primary" href="/pricing/">Add this to a Custom Pack</a>
  </div>
</section>
""" + foot()
    write(f"demos/module-{NEGOTIATION_AGENT['id']}.html", head(f"{NEGOTIATION_AGENT['name']} — {BRAND}",
        NEGOTIATION_AGENT["blurb"], f"/demos/module-{NEGOTIATION_AGENT['id']}.html") + body)


MODULE_CONTACT_NAMES = [
    "Anjali Desai", "Farhan Khan", "Meera Nair", "Tarun Bhatia", "Ritu Singh",
    "Aditya Kulkarni", "Pooja Iyer", "Nikhil Shah", "Simran Kaur", "Rahul Menon",
    "Divya Pillai", "Aman Verma", "Sneha Rao", "Kunal Joshi", "Ishita Bose",
]


def build_module_demo_page(mod):
    idx = next((i for i, m in enumerate(MODULES) if m["id"] == mod["id"]), 0)
    contact = MODULE_CONTACT_NAMES[idx % len(MODULE_CONTACT_NAMES)]
    scenes = [
        scene(mod["pain"], "chat", contact=contact, status="Seen 2 hrs ago"),
        scene(mod["fix"], "chat", contact=contact, status="Online"),
        scene(mod["growth"], "stat"),
        payoff_scene(),
    ]
    applicable = ", ".join(INDUSTRY_BY_SLUG[s]["name"] for s in mod["industries"] if s in INDUSTRY_BY_SLUG)
    body = nav("/demos/") + f"""
<section class="page-hero section-pad-sm">
  <div class="container">
    <div class="eyebrow">Demo / Automation Module</div>
    {badge(mod["badge"])}
    <h1 style="margin-top:14px;">{esc(mod['name'])}</h1>
    <p class="lead">{esc(mod['blurb'])}</p>
    <p class="lead" style="font-size:0.9rem;"><b>{tier_label(mod, full=True)}</b> · Works for: {esc(applicable)}</p>
  </div>
</section>
{cinematic_wrap(scenes, len(scenes))}
<section class="section-pad-sm">
  <div class="container center">
    <a class="btn btn-primary" href="/pricing/">Add this to a Custom Pack</a>
  </div>
</section>
""" + foot()
    write(f"demos/module-{mod['id']}.html", head(f"{mod['name']} Demo — {BRAND}",
        mod["blurb"], f"/demos/module-{mod['id']}.html") + body)


# ---------------------------------------------------------------- PRICING
def build_pricing():
    packs_html = ""
    for p in PRICING_PACKS:
        items = "".join(f"<li>{esc(i)}</li>" for i in p["includes"])
        packs_html += f"""<div class="card price-card">
          <span class="tag">{p['tag']}</span>
          <h3>{p['name']}</h3>
          <div class="price">{p['price']}</div>
          <ul>{items}</ul>
        </div>"""

    def checklist(group, items):
        out = '<div class="check-list">'
        for item in items:
            out += f"""<label class="check-item">
              <input type="checkbox" data-label="{esc(item)}" data-group="{group}">
              {esc(item)}
            </label>"""
        out += "</div>"
        return out

    def module_checklist():
        out = '<div class="check-list">'
        for mod in MODULES:
            out += f"""<label class="check-item">
              <input type="checkbox" data-label="{esc(mod['name'])}" data-group="modules" data-module-id="{mod['id']}">
              {esc(mod['name'])} <span style="color:var(--muted); font-size:0.78rem;">({tier_label(mod)})</span>
            </label>"""
        out += "</div>"
        return out

    industry_chips = ""
    for ind in INDUSTRIES:
        industry_chips += f'<button type="button" class="use-case-chip" data-slug="{ind["slug"]}" data-name="{esc(ind["name"])}">{ind["icon"]} {ind["name"]}</button>'
    industry_modules_json = json.dumps(INDUSTRY_MODULES)

    body = nav("/pricing/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Pricing</div>
    <h1>Four packs. One honest starting price.</h1>
    <p class="lead">Go Digital starts real work moving at ₹2,999/mo. Growth and Expansion scale with you — quoted once we know what you already have.</p>
  </div>
</section>

<section class="section-pad-sm">
  <div class="container"><div class="grid grid-3">{packs_html}</div></div>
</section>

<section class="section-pad">
  <div class="container">
    <div class="eyebrow">Custom Pack</div>
    <h2>Build exactly what you need</h2>
    <p class="lead">Tick what applies — we'll turn it into a WhatsApp message so a real person quotes it, no invented numbers.</p>

    <form id="configurator-form" class="configurator mt-32">
      <div>
        <div class="config-group">
          <h4>Your Industry <span style="color:var(--muted); font-weight:400; text-transform:none; letter-spacing:0;">(optional — tap one)</span></h4>
          <div class="use-case-chip-row" id="config-industry" role="group" aria-label="Choose your industry">{industry_chips}</div>
          <p id="config-recommended" class="lead" style="font-size:0.85rem; margin-top:10px;"></p>
        </div>
        <div class="config-group">
          <h4>Core Modules</h4>
          {module_checklist()}
        </div>
        <div class="config-group">
          <h4>Already Have This?</h4>
          {checklist('have', CUSTOM_HAVE)}
        </div>
        <div class="config-group">
          <h4>Add-ons</h4>
          {checklist('addons', CUSTOM_ADDONS)}
        </div>
      </div>
      <div class="card config-summary">
        <h4 style="margin-top:0;">Your selection</h4>
        <ul id="config-summary-list"><li class="empty">Nothing selected yet.</li></ul>
        <a id="config-wa-cta" class="btn btn-primary btn-block" href="#" target="_blank" rel="noopener">Send Enquiry on WhatsApp</a>
      </div>
    </form>
    <script type="application/json" id="industry-modules-data">{industry_modules_json}</script>
  </div>
</section>
""" + foot()
    write("pricing/index.html", head(f"Pricing — {BRAND}",
        "Go Digital, Growth, Expansion, or a Custom Pack — build your own quote in one WhatsApp message.", "/pricing/") + body)
    # configurator script only needed on this page
    global PRICING_SCRIPT_NEEDED
    PRICING_SCRIPT_NEEDED = True


# ---------------------------------------------------------------- AGENTIC USE CASES
def build_agentic():
    non_agentic = [m for m in MODULES if not m["agentic"]]
    agentic = [m for m in MODULES if m["agentic"]]

    def module_card(mod):
        applicable = ", ".join(INDUSTRY_BY_SLUG[s]["name"] for s in mod["industries"][:4] if s in INDUSTRY_BY_SLUG)
        more = len(mod["industries"]) - 4
        if more > 0:
            applicable += f" +{more} more"
        return f"""<div class="card industry-card">
          {badge(mod['badge'])}
          <h3 style="margin-top:10px;">{esc(mod['name'])}</h3>
          <p>{esc(mod['blurb'])}</p>
          <p style="font-size:0.78rem; color:var(--muted); margin:0;">Works well for: {esc(applicable)}</p>
          <div class="starts-at effort-tag">{tier_label(mod, full=True)}</div>
          <div class="stack" style="margin-top:8px;">
            <a class="btn btn-ghost btn-block" href="/demos/module-{mod['id']}.html">Watch the demo</a>
          </div>
        </div>"""

    non_agentic_cards = "".join(module_card(m) for m in non_agentic)
    agentic_cards = "".join(module_card(m) for m in agentic)
    na = NEGOTIATION_AGENT
    na_applicable_count = len(INDUSTRIES)

    body = nav("/agentic-use-cases/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Agentic Use Cases</div>
    <h1>Can AI actually increase your sales?</h1>
    <p class="lead">Short answer: sometimes, and only for specific, well-defined jobs — never as a blanket replacement for the work. Here's exactly what we can automate, how fast, and for whom — no invented prices, just what it actually is and how long it actually takes.</p>
  </div>
</section>

<section class="section-pad-sm">
  <div class="container">
    <div class="card" style="border: 1px solid var(--accent-dim); background: linear-gradient(180deg, rgba(37,211,102,0.06), transparent);">
      <div class="eyebrow">🏆 The Flagship Play</div>
      {badge(na["badge"])}
      <h2 style="margin-top:10px;">{esc(na['name'])}</h2>
      <p class="lead">{esc(na['blurb'])}</p>
      <p style="font-size:0.85rem; color:var(--muted);">This is how a business actually increases sales — not more traffic, but winning more of the inquiries it's already getting, works for all {na_applicable_count} industries.</p>
      <p style="font-size:0.8rem; color:var(--muted);">🔔 Not AI-or-nothing — this can run pre-set only, hybrid (alerts you for serious customers), or fully agentic. <a href="/demos/module-{na['id']}.html" style="color:var(--accent); font-weight:600;">See all three →</a></p>
      <div class="row-cta">
        <a class="btn btn-primary" href="/demos/module-{na['id']}.html">Watch the full story</a>
      </div>
    </div>
  </div>
</section>

<section class="section-pad-sm">
  <div class="container">
    <div class="eyebrow">⚙️ Non-Agentic Automations</div>
    <h2>Simple, reliable, rule-based</h2>
    <p class="lead">No AI judgment involved — a trigger fires, a template goes out. Deterministic and easy to trust, adapted from proven patterns rather than built from scratch.</p>
    <div class="grid grid-3 mt-32">{non_agentic_cards}</div>
  </div>
</section>

<section class="section-pad-sm">
  <div class="container">
    <div class="eyebrow">🤖 Agentic Automations</div>
    <h2>Where it actually needs to think</h2>
    <p class="lead">Scoring a lead, drafting a reply, matching a price — these need real judgment, not just a trigger. Still no bespoke integrations; each one stands on its own.</p>
    <div class="grid grid-3 mt-32">{agentic_cards}</div>
  </div>
</section>

<section class="section-pad">
  <div class="container">
    <h2>Where we draw the line</h2>
    <p class="lead">Every claim on this site follows one rule: labeled Proven only where a real pilot has actually run, Proposed approach everywhere else. A highly bespoke, trust-driven close — a six-figure B2B contract, a wedding booking — is still human-run, and we're not pretending otherwise. Routine price-matching within limits you set beforehand isn't; that's exactly what the negotiation agent above does, nothing more.</p>
    <div class="row-cta">
      <a class="btn btn-primary" href="/pricing/">Build a Custom Pack</a>
      <a class="btn btn-ghost" href="/industries/">See the mechanism, by industry</a>
    </div>
  </div>
</section>
""" + foot()
    write("agentic-use-cases/index.html", head(f"Agentic Use Cases — {BRAND}",
        "Can AI actually increase your sales? Non-Agentic and Agentic automations, honestly scoped — no invented prices.", "/agentic-use-cases/") + body)


# ---------------------------------------------------------------- BLOGS
def render_blog_block(block):
    if block["type"] == "h2":
        return f"<h2>{esc(block['text'])}</h2>"
    if block["type"] == "p":
        return f"<p>{esc(block['text'])}</p>"
    if block["type"] == "stat":
        return f"""<div class="blog-citation">
          <p>{esc(block['stat'])}</p>
          <a href="{block['url']}" target="_blank" rel="noopener">— {esc(block['source'])} ↗</a>
        </div>"""
    return ""


def build_blogs_index():
    cards = ""
    for post in BLOG_POSTS:
        cards += f"""<a class="card blog-card" href="/blogs/{post['slug']}.html">
          <div class="blog-meta"><span>{esc(post['tag'])}</span><span>·</span><span>{esc(post['read_time'])}</span></div>
          <h3>{esc(post['title'])}</h3>
          <p>{esc(post['dek'])}</p>
        </a>"""
    body = nav("/blogs/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Blogs</div>
    <h1>What's actually happening to businesses like yours</h1>
    <p class="lead">Real reports, real numbers — MSME closures, export share, quick-commerce impact — not filler. {len(BLOG_POSTS)} posts live now; the full 6-per-industry library lands in V2.</p>
  </div>
</section>
<section class="section-pad-sm">
  <div class="container"><div class="grid grid-2">{cards}</div></div>
</section>
""" + foot()
    write("blogs/index.html", head(f"Blogs — {BRAND}",
        "Real, sourced reporting on why Indian businesses are losing customers online — MSME closures, export data, quick-commerce impact.", "/blogs/") + body)


def build_blog_post_page(post):
    blocks = "".join(render_blog_block(b) for b in post["body"])
    related = INDUSTRY_BY_SLUG.get(post["related_industry"]) if post.get("related_industry") else None
    cta = f"""<div class="row-cta center" style="justify-content:center;">
      <a class="btn btn-primary" href="/industries/{related['slug']}.html">See the {esc(related['name'])} fix</a>
      <a class="btn btn-ghost" href="/blogs/">More Blogs</a>
    </div>""" if related else """<div class="row-cta center" style="justify-content:center;">
      <a class="btn btn-primary" href="/industries/">Explore Industries</a>
      <a class="btn btn-ghost" href="/blogs/">More Blogs</a>
    </div>"""
    body = nav("/blogs/") + f"""
<section class="page-hero section-pad-sm">
  <div class="container blog-article">
    <div class="blog-meta" style="justify-content:flex-start;">
      <span class="badge badge-proposed">{esc(post['tag'])}</span>
      <span>{esc(post['read_time'])}</span>
    </div>
    <h1 style="margin-top:14px;">{esc(post['title'])}</h1>
    <p class="lead">{esc(post['dek'])}</p>
  </div>
</section>
<section class="section-pad-sm">
  <div class="container blog-article">
    {blocks}
  </div>
</section>
<section class="section-pad">
  <div class="container">{cta}</div>
</section>
""" + foot()
    write(f"blogs/{post['slug']}.html", head(f"{post['title']} — {BRAND}", post["dek"], f"/blogs/{post['slug']}.html") + body)


# ---------------------------------------------------------------- FREE TOOLS
def build_free_tools_index():
    cards = ""
    for tool in FREE_TOOLS:
        ind = INDUSTRY_BY_SLUG.get(tool["industry"])
        tag = ind["name"] if ind else ""
        cards += f"""<a class="card tool-card" href="/free-tools/{tool['slug']}.html">
          <div class="blog-meta"><span>{esc(tag)}</span></div>
          <h3>{esc(tool['title'])}</h3>
          <p style="color:var(--muted); font-size:0.9rem;">{esc(tool['tagline'])}</p>
        </a>"""
    body = nav("/free-tools/") + f"""
<section class="page-hero">
  <div class="container">
    <div class="eyebrow">Free Tools</div>
    <h1>{len(FREE_TOOLS)} calculators, one per industry</h1>
    <p class="lead">Real, working numbers — no signup, no email gate. Built to be useful on their own, and to show the exact kind of math each industry's automation actually runs on.</p>
  </div>
</section>
<section class="section-pad-sm">
  <div class="container"><div class="grid grid-3">{cards}</div></div>
</section>
""" + foot()
    write("free-tools/index.html", head(f"Free Tools — {BRAND}",
        f"{len(FREE_TOOLS)} free calculators for Indian MSMEs — EMI, income tax, landed cost, quote margin, and more.", "/free-tools/") + body)


def build_free_tool_page(tool):
    ind = INDUSTRY_BY_SLUG.get(tool["industry"])
    fields_html = ""
    for f in tool["fields"]:
        fields_html += f"""<div class="tool-field">
          <label for="f-{f['id']}">{esc(f['label'])}</label>
          <input type="number" id="f-{f['id']}" data-id="{f['id']}" value="{f['default']}" step="{f['step']}">
        </div>"""
    related_link = f'<a class="btn btn-ghost" href="/industries/{ind["slug"]}.html">See the {esc(ind["name"])} fix</a>' if ind else ""
    body = nav("/free-tools/") + f"""
<section class="page-hero section-pad-sm">
  <div class="container">
    <div class="eyebrow">Free Tool{f' / {esc(ind["name"])}' if ind else ''}</div>
    <h1>{esc(tool['title'])}</h1>
    <p class="lead">{esc(tool['tagline'])}</p>
  </div>
</section>
<section class="section-pad-sm">
  <div class="container">
    <div class="tool-layout">
      <form id="tool-form" class="tool-form">{fields_html}</form>
      <div class="tool-result">
        <h4>Result</h4>
        <div id="tool-result-body"></div>
      </div>
    </div>
    <div class="row-cta">
      {related_link}
      <a class="btn btn-primary" href="/free-tools/">More Free Tools</a>
    </div>
  </div>
</section>
<script>{tool['compute_js']}</script>
<script src="/assets/js/free-tools-runtime.js"></script>
""" + foot()
    write(f"free-tools/{tool['slug']}.html", head(f"{tool['title']} — {BRAND}", tool["tagline"], f"/free-tools/{tool['slug']}.html") + body)


# ---------------------------------------------------------------- STUBS (V2)
def build_coming_soon(path, active, title, blurb, nav_label):
    body = nav(active) + f"""
<section class="coming-soon">
  <div class="container">
    <span class="badge badge-proposed">Coming in V2</span>
    <h1>{title}</h1>
    <p class="lead" style="margin:0 auto;">{blurb}</p>
    <div class="row-cta center" style="justify-content:center;">
      <a class="btn btn-primary" href="/industries/">Explore Industries</a>
      <a class="btn btn-ghost" href="/">Back Home</a>
    </div>
  </div>
</section>
""" + foot()
    write(path, head(f"{nav_label} — {BRAND}", blurb, active) + body)


# ---------------------------------------------------------------- misc
def build_404():
    body = nav("") + """
<section class="coming-soon">
  <div class="container">
    <h1>404 — Page not found</h1>
    <p class="lead" style="margin:0 auto;">That page doesn't exist yet.</p>
    <div class="row-cta center" style="justify-content:center;">
      <a class="btn btn-primary" href="/">Back Home</a>
    </div>
  </div>
</section>
""" + foot()
    write("404.html", head(f"404 — {BRAND}", "Page not found") + body)


def build_headers_and_redirects():
    # Cloudflare Pages picks these up automatically from the output root.
    headers = """/assets/*
  Cache-Control: public, max-age=31536000, immutable

/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
"""
    write("_headers", headers)


def inject_pricing_script():
    path = os.path.join(SITE, "pricing", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace(
        '<script src="/assets/js/global-ui.js"></script>',
        '<script src="/assets/js/global-ui.js"></script>\n<script src="/assets/js/pricing-configurator.js"></script>',
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def inject_demos_filter_script():
    path = os.path.join(SITE, "demos", "index.html")
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()
    html = html.replace(
        '<script src="/assets/js/global-ui.js"></script>',
        '<script src="/assets/js/global-ui.js"></script>\n<script src="/assets/js/demos-filter.js"></script>',
    )
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    if os.path.exists(SITE):
        shutil.rmtree(SITE)
    os.makedirs(SITE)
    shutil.copytree(ASSETS_SRC, os.path.join(SITE, "assets"))

    build_home()
    build_industries_index()
    for ind in INDUSTRIES:
        build_industry_page(ind)
    build_demos_index()
    inject_demos_filter_script()
    for ind in INDUSTRIES:
        build_demo_page(ind)
    for mod in MODULES:
        build_module_demo_page(mod)
    build_negotiation_agent_demo()
    build_pricing()
    inject_pricing_script()
    build_agentic()
    build_blogs_index()
    for post in BLOG_POSTS:
        build_blog_post_page(post)
    build_free_tools_index()
    for tool in FREE_TOOLS:
        build_free_tool_page(tool)
    build_404()
    build_headers_and_redirects()

    print(f"Built site into {SITE}")


if __name__ == "__main__":
    main()
