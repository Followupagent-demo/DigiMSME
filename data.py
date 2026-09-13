# AsliKaam V1 — industry content data
# Every entry defaults to "proposed" per the honesty rule (no delivered pilot on record yet).
# Flip an entry's "badge" to "proven" once a real pilot has actually run in that vertical.

BRAND = "AsliKaam"
TAGLINE = "Digital Partner of MSMEs Automation"
TAGLINE_HI = "MSMEs के ऑटोमेशन के लिए डिजिटल पार्टनर"
WHATSAPP_NUMBER = "911234567890"  # TODO: replace with the real WhatsApp Business number before launch
PHONE_NUMBER = "+91 12345 67890"  # TODO: replace with the real business line before launch
SITE_URL = "https://tiny-sky-5603.innndemolog.workers.dev"  # real deployed domain — used for sitemap.xml, robots.txt, and JSON-LD (absolute URLs are required for these, unlike the rest of the site which uses relative links). Update this again if a custom domain is ever attached.

NAV = [
    ("Home", "/"),
    ("Industries", "/industries/"),
    ("Blogs", "/blogs/"),
    ("Demos", "/demos/"),
    ("Agentic Use Cases", "/agentic-use-cases/"),
    ("Free Tools", "/free-tools/"),
    ("Pricing", "/pricing/"),
]

# Hindi nav labels — same href list/order as NAV. Only Home and Industries
# currently have a real /hi/ page (see HI_AVAILABLE_PATHS in build.py); the
# rest still point at their English page until translated, so the label is
# Hindi but the destination isn't yet — full-site coverage lands incrementally.
NAV_HI = [
    ("होम", "/"),
    ("इंडस्ट्रीज़", "/industries/"),
    ("ब्लॉग", "/blogs/"),
    ("डेमो", "/demos/"),
    ("एजेंटिक यूज़ केस", "/agentic-use-cases/"),
    ("फ्री टूल्स", "/free-tools/"),
    ("प्राइसिंग", "/pricing/"),
]

