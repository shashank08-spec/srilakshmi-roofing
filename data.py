"""
Static content: products, brands, testimonials, FAQs, gallery.

Kept as plain Python data structures (rather than in the database) because
this content changes rarely and is what search engines should see rendered
directly in the HTML on first load — good for SEO and for fast page loads.
"""

PRODUCT_CATEGORIES = [
    {
        "slug": "roofing-sheets",
        "icon": "roof",
        "name": "Roofing Sheets",
        "short": "Galvalume & galvanised steel roofing sheets from India's most trusted mills.",
        "description": (
            "Our roofing sheets are manufactured by India's leading steel brands and are "
            "engineered for long-term weather resistance, high load-bearing strength and "
            "energy-efficient reflectivity — ideal for homes, factories, warehouses and "
            "agricultural sheds."
        ),
        "specs": [
            {"label": "Quality Grades", "value": "AZ-70, AZ-150 (Aluminium-Zinc coating)"},
            {"label": "Thickness Options", "value": "0.5 mm, 0.6 mm"},
            {"label": "Profile", "value": "Trapezoidal & corrugated roofing profiles"},
            {"label": "Best For", "value": "Homes, factories, warehouses, sheds, commercial roofs"},
        ],
        "brands": ["Tata", "JSW", "Jindal", "Apollo", "AMNS"],
    },
    {
        "slug": "pipes",
        "icon": "pipe",
        "name": "Pipes & GP Pipes",
        "short": "Structural steel pipes and GP pipes for shed frames, fencing and fabrication.",
        "description": (
            "A complete range of structural and GP (Galvanised Pipe) pipes sourced from "
            "reputed brands and trusted local manufacturers, suited for shed structures, "
            "fencing, scaffolding and general fabrication work."
        ),
        "specs": [
            {"label": "Types", "value": "Structural pipes, GP (Galvanised) pipes"},
            {"label": "Brands", "value": "Tata, MPL, Hariom, Local"},
            {"label": "Best For", "value": "Shed frames, fencing, fabrication, scaffolding"},
        ],
        "brands": ["Tata", "MPL", "Hariom", "Local"],
    },
    {
        "slug": "roofing-accessories",
        "icon": "screw",
        "name": "Roofing Accessories",
        "short": "Screws, turbine ventilators, angular sections and patti for a complete roofing job.",
        "description": (
            "Everything you need to finish a roofing job properly — self-drilling roofing "
            "screws, ridge and turbine ventilators for natural airflow, and structural angular "
            "sections and patti for edge finishing and reinforcement."
        ),
        "specs": [
            {"label": "Screws", "value": "Tata Roofing Screws, Local Roofing Screws"},
            {"label": "Ventilation", "value": "Turbine Ventilators for natural roof cooling"},
            {"label": "Finishing", "value": "Angular sections, Patti"},
        ],
        "brands": ["Tata"],
    },
    {
        "slug": "industrial-shed-materials",
        "icon": "shed",
        "name": "Industrial Shed Materials",
        "short": "Construction plates and bolts built for heavy-duty industrial shed structures.",
        "description": (
            "Structural plates and high-tensile bolts for industrial shed construction, "
            "designed to give fabricators and contractors reliable, load-rated hardware for "
            "large-span factory and warehouse structures."
        ),
        "specs": [
            {"label": "Plates", "value": "Industrial shed construction plates"},
            {"label": "Fasteners", "value": "High-strength structural bolts"},
            {"label": "Best For", "value": "Factories, warehouses, large-span sheds"},
        ],
        "brands": [],
    },
    {
        "slug": "industrial-consumables",
        "icon": "spark",
        "name": "Industrial Consumables",
        "short": "Grinding & cutting wheels, welding rods, turpentine oil and red oxide paint.",
        "description": (
            "Stock up on the everyday consumables every fabrication workshop and site needs — "
            "grinding and cutting wheels, welding rods, turpentine oil and red oxide primer paint "
            "for rust protection."
        ),
        "specs": [
            {"label": "Abrasives", "value": "Grinding Wheels, Cutting Wheels"},
            {"label": "Welding", "value": "Welding Rods (multiple grades)"},
            {"label": "Coatings", "value": "Turpentine Oil, Red Oxide Paint"},
        ],
        "brands": [],
    },
]

BRANDS = [
    {"name": "Tata", "note": "Tata Steel / Tata BlueScope"},
    {"name": "JSW", "note": "JSW Steel"},
    {"name": "Jindal", "note": "Jindal Steel"},
    {"name": "Apollo", "note": "Apollo Roofing"},
    {"name": "AMNS", "note": "ArcelorMittal Nippon Steel"},
    {"name": "Hariom", "note": "Hariom Pipes"},
    {"name": "MPL", "note": "MPL Pipes"},
]

