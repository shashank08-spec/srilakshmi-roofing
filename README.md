# Sri Lakshmi Roofing Industry — Website

A premium, responsive, SEO-optimized business website built with Flask
(Python), PostgreSQL, HTML5/CSS3 and vanilla JavaScript.

## Tech Stack

- **Backend:** Python 3, Flask, Flask-SQLAlchemy
- **Database:** PostgreSQL (SQLite fallback for local development if `DATABASE_URL` is not set)
- **Frontend:** Semantic HTML5, hand-written CSS3 (no framework dependency), vanilla JS
- **Fonts:** Google Fonts (Poppins + Inter)

## Project Structure

```
srilakshmi/
├── app.py                  # Flask app factory, routes, error handlers
├── config.py                # Company info & environment configuration
├── data.py                   # Product catalog, brands, FAQs, testimonials (content)
├── models.py                  # SQLAlchemy models (QuoteRequest, ContactMessage, NewsletterSignup)
├── schema.sql                  # Manual PostgreSQL schema reference
├── requirements.txt
├── .env.example
├── static/
│   ├── css/style.css        # Full design system (colors, components, animations)
│   ├── js/main.js            # Nav, accordion, filters, lightbox, form validation, scroll reveal
│   └── img/                   # favicon.svg, og-cover.jpg
└── templates/
    ├── base.html              # Shared layout: header, nav, footer, floating buttons, SEO meta
    ├── _icons.html            # Inline SVG icon macros
    ├── home.html, about.html, why-choose-us.html, brands.html,
    │   products.html, gallery.html, faq.html, contact.html,
    │   request-quote.html, privacy-policy.html, terms-and-conditions.html,
    │   404.html, 500.html
```

## Local Setup

1. **Install dependencies** (Python 3.10+ recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Configure environment variables:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set:
   - `FLASK_SECRET_KEY` — any long random string
   - `DATABASE_URL` — your PostgreSQL connection string. If you skip this,
     the app automatically falls back to a local SQLite file
     (`srilakshmi_dev.db`) so you can develop without PostgreSQL installed.

3. **Create the PostgreSQL database** (skip if using SQLite fallback):
   ```sql
   CREATE DATABASE srilakshmi_roofing;
   CREATE USER srilakshmi_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE srilakshmi_roofing TO srilakshmi_user;
   ```
   Tables are created automatically the first time the app runs
   (`db.create_all()` inside `app.py`). `schema.sql` is provided if you'd
   rather create them manually.

4. **Run the app:**
   ```bash
   flask --app app run --debug
   ```
   Visit http://127.0.0.1:5000

## Production Deployment

```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

Put this behind Nginx (or your host's reverse proxy) with HTTPS enabled.
Recommended hosts: any VPS (DigitalOcean, Hetzner, AWS Lightsail) or a PaaS
that supports Python + PostgreSQL add-ons (Render, Railway, Heroku).

Before going live:
- Update `SITE_DOMAIN` in `config.py` (or set the `SITE_DOMAIN` env var) to
  your real domain — it feeds canonical URLs, Open Graph tags, the sitemap
  and robots.txt.
- Replace the social links in `config.py` (`SOCIAL_LINKS`) with your real
  Facebook/Instagram/YouTube pages, or remove the ones you don't use from
  `templates/base.html`.
- Replace `static/img/og-cover.jpg` with a real photo of your storefront or
  products for social sharing previews (1200×630px recommended).
- Add real photographs to the Gallery, Home hero and Product cards —
  the current build uses tasteful icon/pattern placeholders so the site
  loads instantly without stock imagery; swap in your own photos by editing
  the relevant `<div class="...__media">` / `.gallery-item__ph` blocks in
  the templates and adding `<img loading="lazy" ...>` tags.
- Set `FLASK_ENV=production` in your production `.env`.
- Set a strong, unique `FLASK_SECRET_KEY`.

## Where Enquiries Go

- **Request a Quote** form → `quote_requests` table
- **Contact** form → `contact_messages` table
- **Newsletter** box (footer) → `newsletter_signups` table

Query them directly in PostgreSQL, or wire up a simple admin view / export
script later (e.g. `psql -c "SELECT * FROM quote_requests ORDER BY created_at DESC;"`).

To also receive enquiries by email, add an SMTP integration (e.g.
Flask-Mail) inside the `contact_submit()` and `request_quote()` view
functions in `app.py`.

## SEO Notes

- Semantic HTML5 landmarks (`header`, `nav`, `main`, `footer`) throughout.
- Meta description + Open Graph + Twitter Card tags on every page (see `templates/base.html`).
- `HardwareStore` (LocalBusiness) JSON-LD schema with address, phone and
  opening hours on every page; `FAQPage` schema on the FAQ page.
- Auto-generated `/sitemap.xml` and `/robots.txt` routes (see `app.py`).
- Lazy-loaded Google Maps iframe on the Contact page.
- Fast-loading by design: no heavy JS frameworks, no external icon fonts
  (icons are inline SVG), a single CSS file, and a single small JS file.

### Recommended follow-ups for SEO

1. Submit `sitemap.xml` to Google Search Console after deployment.
2. Claim/verify a Google Business Profile with the same NAP (Name, Address,
   Phone) shown on the Contact page — this is one of the biggest local SEO
   ranking factors for a business like this.
3. Add real customer reviews to Google Business Profile and consider
   embedding them here later.
4. Once you have a real domain and photos, compress images (WebP where
   possible) before uploading to `static/img/`.

## Customizing Content

All product, brand, FAQ and testimonial content lives in **`data.py`** —
edit that file to add/remove products or update copy without touching any
template or route logic. Company contact info, address and business hours
live in **`config.py`**.
