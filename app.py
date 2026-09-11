"""
Sri Lakshmi Roofing Industry — main Flask application.

Run locally:
    pip install -r requirements.txt
    cp .env.example .env   # then edit .env with real DB credentials
    flask --app app run --debug

See README.md for full setup and deployment instructions.
"""

import os
import re
from datetime import datetime

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    jsonify,
)

from config import config_by_name
from models import db, QuoteRequest, ContactMessage, NewsletterSignup
from data import (
    PRODUCT_CATEGORIES,
    BRANDS,
    WHY_CHOOSE_US,
    TESTIMONIALS,
    FAQS,
    GALLERY_IMAGES,
)

PHONE_RE = re.compile(r"^[+]?[0-9\s-]{7,15}$")
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def save_entry(entry, app):
    """
    Persist a form submission, returning True on success.

    A lost enquiry is a lost customer, so if the database write fails we
    log it loudly and tell the visitor to call or WhatsApp instead of
    showing them a generic error page.
    """
    try:
        db.session.add(entry)
        db.session.commit()
        return True
    except Exception as exc:
        db.session.rollback()
        app.logger.error("Failed to save %r: %s", entry, exc)
        return False


def create_app():
    env_name = os.environ.get("FLASK_ENV", "production")
    app = Flask(__name__)
    app.config.from_object(config_by_name.get(env_name, config_by_name["production"]))

    db.init_app(app)

    # Create tables on first boot. Wrapped defensively: on a hosted platform
    # the database can occasionally be a few seconds behind the web service
    # at startup. Without this guard, a transient connection hiccup would
    # crash the entire site instead of just the enquiry forms — the pages
    # themselves don't need the database to render.
    with app.app_context():
        try:
            db.create_all()
        except Exception as exc:  # pragma: no cover - startup resilience
            app.logger.warning(
                "Database not reachable at startup (%s). Pages will still "
                "render; enquiry forms will retry on next request.", exc
            )

    register_context_processors(app)
    register_routes(app)
    register_error_handlers(app)

    return app


def register_context_processors(app):
    """Make company info & nav data available to every template automatically."""

    @app.context_processor
    def inject_globals():
        return {
            "company_name": app.config["COMPANY_NAME"],
            "company_tagline": app.config["COMPANY_TAGLINE"],
            "company_phones": app.config["COMPANY_PHONES"],
            "company_phone_primary": app.config["COMPANY_PHONE_PRIMARY"],
            "company_phone_primary_tel": app.config["COMPANY_PHONE_PRIMARY_TEL"],
            "company_whatsapp": app.config["COMPANY_WHATSAPP_NUMBER"],
            "company_email": app.config["COMPANY_EMAIL"],
            "company_address": app.config["COMPANY_FULL_ADDRESS"],
            "company_hours": app.config["COMPANY_HOURS"],
            "company_gst": app.config["COMPANY_GST"],
            "maps_embed_src": app.config["GOOGLE_MAPS_EMBED_SRC"],
            "maps_directions_url": app.config["GOOGLE_MAPS_DIRECTIONS_URL"],
            "site_domain": app.config["SITE_DOMAIN"],
            "social_links": app.config["SOCIAL_LINKS"],
            "product_categories": PRODUCT_CATEGORIES,
            "current_year": datetime.utcnow().year,
        }