WHY_CHOOSE_US = [
    {
        "icon": "badge-check",
        "title": "Genuine Branded Products",
        "text": "100% authentic material sourced directly from Tata, JSW, Jindal, Apollo and AMNS — no duplicates, no compromises.",
    },
    {
        "icon": "tag",
        "title": "Affordable Prices",
        "text": "Direct sourcing and bulk stock let us offer competitive, transparent pricing on every product we sell.",
    },
    {
        "icon": "shield",
        "title": "Quality Assurance",
        "text": "Every batch is checked for coating grade, thickness and finish before it leaves our warehouse.",
    },
    {
        "icon": "users",
        "title": "Experienced Team",
        "text": "Years of hands-on experience in roofing and industrial materials means expert advice on every order.",
    },
    {
        "icon": "warehouse",
        "title": "Large Product Inventory",
        "text": "A wide, ready stock of sheets, pipes, accessories and consumables — ready to move without delay.",
    },
    {
        "icon": "truck",
        "title": "Quick Delivery",
        "text": "Fast, reliable dispatch to home owners, factories, contractors and sites across the region.",
    },
    {
        "icon": "heart-handshake",
        "title": "Customer Satisfaction",
        "text": "A trusted name built on long-term relationships with home owners, builders and industrial clients alike.",
    },
]

TESTIMONIALS = [
    {
        "name": "Ravi Kumar",
        "role": "Warehouse Owner, Nalgonda",
        "text": "Sri Lakshmi Roofing Industry supplied Tata roofing sheets for our warehouse expansion. Genuine material, on-time delivery and fair pricing.",
        "rating": 5,
    },
    {
        "name": "Srinivas Reddy",
        "role": "Building Contractor",
        "text": "I've been buying pipes and roofing accessories from them for over 3 years. Always stocked, always reliable.",
        "rating": 5,
    },
    {
        "name": "Anitha Rao",
        "role": "Home Owner, Haliya",
        "text": "Got AZ-150 sheets for my home roof — the team explained the thickness options clearly and helped me choose the right one.",
        "rating": 5,
    },
    {
        "name": "Mahesh Fabricators",
        "role": "Fabrication Workshop",
        "text": "Their industrial consumables — grinding wheels, welding rods — are always genuine and reasonably priced. One-stop shop for us.",
        "rating": 4,
    },
]

FAQS = [
    {
        "q": "Which roofing sheet brands do you supply?",
        "a": "We supply genuine roofing sheets from Tata, JSW, Jindal, Apollo and AMNS, available in AZ-70 and AZ-150 coating grades and 0.5 mm / 0.6 mm thickness.",
    },
    {
        "q": "What is the difference between AZ-70 and AZ-150 sheets?",
        "a": "AZ-70 and AZ-150 refer to the Aluminium-Zinc (Galvalume) coating mass per square metre. AZ-150 carries a heavier coating, giving stronger corrosion resistance and a longer service life than AZ-70 — recommended for coastal or high-humidity areas and long-term industrial use.",
    },
    {
        "q": "Do you deliver to industrial sites and factories?",
        "a": "Yes. We regularly supply factories, warehouses, contractors and construction companies across Nalgonda and the surrounding Telangana region, with delivery arranged for bulk orders.",
    },
    {
        "q": "Can I get a price quote before placing an order?",
        "a": "Absolutely. Use our Request a Quote page, call us directly, or message us on WhatsApp with your requirement (sheet type, thickness, quantity) and we'll respond with current pricing.",
    },
    {
        "q": "Do you supply GP pipes and structural pipes separately?",
        "a": "Yes, we stock both GP (Galvanised) pipes and structural pipes from Tata, MPL, Hariom and trusted local manufacturers for shed frames, fencing and fabrication work.",
    },
    {
        "q": "What industrial consumables do you stock?",
        "a": "We stock grinding wheels, cutting wheels, welding rods, turpentine oil and red oxide paint — everyday essentials for fabrication workshops and construction sites.",
    },
    {
        "q": "Is GST billing available?",
        "a": "Yes, we provide proper GST invoices for all purchases. Our GSTIN is 36AFRFS7352D1ZL.",
    },
    {
        "q": "What are your business hours?",
        "a": "We're open Monday to Saturday, 8:00 AM to 8:00 PM, and Sunday 9:00 AM to 2:00 PM.",
    },
]

GALLERY_IMAGES = [
    {"category": "sheets", "caption": "Tata Galvalume roofing sheets — warehouse stock"},
    {"category": "sheets", "caption": "AZ-150 roofing sheet installation, residential roof"},
    {"category": "pipes", "caption": "GP pipes ready for dispatch"},
    {"category": "shed", "caption": "Industrial shed under construction using our materials"},
    {"category": "accessories", "caption": "Turbine ventilators and roofing screws"},
    {"category": "sheds", "caption": "Completed agricultural shed roofing project"},
    {"category": "consumables", "caption": "Welding rods and grinding wheels in stock"},
    {"category": "sheets", "caption": "JSW roofing sheets — factory roof installation"},
    {"category": "warehouse", "caption": "Our warehouse — large product inventory"},
]