INDUSTRIES = [
    {
        "slug": "export-trading",
        "name": "Export / Trading",
        "icon": "🚢",
        "badge": "proposed",
        "use_case": "A buyer messages for price and sample. No reply for 2 days. They move on to the next supplier in the search results.",
        "name_hi": "एक्सपोर्ट / ट्रेडिंग",
        "use_case_hi": "एक खरीदार कीमत और सैंपल के लिए मैसेज करता है। 2 दिन तक कोई जवाब नहीं मिलता। वह सर्च रिज़ल्ट में अगले सप्लायर के पास चला जाता है।",
        "solution": "Catalog + WhatsApp RFQ routing, same-day quote",
        "solution_bullets": [
            "Product catalog with landed-cost-ready specs, always live",
            "Every inquiry auto-routed to WhatsApp with the right person tagged",
            "Quote templates so a same-day reply is the default, not the exception",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "RFQ sits unread for 2 days",
        "citation": {
            "stat": "India's share of global apparel, textile, leather and footwear exports slipped from a 2013 peak of 4.5% to 3.5% by 2022, as Bangladesh (5.1%) and Vietnam (5.9%) pulled ahead — a gap the World Bank links partly to lower digital adoption in these sectors.",
            "source": "Deccan Herald, citing World Bank",
            "url": "https://www.deccanherald.com/amp/story/business%2Feconomy%2Findia-losing-to-smaller-rivals-like-bangladesh-and-vietnam-in-manufacturing-world-bank-says-3176072",
        },
        "pain": {
            "eyebrow": "The Moment",
            "title": "“Price + sample, please.”",
            "body": "A genuine buyer inquiry lands in the inbox. Nobody's watching it today.",
            "chat": [
                ("in", "Hi, interested in your product. Can you share price + sample?"),
                ("meta", "Seen · 2 days ago"),
                ("in", "Following up — found another supplier, thanks anyway."),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Same inquiry, same day",
            "body": "The RFQ is routed straight to WhatsApp the moment it lands, with a quote template ready to go.",
            "chat": [
                ("in", "Hi, interested in your product. Can you share price + sample?"),
                ("out", "Thanks for reaching out! Here's our catalog + a quote for your quantity 👇"),
                ("out", "Sample dispatch confirmed — tracking shared shortly."),
                ("meta", "PO confirmed · ₹4,20,000 order — would've gone to another supplier"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "One fast reply, compounding",
            "body": "Same-day response rate turns cold leads into repeat buyers across every inquiry channel.",
            "stat_label": "Quote turnaround",
            "stat_from": "4 days",
            "stat_to": "Same day",
        },
    },
    {
        "slug": "hospital",
        "name": "Hospital (multi-branch)",
        "icon": "🏥",
        "badge": "proposed",
        "use_case": "A new branch opens. Zero walk-ins. It's invisible on Google Search and Maps.",
        "name_hi": "हॉस्पिटल (मल्टी-ब्रांच)",
        "use_case_hi": "एक नई ब्रांच खुलती है। कोई वॉक-इन नहीं। गूगल सर्च और मैप्स पर यह दिखती ही नहीं।",
        "solution": "Per-branch GBP + doctor pages + WhatsApp appointments",
        "solution_bullets": [
            "A dedicated Google Business Profile for every branch, not just HQ",
            "Individual doctor pages so patients can find and pick by specialty",
            "WhatsApp appointment booking with automatic confirmations",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "New branch invisible on Google",
        "citation": {
            "stat": "Insured patients are increasingly choosing corporate hospitals for standardized, cashless care — a shift KPMG says is driving standalone and single-region hospitals to fold into larger regional chains across Tier 2/3 cities.",
            "source": "KPMG India",
            "url": "https://kpmg.com/in/en/insights/2025/12/multi-speciality-hospitals-in-india-evolution-of-hospitals-deals-post-covid.html",
        },
        "case_study": {
            "company": "Apollo 24|7",
            "summary": "Apollo 24|7 — one of India's largest hospital chains — built a WhatsApp system (via Infobip) for symptom checking, appointment and diagnostic booking, and reminders. Same mechanism this page describes, already running at scale.",
            "stats": [
                "95% message delivery rate",
                "Call-centre workload down 20%",
                "Diagnostic bookings up 49%",
                "Revenue per order up 72%",
            ],
            "sources": [
                {"label": "Infobip customer case study", "url": "https://www.infobip.com/customer/apollo-247"},
                {"label": "WhatsApp Business official success story", "url": "https://business.whatsapp.com/resources/success-stories/apollo-24-7"},
            ],
        },
        "market_outlook": [
            {"stat": "India's digital healthcare market is projected to reach ₹1.16 trillion by 2028, growing at a 15.76% CAGR from 2023.", "source": "ResearchAndMarkets", "url": "https://www.businesswire.com/news/home/20240702666035/en/Digital-Healthcare-Market-in-India-2024---Forecasts-to-2028-Robust-Growth-Spurred-by-Widespread-Smartphone-and-Internet-Adoption---ResearchAndMarkets.com"},
            {"stat": "India's AI-in-healthcare market is forecast to grow from $21.63M in 2025 to $110.61M by 2030 — a 38.6% CAGR.", "source": "MarketsandMarkets", "url": "https://www.marketsandmarkets.com/Market-Reports/geography/artificial-intelligence-healthcare-market/India"},
        ],
        "pain": {
            "eyebrow": "The Moment",
            "title": "A branch that doesn't exist online",
            "body": "The new branch is open for business. Google Maps still doesn't know it.",
            "chat": [
                ("in", "Is there a branch near Wakad? Can't find it on Maps."),
                ("meta", "No reply · branch has no listing"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Findable, then bookable",
            "body": "Every branch gets its own listing, doctor pages, and a WhatsApp line for appointments.",
            "chat": [
                ("in", "Is there a branch near Wakad?"),
                ("out", "Yes! Wakad branch, open 9am–9pm. Book your slot here 👇"),
                ("out", "Appointment confirmed for Dr. Mehta, Thursday 5:30pm."),
                ("meta", "This branch's new-patient count: up from 12/month to 40"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Every branch, findable",
            "body": "Each new location goes live on Google and WhatsApp on day one instead of month three.",
            "stat_label": "Branches visible on Google",
            "stat_from": "1 of 5",
            "stat_to": "5 of 5",
        },
    },
    {
        "slug": "coaching-institute",
        "name": "Coaching Institute",
        "icon": "🎓",
        "badge": "proposed",
        "use_case": "You're a genuinely good teacher — but no branch in other cities, no software team. A student outside town wants your recorded batch, can't find a way to pay, and enrolls with a teacher who already sells online.",
        "name_hi": "कोचिंग इंस्टीट्यूट",
        "use_case_hi": "आप वाकई एक अच्छे टीचर हैं — पर दूसरे शहरों में कोई ब्रांच नहीं, कोई सॉफ्टवेयर टीम नहीं। शहर के बाहर का एक स्टूडेंट आपका रिकॉर्डेड बैच चाहता है, पेमेंट का तरीका नहीं मिलता, और वह उस टीचर के पास एनरोल कर लेता है जो पहले से ऑनलाइन बेच रहा है।",
        "solution": "Course sales page + payment + auto access",
        "solution_bullets": [
            "A course sales page that explains the batch and its outcomes",
            "Payment collection built in — no separate link juggling",
            "Access granted automatically the moment payment clears",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Out-of-city students can't buy",
        "pain": {
            "eyebrow": "The Moment",
            "title": "“How do I join from outside the city?”",
            "body": "Interest is real. The buying path doesn't exist yet.",
            "chat": [
                ("in", "I'm from Nagpur, can I get the recorded batch?"),
                ("meta", "Seen · no payment link · lead goes cold"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Pay, then learn — same minute",
            "body": "A sales page and checkout mean any student, anywhere, can enrol immediately.",
            "chat": [
                ("in", "I'm from Nagpur, can I get the recorded batch?"),
                ("out", "Yes! Enrol here — instant access after payment 👇"),
                ("out", "Payment received. Your batch access is live now."),
                ("meta", "₹12,000 batch fee booked — would've gone to a teacher selling online already"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "One city becomes every city",
            "body": "The same batch now sells itself to students the classroom could never reach.",
            "stat_label": "Addressable students",
            "stat_from": "1 city",
            "stat_to": "Anywhere",
        },
    },
    {
        "slug": "real-estate-developer",
        "name": "Real Estate Developer",
        "icon": "🏢",
        "badge": "proposed",
        "use_case": "A portal lead comes in. Follow-up happens 3 days later. By then the lead has gone cold.",
        "name_hi": "रियल एस्टेट डेवलपर",
        "use_case_hi": "पोर्टल से एक लीड आती है। फॉलो-अप 3 दिन बाद होता है। तब तक लीड ठंडी पड़ चुकी होती है।",
        "solution": "Microsite + WhatsApp capture + auto brochure/visit booking",
        "solution_bullets": [
            "A project microsite that captures intent the moment someone lands",
            "Instant WhatsApp follow-up — no 3-day gap",
            "Auto-sent brochure and one-tap site-visit booking",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "3-day follow-up delay",
        "pain": {
            "eyebrow": "The Moment",
            "title": "A hot lead, cooling for 3 days",
            "body": "The portal inquiry is in the CRM. Nobody calls back until it's too late.",
            "chat": [
                ("in", "Interested in the 2BHK. Send details?"),
                ("meta", "3 days later — “Already booked elsewhere, thanks.”"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Brochure in, visit booked, same hour",
            "body": "The microsite captures the lead and WhatsApp does the follow-up instantly.",
            "chat": [
                ("in", "Interested in the 2BHK. Send details?"),
                ("out", "Here's the brochure + floor plan 👇 Want to book a site visit?"),
                ("out", "Visit confirmed: Saturday 11am."),
                ("meta", "Visit converted · ₹50,000 booking advance secured — would've gone cold like the last one"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Every lead, followed up on day one",
            "body": "The 3-day gap closes to minutes, across every project and every portal.",
            "stat_label": "Follow-up time",
            "stat_from": "3 days",
            "stat_to": "Minutes",
        },
    },
    {
        "slug": "b2b-manufacturer",
        "name": "B2B Manufacturer",
        "icon": "🏭",
        "badge": "proposed",
        "use_case": "An RFQ finally gets quoted — 4 days late. The order is already gone.",
        "name_hi": "B2B मैन्युफैक्चरर",
        "use_case_hi": "RFQ का आख़िरकार कोटेशन मिलता है — 4 दिन देर से। तब तक ऑर्डर जा चुका होता है।",
        "solution": "Catalog + inquiry-to-WhatsApp + fast quote templates",
        "solution_bullets": [
            "A live catalog buyers can browse and reference in their RFQ",
            "Every inquiry pushed straight to WhatsApp, not lost in email",
            "Pre-built quote templates so pricing goes out same-day",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "RFQ quoted 4 days late",
        "pain": {
            "eyebrow": "The Moment",
            "title": "4 days to a quote — order's gone",
            "body": "Busy with another customer on the floor, stock counts, and the current production run, the WhatsApp inquiry sits unread. By the time it's quoted, the buyer bought elsewhere.",
            "chat": [
                ("in", "Need a quote for 5000 units, urgent."),
                ("meta", "Quoted 4 days later — order already placed with competitor"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Quote out before the buyer moves on",
            "body": "The inquiry routes to WhatsApp instantly, template quote follows within hours.",
            "chat": [
                ("in", "Need a quote for 5000 units, urgent."),
                ("out", "On it — quote attached, valid 7 days 👇"),
                ("out", "PO received, production scheduling confirmed."),
                ("meta", "₹3,80,000 order — booked before the buyer could call the next vendor"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Speed becomes the pitch",
            "body": "Buyers start choosing the fastest quote — which is now always this one.",
            "stat_label": "Quote turnaround",
            "stat_from": "4 days",
            "stat_to": "Hours",
        },
    },
    {
        "slug": "private-school",
        "name": "Private School",
        "icon": "🏫",
        "badge": "proposed",
        "use_case": "Admission week. The phone line is jammed. Enrollments are lost to the school that answered.",
        "name_hi": "प्राइवेट स्कूल",
        "use_case_hi": "एडमिशन वीक। फ़ोन लाइन व्यस्त। एनरोलमेंट उस स्कूल के पास चला जाता है जिसने कॉल का जवाब दिया।",
        "solution": "Admission capture + WhatsApp auto-response + GBP",
        "solution_bullets": [
            "An admission-enquiry form that never goes to a busy line",
            "Instant WhatsApp auto-response with next steps",
            "A Google Business Profile parents actually find during search",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Jammed phone line, admission week",
        "pain": {
            "eyebrow": "The Moment",
            "title": "Missed call, then a reply 6 hours too late",
            "body": "A parent calls — missed. They message instead — it sits unread, then gets a reply 6 hours later. By then they've already called another school.",
            "chat": [
                ("in", "Calling about Grade 2 admission..."),
                ("meta", "Missed call · follow-up message sent"),
                ("meta", "Replied 6 hours later — parent had already enrolled at another school"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Instant reply, a locked-in visit, ₹90,000 that didn't get away",
            "body": "Fee structure goes out immediately, with a small-fee admission-test booking that gets the parent to actually walk in.",
            "chat": [
                ("in", "Interested in Grade 2 admission."),
                ("out", "Thanks for reaching out! Here's our fee structure 👇 Book an admission test slot for ₹99 — confirms your visit."),
                ("in", "Booked, see you Saturday."),
                ("meta", "Admission test attended · admission confirmed · ₹90,000 annual fee booked — would've gone to another school"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Admission week, without the chaos",
            "body": "Every enquiry gets captured and walked to a locked-in visit, whether the line is free or not.",
            "stat_label": "Revenue on the line from one missed call",
            "stat_from": "Lost to another school",
            "stat_to": "₹90,000 booked, same week",
        },
    },
    {
        "slug": "diagnostic-lab",
        "name": "Diagnostic Lab",
        "icon": "🧪",
        "badge": "proposed",
        "use_case": "Home-collection booking has too much friction. The rival lab down the road wins the sample.",
        "name_hi": "डायग्नोस्टिक लैब",
        "use_case_hi": "होम-कलेक्शन बुकिंग में बहुत झंझट है। रास्ते की दूसरी लैब सैंपल जीत ले जाती है।",
        "solution": "Per-branch GBP + WhatsApp booking + digital reports",
        "solution_bullets": [
            "Google presence for every branch so nearby patients find you first",
            "WhatsApp booking for home collection in under a minute",
            "Digital reports delivered where the patient already is — WhatsApp",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Booking friction loses the sample",
        "pain": {
            "eyebrow": "The Moment",
            "title": "Too many steps to book a test",
            "body": "The patient wants a home-collection blood test. The booking process asks for too much, too slowly.",
            "chat": [
                ("in", "Need a home blood test tomorrow morning."),
                ("meta", "No response · patient books with the lab next door"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Selected, paid, and booked — before they put the phone down",
            "body": "A list of tests, a payment link, and a confirmed slot — no back-and-forth, no forms.",
            "chat": [
                ("in", "Need a home blood test tomorrow morning."),
                ("out", "Sure! Which test — CBC, Thyroid Profile, or Lipid Profile?"),
                ("in", "Thyroid Profile please."),
                ("out", "₹499 — pay here to confirm your slot 👇"),
                ("meta", "Paid ✓ Slot booked: 8–9am, technician assigned"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "The nearest lab, and the easiest one",
            "body": "Being both visible and frictionless wins the sample before the rival even replies.",
            "stat_label": "Booking time",
            "stat_from": "Multi-step form, most abandoned",
            "stat_to": "Paid & confirmed in under 2 minutes",
        },
    },
    {
        "slug": "wedding-planner-banquet",
        "name": "Wedding Planner / Banquet",
        "icon": "✨",
        "badge": "proposed",
        "use_case": "A high-value Instagram DM about a wedding date arrives — and gets buried under everything else. Never answered.",
        "name_hi": "वेडिंग प्लानर / बैंक्वेट",
        "use_case_hi": "शादी की तारीख़ को लेकर एक बड़ा इंस्टाग्राम DM आता है — और बाकी सबके नीचे दब जाता है। कभी जवाब नहीं मिलता।",
        "solution": "Proof-of-work site + WhatsApp date/quote flow",
        "solution_bullets": [
            "A portfolio site that shows real work, not just a feed",
            "Every inquiry routed to WhatsApp for date and quote conversations",
            "Nothing high-value gets buried in a DM inbox again",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "High-value DM buried, never answered",
        "pain": {
            "eyebrow": "The Moment",
            "title": "A ₹8L booking, sitting in DMs",
            "body": "The inquiry is real and urgent. It's competing with a hundred comments and never surfaces.",
            "chat": [
                ("in", "Loved your work! Available for Dec 14 wedding, 300 guests?"),
                ("meta", "Buried in DMs · unanswered for a week"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Straight to WhatsApp, same day",
            "body": "The portfolio site routes every serious inquiry to a real conversation, immediately.",
            "chat": [
                ("in", "Available for Dec 14 wedding, 300 guests?"),
                ("out", "Yes! Here's our portfolio + package for 300 guests 👇"),
                ("out", "Date held — advance link shared."),
                ("meta", "₹2,00,000 advance paid — this ₹8L booking almost went unanswered"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "No booking gets lost in a feed again",
            "body": "The highest-value inquiries now get the fastest response, every time.",
            "stat_label": "Response to DM inquiries",
            "stat_from": "Buried",
            "stat_to": "Same day",
        },
    },
    {
        "slug": "gym-fitness-chain",
        "name": "Gym / Fitness Chain",
        "icon": "🏋️",
        "badge": "proposed",
        "use_case": "Trial DMs flood in after a promo. No follow-up happens. Almost none convert to memberships.",
        "name_hi": "जिम / फिटनेस चेन",
        "use_case_hi": "प्रोमो के बाद ट्रायल के लिए ढेरों DM आते हैं। कोई फॉलो-अप नहीं होता। लगभग कोई भी मेंबरशिप में नहीं बदलता।",
        "solution": "WhatsApp trial-booking flow + GBP",
        "solution_bullets": [
            "A WhatsApp flow that books the trial slot instantly",
            "Automatic follow-up after the trial, not left to memory",
            "Google Business Profile that brings in the next wave of trials",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Trial DMs, zero follow-up",
        "citation": {
            "stat": "Cult.fit — India's largest fitness chain, over 230 centers — is now expanding its franchise model deep into Tier 2 and Tier 3 cities, the exact towns independent gyms used to have entirely to themselves.",
            "source": "Indian Retailer",
            "url": "https://www.indianretailer.com/news/cult-fit-to-build-presence-in-smaller-markets-via-franchise-model.n11772",
        },
        "pain": {
            "eyebrow": "The Moment",
            "title": "50 trial DMs, 2 follow-ups",
            "body": "The promo worked. The follow-up didn't happen, and the trials never convert.",
            "chat": [
                ("in", "Saw your offer, want to try a free class."),
                ("meta", "No booking, no follow-up · lead goes cold"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Trial booked, follow-up automatic",
            "body": "The slot books itself in chat, and a follow-up message goes out right after class.",
            "chat": [
                ("in", "Want to try a free class."),
                ("out", "Booked! Monday 7am, Trainer Rahul 👇"),
                ("out", "How was the class? Here's your membership offer."),
                ("meta", "₹8,000 annual membership converted — from a trial that used to just go cold"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Every trial, actually followed up",
            "body": "The promo's real ROI shows up when trials convert instead of going quiet.",
            "stat_label": "Trial → membership follow-up",
            "stat_from": "~4%",
            "stat_to": "100% contacted",
        },
    },
    {
        "slug": "ca-legal-firm",
        "name": "CA / Legal Firm",
        "icon": "⚖️",
        "badge": "proposed",
        "use_case": "No real online presence. The firm loses the client to whoever actually shows up in search.",
        "name_hi": "CA / लीगल फर्म",
        "use_case_hi": "कोई असली ऑनलाइन मौजूदगी नहीं। फर्म उस क्लाइंट को खो देती है जो सर्च में असल में दिखता है।",
        "solution": "Credibility site + WhatsApp consult booking",
        "solution_bullets": [
            "A credibility-first site: expertise, track record, clear services",
            "WhatsApp consult booking so inquiries convert to meetings",
            "Findable when a prospective client actually searches",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Invisible in search results",
        "citation": {
            "stat": "Online compliance platforms now cover everything from GST to ITR filing end to end. When a prospective client can compare a dozen options without leaving their chat app, a firm that doesn't show up online isn't losing on price — it's simply not in the running.",
            "source": "Jurishour — CA Firms & Compliance Platforms in India",
            "url": "https://www.jurishour.in/columns/20-ca-firms-compliance-platforms-working-pan-india/",
        },
        "pain": {
            "eyebrow": "The Moment",
            "title": "Searched, and not found",
            "body": "A prospective client searches “CA near me.” Three other firms show up. This one doesn't.",
            "chat": [
                ("meta", "Google search — firm not listed, not found"),
                ("in", "Went with the firm that came up first."),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Found, then booked",
            "body": "A credibility site and WhatsApp booking turn a search result into a consult.",
            "chat": [
                ("in", "Need help with GST filing, can we talk?"),
                ("out", "Sure — here's our availability, pick a slot 👇"),
                ("out", "Consult confirmed for Wednesday 4pm."),
                ("meta", "₹25,000 retainer engaged — client never even saw the other 3 results"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Search becomes a client pipeline",
            "body": "Visibility plus a booking path turns organic search into steady consult volume.",
            "stat_label": "Found in search",
            "stat_from": "Not listed",
            "stat_to": "Top results",
        },
    },
    {
        "slug": "interior-designer",
        "name": "Interior Designer",
        "icon": "🎨",
        "badge": "proposed",
        "use_case": "The reel gets thousands of views. None of them turn into an actual consult booking.",
        "name_hi": "इंटीरियर डिज़ाइनर",
        "use_case_hi": "रील पर हज़ारों व्यूज़ आते हैं। पर कोई भी असली कंसल्ट बुकिंग में नहीं बदलता।",
        "solution": "Case-study portfolio + WhatsApp consult booking",
        "solution_bullets": [
            "A case-study portfolio that proves the work behind the reels",
            "WhatsApp consult booking right where the interest already is",
            "Views convert to conversations, not just likes",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Reel views, zero consult bookings",
        "pain": {
            "eyebrow": "The Moment",
            "title": "10,000 views, 0 bookings",
            "body": "The reel goes semi-viral. There's no clear next step for someone who wants this for their own home.",
            "chat": [
                ("meta", "10.2k views · 340 likes · 0 DMs converted"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "From view to booked consult",
            "body": "A case-study portfolio and WhatsApp booking turn admiration into an actual project.",
            "chat": [
                ("in", "Loved this design! Do you take on 2BHK projects?"),
                ("out", "Yes! Here's similar work + booking link for a consult 👇"),
                ("out", "Consult booked — site visit next week."),
                ("meta", "₹3,50,000 project confirmed — from a reel that used to convert nothing"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Content finally pays for itself",
            "body": "The same reach now converts into real project pipeline, not just engagement.",
            "stat_label": "Views → consult bookings",
            "stat_from": "0%",
            "stat_to": "Tracked & converting",
        },
    },
    {
        "slug": "retail-store",
        "name": "Retail Store (Kirana / General)",
        "icon": "🛒",
        "badge": "proposed",
        "use_case": "A regular customer can't make it to the store today. There's no way to order from home tied to what's actually in stock — so they open Blinkit instead, and the store never even knows it lost the sale.",
        "name_hi": "रिटेल स्टोर (किराना / जनरल)",
        "use_case_hi": "एक रेगुलर ग्राहक आज दुकान तक नहीं आ सकता। घर से असली स्टॉक के हिसाब से ऑर्डर करने का कोई तरीका नहीं है — तो वह इसकी बजाय Blinkit खोल लेता है, और दुकान को पता भी नहीं चलता कि उसने बिक्री गंवा दी।",
        "solution": "WhatsApp catalog + ordering, tied to real inventory",
        "solution_bullets": [
            "A live WhatsApp catalog tied to actual stock — no promising what's not on the shelf",
            "Order + pay in the same chat, pickup or local delivery either way",
            "Keeps the store's real edge — trust, khata credit, zero delivery markup — while matching quick-commerce convenience",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "No home-ordering tied to real stock",
        "citation": {
            "stat": "Nearly 80% of consumers have shifted at least a quarter of their grocery spending to quick-commerce apps, and over 2 lakh kirana stores closed in a single year — yet local stores still hold 88% of India's retail food market on trust, credit, and zero delivery fees alone.",
            "source": "Outlook Business, citing AICPDF",
            "url": "https://www.outlookbusiness.com/explainers/kirana-stores-are-losing-the-battle-against-zepto-blinkit-and-instamart",
        },
        "pain": {
            "eyebrow": "The Moment",
            "title": "Can't come in today — orders from Blinkit instead",
            "body": "A loyal customer needs 6 items tonight. The store doesn't answer WhatsApp with real stock, so the order goes to an app instead — and the store never finds out.",
            "chat": [
                ("in", "Do you have atta, eggs and milk right now? Can someone drop it?"),
                ("meta", "No reply · customer orders on Blinkit in 9 minutes"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Same store, same trust, now open from home",
            "body": "The exact stock on the shelf shows up in WhatsApp. Order, pay, and it's on the way — from the store that already knows them.",
            "chat": [
                ("in", "Do you have atta, eggs and milk right now?"),
                ("out", "Yes, all in stock! ₹410 total — pay here or add to khata 👇"),
                ("out", "Packed — out for delivery, 20 mins."),
                ("meta", "3rd home order from this customer this month — ~₹3,200/month kept from going to Blinkit"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "The convenience edge, without losing the store's edge",
            "body": "Quick-commerce wins on convenience alone. This closes that one gap — while keeping the trust and credit a delivery app can't offer.",
            "stat_label": "Home-bound orders",
            "stat_from": "Lost to apps",
            "stat_to": "Kept in-store",
        },
    },
    {
        "slug": "automobile-showroom",
        "name": "Automobile Showroom",
        "icon": "🚗",
        "badge": "proposed",
        "use_case": "A walk-in asks about a test drive on Instagram. By the time someone replies, they've already booked one at the showroom down the road.",
        "name_hi": "ऑटोमोबाइल शोरूम",
        "use_case_hi": "एक संभावित ग्राहक इंस्टाग्राम पर टेस्ट ड्राइव के बारे में पूछता है। जवाब मिलने तक, वह रास्ते के शोरूम में पहले ही बुक कर चुका होता है।",
        "solution": "WhatsApp test-drive booking + service reminders",
        "solution_bullets": [
            "Test-drive slots booked straight from any inquiry, no back-and-forth",
            "Automatic service-due and insurance-renewal reminders on WhatsApp",
            "Every walk-in and DM tracked, not just the ones someone remembered to note down",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Test-drive inquiry, no slot booked",
        "pain": {
            "eyebrow": "The Moment",
            "title": "Interested, then gone in a day",
            "body": "The inquiry is real. Nobody follows up fast enough, and the next showroom does.",
            "chat": [
                ("in", "Can I test drive the new model this weekend?"),
                ("meta", "Seen · no slot offered · booked elsewhere"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Slot booked before they close the app",
            "body": "The test drive gets scheduled in the same chat the inquiry came in on.",
            "chat": [
                ("in", "Can I test drive the new model this weekend?"),
                ("out", "Sure! Saturday 11am or 4pm — which works? 👇"),
                ("out", "Booked for 11am. See you at the showroom!"),
                ("meta", "Test drive → sale · ₹9,80,000 — would've walked into the showroom down the road"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "From one sale to a service relationship",
            "body": "Service and renewal reminders keep the customer coming back long after the sale.",
            "stat_label": "Test-drive inquiries booked",
            "stat_from": "Hit or miss",
            "stat_to": "Same chat, same visit",
        },
    },
    {
        "slug": "building-materials-showroom",
        "name": "Building Materials / Tiles Showroom",
        "icon": "🧱",
        "badge": "proposed",
        "use_case": "A site visit needs tile samples and a quick quote. The showroom takes days to send either, so the contractor buys from whoever answers first.",
        "name_hi": "बिल्डिंग मटेरियल / टाइल्स शोरूम",
        "use_case_hi": "साइट विज़िट के लिए टाइल सैंपल और तुरंत कोटेशन चाहिए। शोरूम दोनों भेजने में दिन लगा देता है, तो कॉन्ट्रैक्टर उससे ख़रीदता है जो पहले जवाब दे।",
        "solution": "WhatsApp catalog + sample request + fast quote",
        "solution_bullets": [
            "A browsable catalog so contractors can shortlist before they even call",
            "Sample requests routed straight to WhatsApp, not lost in a register",
            "Quote templates so pricing goes out the same day",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "Sample + quote delay loses the order",
        "pain": {
            "eyebrow": "The Moment",
            "title": "Samples took 3 days. Too late.",
            "body": "The contractor needed to decide this week. By the time the sample arrived, the order was placed elsewhere.",
            "chat": [
                ("in", "Need tile samples + quote for a 2000 sqft site, urgent."),
                ("meta", "Samples sent 3 days later · order already placed"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Catalog first, samples same day",
            "body": "The contractor browses, requests samples, and gets a quote — all inside WhatsApp, same day.",
            "chat": [
                ("in", "Need tile samples + quote for a 2000 sqft site, urgent."),
                ("out", "Here's our catalog — shortlist and we'll courier samples today 👇"),
                ("out", "Quote attached, valid 7 days."),
                ("meta", "₹85,000 tile order confirmed — contractor didn't even check the next supplier"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Speed wins contractor loyalty",
            "body": "Contractors return to whoever quotes fastest — that's now the default here.",
            "stat_label": "Sample-to-quote time",
            "stat_from": "3 days",
            "stat_to": "Same day",
        },
    },
    {
        "slug": "wholesale-distributor",
        "name": "Wholesale Distributor",
        "icon": "📦",
        "badge": "proposed",
        "use_case": "A retailer wants to reorder stock. There's no easy channel to do it, so they call a competing distributor who makes it simpler.",
        "name_hi": "होलसेल डिस्ट्रीब्यूटर",
        "use_case_hi": "एक रिटेलर स्टॉक दोबारा ऑर्डर करना चाहता है। ऐसा करने का कोई आसान तरीका नहीं है, तो वह एक प्रतिद्वंद्वी डिस्ट्रीब्यूटर को कॉल करता है जो इसे आसान बना देता है।",
        "solution": "WhatsApp reorder catalog + repeat-purchase reminders",
        "solution_bullets": [
            "Retailers reorder by browsing a live catalog on WhatsApp, no phone tag",
            "Automatic reorder nudges timed to each retailer's typical cycle",
            "Every inquiry and repeat order tracked in one place",
        ],
        "starts_at": "₹2,999/mo",
        "leak_label": "No easy reorder channel",
        "pain": {
            "eyebrow": "The Moment",
            "title": "Reordering is harder than it should be",
            "body": "A retailer wants to restock. Calling, waiting on hold, and reading out a list by hand is enough friction to make them call someone else.",
            "chat": [
                ("in", "Need to reorder — can I get the list processed today?"),
                ("meta", "Call unanswered · retailer orders from another distributor"),
            ],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix",
            "title": "Reorder in one WhatsApp message",
            "body": "The retailer picks from a live catalog and the order is confirmed the same day.",
            "chat": [
                ("in", "Need to reorder my usual list."),
                ("out", "Here's your usual order — confirm and it ships today 👇"),
                ("out", "Order confirmed, dispatched."),
                ("meta", "₹65,000 reorder — kept from going to a competing distributor"),
            ],
            "accent": "green",
        },
        "growth": {
            "eyebrow": "The Growth",
            "title": "Reorders that happen on their own",
            "body": "Timed nudges mean retailers restock before they even think to call someone else.",
            "stat_label": "Reorder friction",
            "stat_from": "Phone tag",
            "stat_to": "One tap",
        },
    },
]

# ------------------------------------------------------------------
# MODULES — reusable automation add-ons, shared across industries.
# This is what keeps the economics honest: the same n8n-style workflow
# gets adapted per client rather than built from scratch each time.
# effort: "quick" (~2 days to adapt + ship) or "advanced" (~1-2 weeks,
# usually because it touches a live data source like inventory).
# ------------------------------------------------------------------
MODULES = [
    {
        "id": "invoice-reminder",
        "agentic": False,
        "name": "Invoice + Payment Reminders",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "Invoice auto-sent on order/booking, then tiered WhatsApp reminders at 7/14/30 days overdue.",
        "industries": ["export-trading", "b2b-manufacturer", "wholesale-distributor", "interior-designer",
                        "wedding-planner-banquet", "ca-legal-firm", "building-materials-showroom", "real-estate-developer"],
        "pain": {
            "eyebrow": "The Moment", "title": "The invoice went out. The payment didn't.",
            "body": "No one has time to chase every unpaid invoice by hand — so most don't get chased at all.",
            "chat": [("meta", "Invoice #2291 · 21 days overdue · no follow-up sent")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "The reminder sends itself",
            "body": "A WhatsApp nudge goes out automatically at 7, 14, and 30 days — polite, on time, every time.",
            "chat": [
                ("out", "Hi! Friendly reminder — Invoice #2291 (₹18,400) is due. Pay here 👇"),
                ("in", "Sorry, missed this — paying now."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Cash stuck in receivables, freed up",
                    "body": "Nobody spends an afternoon chasing payments anymore — the system already did.",
                    "stat_label": "Average days to collect", "stat_from": "21+ days", "stat_to": "Under 10"},
    },
    {
        "id": "payment-reconciliation",
        "agentic": False,
        "name": "Payment Reconciliation",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "Bank statement and invoice/fee records matched automatically — mismatches flagged, not hunted for.",
        "industries": ["coaching-institute", "gym-fitness-chain", "private-school", "diagnostic-lab", "wholesale-distributor"],
        "pain": {
            "eyebrow": "The Moment", "title": "Whose payment is this, again?",
            "body": "A bank credit shows up. Matching it to the right student, member, or invoice eats an afternoon every week.",
            "chat": [("meta", "47 bank entries · 6 hours spent matching manually this month")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Matched the moment it lands",
            "body": "Every payment is matched against open dues automatically — only real mismatches need a human look.",
            "chat": [
                ("out", "₹4,500 credit matched to Rohan Sharma — March fee, marked paid ✓"),
                ("out", "⚠️ 1 unmatched entry flagged for review."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Hours back, every single week",
                    "body": "Reconciliation stops being a chore that eats a weekly afternoon.",
                    "stat_label": "Time spent matching payments", "stat_from": "Hours weekly", "stat_to": "Minutes"},
    },
    {
        "id": "booking-reminder",
        "agentic": False,
        "name": "Booking Confirmation + No-Show Reminder",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "Every booking auto-confirmed, with a WhatsApp reminder before the slot so no-shows drop.",
        "industries": ["hospital", "diagnostic-lab", "ca-legal-firm", "interior-designer", "gym-fitness-chain", "automobile-showroom"],
        "pain": {
            "eyebrow": "The Moment", "title": "Booked, then forgotten",
            "body": "A slot gets booked. Nobody reminds the customer, so a chunk of appointments become no-shows.",
            "chat": [("meta", "Appointment booked 9 days ago · no reminder sent · no-show")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "A nudge, right before the slot",
            "body": "A confirmation goes out instantly, then a reminder the day before — automatically.",
            "chat": [
                ("out", "Booked! Thursday 4:30pm, confirmed ✓"),
                ("out", "Reminder: your appointment is tomorrow at 4:30pm."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Fewer empty slots, more kept appointments",
                    "body": "The calendar stops leaking time to forgetfulness.",
                    "stat_label": "No-show rate", "stat_from": "1 in 5", "stat_to": "Rare"},
    },
    {
        "id": "claim-email-dispatch",
        "agentic": False,
        "name": "Claim / Document Auto-Email Dispatch",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "A claim or document summary is auto-generated and emailed to the right address the moment it's ready — with WhatsApp status updates back to the customer. No payer-system integration, just a fast, reliable send.",
        "industries": ["hospital", "diagnostic-lab"],
        "pain": {
            "eyebrow": "The Moment", "title": "The claim sits in a drawer",
            "body": "Paperwork for an insurance claim is ready. Actually typing, attaching, and emailing it out gets pushed to \"later.\"",
            "chat": [("meta", "Claim documents ready · 4 days sitting unsent")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Sent the moment it's ready",
            "body": "The claim summary is generated and emailed to the insurer's claims address automatically — the patient gets a WhatsApp update.",
            "chat": [
                ("meta", "Claim #7741 emailed to insurer's claims desk — auto-sent"),
                ("out", "Your claim has been submitted. We'll update you here on status."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Nothing sits in a drawer again",
                    "body": "A same-day send instead of a multi-day backlog — no new integration required.",
                    "stat_label": "Time to dispatch a claim", "stat_from": "Days", "stat_to": "Minutes"},
    },
    {
        "id": "review-reply",
        "agentic": True,
        "name": "Review Request + AI-Drafted Reply",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "A WhatsApp review request goes out after service; AI drafts a reply to every Google review for a quick human approve-and-post.",
        "industries": ["gym-fitness-chain", "diagnostic-lab", "interior-designer", "wedding-planner-banquet", "retail-store", "automobile-showroom"],
        "pain": {
            "eyebrow": "The Moment", "title": "Happy customers, no reviews",
            "body": "Most people don't leave a review unless asked — and nobody has time to ask, or to reply to the ones that come in.",
            "chat": [("meta", "3 new Google reviews · 0 replies in 2 months")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Asked at the right moment, replied to fast",
            "body": "A review request goes out right after service, and every incoming review gets an AI-drafted reply ready to approve.",
            "chat": [
                ("out", "Thanks for visiting today! Mind leaving us a quick review? 👇"),
                ("meta", "New 5★ review — reply drafted, ready to approve"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "A steady stream of fresh, answered reviews",
                    "body": "Review volume and response rate both move — which is what actually moves local search ranking.",
                    "stat_label": "Reviews replied to", "stat_from": "Rarely", "stat_to": "Every one"},
        "case_study": {
            "company": "HM Hotels",
            "summary": "HM Hotels — a 23-property chain across Mallorca, Mexico and the Dominican Republic — rolled out AI-drafted review replies (via Shiji) after a two-month pilot at two hotels, then to the whole chain.",
            "stats": [
                "82% of 661 reviews replied to within the first month",
                "Average reply time: 3 days",
            ],
            "sources": [
                {"label": "Shiji customer case study", "url": "https://www.shijigroup.com/customers/smarter-reviews-happier-guests-unlocking-the-power-of-ai"},
                {"label": "Hospitality Net coverage", "url": "https://www.hospitalitynet.org/casestudy/4126694/smarter-reviews-happier-guests-unlocking-the-power-of-ai"},
            ],
        },
    },
    {
        "id": "stock-check-reserve",
        "agentic": False,
        "name": "Stock Check-and-Reserve",
        "effort": "advanced",
        "badge": "proposed",
        "blurb": "Customer asks if something's in stock on WhatsApp — the bot checks the real inventory sheet and lets them reserve it.",
        "industries": ["retail-store", "building-materials-showroom", "wholesale-distributor"],
        "pain": {
            "eyebrow": "The Moment", "title": "\"Is it in stock?\" — nobody knows without a call",
            "body": "Checking stock means someone walking to the shelf or calling around. Most customers don't wait.",
            "chat": [("in", "Is the 10kg bag in stock right now?"), ("meta", "No answer · customer buys elsewhere")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Checked and reserved, instantly",
            "body": "The chat checks the live inventory sheet and holds the item the moment they confirm.",
            "chat": [
                ("in", "Is the 10kg bag in stock right now?"),
                ("out", "Yes, 6 left! Reserve one? 👇"),
                ("out", "Reserved for you — ready for pickup."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Stock questions become sales, not guesses",
                    "body": "Real-time stock answers keep the customer here instead of one tap away from an app.",
                    "stat_label": "Stock inquiries answered instantly", "stat_from": "Only if someone's free", "stat_to": "Always"},
    },
    {
        "id": "reorder-nudge",
        "agentic": False,
        "name": "Reorder / Repeat-Purchase Nudge",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "A WhatsApp nudge times itself to each customer's usual reorder cycle, before they think to call someone else.",
        "industries": ["wholesale-distributor", "retail-store", "building-materials-showroom"],
        "pain": {
            "eyebrow": "The Moment", "title": "They forgot to reorder — from you",
            "body": "A regular buyer runs low and just orders from whoever's easiest to reach that day. It isn't always this business.",
            "chat": [("meta", "Regular buyer's usual 30-day cycle passed — no nudge sent")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "A nudge, right on cycle",
            "body": "A WhatsApp reminder goes out timed to their usual reorder pattern, with the usual order pre-filled.",
            "chat": [
                ("out", "Running low on your usual order? Reorder in one tap 👇"),
                ("in", "Yes please, same as last time."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Repeat business that doesn't rely on memory",
                    "body": "The reorder happens because the system remembered — not because the customer did.",
                    "stat_label": "Repeat orders captured", "stat_from": "Whoever remembers", "stat_to": "On cycle, automatically"},
    },
    {
        "id": "lead-qualification",
        "agentic": True,
        "name": "Lead Qualification & Scoring Agent",
        "effort": "advanced",
        "badge": "proposed",
        "blurb": "Asks 2-3 quick questions automatically, scores the inquiry hot/warm/cold, and routes only the hot ones straight to you.",
        "industries": ["real-estate-developer", "b2b-manufacturer", "interior-designer", "ca-legal-firm", "wholesale-distributor", "automobile-showroom"],
        "pain": {
            "eyebrow": "The Moment", "title": "20 inquiries, and no way to tell which 3 matter",
            "body": "Every inquiry looks the same at first glance. Time goes to whoever asked first, not whoever's actually ready to buy.",
            "chat": [("meta", "20 inquiries this week · 3 were serious buyers · found out after calling all 20")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Scored before it reaches you",
            "body": "A few quick questions score the inquiry automatically — only the hot ones land in your WhatsApp.",
            "chat": [
                ("in", "Interested in the 3BHK, what's the budget range?"),
                ("out", "Great! Quick check — are you looking to buy in the next 3 months?"),
                ("meta", "🔥 Scored HOT — routed to owner instantly"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Time goes where the deal is",
                    "body": "The serious buyers stop getting lost in the same pile as the window-shoppers.",
                    "stat_label": "Time spent on low-intent leads", "stat_from": "Hours daily", "stat_to": "Only hot leads"},
    },
    {
        "id": "objection-handling",
        "agentic": True,
        "name": "FAQ + Objection-Handling Agent",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "Answers the same 15-20 questions and objections instantly and consistently — escalates only what's genuinely new.",
        "industries": ["coaching-institute", "gym-fitness-chain", "interior-designer", "ca-legal-firm", "diagnostic-lab"],
        "pain": {
            "eyebrow": "The Moment", "title": "The same question, for the 20th time today",
            "body": "\"Is it safe\", \"what's included\", \"can I pay in installments\" — answering these all day leaves no time for anything else, and slow answers lose the sale.",
            "chat": [("meta", "Same 5 questions asked 20+ times this week, answered manually each time")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Answered instantly, every time",
            "body": "Common questions and objections get an instant, consistent answer. Genuinely new questions still reach a human.",
            "chat": [
                ("in", "Can I pay in installments?"),
                ("out", "Yes! 3 easy installments, no extra charge. Want me to set that up? 👇"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Time freed up for the questions that actually need a human",
                    "body": "The repetitive 80% stops eating the day.",
                    "stat_label": "Repetitive questions handled by a human", "stat_from": "Every one", "stat_to": "Only the new ones"},
    },
    {
        "id": "negative-review-recovery",
        "agentic": True,
        "name": "Negative Review Alert + Recovery Agent",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "Flags a bad review the moment it lands, with a drafted apology and a service-recovery offer ready to approve within the hour.",
        "industries": ["gym-fitness-chain", "diagnostic-lab", "wedding-planner-banquet", "retail-store", "automobile-showroom", "interior-designer"],
        "pain": {
            "eyebrow": "The Moment", "title": "A bad review, sitting there for days",
            "body": "By the time anyone notices and responds, the next ten prospects have already read it — unanswered.",
            "chat": [("meta", "1★ review posted 4 days ago · still no reply · visible to every new visitor")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Flagged and drafted within minutes",
            "body": "The moment a negative review lands, an alert goes out with a drafted, empathetic reply and a recovery offer ready to send.",
            "chat": [
                ("meta", "⚠️ New 1★ review — reply + recovery offer drafted, ready to approve"),
                ("out", "We're sorry we missed the mark — we'd like to make it right. Can we call you?"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Damage caught before it compounds",
                    "body": "A fast, human response to a bad review often does more for trust than a string of good ones.",
                    "stat_label": "Time to respond to a bad review", "stat_from": "Days, if ever", "stat_to": "Same hour"},
    },
    {
        "id": "win-back",
        "agentic": False,
        "name": "Abandoned-Inquiry Win-Back Nudge",
        "effort": "advanced",
        "badge": "proposed",
        "blurb": "Re-engages a promising inquiry automatically after a few days of silence, with a fresh nudge instead of writing it off.",
        "industries": ["real-estate-developer", "interior-designer", "wedding-planner-banquet", "coaching-institute", "automobile-showroom"],
        "pain": {
            "eyebrow": "The Moment", "title": "Interested, then silent — and forgotten",
            "body": "The conversation went well, then stopped. Nobody follows up a second time, so it's quietly written off.",
            "chat": [("meta", "Last message 6 days ago · no follow-up sent · lead effectively dead")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "A second chance, sent automatically",
            "body": "After a few days of silence, a re-engagement message goes out on its own — sometimes that's all it takes.",
            "chat": [
                ("out", "Still thinking it over? Happy to answer anything, or share a quick offer 👇"),
                ("in", "Actually yes, I got busy — let's continue."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Leads that would've just gone cold",
                    "body": "A fair share of \"dead\" inquiries were never actually dead — just unattended.",
                    "stat_label": "Cold leads re-engaged", "stat_from": "Written off", "stat_to": "Given a second chance"},
    },
    {
        "id": "seo-content-agent",
        "agentic": True,
        "name": "AI Local-SEO Content Agent",
        "effort": "advanced",
        "badge": "proposed",
        "blurb": "Drafts a weekly local-SEO blog or Google Business post automatically — a 2-minute human review is all it needs before publishing.",
        "industries": ["ca-legal-firm", "interior-designer", "diagnostic-lab", "gym-fitness-chain", "coaching-institute", "retail-store"],
        "pain": {
            "eyebrow": "The Moment", "title": "Nobody has time to write a blog post",
            "body": "Fresh content is what search ranking actually rewards. It also never happens, because nobody has a spare afternoon.",
            "chat": [("meta", "Last blog/GBP post: 3 months ago · search visibility quietly declining")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "A draft, ready every week",
            "body": "A relevant local post gets drafted automatically — approve, tweak if needed, publish.",
            "chat": [
                ("meta", "This week's draft ready: \"5 Signs You Need [Service] Before Monsoon\""),
                ("out", "Reviewed and published ✓"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Consistency, without the time cost",
                    "body": "Search ranking rewards a business that keeps showing up — this makes that the default, not the exception.",
                    "stat_label": "Fresh content published", "stat_from": "Whenever someone remembers", "stat_to": "Every week"},
    },
    {
        "id": "missed-call-winback",
        "agentic": False,
        "name": "Missed-Call Instant Win-Back",
        "effort": "quick",
        "badge": "proposed",
        "blurb": "The moment a call is missed, an automatic WhatsApp picks the conversation back up — before the caller tries someone else.",
        "industries": ["hospital", "diagnostic-lab", "ca-legal-firm", "automobile-showroom", "retail-store", "gym-fitness-chain"],
        "pain": {
            "eyebrow": "The Moment", "title": "A missed call is a lost inquiry",
            "body": "Nobody calls back in time, if at all — and the caller has usually already tried the next number on the list.",
            "chat": [("meta", "Missed call · 14:32 · no callback · number not seen again")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Picked up on WhatsApp, instantly",
            "body": "The moment a call is missed, a WhatsApp message goes out automatically — the conversation doesn't just die.",
            "chat": [
                ("meta", "Missed call · 14:32"),
                ("out", "Sorry we missed your call! How can we help — want us to call you back?"),
                ("in", "Yes please, in 10 mins."),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Every missed call, still a live inquiry",
                    "body": "A missed call stops being an automatic loss.",
                    "stat_label": "Missed calls followed up", "stat_from": "Rarely", "stat_to": "Every one, instantly"},
        "case_study": {
            "company": "Weatherseal by Asian Paints",
            "summary": "Weatherseal — Asian Paints' home-waterproofing brand — runs missed-call callbacks and lead follow-up automatically on WhatsApp (via AiSensy), the same mechanism this page describes, at one of India's largest paint companies.",
            "stats": [],
            "sources": [
                {"label": "AiSensy customer case studies", "url": "https://aisensy.com/case-studies"},
                {"label": "Weatherseal by Asian Paints — official site", "url": "https://weatherseal.com/"},
            ],
        },
    },
    {
        "id": "quotation-drafting",
        "agentic": True,
        "name": "AI Quotation Drafting Agent",
        "effort": "advanced",
        "badge": "proposed",
        "blurb": "Turns a rough customer requirement into a properly formatted, ready-to-send quote — the owner just approves and sends.",
        "industries": ["b2b-manufacturer", "export-trading", "interior-designer", "building-materials-showroom", "wholesale-distributor"],
        "pain": {
            "eyebrow": "The Moment", "title": "A quote that takes 30 minutes to type up",
            "body": "Turning a customer's rough requirement into a clean, formatted quote is slow enough that it often goes out a day late.",
            "chat": [("meta", "Requirement received 9am · quote finally sent 6pm · buyer already compared elsewhere")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "Drafted the moment the requirement lands",
            "body": "The raw requirement is turned into a formatted quote draft automatically — just review and send.",
            "chat": [
                ("in", "Need 2000 units, spec attached, budget-conscious."),
                ("meta", "Quote draft ready: 2000 units, tiered pricing, valid 7 days"),
                ("out", "Quote sent ✓"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Quotes that go out same-day, by default",
                    "body": "Speed becomes the default instead of the exception that happens when someone has spare time.",
                    "stat_label": "Time to draft a quote", "stat_from": "30+ minutes", "stat_to": "Under 2 minutes"},
    },
    {
        "id": "competitor-price-watch",
        "agentic": False,
        "name": "Competitor Price-Watch Alert",
        "effort": "advanced",
        "badge": "proposed",
        "blurb": "Checks competitors' public listings and prices periodically, and alerts the owner the moment something changes.",
        "industries": ["retail-store", "wholesale-distributor", "automobile-showroom", "building-materials-showroom", "gym-fitness-chain"],
        "pain": {
            "eyebrow": "The Moment", "title": "The competitor moved, and nobody noticed",
            "body": "A nearby competitor quietly drops a price or launches an offer. Customers notice immediately. The business finds out weeks later, if at all.",
            "chat": [("meta", "Competitor offer live 3 weeks · noticed only after regular customers started asking about it")],
            "accent": "red",
        },
        "fix": {
            "eyebrow": "The Fix", "title": "An alert, the same day it happens",
            "body": "Public listings and prices are checked automatically — a change triggers an alert immediately.",
            "chat": [
                ("meta", "⚠️ Competitor dropped price on their listing — alert sent"),
                ("out", "Heads up: [Competitor] is now offering 10% off. Want to respond?"),
            ],
            "accent": "green",
        },
        "growth": {"eyebrow": "The Growth", "title": "Reacting same-day instead of weeks late",
                    "body": "Being the last to know stops being the default.",
                    "stat_label": "Time to notice a competitor's price move", "stat_from": "Weeks, if ever", "stat_to": "Same day"},
    },
]

# Curated, capped secondary automations shown per Industry page + Custom Pack
# (kept to 2-3 per industry — deliberately narrower than each module's
# broader `industries` tag list above, which is used for Demos search/filter).
INDUSTRY_MODULES = {
    "export-trading": ["invoice-reminder"],
    "hospital": ["booking-reminder", "claim-email-dispatch"],
    "coaching-institute": ["payment-reconciliation"],
    "real-estate-developer": ["invoice-reminder"],
    "b2b-manufacturer": ["invoice-reminder"],
    "private-school": ["payment-reconciliation"],
    "diagnostic-lab": ["booking-reminder", "claim-email-dispatch"],
    "wedding-planner-banquet": ["invoice-reminder", "review-reply"],
    "gym-fitness-chain": ["payment-reconciliation", "review-reply"],
    "ca-legal-firm": ["invoice-reminder", "booking-reminder"],
    "interior-designer": ["invoice-reminder", "booking-reminder"],
    "retail-store": ["stock-check-reserve", "reorder-nudge", "review-reply"],
    "automobile-showroom": ["booking-reminder", "review-reply"],
    "building-materials-showroom": ["invoice-reminder", "stock-check-reserve"],
    "wholesale-distributor": ["invoice-reminder", "payment-reconciliation", "reorder-nudge"],
}

# ------------------------------------------------------------------
# FLAGSHIP — the negotiation/instant-response agent. Bigger than a
# standard module (4 scenes, not a pain/fix pair), gets its own full
# cinematic demo page and top billing on Agentic Use Cases.
# ------------------------------------------------------------------
NEGOTIATION_AGENT = {
    "id": "negotiation-agent",
    "name": "Instant-Response + Negotiation Agent",
    "badge": "proposed",
    "agentic": True,
    "blurb": "From being the listing that actually gets tapped, to an instant reply, a quote, a negotiation that matches a named competitor's price, a payment link close, and the follow-up + referral that brings the next order.",
    "stages": [
        {
            "kind": "search", "eyebrow": "The Moment", "title": "Found on Google. Skipped in two seconds.",
            "body": "A customer searches and sees 4-5 businesses. The ones without a complete profile — no posts, no website, no way to message — get scrolled past without a second thought.",
            "accent": "red",
            "query": "AC repair near me",
            "winner_idx": 0,
            "results": [
                {"name": "CoolBreeze AC Repair", "rating": 4.5, "reviews": 180, "distance": "0.9 km", "complete": True},
                {"name": "Sharma AC Services", "rating": 4.0, "reviews": 15, "distance": "1.1 km", "complete": False},
                {"name": "Patil Air Solutions", "rating": 3.8, "reviews": 40, "distance": "1.6 km", "complete": True},
                {"name": "Fresh Air Cooling", "rating": 3.6, "reviews": 10, "distance": "2.0 km", "complete": False},
            ],
        },
        {
            "kind": "search", "eyebrow": "The Fix — Step 1", "title": "A profile that actually gets chosen",
            "body": "Posts, a website link, and a WhatsApp button turn a listing into the obvious choice — before a single message is even sent.",
            "accent": "green",
            "query": "AC repair near me",
            "winner_idx": 1,
            "results": [
                {"name": "CoolBreeze AC Repair", "rating": 4.5, "reviews": 180, "distance": "0.9 km", "complete": True},
                {"name": "Sharma AC Services", "rating": 4.0, "reviews": 15, "distance": "1.1 km", "complete": True},
                {"name": "Patil Air Solutions", "rating": 3.8, "reviews": 40, "distance": "1.6 km", "complete": True},
                {"name": "Fresh Air Cooling", "rating": 3.6, "reviews": 10, "distance": "2.0 km", "complete": False},
            ],
        },
        {
            "kind": "chat_screen", "eyebrow": "The Fix — Step 2", "title": "Replied before they could message anyone else",
            "body": "The inquiry gets an instant, pre-drafted response — and a smart follow-up question, not just a generic \"thanks for reaching out.\"",
            "accent": "green", "contact": "Vikram Joshi", "status": "Online",
            "chat": [
                ("in", "Hi, need AC repair, what's the process?"),
                ("out", "Hi! Happy to help — is it a split AC or window unit, and what's the issue?"),
                ("in", "Split AC, not cooling properly."),
            ],
        },
        {
            "kind": "chat_screen", "eyebrow": "The Fix — Step 3", "title": "A quote, not a guessing game",
            "body": "Enough detail is already in hand to send a real quote — not a vague \"we'll get back to you.\"",
            "accent": "green", "contact": "Vikram Joshi", "status": "Online",
            "chat": [
                ("out", "Got it — gas refill + service, ₹899 total. Technician can come today 👇"),
            ],
        },
        {
            "kind": "chat_screen", "eyebrow": "The Fix — Step 4", "title": "When they want to negotiate, it doesn't lose the deal",
            "body": "Most owners lose the back-and-forth to whoever's more flexible on a call. The agent handles it instead — confidently, within limits set in advance.",
            "accent": "green", "contact": "Vikram Joshi", "status": "Online",
            "chat": [
                ("in", "₹899 is a bit much, can you do better?"),
                ("out", "I can help with that! Did another provider quote you something?"),
                ("in", "Yeah, CoolBreeze quoted ₹699."),
                ("out", "We'll match that at ₹699 — and ours includes a 30-day warranty. Shall I book it?"),
                ("in", "Deal, book it."),
            ],
        },
        {
            "kind": "payment", "eyebrow": "The Fix — Step 5", "title": "A payment link closes more than a phone call",
            "body": "Once it's agreed, a payment link goes out immediately — people commit to a link faster than they commit out loud on a call.",
            "accent": "green",
            "business": "Sharma AC Services", "amount": "₹699", "paid": True,
        },
        {
            "kind": "stat", "eyebrow": "The Growth", "title": "One customer becomes many",
            "body": "A follow-up after service brings the next order. A referral offer turns a happy customer into a new one — automatically, every time.",
            "stat_label": "One satisfied customer",
            "stat_from": "One sale, then silence",
            "stat_to": "Repeat orders + referrals",
        },
    ],
}

PRICING_PACKS = [
    {
        "name": "Go Digital Pack",
        "price": "₹2,999/mo",
        "price_note": "billed yearly — ₹35,988 total, one time",
        "support_price": "₹750/mo",
        "support_note": "support, billed yearly — ₹8,999 total",
        "tag": "Entry",
        "includes": ["Google Business Profile setup + optimization", "Business website", "Ongoing content refresh — covered by annual support"],
    },
    {
        "name": "Growth Pack",
        "price": "One-time implementation, quoted",
        "price_note": "",
        "support_price": "Annual support, quoted",
        "support_note": "",
        "tag": "Most Popular",
        "includes": ["Everything in Go Digital", "Booking Engine (appointments / visits / trials)"],
    },
    {
        "name": "Expansion Pack",
        "price": "One-time implementation, quoted",
        "price_note": "",
        "support_price": "Annual support, quoted",
        "support_note": "",
        "tag": "Scale",
        "includes": ["Everything in Growth", "Automations — invoice generation and more"],
    },
]

CUSTOM_HAVE = ["Already have a website", "Already have a Google Business Profile"]
CUSTOM_ADDONS = [
    "Invoice / quote tool", "WhatsApp reminder tool", "Payment portal",
    "Multilingual add-on", "Google Ads landing page", "Customer database export",
    "WhatsApp broadcast", "Review-reply templates", "Missed-call-to-WhatsApp auto-reply",
]

# ------------------------------------------------------------------
# BLOG_POSTS — real, researched posts (not stubs). Every stat here is
# from a checked external source (see "citations" per post) — same
# honesty rule as the Proven/Proposed badges. Most industry-specific
# posts still land in V2; these 4 are live now.
# ------------------------------------------------------------------
BLOG_POSTS = [
    {
        "slug": "why-shops-lose-to-blinkit-zepto",
        "title": "Why Your Favourite Local Shop Is Losing to Blinkit, Zepto & Instamart",
        "dek": "It's not price, and it's not loyalty. It's one specific moment your shop can't win — until it can.",
        "tag": "Retail / Kirana",
        "read_time": "5 min read",
        "related_industry": "retail-store",
        "body": [
            {"type": "p", "text": "You know the shop. Twenty years in the same spot, the owner remembers your order before you finish saying it, and there's always a little extra khata patience when the month runs long. And yet — it's struggling. Not because anyone stopped liking it. Because of one specific moment where it simply isn't in the running anymore."},
            {"type": "stat", "stat": "Nearly 80% of consumers have shifted at least a quarter of their grocery spending to quick-commerce apps, and over 2 lakh kirana stores closed in a single year.", "source": "Outlook Business, citing AICPDF", "url": "https://www.outlookbusiness.com/explainers/kirana-stores-are-losing-the-battle-against-zepto-blinkit-and-instamart"},
            {"type": "h2", "text": "The store isn't losing on trust. It's losing on one moment."},
            {"type": "p", "text": "Here's the part that gets missed in most of the \"kirana vs quick-commerce\" coverage: local stores still hold 88% of India's retail food market. That's not a business in freefall — that's a business that's still winning almost every moment it's actually competing in. The loss is concentrated in exactly one scenario: the customer who can't physically walk in tonight, who has no way to check what's actually on the shelf and order it from home."},
            {"type": "p", "text": "When that moment happens, the shop doesn't lose because Blinkit is cheaper or more trusted. It loses because it's the only option that showed up. A regular customer messages on WhatsApp asking if there's atta and milk in stock — and either nobody replies, or nobody actually knows what's on the shelf right now. The app answers in nine minutes. The shop never even finds out it lost the sale."},
            {"type": "h2", "text": "What quick-commerce actually has that a kirana store doesn't"},
            {"type": "p", "text": "It isn't scale, and it isn't price — it's exactly two things: a live view of what's in stock, and a frictionless way to order it from home. That's it. Everything else — the relationship, the credit, the zero delivery markup, the guy who saves the good mangoes for regulars — those are advantages a delivery app structurally cannot replicate. The gap is narrow. So is the fix."},
            {"type": "h2", "text": "The fix is not \"build an e-commerce site\""},
            {"type": "p", "text": "Nobody needs a kirana store to become a mini-Amazon. What closes the gap is much smaller: a WhatsApp catalog tied to what's genuinely on the shelf right now, so a message gets an honest, instant answer — in stock or not — with a pay-or-khata option and a delivery window. That's the entire mechanism. It doesn't touch pricing, doesn't touch the in-store experience, and it keeps every advantage a quick-commerce app can't touch."},
            {"type": "p", "text": "The shops that will still be here in five years aren't the ones that panic-built a website. They're the ones that closed this one gap and kept doing everything else the same."},
        ],
    },
    {
        "slug": "small-exporters-losing-to-bangladesh-vietnam",
        "title": "The Real Reason Small Indian Exporters Are Losing Orders to Bangladesh and Vietnam",
        "dek": "Same quality. Similar price. The order still goes elsewhere — and it's rarely about the product.",
        "tag": "Export / Trading",
        "read_time": "5 min read",
        "related_industry": "export-trading",
        "body": [
            {"type": "p", "text": "A buyer sends the same inquiry to three suppliers. Yours has the better fabric, comparable pricing, a decade of export experience — and still, the order goes to a factory in Dhaka or Ho Chi Minh City. It's a pattern enough exporters have lived through that it's worth asking: what's actually happening in that gap?"},
            {"type": "stat", "stat": "India's share of global apparel, textile, leather and footwear exports slipped from a 2013 peak of 4.5% to 3.5% by 2022, as Bangladesh (5.1%) and Vietnam (5.9%) pulled ahead — a gap the World Bank links partly to lower digital adoption in these sectors.", "source": "Deccan Herald, citing World Bank", "url": "https://www.deccanherald.com/amp/story/business%2Feconomy%2Findia-losing-to-smaller-rivals-like-bangladesh-and-vietnam-in-manufacturing-world-bank-says-3176072"},
            {"type": "h2", "text": "This isn't a small-player problem — it's most of India's export engine"},
            {"type": "p", "text": "MSMEs account for more than 48.5% of India's exports, per the Ministry of MSME's own 2025-26 Annual Report. So when a report talks about India losing export share to smaller economies, it isn't an abstract macro trend — it's happening one missed RFQ at a time, largely to businesses exactly this size."},
            {"type": "stat", "stat": "The MSME sector contributes around 31.1% of India's GDP and accounts for more than 48.5% of the country's exports.", "source": "Ministry of MSME, Annual Report 2025-26", "url": "https://www.msme.gov.in/static/uploads/2026/05/1bfda06b460e72543530b40817573495.pdf"},
            {"type": "h2", "text": "The World Bank's \"digital adoption gap\" is smaller and more specific than it sounds"},
            {"type": "p", "text": "It's tempting to read \"digital adoption gap\" as something abstract — supply-chain software, ERP systems, factory-floor automation. For most exporters losing orders today, it's much simpler than that: a buyer's WhatsApp message or portal inquiry sits unread for two days while a competing factory replies same-day with a catalog, spec sheet, and quote. The buyer doesn't wait to find out if your product is better. They've already moved on by the time you reply."},
            {"type": "p", "text": "Vietnam and Bangladesh's fastest-growing exporters aren't necessarily more sophisticated manufacturers. Many are simply faster and more consistent in that first 48 hours — a live catalog with landed-cost-ready specs, an inquiry that reaches the right person instantly, a quote template that goes out the same day instead of whenever someone has a free afternoon."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "Not a digital transformation. Three specific things: a catalog that's always current, an inquiry-routing system so nothing sits in a shared inbox, and quote templates that make same-day response the default rather than something that happens when someone remembers. That's the entire mechanism separating suppliers who keep the order from ones who lose it to a factory that simply answered first."},
        ],
    },
    {
        "slug": "local-gyms-losing-to-franchise-chains",
        "title": "Why Local Gyms Are Losing Members to Franchise Chains — Without a Franchise Budget to Fight Back",
        "dek": "It isn't the equipment, and it isn't the trainers. It's what happens in the 48 hours after someone says \"I'll try a class.\"",
        "tag": "Gym / Fitness Chain",
        "read_time": "4 min read",
        "related_industry": "gym-fitness-chain",
        "body": [
            {"type": "p", "text": "Your gym has real trainers who know every member's name, a community that actually shows up, and equipment that's perfectly fine. And yet the franchise that opened two blocks away keeps pulling in your trial sign-ups. It's not the equipment. It's what happens — or doesn't — right after someone says they want to try a class."},
            {"type": "stat", "stat": "Cult.fit — India's largest fitness chain, over 230 centers — is now expanding its franchise model deep into Tier 2 and Tier 3 cities, the exact towns independent gyms used to have entirely to themselves.", "source": "Indian Retailer", "url": "https://www.indianretailer.com/news/cult-fit-to-build-presence-in-smaller-markets-via-franchise-model.n11772"},
            {"type": "h2", "text": "Franchises don't out-train you. They out-follow-up you."},
            {"type": "p", "text": "A promo goes out, DMs flood in asking about a free trial class — and that's usually where it ends. Somebody's meant to reply, book the slot, and follow up after the class with a membership offer, but in a small gym that's someone's already-full afternoon, not a system. A franchise chain runs that exact sequence automatically, every single time, for every single trial. The gap isn't in facilities. It's in whether \"I'll try a class\" reliably turns into a booked slot and a follow-up message — or quietly goes nowhere."},
            {"type": "h2", "text": "The real cost isn't the members you lose. It's the ones you never see leave."},
            {"type": "p", "text": "Most local gyms never find out how many trial inquiries went cold, because there's no system tracking it — the DM just stops getting replies to. A promo that brought in fifty trial messages might convert two or three, not because the class wasn't good, but because forty-seven of them never got a follow-up at all."},
            {"type": "h2", "text": "Fighting back doesn't require a franchise budget"},
            {"type": "p", "text": "It requires exactly two things a franchise's tech stack does automatically: a WhatsApp flow that books the trial slot the moment someone asks, and an automatic follow-up message right after the class with a membership offer while the experience is still fresh. Neither needs new equipment, new trainers, or a rebrand. It needs the follow-up to stop depending on someone remembering to do it."},
        ],
    },
    {
        "slug": "msme-shutdown-crisis-digital-survival",
        "title": "The Quiet MSME Shutdown Crisis: What 75,000 Closed Businesses Are Actually Telling Us",
        "dek": "The closures are accelerating. The gap between what MSMEs know they need and what they've actually done about it is the real story.",
        "tag": "MSME / All Industries",
        "read_time": "6 min read",
        "related_industry": None,
        "body": [
            {"type": "p", "text": "75,082 MSMEs shut down across India over the last five years, according to the government's own Udyam Portal data. That number alone is sobering. What's more telling is the shape of the curve."},
            {"type": "stat", "stat": "MSME closures on the Udyam Portal: 175 in FY21, rising to 6,222 in FY22, 13,290 in FY23, 19,828 in FY24, and 35,567 in FY24-25 alone — nearly half of all five-year closures happening in the most recent year.", "source": "Deccan Herald, citing Government of India data", "url": "https://www.deccanherald.com/business/more-than-75-000-msmes-shut-shop-in-past-five-years-govt-3452060"},
            {"type": "p", "text": "That's not a plateau. It's an acceleration — closures nearly doubled year-on-year in the most recent period alone. And this is happening to a sector that isn't marginal to the economy — it's the backbone of it."},
            {"type": "stat", "stat": "The MSME sector contributes around 31.1% of India's GDP and accounts for more than 48.5% of the country's exports — the country's second-largest source of employment after agriculture.", "source": "Ministry of MSME, Annual Report 2025-26", "url": "https://www.msme.gov.in/static/uploads/2026/05/1bfda06b460e72543530b40817573495.pdf"},
            {"type": "h2", "text": "The paradox: MSMEs know exactly what they need. Most haven't done it."},
            {"type": "p", "text": "This is the part that should reframe how anyone thinks about the crisis. It isn't that small businesses don't understand digital's importance — they clearly do."},
            {"type": "stat", "stat": "80% of Indian MSMEs expect digital procurement to drive growth, despite only 30-40% of them currently having real digital spend.", "source": "India SME Forum & Amazon Business report", "url": "https://www.forbesindia.com/article/news/deep-dive/four-in-five-msmes-expect-digital-procurement-to-drive-growth/2996807/1"},
            {"type": "p", "text": "And the digitization that has happened is shallow, not deep: 90% of MSMEs now accept digital payments, but only 18% have accessed any digital lending platform. Businesses have digitized the easiest, most visible layer — taking a UPI payment — while the harder, more consequential layers (being found, following up, converting an inquiry into a sale) remain almost exactly as manual as they were a decade ago."},
            {"type": "h2", "text": "Why a small digital gap becomes a fatal one"},
            {"type": "p", "text": "Across the stories in this collection — kirana stores losing home-bound orders to quick-commerce, exporters losing RFQs to faster-replying rivals in Bangladesh and Vietnam, gyms losing trial sign-ups to franchises with automated follow-up — the pattern repeats: it's never the whole business that's failing. It's one specific, narrow moment where a competitor with a slightly better digital reflex wins the customer outright. But because that one moment often represents the growth an already-stable business needed to survive rising costs, even a 15-20% shift in customer behavior toward \"whoever responds fastest\" is enough to tip a shop from steady to shut."},
            {"type": "h2", "text": "The businesses in the closure numbers, and the ones that will still be open in five years"},
            {"type": "p", "text": "The difference rarely comes down to which business built the more sophisticated digital operation. It comes down to which one closed its one specific leak — the missed WhatsApp reply, the invisible Google listing, the follow-up that never happened — while everything else about how they ran the business stayed exactly the same. That's a narrower, cheaper, and far more survivable fix than \"go digital\" makes it sound."},
        ],
    },
    {
        "slug": "hospital-multi-branch-appointment-booking-trust-gap",
        "title": "Why Your Hospital's Fourth Branch Isn't Growing Like the First Three",
        "dek": "The doctors are just as good at every branch. It's the front desk at the new one where patients actually go missing.",
        "tag": "Hospital (multi-branch)",
        "read_time": "5 min read",
        "related_industry": "hospital",
        "body": [
            {"type": "p", "text": "A patient loyal to your hospital's original branch for a decade calls the new branch that opened across town last year, asking if the same cardiologist has a Saturday slot there too. The person answering doesn't know — that branch runs its own diary, the receptionist has never met the doctor, and the call ends with \"let me check and call you back.\" It never happens. The patient books elsewhere. Nothing about the care was ever in question. The hospital simply couldn't answer a basic question about itself fast enough."},
            {"type": "stat", "stat": "India's hospital sector is projected to sustain 11-12% annual growth, driven by rising insurance penetration, medical tourism and continued private-sector expansion into new cities.", "source": "IBEF, citing CareEdge Ratings", "url": "https://www.ibef.org/news/india-s-hospital-sector-to-sustain-11-12-growth-driven-by-insurance-penetration-and-medical-tourism-careedge"},
            {"type": "h2", "text": "The expansion math works until branch four"},
            {"type": "p", "text": "It's tempting to treat growing pains as a facilities or staffing problem. But most multi-branch hospital groups don't lose patients because a new branch is under-equipped — they lose them because the systems that made the first branch trustworthy, a known booking process, a front desk that could always answer \"is Dr. X in today,\" don't automatically travel to branch four, five and six. Growth outpaces the informal, relationship-based systems that quietly carried the original branch for years."},
            {"type": "stat", "stat": "In a cross-sectional study of the Indian general population, 68.8% of respondents said they actively make enquiries about healthcare facilities and practitioners before deciding where to seek care.", "source": "National Journal of Community Medicine", "url": "https://njcmindia.com/index.php/file/article/view/3855"},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "Closing this gap rarely means better doctors or bigger buildings. It means closing the \"which branch, which doctor, which slot\" answer gap: real-time, branch-accurate schedules that don't require a phone transfer to confirm; a single number or WhatsApp line that can book a slot at whichever branch is nearest, instantly, instead of routing a caller into a guessing game; and an automatic reminder the day before, so a slot that took two calls to book doesn't fall to a no-show. None of that touches clinical quality. It's the layer that decides whether a patient who already trusts the brand can actually get an appointment at the branch nearest them."},
        ],
    },
    {
        "slug": "coaching-institute-enquiry-enrollment-leak",
        "title": "The Batch Is Full in Your Head. The Enquiry List Says Otherwise.",
        "dek": "Coaching institutes aren't short on demand. They're short on a system that turns a WhatsApp \"what's the fee\" into a seat filled.",
        "tag": "Coaching Institute",
        "read_time": "5 min read",
        "related_industry": "coaching-institute",
        "body": [
            {"type": "p", "text": "It's April, a fresh batch is about to start, and forty enquiry messages are sitting across WhatsApp, a paper register and a faculty member's personal phone. A parent asks about the NEET batch timing and fee, and gets an answer two days later, once the counsellor is free. By then they've already enrolled at the institute down the road that replied within the hour."},
            {"type": "stat", "stat": "27% of Indian students availed private coaching in the 2024-25 academic year — 30.7% in urban areas versus 25.5% in rural areas — with average household spending on coaching rising sharply at each stage of school.", "source": "Business Standard, citing MoSPI's Comprehensive Modular Survey: Education (CMS:E) 2025", "url": "https://www.business-standard.com/education/news/education-mospi-survey-private-school-government-scholarship-fees-coaching-tuition-urban-rural-125082601316_1.html"},
            {"type": "h2", "text": "The demand isn't the problem. The intake funnel is."},
            {"type": "p", "text": "A government survey confirming that more than a quarter of India's students now take private coaching should be good news for every institute owner — and it is. The catch is that this demand doesn't arrive pre-sorted. It arrives as a flood of enquiries during a handful of admission windows each year, all landing in the same inboxes and the same unpaid intern's WhatsApp at once. The institutes that grow aren't necessarily the ones with the strongest faculty on paper — they're the ones whose enquiries never sit unanswered long enough for a parent to call the next number on their list."},
            {"type": "stat", "stat": "India's coaching institutes market is valued at USD 7.2 billion in 2025 and projected to reach USD 17.8 billion by 2034.", "source": "IMARC Group", "url": "https://www.imarcgroup.com/india-coaching-institutes-market"},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A same-day, ideally same-hour, response to every enquiry regardless of which counsellor happens to be free; batch and fee information available instantly instead of \"let me check with sir\"; and a structured follow-up sequence for the parents who don't decide on the first call, since most enrollment decisions take several touchpoints, not one. None of it changes how the batch is taught. It changes whether the enquiry list turns into the batch roster."},
        ],
    },
    {
        "slug": "real-estate-developer-portal-lead-response-gap",
        "title": "The Lead Cost ₹800. It Went Cold Because Nobody Called Back for Six Hours.",
        "dek": "The site is good and the price is fair — the buyer still books a visit with whichever developer called first.",
        "tag": "Real Estate Developer",
        "read_time": "4 min read",
        "related_industry": "real-estate-developer",
        "body": [
            {"type": "p", "text": "A buyer scrolling a property portal at 9pm submits interest in three projects in the same locality. Two call back before midnight. The third calls back the next afternoon — after the buyer has already scheduled a site visit with a competitor. That third project wasn't worse. It just wasn't first."},
            {"type": "stat", "stat": "Nearly 60% of the entire property-buying journey — from search to shortlisting — is now conducted online, up from 39% before the pandemic.", "source": "ANAROCK Consumer Sentiment Survey, H1 2025", "url": "https://websitemedia.anarock.com/media/Homebuyer_Sentiment_Survey_H1_2025_e9f8bd6e5e.pdf"},
            {"type": "h2", "text": "The buyer already did the shopping online. Sales teams are often still catching up."},
            {"type": "p", "text": "This doesn't mean developers need slicker websites or another portal listing. It means the moment that decides which project gets the site visit has already moved from the sales office to a portal inbox and a WhatsApp thread — and most sales teams are still organized around office hours, not an inbox that fills up at 9pm from three different portals at once."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "Instant acknowledgment of every portal lead, even an automated one, before the buyer's attention moves to the next listing; a booking flow that lets a shortlisted buyer pick a site-visit slot without waiting for a callback; and a follow-up cadence for the buyer who didn't book on the first contact, since for most buyers the eventual decision comes after more than one conversation. None of it requires a lower price or a better location. It requires being the developer who answered while the buyer was still looking."},
        ],
    },
    {
        "slug": "b2b-manufacturer-rfq-response-speed",
        "title": "Your Factory Had the Better Price. The Order Still Went to Whoever Replied First.",
        "dek": "On IndiaMART and TradeIndia, the RFQ doesn't wait for anyone — least of all a supplier who checks messages once a day.",
        "tag": "B2B Manufacturer",
        "read_time": "5 min read",
        "related_industry": "b2b-manufacturer",
        "body": [
            {"type": "p", "text": "A buyer sends an RFQ for 5,000 units to four listed suppliers on a B2B portal at the same time. Three reply within hours with a spec sheet and a price. The fourth — with genuinely better production capability — replies two days later, by when the buyer has already issued a purchase order elsewhere. The RFQ wasn't lost on merit. It was lost to the clock."},
            {"type": "stat", "stat": "IndiaMART handled 106 million unique business enquiries in FY 2024-25 across its supplier base — a volume of live buyer demand that rewards whichever supplier responds first, not necessarily whoever has the best product.", "source": "IndiaMART InterMESH, Annual Report FY 2024-25", "url": "https://investor.indiamart.com/files/IndiaMART_Annual_Report_FY_2024-25.pdf"},
            {"type": "h2", "text": "The order isn't lost on quality. It's lost in the queue."},
            {"type": "p", "text": "Manufacturers spend real money and years building production capability, certifications, and pricing that can compete. Almost none of that shows up in the moment that actually decides most RFQs — the first 24 hours after a buyer posts an enquiry, when it's sitting simultaneously in three or four other suppliers' inboxes too. A factory doesn't need to out-manufacture a competitor to lose an order to them. It only needs to out-wait them."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A spec sheet and price template that can go out inside a few hours, not a few days, so a quote never waits on someone with a free afternoon; routing enquiries to whoever's actually available instead of a shared inbox nobody owns; and a same-day follow-up on every RFQ that doesn't convert immediately, since many orders go to whoever's still in the conversation when the buyer is finally ready to decide. None of it touches the factory floor. It decides whether the factory floor ever sees the order."},
        ],
    },
    {
        "slug": "private-school-admission-enquiry-conversion",
        "title": "The Waitlist Filled Itself. The Parent Who Called on Day One Went Elsewhere.",
        "dek": "Private schools aren't short on applicants. They're short on a system that keeps the fastest-deciding parents from walking to the school next door.",
        "tag": "Private School",
        "read_time": "5 min read",
        "related_industry": "private-school",
        "body": [
            {"type": "p", "text": "It's admission season, the front office is swamped, and a parent calls asking about the Grade 1 seat. They're told to \"fill the form and someone will call back\" — and they do, twice — before enrolling their child at a school that scheduled a campus tour the same week."},
            {"type": "stat", "stat": "Private unaided school enrollment rose 6.9% to 90 million students in 2023-24, even as government school enrollment fell 6.4% to 127.5 million in the same year.", "source": "IndiaSpend", "url": "https://www.indiaspend.com/data-viz/dataviz-private-schools-show-better-outcomes-but-govt-schools-are-catching-up-965449"},
            {"type": "h2", "text": "The competition isn't government schools anymore. It's the private school two streets over."},
            {"type": "p", "text": "As more parents choose private schooling, the fight for a specific school's seats increasingly happens between private schools competing for the same pool of increasingly selective parents — not between private and government education. A parent who has already decided to pay private fees is now comparing three or four schools' admission processes, and the one that responds fastest, explains its process clearest and books a campus visit soonest usually gets the form submitted first."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "An admission enquiry that gets a real, same-day answer instead of \"someone will call back\"; a clear, upfront explanation of process, fees and next steps so parents aren't left guessing; and a follow-up sequence for families who enquired but haven't yet completed the form. In a competitive intake season, most admission decisions come down to whichever school stayed easiest to reach through the process."},
        ],
    },
    {
        "slug": "diagnostic-lab-home-collection-booking-friction",
        "title": "Your Lab Is Just as Accurate. The Big Chain's App Is Just Easier to Book.",
        "dek": "Most of India's diagnostic testing still happens outside the big chains — the leak is in how easily a patient can book a home sample, not in the quality of the test.",
        "tag": "Diagnostic Lab",
        "read_time": "4 min read",
        "related_industry": "diagnostic-lab",
        "body": [
            {"type": "p", "text": "A regular patient needs a routine blood test, calls the neighbourhood lab to ask about home collection, gets put on hold, and decides to just open a large chain's app instead — books a slot, gets a confirmation and a time window in under two minutes. Not because the local lab is less accurate. Because it took two minutes instead of five on hold."},
            {"type": "stat", "stat": "Of India's diagnostic testing market, unorganized standalone labs account for roughly 46%, hospital-based labs 37%, and organized chains just 17% — meaning independent labs still hold most of the market even as chains expand.", "source": "CARE Ratings, \"Indian Diagnostics Industry\" opinion piece", "url": "https://www.careratings.com/uploads/newsfiles/1763463740_Indian%20Diagnostics%20Industry_%20Opinion%20Piece.pdf"},
            {"type": "h2", "text": "The independent lab isn't losing the market. It's losing the booking moment."},
            {"type": "p", "text": "A 17% organized share means the overwhelming majority of testing still happens at local, independent labs — a real, durable advantage built on trust and proximity that a chain's brand can't instantly replicate. What chains have built instead is a frictionless booking flow for home collection, plus a report that lands on a phone before the local lab has even finished processing the sample. That's a narrow, specific gap, not an accuracy or trust gap."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A home-collection booking that takes a message and returns a confirmed time window, not a hold-and-callback; digital report delivery that reaches the patient as fast as a chain's app; and a simple reminder system for repeat or follow-up tests, since most patients default to whichever lab was least friction last time. None of it requires new equipment. It requires the booking-to-report journey to feel as fast as the chain's app, even though the lab itself is exactly the one down the street."},
        ],
    },
    {
        "slug": "wedding-planner-banquet-peak-season-quote-speed",
        "title": "Six Weeks, 32 Lakh Weddings, and a Quote That Went Out Two Days Too Late",
        "dek": "In wedding season, every couple is messaging four vendors at once — the booking goes to whoever answers with a quote first.",
        "tag": "Wedding Planner / Banquet",
        "read_time": "5 min read",
        "related_industry": "wedding-planner-banquet",
        "body": [
            {"type": "p", "text": "It's peak wedding week. A couple messages five banquet halls and planners the same evening, asking for a quote for a 300-guest function. Four reply within a day with a rough package. The fifth — genuinely busy running that week's wedding — replies three days later, to find the date already blocked elsewhere."},
            {"type": "stat", "stat": "An estimated 32 lakh weddings were expected across India in a single wedding-season window (November 4 – December 14), generating around ₹3.75 lakh crore in business — a volume of simultaneous demand that compresses much of the year's booking decisions into a few weeks.", "source": "Deccan Herald, citing the Confederation of All India Traders (CAIT)", "url": "https://www.deccanherald.com/amp/story/india%2F32-lakh-weddings-in-india-during-november-4-december-14-to-generate-rs-375-lakh-crore-business-cait-1160192.html"},
            {"type": "h2", "text": "It isn't a slow-season problem. It's a compressed-demand problem."},
            {"type": "p", "text": "Wedding planners and banquet owners rarely lose bookings because of a weak year — the numbers above show the opposite, an enormous volume of decisions moving through a short calendar window. The risk is structural: when tens of lakhs of families are all deciding, comparing and booking in the same compressed weeks, a planner who's genuinely occupied delivering this week's wedding has no time left to write next month's quote, and the couple waiting for it doesn't wait long before moving to whoever answered first."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A quote template that can go out within hours even during the busiest week, instead of waiting for a free afternoon; a live availability calendar so a couple isn't left wondering if a date is even open; and a structured follow-up for quoted-but-undecided couples, since a deposit rarely gets paid on the first message. None of it means taking more events than the team can actually deliver. It means not losing the ones already within reach to a slower reply."},
        ],
    },
    {
        "slug": "ca-legal-firm-client-intake-response-speed",
        "title": "The Client Called Three CAs Before 10 AM. Yours Called Back After Lunch.",
        "dek": "Most Indian CA and law firms are one or two people deep — which is exactly why the first firm to respond usually wins the client.",
        "tag": "CA / Legal Firm",
        "read_time": "5 min read",
        "related_industry": "ca-legal-firm",
        "body": [
            {"type": "p", "text": "A small business owner gets an urgent GST notice, calls their regular CA's office, doesn't get through, and — with the deadline looming — calls two more numbers off Google before lunch. Whoever picks up and explains the next steps clearly gets the client, often not just for this one filing."},
            {"type": "stat", "stat": "India has over 1,00,000 registered CA firms, and more than 72% of them are single-partner (sole proprietorship) practices — meaning most Indian CA firms are exactly one or two people managing intake, compliance and client work at once.", "source": "The Finance Story, citing ICAI data", "url": "https://thefinancestory.com/mid-sized-indian-ca-firms-employing-20-percent-audit-workforce"},
            {"type": "h2", "text": "The client isn't leaving for a bigger firm. They're leaving for whoever answered."},
            {"type": "p", "text": "With the profession this fragmented, competition for a new client rarely comes down to expertise — most CAs and small law firms handling SME and individual work are competent at the basics. It comes down to which of the three or four numbers a worried client dialled actually picked up, called back the same day, and said clearly what to send over next. A firm can lose a client to a \"bigger, more digital\" competitor without that competitor being bigger at all — just faster to respond."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A system for new-client enquiries that doesn't depend on whoever happens to be free between meetings; a simple, repeatable checklist for what documents a client needs to send, so intake doesn't stall on back-and-forth; and a follow-up for enquiries that went quiet, since a client who didn't hear back in a day has usually already called someone else. None of it requires new legal or accounting expertise. It requires the practice to feel as responsive as the firm advertising a faster turnaround down the road."},
        ],
    },
    {
        "slug": "interior-designer-lead-to-consultation-conversion",
        "title": "They Filled Out Your Contact Form. Then They Hired the Designer Who Called First.",
        "dek": "India's interior design market is worth tens of billions of dollars — most of it going to whoever turns an enquiry into a site visit fastest.",
        "tag": "Interior Designer",
        "read_time": "4 min read",
        "related_industry": "interior-designer",
        "body": [
            {"type": "p", "text": "A couple who just got their new apartment keys fills out contact forms on three designers' Instagram pages the same weekend, asking for a rough estimate. Two reply within a day with a ballpark range and a consultation slot. The third replies four days later, after the couple has already paid a token advance elsewhere."},
            {"type": "stat", "stat": "India's interior design market was valued at USD 36.89 billion in 2025 and is projected to reach USD 74.73 billion by 2034, growing at a CAGR of 8.16% — a genuinely large and fast-expanding market, not one dominated only by large firms.", "source": "IMARC Group", "url": "https://www.imarcgroup.com/india-interior-design-market"},
            {"type": "h2", "text": "The market is growing faster than most designers' follow-up systems"},
            {"type": "p", "text": "A market this size means there's no shortage of homeowners looking for a designer — the shortage is in how quickly a genuine enquiry turns into a booked consultation. Interior design decisions involve real money and multiple comparisons, so homeowners routinely message several designers at once and default to whoever makes the process feel easiest first: a fast reply, a rough estimate, a concrete next step."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A same-day response to every enquiry with at least a ballpark estimate, even before a site visit; an easy way to book that first consultation without back-and-forth scheduling; and a follow-up for leads who went quiet after the first message, since most homeowners take more than one conversation to commit. None of it changes the design work itself. It decides whether the design work ever gets the chance to start."},
        ],
    },
    {
        "slug": "automobile-showroom-online-lead-response-speed",
        "title": "The Buyer WhatsApped Three Showrooms About the Same Car. Only One Replied Same Day.",
        "dek": "Nearly half of new car buyers now message a dealership directly to check availability — the sale goes to whichever one answers first.",
        "tag": "Automobile Showroom",
        "read_time": "5 min read",
        "related_industry": "automobile-showroom",
        "body": [
            {"type": "p", "text": "A buyer checks a model on a car-listing portal, then WhatsApps three nearby showrooms to ask if a specific colour and variant is in stock. Two reply within the hour with a photo of the car on the lot and a test-drive slot. The third replies the next day, by when the buyer has already put down a booking amount elsewhere."},
            {"type": "stat", "stat": "48% of new automobile buyers in India used WhatsApp to directly connect with a dealership to check vehicle availability, making it the most preferred communication channel — and dealers using digital tools reported an 18% increase in lead volume alongside a 34% reduction in cost per lead.", "source": "Autocar Professional, citing a Meta–FADA whitepaper", "url": "https://www.autocarpro.in/news/meta-and-fada-whitepaper-highlights-digital-tools-driving-auto-sales-and-leads-124514"},
            {"type": "h2", "text": "The showroom isn't losing to a better deal. It's losing to a faster reply."},
            {"type": "p", "text": "With WhatsApp now the primary channel buyers use before ever walking in, a showroom's real competition isn't just the dealer across town — it's how quickly its own sales staff notice and answer a message versus how quickly the next showroom does. A walk-in that would have happened anyway quietly turns into a lost sale the moment a buyer's WhatsApp query sits unanswered long enough for them to book a test drive elsewhere."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A system that makes sure a WhatsApp stock enquiry gets answered the same hour, with an honest answer on availability and colour, not a vague \"let me check\"; a structured test-drive follow-up so an interested walk-in doesn't go cold; and automated service reminders that keep existing customers coming back instead of drifting to whichever service centre replies faster next time. None of it requires better pricing. It requires being the showroom that answered first."},
        ],
    },
    {
        "slug": "building-materials-showroom-contractor-quote-delay",
        "title": "The Contractor Needed 400 Boxes by Friday. Your Showroom Didn't Answer Till Monday.",
        "dek": "India makes more tiles than almost anywhere else on Earth — the local showroom's real competitor is whichever supplier confirms stock and price fastest.",
        "tag": "Building Materials / Tiles Showroom",
        "read_time": "4 min read",
        "related_industry": "building-materials-showroom",
        "body": [
            {"type": "p", "text": "A contractor mid-project needs to confirm a bulk tile order for a site before Friday. They message two showrooms with the exact size and quantity, and book with whichever one calls back that same day with a firm price and stock confirmation — not necessarily the one with the better price, just the one that didn't leave the question hanging over a busy weekend."},
            {"type": "stat", "stat": "India is the world's second-largest producer, consumer and exporter of ceramic tiles, a scale that makes the domestic contractor and bulk-order market one of the most competitive segments of the building materials trade.", "source": "IBEF, \"Tiles of Transformation\" case study", "url": "https://www.ibef.org/research/case-study/tiles-of-transformation-exploring-india-s-ceramic-tile-industry"},
            {"type": "h2", "text": "The showroom isn't losing on range or price. It's losing on the quote turnaround."},
            {"type": "p", "text": "With an industry this large, most local showrooms genuinely stock a wide enough range at a competitive enough price for most contractor jobs — the choice rarely comes down to catalogue depth. It comes down to a narrower moment: a contractor with a live site and a deadline needs a firm yes or no on stock and price, fast, and will simply move to the next number on their contact list rather than wait."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A way for staff to check and confirm real stock without a customer waiting on hold for a callback; a fast, standard quote format for bulk and contractor orders instead of an ad-hoc conversation each time; and a simple way to flag repeat contractor customers so their orders get priority response. None of it touches the showroom floor or the supplier relationships that built the range. It decides whether a contractor's next order comes back to the same showroom or the next one down the road."},
        ],
    },
    {
        "slug": "wholesale-distributor-retailer-reorder-cadence",
        "title": "The Retailer Ran Out of Stock on a Tuesday. They Reordered From Someone Else by Thursday.",
        "dek": "General trade still moves most of India's FMCG business — the distributor's real risk is a retailer quietly switching who they reorder from.",
        "tag": "Wholesale Distributor",
        "read_time": "5 min read",
        "related_industry": "wholesale-distributor",
        "body": [
            {"type": "p", "text": "A kirana retailer runs low on a fast-moving SKU, tries reaching their usual distributor's beat salesman, and doesn't get a callback that day. They place the reorder with a rival distributor's number saved from an earlier WhatsApp broadcast instead. The original distributor doesn't find out until the next scheduled visit — by when the retailer's habit has already started to shift."},
            {"type": "stat", "stat": "Traditional trade — the general trade network of over 11.5 million stores served by wholesalers and distributors — still accounts for 81.8% of FMCG sales in India, remaining the dominant retail channel despite the growth of e-commerce and modern trade.", "source": "NielsenIQ, \"Four Key Trends Shaping the FMCG Landscape in India\"", "url": "https://nielseniq.com/global/en/insights/analysis/2022/explore-the-four-key-trends-shaping-the-fmcg-landscape-in-india/"},
            {"type": "h2", "text": "The channel isn't shrinking. The relationship inside it is what's fragile."},
            {"type": "p", "text": "With general trade still moving over four-fifths of India's FMCG volume, a distributor's business isn't threatened by the channel disappearing — it's threatened by a quieter risk: a retailer's reorder habit silently drifting to whichever distributor's salesman or WhatsApp line responds first when stock runs low. Margins on any single SKU are thin enough that losing a retailer's default reorder pattern, even briefly, is what actually erodes a distributor's business over a year, not any single lost sale."},
            {"type": "h2", "text": "What actually closes the gap"},
            {"type": "p", "text": "A simple way for retailers to reorder the moment they're low, without waiting for the next scheduled beat visit; visibility into which SKUs and retailers are due for a reorder, so follow-up doesn't rely on memory; and a fast, predictable response when a retailer does reach out, since the ones who switch distributors usually do it quietly, only after being made to wait once too often. None of it requires undercutting margins. It requires being the easiest distributor to reorder from before a retailer even considers checking who else might answer faster."},
        ],
    },
    {
        "slug": "grow-gym-business-2027",
        "title": "7 Ways to Grow Your Gym Business in 2027 (That Aren't \"Buy More Machines\")",
        "dek": "The fastest-growing part of India's fitness market isn't bigger gyms — it's smaller, sharper ones. Here's where the real growth is headed.",
        "tag": "Gym / Fitness Chain",
        "read_time": "5 min read",
        "related_industry": "gym-fitness-chain",
        "body": [
            {"type": "p", "text": "Budget season rolls around and the instinct is the same every year: add a few more machines, repaint the walls, maybe run a January discount. It's what most local gyms have always done to plan for growth — and increasingly, it's not where the growth in India's fitness market actually is."},
            {"type": "stat", "stat": "India's fitness industry is projected to more than double from an estimated ₹16,200 crore in 2024 to ₹37,700 crore by 2030, growing at a 15% CAGR.", "source": "Deloitte & Health and Fitness Association of India, India Fitness Market Report 2025", "url": "https://www.healthandfitness.org/wp-content/uploads/India-Fitness-Market-2025_FINAL_Print.pdf"},
            {"type": "h2", "text": "The growth isn't in more members. It's in a different kind of class."},
            {"type": "p", "text": "Value gyms — the standard membership-and-machines model most local gyms run — still make up the bulk of the industry: 56% of revenue, 78% of members, 80% of facilities. But that segment is also the slowest-growing one. The category expanding fastest is the opposite of \"more of the same\": small-format, instructor-led classes — HIIT, strength circuits, yoga, mobility work for older members — built around a specific outcome rather than open gym access."},
            {"type": "stat", "stat": "Boutique fitness formats are growing at close to a 19% CAGR through 2030, nearly a third faster than the 14% CAGR projected for standard value gyms — even though boutique studios still hold only about 7% of total market revenue today.", "source": "Deloitte & Health and Fitness Association of India, India Fitness Market Report 2025", "url": "https://www.healthandfitness.org/wp-content/uploads/India-Fitness-Market-2025_FINAL_Print.pdf"},
            {"type": "h2", "text": "What this actually means for a gym planning 2027, not a chain planning an IPO"},
            {"type": "p", "text": "None of this requires becoming a boutique studio or ripping out equipment that's already paid for. It means carving out one or two specific, bookable formats inside the gym that already exists — a 6am strength circuit, a women-only hour, a 55+ mobility class — instead of selling the same open membership to everyone who walks in. It means using the hours a gym is usually quietest, mid-morning to mid-afternoon, for exactly that kind of small-batch class rather than leaving the floor half-used. And it means treating a nearby office park or mid-size company as a real lead source: corporate wellness tie-ups are one of the more reliable ways an independent gym can add members in bulk without spending on ads, and most companies budgeting for employee wellness don't need their own in-house gym to do it."},
            {"type": "h2", "text": "The gyms that will look different in 2027 already started this year"},
            {"type": "p", "text": "None of this is about outspending a franchise on equipment — that fight is already lost. It's about picking one underused format, one nearby partnership, and one clearly bookable slot, and making sure all three show up where someone is actually searching for a gym near them right now. That's a smaller, cheaper bet than a renovation, and it compounds a lot faster than another round of new machines."},
        ],
    },
    {
        "slug": "grow-coaching-institute-2027",
        "title": "How to Grow Your Coaching Institute in 2027 Without Renting a Bigger Classroom",
        "dek": "The ceiling on most coaching institutes isn't demand — it's how many students can physically sit in one room. Hybrid batches and adjacent skill courses are where growth is actually headed.",
        "tag": "Coaching Institute",
        "read_time": "5 min read",
        "related_industry": "coaching-institute",
        "body": [
            {"type": "p", "text": "Every batch fills up around the same size every year — not because interest has plateaued, but because a classroom only holds so many chairs. For most coaching institutes, that physical ceiling has quietly become the real limit on growth, long before quality or reputation ever becomes the constraint."},
            {"type": "stat", "stat": "India's online coaching market is projected to grow from USD 510.1 million in 2025 to USD 1,998.4 million by 2034 — a 15.89% CAGR, roughly 50% faster than the 10.29% CAGR projected for the coaching industry overall.", "source": "IMARC Group, India Online Coaching Market Report", "url": "https://www.imarcgroup.com/india-online-coaching-market"},
            {"type": "h2", "text": "Hybrid isn't a pandemic leftover anymore — it's policy-backed infrastructure"},
            {"type": "p", "text": "A recorded or livestreamed batch used to be a hard sell to parents who wanted their child physically supervised. That resistance has eased considerably, partly because the government has spent years normalizing digital learning at a policy level. The National Education Policy (NEP) 2020 mandates structural technology integration across schooling, backed by public digital infrastructure like PM eVidya, SWAYAM and DIKSHA — the same digital-first framing that once made online batches feel like a compromise now makes them feel like where education is already headed anyway."},
            {"type": "h2", "text": "The second lever: what a coaching institute teaches, not just where"},
            {"type": "p", "text": "Exam-prep coaching isn't the only thing growing in this market. Professional and skill-based courses — spoken English, basic computer literacy, IT certifications — sit inside the same broader coaching industry and often use the exact infrastructure an exam-prep institute already has: faculty, a classroom, a WhatsApp broadcast list of past and current students. Running a short skill course in the months between major exam cycles, when the classroom would otherwise sit half-empty, is a low-risk way to add a second revenue line without hiring a second campus."},
            {"type": "h2", "text": "What actually moves an institute forward in 2027"},
            {"type": "p", "text": "Not a new building. A recorded or live-streamed version of a batch that's already running, priced to reach students outside the immediate catchment area; a clear, upfront explanation to parents of exactly how the hybrid format works, since the objection is usually about trust, not technology; and one adjacent short course that uses the same faculty and space in the institute's quietest months. None of it touches how well the core batch is taught. It decides how many students that teaching actually reaches."},
        ],
    },
    {
        "slug": "what-sells-most-during-diwali-india",
        "title": "What Actually Sells the Most During Diwali in India",
        "dek": "Every shop owner has a hunch about what moves during Diwali. Here's what the real trade data says — category by category.",
        "tag": "Seasonal / Festive",
        "read_time": "4 min read",
        "related_industry": None,
        "body": [
            {"type": "p", "text": "Ask ten shop owners what sells during Diwali and most will say \"everything\" — which is close to true, but not useful for actually planning stock, staff or a marketing push. The trade body that tracks this nationwide has a far more specific answer."},
            {"type": "stat", "stat": "Diwali 2025 trade across India hit a record ₹6.05 lakh crore (₹5.40 lakh crore in goods, ₹65,000 crore in services), up sharply from ₹4.25 lakh crore the year before. Grocery & FMCG led at 12% of trade, followed by gold & jewellery at 10%, electronics & electricals at 8%, and ready-made garments and gift items at 7% each.", "source": "Confederation of All India Traders (CAIT), Diwali 2025 trade survey", "url": "https://cait.in/record-breaking-diwali-sales-of-%E2%82%B95-40-lakh-crore-in-goods-65-thousand-crores-in-services-reflect-indias-economic-strength-and-swadeshi-spirit/"},
            {"type": "h2", "text": "Grocery isn't a side note — it's the single biggest category"},
            {"type": "p", "text": "The single largest slice of Diwali trade isn't gold or electronics, the categories that dominate ad spend and headlines. It's everyday grocery and FMCG — sweets, dry fruits, cooking essentials, packaged snacks — bought in bulk for gifting and home entertaining, in volumes far beyond a normal week. For a kirana store or general grocery shop, Diwali isn't primarily an electronics or gold-jewellery event to compete on; it's the single biggest stock-and-staffing week of the entire year in the category it already owns."},
            {"type": "h2", "text": "Online buying skews toward a narrower, faster-moving set of categories"},
            {"type": "p", "text": "The category mix shifts again once you isolate what's bought online rather than in-store. In the days right before Diwali, Health & Beauty was the fastest-moving online category — gifting kits, skincare sets and hairstyling products — even as fashion and home décor also led online spend."},
            {"type": "stat", "stat": "93% of Indian shoppers bought online during the 2025 festive season, with fashion, home décor and health & beauty the leading categories — and Health & Beauty alone saw a 63% spike in the run-up to Diwali (October 7–12), driven by gifting kits, skincare and hairstyling products.", "source": "Criteo, via BW Marketing World", "url": "https://www.bwmarketingworld.com/article/diwali-2025-drives-14-surge-in-online-retail-sales-report-576873"},
            {"type": "h2", "text": "What this means for planning next Diwali, not just reacting to this one"},
            {"type": "p", "text": "The pattern is consistent enough to plan around a year out: grocery and FMCG for the volume, gold and garments for the ticket size, gifting-adjacent categories (dry fruits, sweets hampers, decor, personal care sets) for the margin, and a narrower online-specific spike in beauty and fashion gifting in the final week. A shop that stocks and staffs against that actual mix — rather than a general \"Diwali rush\" guess — starts the season with inventory in the categories that are genuinely moving."},
        ],
    },
    {
        "slug": "what-sells-during-dussehra-durga-puja",
        "title": "What Sells During Dussehra and Durga Puja — And Why the Data Gets Thinner Here",
        "dek": "Diwali has one clean nationwide number behind it. Dussehra and Durga Puja are bigger in some places than Diwali itself — but the hard data is far more regional.",
        "tag": "Seasonal / Festive",
        "read_time": "4 min read",
        "related_industry": None,
        "body": [
            {"type": "p", "text": "In large parts of eastern India, Durga Puja isn't the warm-up act before Diwali — it's the main event, the one week a shop plans its entire year around. Nationally, the picture is less tidy, and it's worth being upfront about that rather than pretending there's one clean number for a festival that plays out so differently region to region."},
            {"type": "stat", "stat": "West Bengal's Durga Puja economy is estimated at around ₹65,000 crore for 2025, with Kolkata alone contributing nearly 70% of that total. Organised retailers reported jewellery sales up 25%, footwear up 20%, apparel up 22%, and food & beverage up 18% year-on-year, while Kolkata's major malls together clocked around ₹900 crore in business, an 8–10% rise over the previous year.", "source": "The Federal, on West Bengal's Durga Puja economy", "url": "https://thefederal.com/category/states/east/west-bengal/bengal-durga-puja-economy-hits-record-rs-65000-crore-amid-rains-gst-pause-209971"},
            {"type": "h2", "text": "Where the data is strong: Bengal's retail categories"},
            {"type": "p", "text": "Inside that regional number, the pattern is specific: new clothes for the family, the traditional core of Puja shopping, lead the apparel and footwear growth; jewellery sees a distinct bump tied to the festival's gifting and auspicious-purchase customs; and food & beverage spend rises as households and pandal committees both spend heavily on catering and eating out during the five main days."},
            {"type": "h2", "text": "Nationally, Dussehra is an \"auspicious purchase\" day more than a retail category story"},
            {"type": "p", "text": "Outside Bengal, Dussehra (Vijayadashami) is culturally significant as an auspicious day to buy vehicles, tools, gold and big-ticket items — rather than a festival tied to one dominant category the way Diwali is. That tradition does show up in hard numbers, just not ones specific to Dussehra alone, since it usually lands inside the broader Navratri festive window that retailers and auto dealers report together."},
            {"type": "stat", "stat": "Retail vehicle sales rose 34% year-on-year during the 2025 Navratri period, with two-wheelers up 36% and passenger vehicles up 34.8% — dealerships nationally reported record footfalls and deliveries during the window that includes Dussehra.", "source": "Business Standard, citing FADA (Federation of Automobile Dealers Associations)", "url": "https://www.business-standard.com/industry/auto/retail-vehicle-sales-rise-september-2025-navratri-record-high-fada-125100700271_1.html"},
            {"type": "h2", "text": "The honest takeaway"},
            {"type": "p", "text": "There's no single national Dussehra sales figure worth quoting as gospel, because the festival isn't one event — it's a Bengal-scale retail season in the east and an auspicious-purchase day for vehicles, gold and tools everywhere else. For a business in Kolkata or elsewhere in Bengal, the categories to stock hard around are clothing, footwear, jewellery and food service. For a vehicle dealer, gold showroom or hardware business anywhere else in India, Dussehra is worth treating as a smaller sibling of the Navratri-to-Diwali stretch — real, auspicious-day-driven demand, just folded into a bigger festive window rather than standing alone in the data."},
        ],
    },
    {
        "slug": "amazon-flipkart-festive-sales-impact-on-local-shops",
        "title": "What Amazon's and Flipkart's Festival Sales Actually Do to Your Local Shop",
        "dek": "Two mega sales, a few weeks apart, pull in more customer visits than most countries have people. Here's what the numbers say actually happens to offline retail around them.",
        "tag": "Seasonal / Festive",
        "read_time": "5 min read",
        "related_industry": "retail-store",
        "body": [
            {"type": "p", "text": "Every September, the same anxious question does the rounds among shop owners: is this the year Amazon's and Flipkart's festival sales finally hollow out local retail for good? The two platforms now report numbers large enough to make that fear feel reasonable. What actually happened to offline trade in the same weeks is a lot less dramatic than that number suggests."},
            {"type": "stat", "stat": "Amazon's Great Indian Festival 2025 recorded 276 crore (2.76 billion) customer visits, with more than 70% coming from Tier 2 and Tier 3 cities, and enabled over ₹1,000 crore in customer savings through bank offers, GST benefits and cashback.", "source": "About Amazon India, official results", "url": "https://www.aboutamazon.in/news/retail/amazon-great-indian-festival-2025-highlights-results"},
            {"type": "h2", "text": "Flipkart's numbers, run in the same window, are just as large"},
            {"type": "p", "text": "Flipkart's Big Billion Days ran the same September–October stretch, off a marketplace of more than 500 million registered users and over 1.4 million sellers — with transacting sellers up 25% in the six months before the sale, disproportionately new entrants from Tier 2/3 towns like Agra, Indore, Rajkot and Surat. Both platforms have deliberately timed their biggest sale of the year to the same festive weeks, concentrating an enormous share of India's annual online retail demand into roughly a month."},
            {"type": "h2", "text": "The trade body representing local retailers has been fighting this exact tension for years"},
            {"type": "p", "text": "This isn't a new complaint. The Confederation of All India Traders, which says it represents around 7 crore (70 million) traders nationally, has for years accused both platforms of predatory discounting during these festival sales — deep, below-cost price cuts it argues violate India's foreign investment rules for e-commerce marketplaces. That fight continued into the 2025 sale cycle, with fresh complaints over cancelled orders, delayed refunds, and misleading discount pricing during both companies' 2025 festivals."},
            {"type": "h2", "text": "But offline retail's own festive numbers, in the same weeks, tell a different story"},
            {"type": "p", "text": "Traditional retail stores accounted for 85% of overall festive trade in 2025, and CAIT's own survey put total festive trade at ₹6.05 lakh crore, up 25% year-on-year, driven by close to 90 million small traders and local manufacturers, with 72% of traders reporting higher sales than the year before. Both realities are true at once: two online platforms posting record visit numbers, and offline retail posting its best festive season on record, in the same weeks."},
            {"type": "h2", "text": "What this actually means for a local shop"},
            {"type": "p", "text": "The overlap that genuinely hurts is narrow and specific — big-ticket electronics, premium fashion and appliances, the exact categories where these platforms' discounts are steepest and delivery speed matters most. Everyday categories — grocery, festive food, personal gifting, anything bought on trust or needed same-day — aren't where these sales actually compete with a local shop, and the trade data backs that up. The useful response isn't panic about the whole season; it's making sure a shop's own festive push leans hardest into exactly the categories these platforms are structurally worst at."},
        ],
    },
    {
        "slug": "festive-season-readiness-checklist-small-retailers",
        "title": "The Festive Season Readiness Checklist for Small Indian Retailers",
        "dek": "Six to eight weeks decide a disproportionate share of the year. Most of what goes wrong in that window isn't about demand — it's about not being ready for it.",
        "tag": "Seasonal / Festive",
        "read_time": "5 min read",
        "related_industry": "retail-store",
        "body": [
            {"type": "p", "text": "By the time Navratri actually starts, it's already too late to fix the things that decide whether the festive season is a good one or a chaotic one — the stock that should've been ordered a month ago, the billing software still running last year's tax rates, the extra hand that should've been hired in August. The businesses with a genuinely strong festive season are rarely the ones with the best last-minute hustle. They're the ones that finished the boring prep work early."},
            {"type": "stat", "stat": "For apparel retailers, the combined festive-and-wedding season can account for around 35% of annual sales — meaning a handful of autumn-winter weeks disproportionately decide the entire year's numbers for many retail categories.", "source": "CRISIL Ratings, cited in festive retail coverage", "url": "https://www.thecore.in/economy/india-festive-season-retail-2026-inflation-fmcg-demand-outlook-870405"},
            {"type": "h2", "text": "Stock and cash: order and price before the rush, not during it"},
            {"type": "p", "text": "Reorder fast-moving festive lines well before the peak weeks, based on last year's actual sell-through rather than a round-number guess — running out mid-Diwali loses the sale to whichever shop still has stock. Since the September 2025 GST 2.0 rate changes, this also means double-checking that billing software actually reflects the current four-slab structure; plenty of small retailers were still billing at old rates weeks after the new ones took effect, which creates real compliance risk right in the busiest season to be dealing with it."},
            {"type": "h2", "text": "Staffing and cash flow: the crunch is real and predictable"},
            {"type": "p", "text": "Festive weeks bring a genuine volume spike that a shop's normal staffing usually can't absorb without visible strain — slower billing, unanswered questions, customers who leave rather than wait. Bringing on temporary help for the two or three peak weeks, decided in advance rather than reactively, is one of the highest-return calls a small retailer makes each year. On the cash side, festive spending patterns mean more credit and khata requests during the exact weeks a shop also has more stock to pay suppliers for — worth planning a cash buffer for deliberately, rather than discovering the gap mid-season."},
            {"type": "h2", "text": "Visibility and follow-through: be findable, then don't let the customer disappear"},
            {"type": "p", "text": "A shop's Google listing and WhatsApp presence matter more in festive weeks than any other time of year, simply because more first-time and occasional customers are searching and comparing than usual. And the season doesn't end at the last sale: a simple thank-you or repeat-offer message to festive-season customers, sent in the quieter weeks that follow, is what turns a one-time Diwali sale into a customer who comes back in February. Most of what separates a good festive season from a great one isn't a bigger discount. It's not being caught unprepared for demand that, every single year, was entirely predictable."},
        ],
    },
    {
        "slug": "grow-automobile-showroom-business-2027-ev",
        "title": "How Automobile Showrooms Can Grow Through India's EV Shift in 2027",
        "dek": "EVs aren't a future category dealerships can plan for later. They're already showing up on the sales floor — and the showrooms treating them as a side hobby are the ones about to fall behind.",
        "tag": "Automobile Showroom",
        "read_time": "5 min read",
        "related_industry": "automobile-showroom",
        "body": [
            {"type": "p", "text": "A customer walks in asking about an electric scooter's real-world range and charging time, and the salesperson who usually handles two-wheeler enquiries doesn't have a confident answer. It's a small moment, easy to shrug off once — except it's happening at more and more showrooms, more and more often, and the honest answer is that the shift it signals isn't going to slow down."},
            {"type": "stat", "stat": "India registered around 25.5 lakh electric vehicles across all categories in FY 2025-26, continuing a run of consecutive years of strong year-on-year growth in EV adoption.", "source": "EVreporter", "url": "https://evreporter.com/india-sold-2550865-electric-vehicles-across-categories-in-fy-2025-26/"},
            {"type": "h2", "text": "This is overwhelmingly a two-wheeler story first"},
            {"type": "p", "text": "For most showrooms outside the metro car market, the EV opportunity isn't really about electric cars yet — it's about two-wheelers, which already make up around two-thirds of all EV sales in the country and are growing fastest of any segment. That matters because it puts the EV shift within reach of exactly the kind of small and mid-size dealership that couldn't easily compete on electric cars, but can absolutely compete on electric scooters and bikes."},
            {"type": "stat", "stat": "India's official policy target is for EVs to reach 30% of private car sales, 70% of commercial vehicle sales, 40% of bus sales, and 80% of two- and three-wheeler sales by 2030 — meaning two-wheelers are the segment where the government itself expects the fastest transition.", "source": "IBEF (India Brand Equity Foundation)", "url": "https://www.ibef.org/industry/electric-vehicle"},
            {"type": "h2", "text": "What actually helps a showroom grow through this, not just survive it"},
            {"type": "p", "text": "It starts with treating EV enquiries as seriously as ICE ones: at least one staff member who can confidently walk a customer through real-world range, charging time and the state and central subsidy paperwork most first-time EV buyers find confusing. It extends to a genuinely useful local partnership — tying up with a nearby electrician or charging-point installer to offer a simple home-charging setup alongside the sale, something very few small showrooms currently bother to do. And it means recognizing EV owners need a different kind of post-sale relationship: battery health check-ins and charging troubleshooting instead of the usual service-due reminders, sent on WhatsApp the same way a showroom already reminds petrol customers about their next service."},
            {"type": "h2", "text": "The showrooms leading in 2027 are being built right now"},
            {"type": "p", "text": "None of this requires a large upfront bet on EV inventory alone. It requires not treating the EV customer walking in today as a niche enquiry to handle awkwardly, but as the first wave of a segment that, by the government's own targets, is meant to be the fastest-growing part of the entire market by the end of the decade."},
        ],
    },
    {
        "slug": "indian-festival-sale-calendar-for-small-business-2027",
        "title": "The Indian Festival Calendar Every Small Business Should Plan 2027 Around",
        "dek": "Akshaya Tritiya, Raksha Bandhan, Navratri, Diwali, wedding season — each one moves real money, on a predictable schedule. Here's what the numbers behind each one actually look like.",
        "tag": "Seasonal / Festive",
        "read_time": "6 min read",
        "related_industry": None,
        "body": [
            {"type": "p", "text": "Most small businesses plan their year around one big date — usually Diwali — and treat everything else as a bonus if it happens to land well. The trade data tells a different story: several other dates on the calendar move genuinely serious money, on a schedule that's exactly as predictable as Diwali's, which makes them just as plannable."},
            {"type": "stat", "stat": "Akshaya Tritiya 2026 generated an estimated ₹20,000 crore in gold and silver trade nationally, according to CAIT — up from around ₹16,000 crore the year before, even as gold and silver prices hit record highs.", "source": "IANS", "url": "https://ianslive.in/akshaya-tritiya-likely-to-generate-business-worth-rs-20000-crore-in-gold-and-silver--20260419092247"},
            {"type": "h2", "text": "Spring to monsoon: gold, then gifting"},
            {"type": "p", "text": "Akshaya Tritiya, usually falling in April or May, is a single-category event almost entirely about gold and silver — not a broad retail day, but a genuinely enormous one for any jewellery or precious-metals business, worth planning stock, staff and marketing around specifically. Raksha Bandhan, typically in August, is a different shape entirely: broader than just rakhis, pulling in sweets, gifts, apparel, electronics and dry fruits alongside the core rakhi trade."},
            {"type": "stat", "stat": "Raksha Bandhan 2026 trade was projected to cross ₹30,000 crore nationally, with the rakhi segment alone accounting for around ₹25,000 crore of that.", "source": "The Print, citing CAIT", "url": "https://theprint.in/india/rakhi-trade-expands-with-new-themes-viksit-bharat-nari-vandan-could-cross-rs-30000-cr-says-cait/3024467/"},
            {"type": "h2", "text": "Navratri to Diwali: the six-week stretch that decides the year"},
            {"type": "p", "text": "This is the one every business already half-plans around, but usually as a single blur rather than two distinct moments. Navratri and Dussehra bring an auspicious-purchase spike, particularly strong for vehicles, gold and tools — retail vehicle sales rose 34% year-on-year in Navratri 2025, per FADA data. Diwali itself, a few weeks later, is the single largest retail event of the year by a wide margin."},
            {"type": "stat", "stat": "Diwali 2025 trade hit ₹6.05 lakh crore nationally, up 25% year-on-year, led by grocery and FMCG, gold and jewellery, electronics, and garments — in that order.", "source": "Confederation of All India Traders (CAIT)", "url": "https://cait.in/record-breaking-diwali-sales-of-%E2%82%B95-40-lakh-crore-in-goods-65-thousand-crores-in-services-reflect-indias-economic-strength-and-swadeshi-spirit/"},
            {"type": "h2", "text": "Wedding season: the quiet giant, and what it means for 2027"},
            {"type": "p", "text": "Running from early November through mid-December, wedding season doesn't get talked about as a retail event the way Diwali does — but by CAIT's own estimates it moves more money: India's 2025 wedding season was projected to generate ₹6.5 lakh crore in business from an estimated 46 lakh weddings, larger than the entire Diwali trade figure for the same year. A jewellery business has two real peaks a year, not one — Akshaya Tritiya and Dhanteras/Diwali. A gifting, apparel or electronics business has at least three: Raksha Bandhan, the Navratri-Diwali stretch, and wedding season. And any business connected to weddings — caterers, decorators, jewellers, garment shops, banquet halls — is looking at a bigger single revenue event in November-December than most businesses see at Diwali. The businesses that plan a full calendar, not just one headline festival, are the ones that stop treating every one of these weeks as a surprise."},
        ],
    },
    {
        "slug": "invoice-collections-cadence-msme-working-capital",
        "title": "Why Indian MSMEs Are Sitting on Crores in Unpaid Invoices — And It's Not a Trust Problem",
        "dek": "The average Indian SME waits 73 days to collect on paperwork that says 30. The gap isn't the customer. It's that nobody's actually chasing it, every time, on schedule.",
        "tag": "Invoice + Payment Reminders",
        "read_time": "4 min read",
        "related_industry": None,
        "related_module": "invoice-reminder",
        "body": [
            {"type": "p", "text": "An invoice goes out the day the order ships or the booking is confirmed. On paper, it's due in 30 days. In practice, whether it actually gets paid on time depends on someone remembering to follow up — and in a business already running five other things at once, that someone usually doesn't, until the gap is embarrassing and the cash is genuinely needed."},
            {"type": "stat", "stat": "Indian SMEs take an average of 73 days to collect on invoices, even though 82.6% of those invoices are issued with credit terms of 30 days or less — and the average SME is carrying ₹3.83 crore in receivables overdue by more than 360 days.", "source": "Recordent, Indian SME Receivables Report 2026", "url": "https://smestreet.in/infocus/indian-smes-face-mounting-working-capital-stress-as-average-overdue-receivables-cross-383-crore-recordent-12111904"},
            {"type": "h2", "text": "It's not a credit-policy problem. It's a collections-discipline problem."},
            {"type": "p", "text": "That number is worth sitting with: the terms businesses set aren't the issue — most are already conservative, 30 days or less. The entire gap between what's promised and what's actually collected happens after the invoice is sent, in the follow-up that either happens reliably or doesn't. At national scale, it clearly doesn't, often enough to leave the average SME sitting on crores that should already be working capital."},
            {"type": "h2", "text": "Why the reminder has to check before it sends"},
            {"type": "p", "text": "The mechanism itself is simple on purpose: a WhatsApp nudge at 7, 14, and 30 days overdue, with the tone escalating each time — a friendly nudge, then a firmer reminder, then a final notice, the way a good AR person would actually phrase it rather than three identical templates. The detail that matters most is what happens right before each send: the system checks payment status again first. A customer who quietly paid on day 9 never gets an awkward day-14 reminder demanding money they've already sent — which is exactly the kind of mistake that damages a relationship faster than the original follow-up would have helped it."},
            {"type": "p", "text": "None of this replaces judgment on a genuinely difficult account. What it replaces is the much more common failure mode — the invoice that simply never got chased because nobody had a free afternoon that week. Fixing that one gap, reliably, for every invoice, is a smaller and cheaper change than it sounds, and it's exactly the discipline gap the national data is describing."},
        ],
    },
    {
        "slug": "payment-reconciliation-manual-matching-hidden-cost",
        "title": "The Spreadsheet That's Quietly Costing You Revenue",
        "dek": "Every unmatched payment is either money you haven't collected or money you've already been paid and are still chasing. Most businesses can't tell which, fast enough for it to matter.",
        "tag": "Payment Reconciliation",
        "read_time": "4 min read",
        "related_industry": None,
        "related_module": "payment-reconciliation",
        "body": [
            {"type": "p", "text": "The bank statement shows 40 credits this week. The invoice or fee register shows 45 still open. Someone now has to manually match names, amounts and dates against each other — and a partial payment, a rounding difference, or a customer paying under a slightly different name is enough to break that match silently, with nobody noticing until much later."},
            {"type": "h2", "text": "Why this breaks specifically at volume, not on day one"},
            {"type": "p", "text": "A 20-transaction week is manageable by eye. A 200-transaction week isn't — and that's exactly the point where mismatches start hiding rather than announcing themselves. A duplicate payment goes uncredited. A ₹340 shortfall doesn't get flagged, so the late fee that should apply never does. A customer who already paid keeps getting a reminder meant for someone else, and the relationship absorbs the damage. None of these show up as one big obvious error — they show up as a slow, invisible leak across hundreds of small ones."},
            {"type": "h2", "text": "What automated matching actually does differently"},
            {"type": "p", "text": "The value isn't doing the matching faster than a person could. It's that the system pulls the transaction record and the invoice or fee register and matches on amount, reference and date automatically for the clean cases — which is the overwhelming majority of them — and only surfaces the exceptions that genuinely need a human decision. Instead of a person re-checking 200 line items to find the 6 that are actually ambiguous, they only ever see the 6."},
            {"type": "p", "text": "Reconciliation isn't bookkeeping busywork sitting at the bottom of the priority list. Every unmatched entry is either a customer being wrongly chased for money already paid, or money that's already missing and nobody's noticed yet. At real transaction volume, manual matching guarantees some number of both — indefinitely, until something forces a full manual audit."},
        ],
    },
    {
        "slug": "appointment-no-show-reminder-whatsapp-confirmation",
        "title": "The No-Show Isn't About the Customer Forgetting",
        "dek": "A hospital chain ran a systematic test of reminder wording across 14 sites and found the message design alone moved no-show rates. The lesson: reminders work, but only if they're actually built to.",
        "tag": "Booking Confirmation + No-Show Reminder",
        "read_time": "4 min read",
        "related_industry": None,
        "related_module": "booking-reminder",
        "body": [
            {"type": "p", "text": "A booking gets confirmed, the slot goes on the calendar, and then — often — nothing happens again until the appointment time comes and goes with no one showing up. The booking wasn't cancelled. It just lost priority against whatever came up in the days between, with nothing pulling it back to the top of mind before it was too late."},
            {"type": "stat", "stat": "Clalit Health Services — Israel's largest healthcare provider — randomly assigned patients across 14 hospitals to receive one of nine different pre-appointment reminder messages, sent five days before their scheduled visit. Message wording alone was enough to move no-show rates.", "source": "PLOS ONE, Berliner Senderey et al. (2020), \"It's how you say it\"", "url": "https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0234817"},
            {"type": "h2", "text": "A no-show usually isn't forgetting — it's a booking that lost priority"},
            {"type": "p", "text": "Most people don't erase an appointment from memory entirely. It just stops being the most urgent thing on a given day, and without something nudging it back into view close to the actual date, there's nothing forcing a decision either way. A generic one-way SMS sent once, with nothing to respond to, does almost nothing to change that."},
            {"type": "h2", "text": "Why a plain confirmation-style reminder outperforms a generic one"},
            {"type": "p", "text": "The module's design leans on two specific things the research above points at: the reminder has to actually be read, and it has to ask for something small in return. WhatsApp's high open rate means the message is seen close to the moment that matters, instead of sitting in an SMS inbox or a missed voicemail. And a reminder that asks for a tap to confirm creates a small, real commitment — a passive \"your appointment is on X\" blast doesn't ask anything of the reader, so it doesn't reset their intent to actually show up."},
            {"type": "p", "text": "The fix here was never \"remind harder.\" It's reminding at the right moment, on a channel that gets opened, with a response that re-commits the person — the exact lever a 14-hospital study spent real research budget proving actually moves the number."},
        ],
    },
    {
        "slug": "claim-document-dispatch-speed-customer-trust",
        "title": "Why \"We'll Email It to You\" Is Where So Many Service Businesses Lose Trust",
        "dek": "The moment a claim, report or document is ready internally has little to do with the moment it actually reaches the right inbox — and that gap is where confidence in the business quietly erodes.",
        "tag": "Claim / Document Auto-Email Dispatch",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "claim-email-dispatch",
        "body": [
            {"type": "p", "text": "A diagnostic report is finalized, or an insurance claim summary is complete. Internally, the work is done. Getting it into the customer's inbox is a separate step — someone has to be free to draft the email, attach the right file, confirm the right address — and if that step queues behind everything else on someone's desk, \"ready\" and \"delivered\" can end up a day or two apart, with the customer able to tell only one of those two states."},
            {"type": "h2", "text": "The customer isn't measuring your internal process. They're measuring silence."},
            {"type": "p", "text": "Businesses tend to think processing time is what gets judged. What a customer actually experiences is the silence after being told \"it's being processed,\" with no update on where things stand. A same-day dispatch, paired with a real-time WhatsApp status ping the moment the email actually goes out, closes that anxiety gap — even when the true internal processing time hasn't changed by a single hour."},
            {"type": "h2", "text": "Why this doesn't need a payer-system integration to fix"},
            {"type": "p", "text": "Many of these delays aren't a data problem at all — they're a queuing problem. The document is frequently ready well before it's actually sent, simply waiting on a person with free time. Auto-generating and emailing it the instant it's marked ready, plus a WhatsApp status update back to the customer, removes the \"someone has to remember to send this\" step entirely, without needing any integration into an insurer's, lab's, or authority's own system."},
            {"type": "p", "text": "None of this changes how long the underlying work takes. It changes whether the gap between finishing and delivering is minutes or days — and that gap, more than the actual turnaround time, is usually what a customer remembers about how the business handled them."},
        ],
    },
    {
        "slug": "google-review-reply-declining-trust-local-seo",
        "title": "Consumers Trust Reviews Less Than They Used To. Here's What Still Moves the Needle.",
        "dek": "Trust in reviews has fallen from 84% at its 2016-17 peak to 42% today. What's replacing blind trust in the star rating is scrutiny of how a business actually responds.",
        "tag": "Review Request + AI-Drafted Reply",
        "read_time": "4 min read",
        "related_industry": None,
        "related_module": "review-reply",
        "body": [
            {"type": "p", "text": "For years, the advice to local businesses was simple: get more reviews, keep the star rating high. That advice is getting less useful every year — not because reviews stopped mattering, but because fewer people are taking them at face value."},
            {"type": "stat", "stat": "Consumer trust in online reviews as much as personal recommendations from friends and family has fallen sharply — from 84% at its 2016-17 peak to 42% in BrightLocal's 2025 Local Consumer Review Survey.", "source": "BrightLocal, Local Consumer Review Survey 2025", "url": "https://www.brightlocal.com/research/local-consumer-review-survey-2025/"},
            {"type": "h2", "text": "If the rating alone doesn't build trust anymore, what does?"},
            {"type": "p", "text": "As blanket trust in star ratings erodes, the review thread itself becomes the signal a prospective customer actually reads: not just what happened, but whether the business responded, and how. An unanswered review — good or bad — reads as an unmanaged business. A thoughtful reply, even to a middling 3-star review, reads as one that's actually paying attention to what customers say."},
            {"type": "h2", "text": "Why \"ask for a review\" and \"reply to every review\" have to be the same system"},
            {"type": "p", "text": "Most businesses only engage with reviews reactively — after a bad one forces a scramble. Asking for a review right after good service, while the experience is still fresh, produces the positive volume. Replying quickly and consistently to whatever actually comes in, good or bad, is what a visitor notices when comparing a few similar-looking businesses in a search result. Doing only one half of that is most of why review sections end up looking abandoned."},
            {"type": "p", "text": "An AI-drafted reply, reviewed and approved by a human before it posts, doesn't replace judgment on how to handle a genuinely difficult review. What it removes is the far more common failure: \"I'll get to it later\" turning into never, simply because writing a reply from a blank screen takes longer than it should for something this repetitive."},
        ],
    },
    {
        "slug": "stock-check-reserve-whatsapp-lost-sales",
        "title": "The Sale You Never Know You Lost",
        "dek": "No answer, a slow answer, or a wrong answer to \"is this in stock?\" all end the same way — the customer buys elsewhere, and it never shows up as a lost sale anywhere in your books.",
        "tag": "Stock Check-and-Reserve",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "stock-check-reserve",
        "body": [
            {"type": "p", "text": "A customer messages asking if something specific is in stock. By the time someone actually checks the shelf or the warehouse and replies, twenty or thirty minutes have passed — or worse, nobody replies with real confidence at all, because the \"official\" count in the register hasn't matched what's physically there for weeks."},
            {"type": "h2", "text": "The instant answer doesn't need a live inventory system"},
            {"type": "p", "text": "This isn't a pitch for ripping out and replacing inventory infrastructure. The module reads whatever stock sheet the business is already actually using — even a simple spreadsheet updated by hand — and answers against that. The fix is closing the gap between \"someone in the business knows the answer\" and \"the customer actually gets it in the next thirty seconds,\" not building a new system from scratch."},
            {"type": "h2", "text": "Why \"reserve\" matters as much as \"check\""},
            {"type": "p", "text": "An accurate stock answer without a way to reserve just moves the decision point rather than closing it — the customer still has to physically show up before someone else buys the item, and a meaningful share simply won't bother making a second trip on a maybe. Letting them reserve on the same WhatsApp thread turns a stock inquiry into a held sale, instead of one more inquiry that quietly evaporates."},
        ],
    },
    {
        "slug": "reorder-nudge-repeat-purchase-timing",
        "title": "The Reorder That Never Came: Why Repeat Customers Quietly Switch Suppliers",
        "dek": "A regular customer doesn't usually leave over one bad experience. They leave because nobody reached out at the exact moment they were about to reorder — so someone else did.",
        "tag": "Reorder / Repeat-Purchase Nudge",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "reorder-nudge",
        "body": [
            {"type": "p", "text": "A distributor's best customer reorders roughly every three weeks, like clockwork — except nobody at the business is actually tracking that rhythm. The business waits passively for the phone to ring, and in week four, when stock is genuinely running low on the customer's side, whichever supplier reaches out first gets the order. Sometimes that's a competitor doing exactly this on purpose."},
            {"type": "h2", "text": "Every customer has a rhythm. Most businesses aren't tracking it."},
            {"type": "p", "text": "Repeat-purchase timing isn't guesswork — it's already sitting in the business's own order history. This customer reorders roughly every 21 days; that one, every 45. A nudge timed just before that window, rather than a generic monthly blast sent to everyone regardless of where they actually are in their own cycle, reads as attentive service. A blast sent to the wrong customer at the wrong time reads as spam."},
            {"type": "h2", "text": "Why this beats a blanket \"come back\" campaign"},
            {"type": "p", "text": "A nudge sent too early feels pushy. Sent too late, the order's already gone elsewhere. Timing it to each customer's own actual cycle — not a calendar the business picked for its own convenience — is what makes the message feel like the business remembered them specifically, rather than a marketing automation firing on a schedule that has nothing to do with the customer's actual need."},
        ],
    },
    {
        "slug": "lead-qualification-scoring-speed-to-lead",
        "title": "The 5-Minute Rule Almost Nobody Follows",
        "dek": "A landmark study found waiting 30 minutes instead of 5 to contact a new lead cuts the odds of qualifying them by 21x. Most businesses' actual response time isn't measured in minutes at all.",
        "tag": "Lead Qualification & Scoring Agent",
        "read_time": "4 min read",
        "related_industry": None,
        "related_module": "lead-qualification",
        "body": [
            {"type": "p", "text": "A researcher at MIT Sloan analyzed three years of data — over 15,000 leads and 100,000 call attempts across six companies — and found a response-time cliff so steep it's still cited constantly, over a decade later, because nothing since has really contradicted it."},
            {"type": "stat", "stat": "Waiting 30 minutes instead of 5 to contact a new web-generated lead reduces the odds of qualifying that lead by a factor of 21 — a finding later replicated across 2,241 US companies in a Harvard Business Review follow-up study.", "source": "Lead Response Management study, Oldroyd (MIT Sloan) / InsideSales.com", "url": "https://www.onecavo.com/wp-content/uploads/2015/11/MIT-InsideSales.com_Lead-Response-Management.pdf"},
            {"type": "h2", "text": "Every inquiry isn't worth the same five minutes"},
            {"type": "p", "text": "Fast response matters, but giving every single inquiry the same depth of attention doesn't scale past a handful a day. What lead qualification actually solves is triage: two or three quick, specific questions — budget, timeline, what exactly they need — sort a flood of inbound into what deserves an owner's immediate personal attention right now, versus what can get a solid, professional automated reply and wait its turn."},
            {"type": "h2", "text": "Why the scoring has to happen before a human ever sees it"},
            {"type": "p", "text": "The goal isn't replacing judgment on a hot lead — it's making sure the owner's most valuable five minutes go to the three inquiries actually ready to buy right now, instead of being spent triaging window-shoppers by hand. The 21x gap above isn't decided at the negotiation table. It's decided in the first few minutes, by whoever's actually looking at the inbox that fast — and for most small businesses, that's currently nobody, reliably."},
        ],
    },
    {
        "slug": "faq-objection-handling-consistency",
        "title": "You've Answered the Same 15 Questions a Thousand Times",
        "dek": "The gap between a business that closes well and one that doesn't often comes down to whether the predictable questions get a fast, consistent answer — or a different one depending on who happened to be free.",
        "tag": "FAQ + Objection-Handling Agent",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "objection-handling",
        "body": [
            {"type": "p", "text": "\"Do you deliver to my area?\" \"What's the warranty?\" \"Can I pay in installments?\" The same handful of questions come up constantly in any business — but the quality of the answer varies by who's actually free to reply that day, and a slow or inconsistent answer to a genuinely basic question reads as unpreparedness, even when the underlying product or service is completely fine."},
            {"type": "h2", "text": "Objections aren't rejections — they're a request to be convinced"},
            {"type": "p", "text": "A price objection, or a \"let me think about it,\" is usually a request for more specific reassurance, not a firm no. A vague, generic reply loses the sale almost as surely as no reply at all. A specific, immediate answer — one that actually addresses the exact thing the customer raised — is what moves them forward, because it proves someone was actually listening to the objection rather than reading from a script."},
            {"type": "h2", "text": "Why \"escalate only what's genuinely new\" is the important part"},
            {"type": "p", "text": "This isn't trying to replace a salesperson on a genuinely unusual question — those still need a human, and should get one immediately. It's making sure the large share of questions that are entirely predictable never sit unanswered or get a half-effort reply, which frees the owner's actual attention for the smaller number of conversations that genuinely need it."},
        ],
    },
    {
        "slug": "negative-review-recovery-first-hour-window",
        "title": "The First Hour After a Bad Review Decides Whether It's a Crisis or a Non-Event",
        "dek": "Consumers now expect a fast response — and a well-handled bad review, addressed quickly, often does more for trust than another five-star one sitting unanswered.",
        "tag": "Negative Review Alert + Recovery Agent",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "negative-review-recovery",
        "body": [
            {"type": "p", "text": "A two-star review lands. It sits there — read by a handful of prospective customers before anyone from the business even notices it exists, let alone responds. By the time a reply finally goes up, days later, it reads less like resolution and more like an afterthought."},
            {"type": "stat", "stat": "19% of consumers now expect a same-day response to a review — more than triple the 6% who expected that just a year earlier — even as overall trust in reviews has fallen to 42%, making how a business actually responds the signal that's replacing blind trust in the star rating itself.", "source": "BrightLocal, Local Consumer Review Survey 2025", "url": "https://www.brightlocal.com/research/local-consumer-review-survey-2025/"},
            {"type": "h2", "text": "A bad review left unanswered confirms the reader's worst assumption"},
            {"type": "p", "text": "A prospective customer reading a bad review isn't only judging the incident described — they're judging whether the business ever addressed it. Silence reads as \"this is exactly the kind of business that doesn't care,\" even when the actual issue was a genuine one-off that any business could have."},
            {"type": "h2", "text": "Why speed matters more than the perfect apology"},
            {"type": "p", "text": "The value of catching this within the hour isn't crafting flawless PR language — it's that a fast, genuine acknowledgment plus a concrete recovery offer, sent before the review has had time to sit and be read by fifty more prospective customers, frequently gets the reviewer to update or remove it. That almost never happens once a bad review has sat unanswered for a week."},
        ],
    },
    {
        "slug": "abandoned-inquiry-win-back-follow-up-silence",
        "title": "The Inquiry You Wrote Off Isn't Actually Gone",
        "dek": "Most \"lost\" leads weren't lost to a competitor's better pitch. They were lost to silence, on both sides, that nobody broke first.",
        "tag": "Abandoned-Inquiry Win-Back Nudge",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "win-back",
        "body": [
            {"type": "p", "text": "A promising inquiry comes in, a couple of messages get exchanged, and then — nothing. No explicit no, just quiet. Most businesses read that silence as a lost deal and move on. Often, it's just a customer who got busy, or is comparing a few options, waiting to see who follows up first."},
            {"type": "h2", "text": "A quiet inquiry isn't a 'no' — it's usually just a full inbox on both sides"},
            {"type": "p", "text": "Writing off silence as disinterest loses deals that were genuinely still winnable. The customer who went quiet frequently ends up buying from whichever business happened to follow up again — not because that business's offer was better, but because it was the one still in the conversation when the customer finally circled back to make a decision."},
            {"type": "h2", "text": "Why a specific, well-timed nudge outperforms a generic \"still interested?\""},
            {"type": "p", "text": "A follow-up sent a few days later that references the actual thing the customer originally asked about — not a generic check-in — reads as attentive follow-through rather than desperation. It's a small difference in wording that often reopens a conversation both sides had genuinely let go cold, at close to zero cost to send."},
        ],
    },
    {
        "slug": "local-seo-content-cadence-google-business-profile",
        "title": "Why Your Google Business Profile Looks Abandoned — Even If Your Business Isn't",
        "dek": "A listing that hasn't posted in months signals the same thing to a browsing customer that it does to a search algorithm: this business isn't actively here anymore.",
        "tag": "AI Local-SEO Content Agent",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "seo-content-agent",
        "body": [
            {"type": "p", "text": "Two competing businesses, similar ratings, similar reviews. One's Google Business Profile has a post from eight months ago. The other posted an update last week. A customer scanning search results reads the second as more current and more attentive — even if both businesses are equally open, equally busy, equally real."},
            {"type": "h2", "text": "Consistency, not virality, is what a Business Profile post is for"},
            {"type": "p", "text": "This isn't about writing something that goes viral. It's about maintaining a visible, boring cadence — a weekly post, a current offer, a photo from a recently completed job — that signals the business is active and paying attention. Each individual post takes almost no creative effort; what most businesses actually lack isn't ideas, it's a system that forces the habit."},
            {"type": "h2", "text": "Why a 2-minute review beats a from-scratch draft, every time"},
            {"type": "p", "text": "The real bottleneck was never a shortage of things to say — it's the blank page. A draft that's already written, ready to skim, tweak and approve in two minutes, removes the cost that keeps \"we should post more often\" as a permanent intention instead of something that actually happens week after week."},
        ],
    },
    {
        "slug": "missed-call-instant-winback-whatsapp",
        "title": "The Missed Call Is the Fastest-Dying Lead in Your Business",
        "dek": "A caller who couldn't get through rarely calls back later. They call the next name on their list — often within minutes, while the phone's still in their hand.",
        "tag": "Missed-Call Instant Win-Back",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "missed-call-winback",
        "body": [
            {"type": "p", "text": "A call comes in and, for whatever reason, nobody picks up in time. In most businesses, that's simply a missed call — noticed later, if at all, with no real way to know who called or why. To the caller, though, that exact moment is the most active point of their search: phone out, actively comparing options, already dialling."},
            {"type": "h2", "text": "A missed call isn't a lost lead yet — for about ten minutes"},
            {"type": "p", "text": "The caller's intent decays fast for a simple reason: the very next action available to them is dialling the next result on the list. The same research on lead response speed that shows online-inquiry qualification odds collapsing within minutes applies even more sharply here, because a phone call means the person was already actively reaching out, not passively waiting for a reply."},
            {"type": "h2", "text": "Why the win-back message has to fire from the missed call itself"},
            {"type": "p", "text": "An automatic WhatsApp the moment the call is missed — \"Sorry we missed your call, how can we help?\" — reaches the caller while they're still mid-search, often before they've dialled the next number. That turns a missed call from a dead end sitting unnoticed in a call log into a live conversation on a channel they can answer immediately, without having to call back and risk missing again."},
        ],
    },
    {
        "slug": "ai-quotation-drafting-b2b-response-speed",
        "title": "The Deal That Went to Whoever Sent the Quote First",
        "dek": "In B2B and services buying, a fast, clean, professional-looking quote often outcompetes a marginally better price that arrives a day later.",
        "tag": "AI Quotation Drafting Agent",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "quotation-drafting",
        "body": [
            {"type": "p", "text": "A buyer requests quotes from three vendors for the same job. Two reply within a day with a clean, itemized document. The third takes four days, because turning a rough requirement into a proper quote has to wait for whoever on the team has a free hour to format it. By day four, the decision is often already made."},
            {"type": "h2", "text": "A slow quote doesn't just lose time — it loses credibility"},
            {"type": "p", "text": "A quote that takes days to arrive doesn't only delay a decision. It quietly signals how responsive this vendor is likely to be after the sale too. Buyers reasonably read turnaround speed as a preview of what working with a business will actually feel like — fast and organized, or slow and understaffed."},
            {"type": "h2", "text": "Why \"properly formatted\" matters as much as \"fast\""},
            {"type": "p", "text": "The module isn't only about speed — it turns a rough, informally-described requirement into a clean, itemized, professional-looking quote automatically, so the owner isn't trading polish for speed. They get both: a document that looks like it came from an organized business, ready to approve and send within minutes of the original request, instead of built from scratch under time pressure."},
        ],
    },
    {
        "slug": "competitor-price-watch-margin-protection",
        "title": "You Don't Need to Watch Competitors Constantly. You Need to Know the Moment It Actually Matters.",
        "dek": "Most small businesses either obsess over competitor pricing or ignore it entirely. Neither is the fix — the fix is knowing the instant something genuinely changes.",
        "tag": "Competitor Price-Watch Alert",
        "read_time": "3 min read",
        "related_industry": None,
        "related_module": "competitor-price-watch",
        "body": [
            {"type": "p", "text": "A business sets its pricing once and rarely revisits it. Meanwhile, a competitor quietly runs a discount, or changes a listed price — and by the time anyone notices, often from a customer mentioning it in passing, the business has been losing comparison-shoppers for weeks without ever knowing why."},
            {"type": "h2", "text": "Manually checking competitor prices doesn't scale, and it doesn't need to"},
            {"type": "p", "text": "Nobody has time to check five competitor listings by hand every day, and trying to creates exactly the \"check obsessively for a week, then forget for a month\" pattern that helps nobody. What's actually useful isn't constant manual monitoring — it's a system that only surfaces a change when one genuinely happens, so attention gets spent on the moment that matters instead of ongoing vigilance nobody can sustain."},
            {"type": "h2", "text": "Why an alert is worth more than a dashboard"},
            {"type": "p", "text": "A dashboard someone has to remember to open adds one more task that quietly stops happening after the first busy week. An alert that reaches the owner directly the moment a real price change happens turns \"keeping an eye on competitors\" from a to-do list item nobody gets to into something that simply happens on its own, in the background, without needing to be remembered."},
        ],
    },
]

# ------------------------------------------------------------------
# FREE_TOOLS — real, working client-side calculators, one per industry.
# "fields" define the input form; "compute_js" is a plain JS function
# body (NOT an f-string — keep it that way in build.py, its braces are
# real JS syntax) that reads values and returns a result-panel HTML string.
# ------------------------------------------------------------------
FREE_TOOLS = [
    {
        "slug": "landed-cost-calculator",
        "title": "Landed Cost Calculator",
        "tagline": "FOB, freight, insurance, and duty — the real cost per shipment, not just the FOB price.",
        "industry": "export-trading",
        "fields": [
            {"id": "fob", "label": "FOB Value (₹)", "default": 500000, "step": 1000},
            {"id": "freight", "label": "Freight (₹)", "default": 40000, "step": 1000},
            {"id": "insurance", "label": "Insurance (₹)", "default": 5000, "step": 500},
            {"id": "duty", "label": "Customs Duty (%)", "default": 7.5, "step": 0.5},
            {"id": "other", "label": "Other Charges (₹)", "default": 8000, "step": 500},
        ],
        "compute_js": """function computeResult(v) {
  var cif = v.fob + v.freight + v.insurance;
  var dutyAmt = cif * (v.duty / 100);
  var landed = cif + dutyAmt + v.other;
  var markup = ((landed - v.fob) / v.fob * 100).toFixed(1);
  return '<div class="tr-row"><span>CIF Value</span><b>₹' + Math.round(cif).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Duty (' + v.duty + '%)</span><b>₹' + Math.round(dutyAmt).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row tr-total"><span>Total Landed Cost</span><b>₹' + Math.round(landed).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-note">' + markup + '% above FOB — quote from this number, not the FOB price.</div>';
}""",
        "content": [{'type': 'h2', 'text': "Landed cost isn't just FOB + duty — the rate depends on your HS code"},
 {'type': 'p',
  'text': 'Basic Customs Duty (BCD) in India is set per HS (Harmonized System) code, not as one '
          'flat number — which is why two exporters shipping similar-looking goods can land at '
          'very different total costs. The Union Budget 2025-26 simplified the BCD structure to '
          'just 8 slabs (including zero), collapsing dozens of legacy rates, but the actual rate '
          'for any specific product still has to be checked against its HS code on ICEGATE before '
          "it's quoted to a buyer."},
 {'type': 'table',
  'caption': 'Illustrative Basic Customs Duty ranges by category (post Union Budget 2025-26 '
             'rationalisation)',
  'headers': ['Category', 'Typical BCD range', 'Note'],
  'rows': [['Industrial machinery and capital goods',
            '0% – 7.5%',
            'Many lines fully exempted to support domestic manufacturing'],
           ['Consumer electronics (e.g. display panels)',
            '5% – 20%',
            'Duty on Interactive Flat Panel Displays raised to 20% in Budget 2025-26 to correct an '
            'inverted duty structure'],
           ['Textiles and technical textile fabrics',
            '10% – 20%',
            'Knitted fabric BCD revised to 20% or ₹115/kg, whichever is higher'],
           ['Chemicals',
            'Wide range, some lines up to 70%+',
            'Specific lines (e.g. lab chemicals) were cut from 150% to 70% in Budget 2025-26 — '
            'highly HS-code specific']],
  'note': 'These are illustrative category ranges, not quotable rates — always confirm the exact '
          "duty for your product's specific HS code on ICEGATE (icegate.gov.in) before pricing a "
          'shipment.'},
 {'type': 'stat',
  'stat': 'Union Budget 2025-26 removed 7 more customs tariff rates for industrial goods, bringing '
          'the total number of Basic Customs Duty slabs down to 8 (including zero) — while keeping '
          'the effective duty burden on most goods roughly unchanged.',
  'source': 'Press Information Bureau, Government of India',
  'url': 'https://pib.gov.in/PressReleseDetailm.aspx?PRID=2098364'},
 {'type': 'stat',
  'stat': 'Under CIF Incoterms rules, the minimum insurance cover required is 110% of the invoice '
          'value of the goods — insurance premiums themselves typically run 0.5%-1% of FOB/CIF '
          'value depending on cargo type and route, well below what most first-time exporters '
          'budget for.',
  'source': 'iContainers — CIF Incoterm guide',
  'url': 'https://www.icontainers.com/help/incoterms/cif/'}],
    },
    {
        "slug": "missed-appointment-loss-calculator",
        "title": "Missed-Appointment Revenue Loss Calculator",
        "tagline": "See what no-shows are actually costing a branch every month.",
        "industry": "hospital",
        "fields": [
            {"id": "perDay", "label": "Appointments Booked / Day", "default": 40, "step": 1},
            {"id": "noShow", "label": "No-Show Rate (%)", "default": 18, "step": 1},
            {"id": "revenue", "label": "Avg Revenue / Appointment (₹)", "default": 600, "step": 50},
            {"id": "days", "label": "Working Days / Month", "default": 26, "step": 1},
        ],
        "compute_js": """function computeResult(v) {
  var missedPerDay = v.perDay * (v.noShow / 100);
  var monthlyLoss = missedPerDay * v.revenue * v.days;
  return '<div class="tr-row"><span>Missed appointments / day</span><b>' + missedPerDay.toFixed(1) + '</b></div>'
       + '<div class="tr-row tr-total"><span>Revenue lost / month</span><b>₹' + Math.round(monthlyLoss).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-note">An automatic reminder the day before a slot is the cheapest fix for this number.</div>';
}""",
        "content": [{'type': 'h2', 'text': "No-shows aren't a rounding error — they're a recurring revenue leak"},
 {'type': 'p',
  'text': "Every missed slot is lost revenue that already had a cost attached to it — the doctor's "
          'time, the front-desk booking effort, and the opportunity cost of a patient who could '
          'have filled that slot instead. A no-show isn\'t "nothing happened"; it\'s a slot that '
          'generated zero revenue but was fully staffed for.'},
 {'type': 'stat',
  'stat': 'A 2023 rapid systematic review in the Journal of the American Medical Informatics '
          'Association found the global average outpatient no-show rate runs around 23%, ranging '
          'from roughly 13% in Oceania to as high as 43% in parts of Africa, with Asia among the '
          'higher-rate regions in the pooled studies.',
  'source': 'Journal of the American Medical Informatics Association (Oxford Academic), 2023',
  'url': 'https://academic.oup.com/jamia/article/30/3/559/6889491'},
 {'type': 'p',
  'text': 'A single, India-specific published no-show rate proving one exact number for Indian '
          "hospitals wasn't findable in peer-reviewed literature at the time of writing — so we're "
          'not going to pretend one exists. What the global research does show consistently is '
          'that no-show rates in the high-teens to mid-20s percent range are common across '
          "outpatient settings worldwide, which puts this calculator's default 18% well within the "
          'range multiple independent studies report — not an outlier assumption.'},
 {'type': 'p',
  'text': "The same systematic review's core finding is worth repeating: predictive, "
          'reminder-based interventions are the most consistently effective lever for reducing '
          'no-shows — which is exactly why an automatic WhatsApp reminder the day before a slot is '
          'the standard, low-cost fix, not a nice-to-have.'}],
    },
    {
        "slug": "batch-profitability-calculator",
        "title": "Batch Profitability Calculator",
        "tagline": "Know the real margin on a batch before you price the next one.",
        "industry": "coaching-institute",
        "fields": [
            {"id": "students", "label": "Students in Batch", "default": 30, "step": 1},
            {"id": "fee", "label": "Fee per Student (₹)", "default": 12000, "step": 500},
            {"id": "faculty", "label": "Faculty Cost (₹)", "default": 60000, "step": 1000},
            {"id": "overhead", "label": "Other Overhead (₹)", "default": 20000, "step": 1000},
        ],
        "compute_js": """function computeResult(v) {
  var revenue = v.students * v.fee;
  var cost = v.faculty + v.overhead;
  var profit = revenue - cost;
  var margin = revenue > 0 ? (profit / revenue * 100).toFixed(1) : '0';
  return '<div class="tr-row"><span>Total Revenue</span><b>₹' + revenue.toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Total Cost</span><b>₹' + cost.toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row tr-total"><span>Profit (' + margin + '% margin)</span><b>₹' + profit.toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2',
  'text': "What a healthy batch margin actually looks like in India's coaching market"},
 {'type': 'stat',
  'stat': "India's coaching institutes market is valued at USD 7.2 billion in 2025 and projected "
          'to reach USD 17.8 billion by 2034 — a sector growing fast enough that margin discipline '
          'on each batch matters more, not less, as competition for the same students intensifies.',
  'source': 'IMARC Group',
  'url': 'https://www.imarcgroup.com/india-coaching-institutes-market'},
 {'type': 'stat',
  'stat': 'Independent tutors with low fixed overhead typically run profit margins of 60%-80%, '
          'while mid-sized coaching institutes carrying rented classroom space and faculty '
          'salaries usually operate at a much thinner 35%-55%.',
  'source': 'Bajaj Finserv — Coaching Institute Business guide',
  'url': 'https://www.bajajfinserv.in/coaching-institute-business'},
 {'type': 'p',
  'text': 'That gap is almost entirely explained by the two cost lines this calculator asks for: '
          'faculty cost and other overhead. A batch that looks profitable on fee collections alone '
          'can still be a 35%-margin batch once a fair share of rent, staff and marketing spend is '
          "allocated to it — which is the number that actually determines whether it's worth "
          'running again next term.'}],
    },
    {
        "slug": "home-loan-emi-calculator",
        "title": "Home Loan EMI Calculator",
        "tagline": "The monthly number a buyer actually cares about.",
        "industry": "real-estate-developer",
        "fields": [
            {"id": "principal", "label": "Loan Amount (₹)", "default": 4000000, "step": 50000},
            {"id": "rate", "label": "Interest Rate (% p.a.)", "default": 8.5, "step": 0.1},
            {"id": "years", "label": "Tenure (years)", "default": 20, "step": 1},
        ],
        "compute_js": """function computeResult(v) {
  var r = v.rate / 12 / 100;
  var n = v.years * 12;
  var emi = r === 0 ? v.principal / n : (v.principal * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
  var totalPay = emi * n;
  var totalInterest = totalPay - v.principal;
  return '<div class="tr-row tr-total"><span>Monthly EMI</span><b>₹' + Math.round(emi).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Total Interest</span><b>₹' + Math.round(totalInterest).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Total Payment</span><b>₹' + Math.round(totalPay).toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2', 'text': 'Home loan interest rates — leading Indian banks (as of September 2026)'},
 {'type': 'table',
  'caption': 'Rates as published on each bank\'s own site',
  'headers': ['Bank', 'Interest Rate (p.a.)', 'Source'],
  'rows': [[{'text': 'SBI',
             'url': 'https://sbi.co.in/web/personal-banking/loans/home-loans/interest-rates'},
            '7.25% – 8.45%',
            {'text': 'SBI official rate page',
             'url': 'https://sbi.co.in/web/personal-banking/loans/home-loans/interest-rates'}],
           [{'text': 'HDFC Bank',
             'url': 'https://www.hdfcbank.com/personal/borrow/popular-loans/home-loan/home-loan-interest-rate'},
            '7.75% – 9.40%',
            {'text': 'HDFC Bank official rate page',
             'url': 'https://www.hdfcbank.com/personal/borrow/popular-loans/home-loan/home-loan-interest-rate'}],
           [{'text': 'ICICI Bank',
             'url': 'https://www.icicibank.com/personal-banking/loans/home-loan/interest-rate'},
            '7.50% – 9.00%',
            {'text': 'ICICI Bank official rate page',
             'url': 'https://www.icicibank.com/personal-banking/loans/home-loan/interest-rate'}],
           [{'text': 'Axis Bank',
             'url': 'https://www.axisbank.com/retail/loans/home-loan/interest-rate'},
            '8.00% – 9.15%',
            {'text': 'Axis Bank official rate page',
             'url': 'https://www.axisbank.com/retail/loans/home-loan/interest-rate'}],
           [{'text': 'Kotak Mahindra Bank',
             'url': 'https://www.kotak.com/en/personal-banking/loans/home-loan/interest-rates.html'},
            '7.60% – 9.45%',
            {'text': 'Kotak official rate page',
             'url': 'https://www.kotak.com/en/personal-banking/loans/home-loan/interest-rates.html'}],
           [{'text': 'Punjab National Bank', 'url': 'https://www.pnbindia.in/home-loan.html'},
            '7.50% – 9.75%',
            {'text': 'PNB official rate page', 'url': 'https://www.pnbindia.in/home-loan.html'}]],
  'note': 'Rates change with RBI repo-rate moves and vary by CIBIL score, loan-to-value and '
          'employment type — the figures above are as reported across bank-published rate pages in '
          "September 2026. Always confirm the live number on the bank's own page before quoting it "
          'to a customer.'},
 {'type': 'h2', 'text': "What homes actually cost, and how fast that's moving"},
 {'type': 'stat',
  'stat': "Average residential prices across India's top 7 cities rose about 8% in 2025, from "
          'roughly ₹8,590/sq ft at end-2024 to ₹9,260/sq ft at end-2025 — with NCR the standout, '
          'posting double-digit growth while most other metros saw single-digit appreciation.',
  'source': 'ANAROCK Research',
  'url': 'https://telanganatoday.com/housing-sales-volume-down-14-pc-in-2025-in-7-cities-anarock'},
 {'type': 'stat',
  'stat': "Over a 5-year window, ANAROCK data shows construction costs across India's top 7 cities "
          'up roughly 34%, while average housing prices in those same cities rose about 59% — '
          'appreciation that has outpaced the cost of actually building the homes.',
  'source': 'ANAROCK Research, via Business Standard',
  'url': 'https://www.business-standard.com/industry/news/india-housing-prices-construction-costs-top-seven-cities-anarock-126090300706_1.html'},
 {'type': 'p',
  'text': 'That appreciation is exactly why the loan amount a buyer types into this calculator '
          'keeps climbing every year, even for the same 2BHK — and why a same-day EMI number, '
          'backed by a real bank rate rather than a guessed one, is what actually moves a hesitant '
          'lead toward booking a site visit.'}],
    },
    {
        "slug": "quote-margin-calculator",
        "title": "Quote Margin Calculator",
        "tagline": "Check the real margin on an RFQ before it goes out.",
        "industry": "b2b-manufacturer",
        "fields": [
            {"id": "cost", "label": "Cost Price / Unit (₹)", "default": 180, "step": 5},
            {"id": "price", "label": "Quoted Price / Unit (₹)", "default": 240, "step": 5},
            {"id": "qty", "label": "Order Quantity", "default": 5000, "step": 100},
        ],
        "compute_js": """function computeResult(v) {
  var marginUnit = v.price - v.cost;
  var marginPct = v.price > 0 ? (marginUnit / v.price * 100).toFixed(1) : '0';
  var totalProfit = marginUnit * v.qty;
  return '<div class="tr-row"><span>Margin / Unit</span><b>₹' + marginUnit.toFixed(2) + '</b></div>'
       + '<div class="tr-row"><span>Margin %</span><b>' + marginPct + '%</b></div>'
       + '<div class="tr-row tr-total"><span>Total Profit on Order</span><b>₹' + Math.round(totalProfit).toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2', 'text': "What's actually a healthy margin on a manufacturing quote"},
 {'type': 'stat',
  'stat': "CRISIL's SME Tracker found CRISIL-rated micro and small enterprises (MSEs) in men's "
          'apparel manufacturing running an average operating profit margin of 9.8% — about 200 '
          "basis points higher than kids' apparel (7.5%) and women's apparel (6.9%) makers in the "
          'same rated cohort.',
  'source': 'CRISIL SME Tracker',
  'url': 'https://www.simamills.in/latest-news/crisil-sme-tracker-for-mses-mens-apparel-is-where-the-money-is/'},
 {'type': 'p',
  'text': 'That single-digit range is typical of Indian manufacturing more broadly — most SME '
          'manufacturers operate on net margins in the 5%-10% band, thin enough that a quote sent '
          'out 3 days late to a price-sensitive buyer, or shaved by a percentage point to win the '
          'order, can erase most of the profit on that run before a single unit ships. Checking '
          'the real margin on an RFQ before it goes out, not after the PO lands, is what keeps a '
          '"won" order from actually being a break-even one.'}],
    },
    {
        "slug": "admission-conversion-calculator",
        "title": "Admission-to-Enrollment Conversion Calculator",
        "tagline": "See exactly where admission-week enquiries are actually leaking.",
        "industry": "private-school",
        "fields": [
            {"id": "enquiries", "label": "Enquiries Received", "default": 120, "step": 1},
            {"id": "tests", "label": "Admission Tests Booked", "default": 70, "step": 1},
            {"id": "admits", "label": "Admissions Confirmed", "default": 45, "step": 1},
            {"id": "fee", "label": "Avg Annual Fee (₹)", "default": 90000, "step": 1000},
        ],
        "compute_js": """function computeResult(v) {
  var toTest = v.enquiries > 0 ? (v.tests / v.enquiries * 100).toFixed(1) : '0';
  var toAdmit = v.tests > 0 ? (v.admits / v.tests * 100).toFixed(1) : '0';
  var overall = v.enquiries > 0 ? (v.admits / v.enquiries * 100).toFixed(1) : '0';
  var revenue = v.admits * v.fee;
  return '<div class="tr-row"><span>Enquiry → Test Booked</span><b>' + toTest + '%</b></div>'
       + '<div class="tr-row"><span>Test → Admission</span><b>' + toAdmit + '%</b></div>'
       + '<div class="tr-row"><span>Overall Conversion</span><b>' + overall + '%</b></div>'
       + '<div class="tr-row tr-total"><span>Revenue Booked</span><b>₹' + revenue.toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2',
  'text': "Fee income is growing across India's schools — but so is scrutiny on every enquiry"},
 {'type': 'stat',
  'stat': 'Fee income across 96 CRISIL-rated Indian schools and colleges, together generating '
          'nearly ₹20,000 crore in annual fee income, was projected to grow 12%-14% in FY25 on '
          'higher enrolments and fee revisions, with operating margins holding around 28%.',
  'source': 'CRISIL Ratings',
  'url': 'https://www.crisilratings.com/en/home/newsroom/press-releases/2024/10/fee-income-of-educational-institutes-to-grow-12-14percent-this-fiscal.html'},
 {'type': 'stat',
  'stat': 'Government survey data shows households spending on private schooling running nearly 9x '
          'what government-school families spend — ₹25,002 vs ₹2,863 per student annually — with '
          'urban course-fee spending (₹15,143) nearly 4x the rural average (₹3,979).',
  'source': 'MoSPI Comprehensive Modular Survey: Education (CMS:E) 2025, via Business Standard',
  'url': 'https://www.business-standard.com/education/news/education-mospi-survey-private-school-government-scholarship-fees-coaching-tuition-urban-rural-125082601316_1.html'},
 {'type': 'p',
  'text': 'That gap is exactly why the Avg. Annual Fee figure in this calculator swings so widely '
          'by school and city — a ₹90,000 default sits well above the national private-school '
          'average, but squarely in range for a mid-tier CBSE/ICSE school in a metro. Whatever the '
          'actual number, admission-week revenue is only ever as real as the conversion funnel '
          "behind it: an enquiry that never gets a same-day WhatsApp reply doesn't become a test "
          "booking, and a test booking that isn't followed up doesn't become an admission — "
          'regardless of how strong the fee income looks on paper.'}],
    },
    {
        "slug": "home-collection-savings-calculator",
        "title": "Home-Collection Time & Cost Savings Calculator",
        "tagline": "What home collection actually saves a patient, per month.",
        "industry": "diagnostic-lab",
        "fields": [
            {"id": "labTime", "label": "Time to Visit Lab (mins)", "default": 45, "step": 5},
            {"id": "homeTime", "label": "Time for Home Collection (mins)", "default": 10, "step": 5},
            {"id": "travelCost", "label": "Travel Cost to Lab (₹)", "default": 100, "step": 10},
            {"id": "testsMonth", "label": "Tests / Month (household)", "default": 2, "step": 1},
        ],
        "compute_js": """function computeResult(v) {
  var timeSaved = (v.labTime - v.homeTime) * v.testsMonth;
  var costSaved = v.travelCost * v.testsMonth;
  return '<div class="tr-row"><span>Time Saved / Month</span><b>' + timeSaved + ' mins</b></div>'
       + '<div class="tr-row tr-total"><span>Cost Saved / Month</span><b>₹' + costSaved.toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2',
  'text': 'What home collection actually costs — and why the big chains already made it free'},
 {'type': 'table',
  'caption': 'Published test pricing across major Indian diagnostic chains (illustrative, '
             'September 2026)',
  'headers': ['Chain', 'Thyroid Profile', 'Home collection'],
  'rows': [[{'text': 'Dr Lal PathLabs',
             'url': 'https://www.lalpathlabs.com/pathology-test/thyroid-profile-total'},
            '~₹930 (varies by city)',
            'Free in 30+ cities'],
           [{'text': 'Metropolis Healthcare',
             'url': 'https://www.metropolisindia.com/parameter/thyroid-panel-4'},
            '~₹505–₹600 (Mumbai pricing)',
            'Home collection available, priced by location'],
           [{'text': 'Thyrocare', 'url': 'https://thyrocareservices.com/'},
            'Bundled from ₹799–₹999 (Aarogyam packages, 60-80+ tests)',
            'Free home collection, no hidden charge']],
  'note': 'Prices vary by city, package and ongoing offers — figures above are as '
          "published/aggregated in September 2026. Always confirm current pricing on the lab's own "
          'website before quoting a patient.'},
 {'type': 'p',
  'text': 'The pattern across all three major chains is the same: free or near-free home '
          'collection is now the industry default, not a premium add-on. A local lab that still '
          "treats a home-collection request as a scheduling hassle isn't just losing convenience "
          'points — it\'s competing against national chains that have already made "send someone '
          'to my house" the cheapest way to win the sample.'}],
    },
    {
        "slug": "wedding-budget-calculator",
        "title": "Wedding Budget Calculator",
        "tagline": "A realistic total before the vendor conversations start.",
        "industry": "wedding-planner-banquet",
        "fields": [
            {"id": "guests", "label": "Guest Count", "default": 300, "step": 10},
            {"id": "plate", "label": "Per-Plate Cost (₹)", "default": 1200, "step": 50},
            {"id": "venue", "label": "Venue Cost (₹)", "default": 300000, "step": 5000},
            {"id": "decor", "label": "Decor Budget (₹)", "default": 150000, "step": 5000},
            {"id": "photo", "label": "Photography (₹)", "default": 80000, "step": 5000},
        ],
        "compute_js": """function computeResult(v) {
  var catering = v.guests * v.plate;
  var subtotal = catering + v.venue + v.decor + v.photo;
  var misc = subtotal * 0.1;
  var total = subtotal + misc;
  return '<div class="tr-row"><span>Catering</span><b>₹' + catering.toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Venue + Decor + Photography</span><b>₹' + (v.venue + v.decor + v.photo).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Misc & Contingency (10%)</span><b>₹' + Math.round(misc).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row tr-total"><span>Estimated Total</span><b>₹' + Math.round(total).toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2', 'text': 'Real numbers before the vendor calls start'},
 {'type': 'stat',
  'stat': 'An estimated 32 lakh weddings were expected across India in a single wedding-season '
          'window (November 4 – December 14), generating around ₹3.75 lakh crore in business — a '
          'volume of simultaneous demand compressed into a few weeks.',
  'source': 'Deccan Herald, citing the Confederation of All India Traders (CAIT)',
  'url': 'https://www.deccanherald.com/amp/story/india%2F32-lakh-weddings-in-india-during-november-4-december-14-to-generate-rs-375-lakh-crore-business-cait-1160192.html'},
 {'type': 'stat',
  'stat': "India's average wedding budget stood at ₹39.5 lakh in 2025, up 8% year-on-year — "
          'ranging from ₹15-25 lakh for a Tier-2 city wedding, to ₹35-38 lakh in a metro, up to '
          '₹58 lakh for a destination wedding.',
  'source': 'WedMeGood Annual Wedding Industry Report 2025-26',
  'url': 'https://www.wedmegood.com/blog/wedmegood-annual-wedding-industry-report-2025-2026/'},
 {'type': 'p',
  'text': 'Those ranges are exactly why a couple asking "what\'s this actually going to cost?" '
          'needs a real number fast, not a vague estimate a week later — by the time a planner '
          "gets back to them with a rough figure, they've often already gotten a faster answer "
          'from someone else. A guest count, per-plate cost and venue budget plugged in here gets '
          'them a realistic total in the same conversation, while the quote is still theirs to '
          'win.'}],
    },
    {
        "slug": "bmi-tdee-calculator",
        "title": "BMI & Calorie (TDEE) Calculator",
        "tagline": "The two numbers every trial member asks about first.",
        "industry": "gym-fitness-chain",
        "fields": [
            {"id": "weight", "label": "Weight (kg)", "default": 70, "step": 1},
            {"id": "height", "label": "Height (cm)", "default": 170, "step": 1},
            {"id": "age", "label": "Age", "default": 28, "step": 1},
            {"id": "activity", "label": "Activity Multiplier (1.2–1.9)", "default": 1.375, "step": 0.025},
        ],
        "compute_js": """function computeResult(v) {
  var heightM = v.height / 100;
  var bmi = v.weight / (heightM * heightM);
  var category = bmi < 18.5 ? 'Underweight' : bmi < 25 ? 'Normal' : bmi < 30 ? 'Overweight' : 'Obese';
  var bmr = 10 * v.weight + 6.25 * v.height - 5 * v.age + 5;
  var tdee = bmr * v.activity;
  return '<div class="tr-row"><span>BMI</span><b>' + bmi.toFixed(1) + ' — ' + category + '</b></div>'
       + '<div class="tr-row tr-total"><span>Daily Calories (TDEE)</span><b>' + Math.round(tdee).toLocaleString('en-IN') + ' kcal</b></div>';
}""",
        "content": [{'type': 'h2', 'text': 'Why this calculator\'s "Normal" range isn\'t the same for every body'},
 {'type': 'table',
  'caption': 'BMI classification — WHO global vs. ICMR/WHO Asia-Pacific cutoffs for Indian bodies',
  'headers': ['Category', 'WHO global cutoff', 'ICMR (2022) / WHO Asia-Pacific cutoff'],
  'rows': [['Underweight', '< 18.5', '< 18.5'],
           ['Normal', '18.5 – 24.9', '18.5 – 22.9'],
           ['Overweight', '25.0 – 29.9', '23.0 – 24.9'],
           ['Obese', '≥ 30.0', '≥ 25.0']],
  'note': 'Source: Indian Council of Medical Research (ICMR), 2022 guidelines, and WHO '
          'Asia-Pacific BMI classification. Cutoffs vary slightly across published summaries — '
          'treat as a directional guide, not a clinical diagnosis.'},
 {'type': 'p',
  'text': 'Indians and other South Asians tend to carry more visceral fat — the fat around '
          'internal organs that drives metabolic risk — at a lower body weight than Western '
          "populations, which is why ICMR and WHO's own Asia-Pacific guidance recommend lower "
          'cutoffs: overweight from a BMI of 23, not 25. A trial member who reads "Normal" on a '
          'Western BMI chart may already be in the overweight range by the standard actually '
          'relevant to their own health risk — a distinction worth surfacing before, not after, '
          'they sign up.'}],
    },
    {
        "slug": "income-tax-calculator",
        "title": "Income Tax Calculator (New Regime, Illustrative)",
        "tagline": "A quick estimate — always confirm current slabs on incometax.gov.in.",
        "industry": "ca-legal-firm",
        "fields": [
            {"id": "income", "label": "Annual Taxable Income (₹)", "default": 1200000, "step": 10000},
        ],
        "compute_js": """function computeResult(v) {
  var slabs = [[300000,0],[700000,0.05],[1000000,0.10],[1200000,0.15],[1500000,0.20],[Infinity,0.30]];
  var tax = 0, prev = 0;
  for (var i = 0; i < slabs.length; i++) {
    var upper = Math.min(v.income, slabs[i][0]);
    if (upper > prev) tax += (upper - prev) * slabs[i][1];
    prev = slabs[i][0];
    if (v.income <= slabs[i][0]) break;
  }
  if (v.income <= 700000) tax = 0; // Section 87A rebate, simplified
  var cess = tax * 0.04;
  var total = tax + cess;
  return '<div class="tr-row"><span>Tax (before cess)</span><b>₹' + Math.round(tax).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row"><span>Health & Education Cess (4%)</span><b>₹' + Math.round(cess).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row tr-total"><span>Estimated Total Tax</span><b>₹' + Math.round(total).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-note">Illustrative only, simplified new-regime slabs — a CA can confirm your exact liability and deductions.</div>';
}""",
        "content": [{'type': 'h2',
  'text': 'The real slabs — this calculator uses a simplified version, always confirm the exact '
          'one'},
 {'type': 'table',
  'caption': 'New Tax Regime slabs — FY 2025-26 / FY 2026-27 (AY 2026-27 / 2027-28)',
  'headers': ['Taxable Income', 'Rate'],
  'rows': [['Up to ₹4,00,000', 'Nil'],
           ['₹4,00,001 – ₹8,00,000', '5%'],
           ['₹8,00,001 – ₹12,00,000', '10%'],
           ['₹12,00,001 – ₹16,00,000', '15%'],
           ['₹16,00,001 – ₹20,00,000', '20%'],
           ['₹20,00,001 – ₹24,00,000', '25%'],
           ['Above ₹24,00,000', '30%']],
  'note': 'Section 87A rebate makes income up to ₹12 lakh effectively tax-free under the new '
          'regime (₹12.75 lakh for salaried taxpayers, after the ₹75,000 standard deduction). The '
          'new regime is the default regime unless the old regime is specifically opted into.'},
 {'type': 'table',
  'caption': 'Old Tax Regime slabs (unchanged for several years)',
  'headers': ['Taxable Income', 'Rate'],
  'rows': [['Up to ₹2,50,000', 'Nil'],
           ['₹2,50,001 – ₹5,00,000', '5%'],
           ['₹5,00,001 – ₹10,00,000', '20%'],
           ['Above ₹10,00,000', '30%']],
  'note': 'Section 87A rebate makes income up to ₹5 lakh effectively tax-free under the old '
          'regime. Standard deduction of ₹50,000 applies for salaried/pension income only.'},
 {'type': 'p',
  'text': 'This calculator runs a simplified, illustrative version of the new-regime slabs and a '
          '4% cess — it does not reflect deductions, exemptions, or every nuance of the slab '
          "structure shown above. It's meant to give a rough directional number in a client "
          'conversation, not a filing-ready figure. Always confirm the exact, current slab '
          'structure and any applicable deductions directly on incometax.gov.in, or with a CA, '
          "before it's used for anything beyond a ballpark estimate."}],
    },
    {
        "slug": "renovation-cost-estimator",
        "title": "Renovation Cost Estimator",
        "tagline": "A ballpark before the first site visit.",
        "industry": "interior-designer",
        "fields": [
            {"id": "area", "label": "Area (sq ft)", "default": 1000, "step": 50},
            {"id": "rate", "label": "Package Rate (₹/sq ft)", "default": 1800, "step": 100},
        ],
        "compute_js": """function computeResult(v) {
  var low = v.area * v.rate * 0.9;
  var high = v.area * v.rate * 1.15;
  return '<div class="tr-row tr-total"><span>Estimated Range</span><b>₹' + Math.round(low).toLocaleString('en-IN') + ' – ₹' + Math.round(high).toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-note">Final cost depends on material grade and site condition — this is a planning-stage range.</div>';
}""",
        "content": [{'type': 'h2', 'text': 'What renovation actually costs per sq ft right now'},
 {'type': 'stat',
  'stat': 'Full home renovation costs in India typically run ₹800-₹3,000 per sq ft depending on '
          'scope and material grade, with luxury renovations exceeding ₹5,000/sq ft — and overall '
          'renovation costs have risen roughly 12%-18% since 2024 on higher material and labour '
          'prices.',
  'source': 'AECORD / NoBroker home renovation cost guides, 2026',
  'url': 'https://aecord.com/blog/home-renovation-cost-in-india-2026'},
 {'type': 'p',
  'text': "This calculator's default rate of ₹1,800/sq ft sits comfortably in the mid-segment band "
          'that most metro renovations actually land in — basic cosmetic work (repaint, basic '
          'flooring, fixture swaps) starts lower, around ₹500-800/sq ft, while premium finishes '
          'and structural changes push well past ₹3,000/sq ft. The point of a range instead of a '
          'single number is that the final cost genuinely depends on material grade and site '
          'condition — which is exactly why this estimate is a planning-stage starting point, not '
          'a quote.'}],
    },
    {
        "slug": "revenue-leakage-calculator",
        "title": "Revenue Leakage Calculator",
        "tagline": "What's actually walking to Blinkit and Zepto every month.",
        "industry": "retail-store",
        "fields": [
            {"id": "missed", "label": "\"Can't Visit\" Enquiries / Day", "default": 4, "step": 1},
            {"id": "orderValue", "label": "Avg Order Value (₹)", "default": 400, "step": 50},
            {"id": "days", "label": "Days / Month", "default": 30, "step": 1},
        ],
        "compute_js": """function computeResult(v) {
  var monthlyLeak = v.missed * v.orderValue * v.days;
  return '<div class="tr-row tr-total"><span>Revenue Leaking / Month</span><b>₹' + monthlyLeak.toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-note">That\\'s what a WhatsApp catalog tied to real stock is built to keep in-store.</div>';
}""",
        "content": [{'type': 'h2', 'text': "What's actually walking out the door to quick-commerce"},
 {'type': 'stat',
  'stat': 'Nearly 80% of consumers have shifted at least a quarter of their grocery spending to '
          'quick-commerce apps, and over 2 lakh kirana stores closed in a single year — yet local '
          "stores still hold 88% of India's retail food market on trust, credit, and zero delivery "
          'fees alone.',
  'source': 'Outlook Business, citing AICPDF',
  'url': 'https://www.outlookbusiness.com/explainers/kirana-stores-are-losing-the-battle-against-zepto-blinkit-and-instamart'},
 {'type': 'stat',
  'stat': "Blinkit, Zepto and Swiggy Instamart together control over 90% of India's quick-commerce "
          "order volume, with the sector's gross merchandise value estimated at USD 6.1 billion in "
          '2024 and projected to grow at a roughly 48% CAGR through 2028.',
  'source': 'Datum Intelligence, cited via Startupfeed',
  'url': 'https://startupfeed.in/quick-commerce-war-2026-blinkit-zepto-instamart-amazon-flipkart/'},
 {'type': 'p',
  'text': 'That second number is the one that matters for this calculator: a market growing at '
          "nearly 50% a year isn't a passing phase a kirana store can wait out — it's the size of "
          'the tap this tool is measuring. Every "can\'t visit today" enquiry that goes unanswered '
          "doesn't just lose one order; it's one more data point nudging that customer's default "
          'habit toward whichever app answered in nine minutes.'}],
    },
    {
        "slug": "car-loan-emi-calculator",
        "title": "Car Loan EMI Calculator",
        "tagline": "The monthly number that closes or kills a test-drive lead.",
        "industry": "automobile-showroom",
        "fields": [
            {"id": "price", "label": "On-Road Price (₹)", "default": 900000, "step": 10000},
            {"id": "down", "label": "Down Payment (₹)", "default": 150000, "step": 10000},
            {"id": "rate", "label": "Interest Rate (% p.a.)", "default": 9.5, "step": 0.1},
            {"id": "years", "label": "Tenure (years)", "default": 5, "step": 1},
        ],
        "compute_js": """function computeResult(v) {
  var principal = v.price - v.down;
  var r = v.rate / 12 / 100;
  var n = v.years * 12;
  var emi = r === 0 ? principal / n : (principal * r * Math.pow(1 + r, n)) / (Math.pow(1 + r, n) - 1);
  return '<div class="tr-row"><span>Loan Amount</span><b>₹' + principal.toLocaleString('en-IN') + '</b></div>'
       + '<div class="tr-row tr-total"><span>Monthly EMI</span><b>₹' + Math.round(emi).toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2',
  'text': 'Car loan interest rates — leading Indian banks and NBFCs (as of September 2026)'},
 {'type': 'table',
  'caption': 'Rates as published on each lender\'s own site',
  'headers': ['Lender', 'Interest Rate (p.a.)', 'Source'],
  'rows': [[{'text': 'SBI',
             'url': 'https://sbi.co.in/web/personal-banking/loans/car-loan/interest-rate'},
            '8.70% – 9.85% (new car)',
            {'text': 'SBI official rate page',
             'url': 'https://sbi.co.in/web/personal-banking/loans/car-loan/interest-rate'}],
           [{'text': 'HDFC Bank',
             'url': 'https://www.hdfcbank.com/personal/borrow/popular-loans/car-loan/interest-rate'},
            'From 9.40% (new car)',
            {'text': 'HDFC Bank official rate page',
             'url': 'https://www.hdfcbank.com/personal/borrow/popular-loans/car-loan/interest-rate'}],
           [{'text': 'ICICI Bank',
             'url': 'https://www.icicibank.com/personal-banking/loans/car-loan/interest-rate'},
            '7.90% – 11.20% (new car)',
            {'text': 'ICICI Bank official rate page',
             'url': 'https://www.icicibank.com/personal-banking/loans/car-loan/interest-rate'}],
           [{'text': 'Axis Bank',
             'url': 'https://www.axisbank.com/retail/loans/car-loan/interest-rates-charges'},
            '8.90% – 11.80% (new car)',
            {'text': 'Axis Bank official rate page',
             'url': 'https://www.axisbank.com/retail/loans/car-loan/interest-rates-charges'}],
           [{'text': 'Bajaj Finserv',
             'url': 'https://www.bajajfinserv.in/new-car-finance-interest-rates-and-charges'},
            'Up to 12% (new car)',
            {'text': 'Bajaj Finserv official rate page',
             'url': 'https://www.bajajfinserv.in/new-car-finance-interest-rates-and-charges'}]],
  'note': 'Rates depend on credit score, income and loan tenure, and shift with RBI policy changes '
          '— figures above are as reported across lender-published rate pages in September 2026. '
          "Always confirm the live rate on the lender's own page before it's quoted to a walk-in "
          'customer.'},
 {'type': 'p',
  'text': 'A one-percentage-point gap between lenders on a ₹7.5 lakh car loan can shift the EMI by '
          '₹700-800 a month — often the exact difference between a test-drive customer saying yes '
          'on the spot or asking for "a day to think about it." Having the real, current range on '
          'hand during that conversation, instead of a guessed number, is what keeps the financing '
          'question from stalling the sale.'}],
    },
    {
        "slug": "tile-quantity-calculator",
        "title": "Tile Quantity Calculator",
        "tagline": "How many boxes to actually quote for a room.",
        "industry": "building-materials-showroom",
        "fields": [
            {"id": "length", "label": "Room Length (ft)", "default": 12, "step": 0.5},
            {"id": "width", "label": "Room Width (ft)", "default": 10, "step": 0.5},
            {"id": "tileSize", "label": "Tile Size (sq ft/tile)", "default": 4, "step": 0.5},
            {"id": "wastage", "label": "Wastage (%)", "default": 10, "step": 1},
        ],
        "compute_js": """function computeResult(v) {
  var area = v.length * v.width;
  var tilesNeeded = Math.ceil((area * (1 + v.wastage / 100)) / v.tileSize);
  return '<div class="tr-row"><span>Room Area</span><b>' + area.toFixed(0) + ' sq ft</b></div>'
       + '<div class="tr-row tr-total"><span>Tiles Needed (incl. wastage)</span><b>' + tilesNeeded + ' tiles</b></div>';
}""",
        "content": [{'type': 'h2', 'text': 'The real tile market behind this order'},
 {'type': 'stat',
  'stat': "Kajaria Ceramics leads India's organized tile market with roughly 17% share, followed "
          'by Somany Ceramics and Prism Johnson (~9% each) — but organized players collectively '
          'hold only about 46% of the overall market in FY25, with the unorganized sector, '
          'concentrated in Morbi, Gujarat, still commanding the majority ~54% of volume.',
  'source': 'Industry equity research (Nirmal Bang Tiles Sector coverage)',
  'url': 'https://images.assettype.com/bloombergquint/2023-10/8237a072-8413-4db8-99ec-cf28e29727e5/Nirmal_Bang_Tiles_Sector_Initiating_Coverage_Note.pdf'},
 {'type': 'stat',
  'stat': 'Fully installed vitrified tile flooring in India typically runs ₹100-₹170 per sq ft '
          'including labour, with labour alone adding roughly 30%-40% to the material cost — and '
          'metro-city labour rates running 15%-20% higher than Tier-2/3 towns.',
  'source': 'Tile installation cost guides, 2025-26',
  'url': 'https://www.houseyog.com/blog/floor-tiling-cost-per-sqft-india/'},
 {'type': 'p',
  'text': 'That labour share is exactly why the wastage percentage in this calculator matters more '
          'than it looks — a 10% wastage buffer is the industry-standard allowance for cuts, '
          'breakage and pattern-matching, and under-ordering by even one box means a second '
          'showroom trip, a delayed site, and a contractor who remembers which supplier made them '
          'wait.'}],
    },
    {
        "slug": "bulk-order-margin-calculator",
        "title": "Bulk Order Margin Calculator",
        "tagline": "Real margin on a reorder, before it ships.",
        "industry": "wholesale-distributor",
        "fields": [
            {"id": "cost", "label": "Unit Cost (₹)", "default": 85, "step": 5},
            {"id": "sell", "label": "Unit Selling Price (₹)", "default": 110, "step": 5},
            {"id": "qty", "label": "Order Quantity", "default": 800, "step": 10},
        ],
        "compute_js": """function computeResult(v) {
  var marginUnit = v.sell - v.cost;
  var marginPct = v.sell > 0 ? (marginUnit / v.sell * 100).toFixed(1) : '0';
  var totalMargin = marginUnit * v.qty;
  return '<div class="tr-row"><span>Margin / Unit</span><b>₹' + marginUnit.toFixed(2) + ' (' + marginPct + '%)</b></div>'
       + '<div class="tr-row tr-total"><span>Total Margin on Order</span><b>₹' + Math.round(totalMargin).toLocaleString('en-IN') + '</b></div>';
}""",
        "content": [{'type': 'h2', 'text': "Real margin benchmarks for India's general trade"},
 {'type': 'stat',
  'stat': 'Traditional trade — the general trade network of over 11.5 million stores served by '
          'wholesalers and distributors — still accounts for 81.8% of FMCG sales in India, '
          'remaining the dominant retail channel despite the growth of e-commerce and modern '
          'trade.',
  'source': 'NielsenIQ, "Four Key Trends Shaping the FMCG Landscape in India"',
  'url': 'https://nielseniq.com/global/en/insights/analysis/2022/explore-the-four-key-trends-shaping-the-fmcg-landscape-in-india/'},
 {'type': 'stat',
  'stat': "FMCG distributor gross margins in India's general trade typically run 10%-20% depending "
          'on category and competitive intensity — industry guidance puts anything below ~8% as '
          'too thin to reliably cover freight, warehousing and staffing costs once real operating '
          'expenses are netted out.',
  'source': 'Industry distributor-margin guides, 2026',
  'url': 'https://spirestock.com/blog/fmcg-distributor-margin-profit-guide-india'},
 {'type': 'p',
  'text': 'That floor is the number worth checking an order against before it ships, not after: a '
          'reorder priced to win on volume alone, at an 8% margin or below, can look like a win on '
          'the top line while barely covering what it actually costs to get the stock into the '
          "retailer's hands."}],
    },
]


# ---------------------------------------------------------------- AGENTIC BRAIN TERMINAL
# All 15 target industries (matching INDUSTRIES' own names/icons, so this
# stays consistent with the rest of the site) — each showing the same
# underlying agent adapting its reasoning to a different business: it
# checks a real constraint (inventory, a rate table, a margin rule, a
# route map, a credit history), then carries the conversation through to
# an actual close (a booking, a reservation, a payment) — not a single
# question-and-answer, so it reads as one agent handling the full
# interaction end-to-end rather than a narrow FAQ chatbot. "customer" is
# the opening message; "resolution" is the agent's reply plus the
# customer's own confirmation that closes the loop. Cycled client-side on
# the Agentic Use Cases page by agentic-brain.js.
BRAIN_SCENARIOS = [
    {
        "industry": "Export / Trading", "icon": "🚢",
        "customer": [("in", "Need a container quote for basmati rice to Dubai. Can you match the sample pricing from another supplier?")],
        "thinking": ["Reading margin sheet…", "Dubai freight slab confirmed", "Competitor rate: match approved within policy"],
        "resolution": [("out", "We can match that rate — I've attached your shipping cost breakdown. Reply 'Book' and I'll reserve the container space today."),
                        ("in", "Perfect, I'll wire the advance today.")],
    },
    {
        "industry": "Hospital (multi-branch)", "icon": "🏥",
        "customer": [("in", "Need an emergency ultrasound at your Saket branch today. Do you take Apollo Munich insurance?")],
        "thinking": ["Checking live slot matrix…", "Saket branch: 4 PM opening found", "Insurance panel: covered"],
        "resolution": [("out", "Yes, fully covered under your plan — I've held a priority 4:00 PM slot for you at Saket. Just confirm your ID details."),
                        ("in", "Great, see you at 4.")],
    },
    {
        "industry": "Coaching Institute", "icon": "🎓",
        "customer": [("in", "Want to join the NEET dropper batch, but we live 12km away. Is there a hybrid option?")],
        "thinking": ["Checking batch schedule…", "12km is outside walk-in radius", "Hybrid-schedule FAQ retrieved"],
        "resolution": [("out", "Yes! She'd only need to come in twice a week for live mock tests — the rest streams in full HD. Want the timetable?"),
                        ("in", "That works — send me the hybrid schedule.")],
    },
    {
        "industry": "Real Estate Developer", "icon": "🏢",
        "customer": [("in", "Saw your 3BHK sample flat. Is the Dec 2026 possession date firm? Can I tour it this evening?")],
        "thinking": ["Checking project registry…", "Phase 2 on schedule for Dec 2026", "Site consultant free at 6 PM"],
        "resolution": [("out", "Possession is firm for Dec 2026. I've booked you a walkthrough with our site manager at 6:00 PM today — see you there?"),
                        ("in", "Sounds good, I'll be there at 6.")],
    },
    {
        "industry": "B2B Manufacturer", "icon": "🏭",
        "customer": [("in", "Looking to source 10,000 custom aluminum brackets. What's your tooling lead time for a sample run?")],
        "thinking": ["Reading factory queue…", "Tooling line has capacity this week", "Standard sample lead time: 4 days"],
        "resolution": [("out", "We can deliver your prototype sample run in 4 days. Upload your CAD drawings here and we'll start tooling today."),
                        ("in", "Sending the CAD files now.")],
    },
    {
        "industry": "Private School", "icon": "🏫",
        "customer": [("in", "I want to enroll my son in 5th grade, but your bus route doesn't cover Sector 4. What do I do?")],
        "thinking": ["Parsing route map…", "Sector 4 is 2km from Route C stop", "Retrieving hybrid-schedule FAQ"],
        "resolution": [("out", "Don't worry! Our closest bus stop is just 3 minutes from you at 7:40 AM. We also offer a hybrid schedule — want to see the timing chart?"),
                        ("in", "Thank you, that's a relief!")],
    },
    {
        "industry": "Diagnostic Lab", "icon": "🧪",
        "customer": [("in", "Can someone come home for a fasting blood test tomorrow morning, before 8am?")],
        "thinking": ["Checking phlebotomist slots…", "7:30 AM home-collection slot open in your pincode", "Fasting-test prep note required"],
        "resolution": [("out", "Yes, 7:30 AM works! Please stay fasting from midnight — I'll send the address confirmation and the technician's name shortly."),
                        ("in", "Okay, I'll stay fasting. See you at 7:30.")],
    },
    {
        "industry": "Wedding Planner / Banquet", "icon": "✨",
        "customer": [("in", "Is your ballroom available for November 14th? We're expecting around 400 guests.")],
        "thinking": ["Scanning venue calendar…", "Nov 14 is open", "Ballroom capacity: safe up to 550 guests"],
        "resolution": [("out", "It's open, and comfortably fits your guest count. I've held the date for 24 hours — shall we set up a walkthrough?"),
                        ("in", "Let's lock the walkthrough for this weekend.")],
    },
    {
        "industry": "Gym / Fitness Chain", "icon": "🏋️",
        "customer": [("in", "Want to join the weight-loss program, but I have a chronic knee injury. Do your trainers customize plans?")],
        "thinking": ["Filtering trainer profiles…", "3 rehab-certified coaches active at this branch", "Loading injury-safe guardrails"],
        "resolution": [("out", "Yes — we have 3 rehab-certified coaches here. I've booked you a free 15-minute posture assessment this week."),
                        ("in", "I'll take the assessment slot, thanks.")],
    },
    {
        "industry": "CA / Legal Firm", "icon": "⚖️",
        "customer": [("in", "Got an income tax notice about a mismatch from FY 2024. How fast can you draft a response?")],
        "thinking": ["Categorizing notice type…", "Urgency: high, but routine", "Tax desk availability: immediate"],
        "resolution": [("out", "This is a routine procedural notice, nothing to panic about. Upload a photo of it here and we'll have a draft response in 2 hours."),
                        ("in", "Uploading the notice now.")],
    },
    {
        "industry": "Interior Designer", "icon": "🎨",
        "customer": [("in", "Want to redo my 2BHK living room, minimalist style, but budget is capped at ₹2.5 lakh. Doable?")],
        "thinking": ["Browsing portfolio…", "Minimalist layouts run lower on materials", "Budget check: within range"],
        "resolution": [("out", "Completely doable — we've done 14 minimalist living rooms inside that exact budget. Here are 3 concept moodboards to start."),
                        ("in", "Love the moodboards — let's proceed.")],
    },
    {
        "industry": "Retail Store (Kirana / General)", "icon": "🛒",
        "customer": [("in", "Hey, do you have the 8-inch ceramic tiles in stock? Need 50 boxes today.")],
        "thinking": ["Reading inventory sheet…", "54 boxes found in Warehouse B", "Intent: high-urgency purchase"],
        "resolution": [("out", "Yes, we have 54 boxes ready! I've provisionally reserved 50 for you. Can I send a secure UPI link to lock in the dispatch before the van leaves at 2 PM?"),
                        ("in", "Sending the UPI payment now.")],
    },
    {
        "industry": "Automobile Showroom", "icon": "🚗",
        "customer": [("in", "Want to book a test drive for the SUV top variant this Sunday. Is the automatic version available?")],
        "thinking": ["Checking demo fleet…", "Automatic SUV: active and fuelled", "Sunday booking roster: open"],
        "resolution": [("out", "Yes, the automatic SUV is ready for Sunday — I've booked you the 10:30 AM slot. Just bring your driving licence."),
                        ("in", "Booked — see you Sunday.")],
    },
    {
        "industry": "Building Materials / Tiles Showroom", "icon": "🧱",
        "customer": [("in", "Need 200 boxes of matte-finish vitrified tiles. Can you match the wholesale-market rate?")],
        "thinking": ["Checking bulk-margin table…", "Order size: 200 boxes", "Authorized dealer rate: match allowed"],
        "resolution": [("out", "We can match that wholesale rate for a 200-box order, plus arrange safe on-site delivery. Here's your commercial invoice to review."),
                        ("in", "Approved, please share the invoice.")],
    },
    {
        "industry": "Wholesale Distributor", "icon": "📦",
        "customer": [("in", "Our shop's out of stock on item #X90. Can we get 50 cases on the usual credit terms?")],
        "thinking": ["Checking account ledger…", "Client credit history: excellent", "Item #X90: 400 cases in stock"],
        "resolution": [("out", "Approved on your standard 30-day terms — 50 cases of #X90 are being packed for tonight's dispatch."),
                        ("in", "Thanks, dispatch it today.")],
    },
]
