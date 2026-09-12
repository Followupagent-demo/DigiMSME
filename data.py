# AsliKaam V1 — industry content data
# Every entry defaults to "proposed" per the honesty rule (no delivered pilot on record yet).
# Flip an entry's "badge" to "proven" once a real pilot has actually run in that vertical.

BRAND = "AsliKaam"
TAGLINE = "Digital Partner of MSMEs Automation"
TAGLINE_HI = "MSMEs के ऑटोमेशन के लिए डिजिटल पार्टनर"
WHATSAPP_NUMBER = "911234567890"  # TODO: replace with the real WhatsApp Business number before launch
PHONE_NUMBER = "+91 12345 67890"  # TODO: replace with the real business line before launch
SITE_URL = "https://asli-kaam.pages.dev"  # TODO: replace with the real production domain before launch — used for sitemap.xml, robots.txt, and JSON-LD (absolute URLs are required for these, unlike the rest of the site which uses relative links)

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
        "tag": "Entry",
        "includes": ["Google Business Profile setup + optimization", "Business website", "Monthly blog content"],
    },
    {
        "name": "Growth Pack",
        "price": "Contact us for a quote",
        "tag": "Most Popular",
        "includes": ["Everything in Go Digital", "Booking Engine (appointments / visits / trials)"],
    },
    {
        "name": "Expansion Pack",
        "price": "Contact us for a quote",
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
    },
]