def register_routes(app):

    @app.route("/")
    def home():
        return render_template(
            "home.html",
            page_title=f"{app.config['COMPANY_NAME']} | Steel Roofing Sheets, Pipes & Industrial Materials in Nalgonda",
            meta_description=(
                "Sri Lakshmi Roofing Industry, Haliya, Nalgonda — trusted supplier of Tata, JSW, "
                "Jindal, Apollo & AMNS roofing sheets, pipes, roofing accessories and industrial "
                "shed materials. Call or WhatsApp for a free quote."
            ),
            why_choose_us=WHY_CHOOSE_US[:6],
            testimonials=TESTIMONIALS,
            products=PRODUCT_CATEGORIES,
            brands=BRANDS,
        )

    @app.route("/about")
    def about():
        return render_template(
            "about.html",
            page_title=f"About Us | {app.config['COMPANY_NAME']}",
            meta_description=(
                "Learn about Sri Lakshmi Roofing Industry — a trusted supplier of steel roofing "
                "sheets, pipes and industrial building materials based in Haliya, Nalgonda, Telangana."
            ),
        )

    @app.route("/why-choose-us")
    def why_choose_us():
        return render_template(
            "why-choose-us.html",
            page_title=f"Why Choose Us | {app.config['COMPANY_NAME']}",
            meta_description=(
                "Genuine branded roofing materials, affordable prices, quality assurance and quick "
                "delivery — see why customers across Telangana choose Sri Lakshmi Roofing Industry."
            ),
            reasons=WHY_CHOOSE_US,
            testimonials=TESTIMONIALS,
        )

    @app.route("/brands")
    def brands():
        return render_template(
            "brands.html",
            page_title=f"Our Brands | {app.config['COMPANY_NAME']}",
            meta_description=(
                "Sri Lakshmi Roofing Industry stocks genuine Tata, JSW, Jindal, Apollo, AMNS "
                "roofing sheets and Tata, MPL, Hariom pipes — 100% authentic, factory-sourced material."
            ),
            brands=BRANDS,
        )

    @app.route("/products")
    def products():
        return render_template(
            "products.html",
            page_title=f"Products | Roofing Sheets, Pipes & Industrial Materials | {app.config['COMPANY_NAME']}",
            meta_description=(
                "Browse our full range: Tata/JSW/Jindal/Apollo/AMNS roofing sheets, GP & structural "
                "pipes, roofing accessories, industrial shed materials and consumables."
            ),
            products=PRODUCT_CATEGORIES,
        )

    @app.route("/gallery")
    def gallery():
        return render_template(
            "gallery.html",
            page_title=f"Gallery | {app.config['COMPANY_NAME']}",
            meta_description="See our roofing sheet installations, shed projects, pipes and warehouse stock in action.",
            images=GALLERY_IMAGES,
        )

    @app.route("/faq")
    def faq():
        return render_template(
            "faq.html",
            page_title=f"Frequently Asked Questions | {app.config['COMPANY_NAME']}",
            meta_description="Answers to common questions about our roofing sheets, pipes, pricing, delivery and GST billing.",
            faqs=FAQS,
        )

    @app.route("/contact")
    def contact():
        return render_template(
            "contact.html",
            page_title=f"Contact Us | {app.config['COMPANY_NAME']}",
            meta_description=(
                "Visit or contact Sri Lakshmi Roofing Industry, Survey No. 238, Eshwar Nagar, "
                "DVK Road, Anumula, Haliya, Nalgonda, Telangana. Call, WhatsApp or send an enquiry."
            ),
        )

    @app.route("/contact/submit", methods=["POST"])
    def contact_submit():
        name = (request.form.get("name") or "").strip()
        phone = (request.form.get("phone") or "").strip()
        email = (request.form.get("email") or "").strip()
        subject = (request.form.get("subject") or "").strip()
        message = (request.form.get("message") or "").strip()

        errors = []
        if len(name) < 2:
            errors.append("Please enter your full name.")
        if not PHONE_RE.match(phone):
            errors.append("Please enter a valid phone number.")
        if email and not EMAIL_RE.match(email):
            errors.append("Please enter a valid email address.")
        if len(message) < 5:
            errors.append("Please enter your message.")

        if errors:
            for e in errors:
                flash(e, "error")
            return redirect(url_for("contact") + "#contact-form")

        entry = ContactMessage(name=name, phone=phone, email=email or None, subject=subject or None, message=message)

        if save_entry(entry, app):
            flash("Thank you! Your message has been received. Our team will contact you shortly.", "success")
        else:
            flash(
                "Sorry, we couldn't submit your message just now. Please call us on "
                f"{app.config['COMPANY_PHONE_PRIMARY']} or message us on WhatsApp — "
                "we'll respond right away.",
                "error",
            )
        return redirect(url_for("contact") + "#contact-form")

    @app.route("/request-a-quote", methods=["GET", "POST"])
    def request_quote():
        if request.method == "GET":
            preselect = request.args.get("product", "")
            return render_template(
                "request-quote.html",
                page_title=f"Request a Quote | {app.config['COMPANY_NAME']}",
                meta_description=(
                    "Get a free, no-obligation price quote on roofing sheets, pipes, accessories "
                    "and industrial materials from Sri Lakshmi Roofing Industry."
                ),
                products=PRODUCT_CATEGORIES,
                preselect=preselect,
            )

        name = (request.form.get("name") or "").strip()
        phone = (request.form.get("phone") or "").strip()
        email = (request.form.get("email") or "").strip()
        product = (request.form.get("product") or "").strip()
        quantity = (request.form.get("quantity") or "").strip()
        message = (request.form.get("message") or "").strip()

        errors = []
        if len(name) < 2:
            errors.append("Please enter your full name.")
        if not PHONE_RE.match(phone):
            errors.append("Please enter a valid phone number.")
        if email and not EMAIL_RE.match(email):
            errors.append("Please enter a valid email address.")
        if not product:
            errors.append("Please select the product you need.")

        if errors:
            for e in errors:
                flash(e, "error")
            return redirect(url_for("request_quote"))

        entry = QuoteRequest(
            name=name, phone=phone, email=email or None,
            product=product, quantity=quantity or None, message=message or None,
        )

        if save_entry(entry, app):
            flash("Thank you! Your quote request has been submitted. We'll get back to you shortly.", "success")
        else:
            flash(
                "Sorry, we couldn't submit your request just now. Please call us on "
                f"{app.config['COMPANY_PHONE_PRIMARY']} or message us on WhatsApp — "
                "we'll get you a quote right away.",
                "error",
            )
        return redirect(url_for("request_quote"))

    @app.route("/newsletter/subscribe", methods=["POST"])
    def newsletter_subscribe():
        email = (request.form.get("email") or "").strip()
        if not EMAIL_RE.match(email):
            flash("Please enter a valid email address to subscribe.", "error")
            return redirect(request.referrer or url_for("home"))

        try:
            existing = NewsletterSignup.query.filter_by(email=email).first()
            if not existing:
                save_entry(NewsletterSignup(email=email), app)
        except Exception as exc:
            db.session.rollback()
            app.logger.error("Newsletter signup failed for %s: %s", email, exc)

        # Always thank the visitor — a failed newsletter save is not something
        # they can act on, and the error is captured in the logs.
        flash("Thanks for subscribing to our updates!", "success")
        return redirect(request.referrer or url_for("home"))

    @app.route("/privacy-policy")
    def privacy_policy():
        return render_template(
            "privacy-policy.html",
            page_title=f"Privacy Policy | {app.config['COMPANY_NAME']}",
            meta_description="Privacy policy for Sri Lakshmi Roofing Industry's website.",
        )

    @app.route("/terms-and-conditions")
    def terms_conditions():
        return render_template(
            "terms-and-conditions.html",
            page_title=f"Terms & Conditions | {app.config['COMPANY_NAME']}",
            meta_description="Terms and conditions for Sri Lakshmi Roofing Industry's website and services.",
        )

    @app.route("/robots.txt")
    def robots_txt():
        content = (
            "User-agent: *\n"
            "Allow: /\n"
            f"Sitemap: {app.config['SITE_DOMAIN']}/sitemap.xml\n"
        )
        return app.response_class(content, mimetype="text/plain")

    @app.route("/sitemap.xml")
    def sitemap_xml():
        pages = [
            "", "about", "why-choose-us", "brands", "products", "gallery",
            "faq", "contact", "request-a-quote", "privacy-policy", "terms-and-conditions",
        ]
        domain = app.config["SITE_DOMAIN"]
        urls = "".join(
            f"<url><loc>{domain}/{p}</loc><changefreq>weekly</changefreq></url>"
            for p in pages
        )
        xml = f'<?xml version="1.0" encoding="UTF-8"?>' \
              f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>'
        return app.response_class(xml, mimetype="application/xml")


def register_error_handlers(app):
    @app.errorhandler(404)
    def not_found(e):
        return render_template(
            "404.html",
            page_title=f"Page Not Found | {app.config['COMPANY_NAME']}",
            meta_description="The page you're looking for could not be found.",
        ), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template(
            "500.html",
            page_title=f"Server Error | {app.config['COMPANY_NAME']}",
            meta_description="Something went wrong on our end.",
        ), 500


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
