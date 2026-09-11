"""
Central configuration for the Sri Lakshmi Roofing Industry website.

All values that might differ between local development, staging, and
production live here so the rest of the codebase never hard-codes them.
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Base configuration shared by every environment."""

    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", "dev-secret-key-change-me")

    # SQLAlchemy expects "postgresql://", some hosts (Heroku/Render) still
    # hand out "postgres://" — normalise it so both work without edits.
    _raw_db_url = os.environ.get(
        "DATABASE_URL", "sqlite:///srilakshmi_dev.db"
    )
    if _raw_db_url.startswith("postgres://"):
        _raw_db_url = _raw_db_url.replace("postgres://", "postgresql://", 1)

    SQLALCHEMY_DATABASE_URI = _raw_db_url
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Company / business info (single source of truth) -----------------
    COMPANY_NAME = "Sri Lakshmi Roofing Industry"
    COMPANY_TAGLINE = "Best Place for all Roofing Needs"
    COMPANY_LEGAL_NAME = "Sri Lakshmi Roofing Industry"
    COMPANY_GST = "36AFRFS7352D1ZL"

    COMPANY_ADDRESS_LINE1 = "Survey No. 238, Eshwar Nagar, DVK Road"
    COMPANY_ADDRESS_LINE2 = "Anumula, Haliya"
    COMPANY_ADDRESS_CITY = "Nalgonda"
    COMPANY_ADDRESS_STATE = "Telangana"
    COMPANY_ADDRESS_COUNTRY = "India"
    COMPANY_ADDRESS_PIN = "508377"
    COMPANY_FULL_ADDRESS = (
        "Survey No. 238, Eshwar Nagar, DVK Road, Anumula, Haliya, "
        "Nalgonda, Telangana, India – 508377"
    )

    COMPANY_PHONES = ["+91 9100490888", "+91 9100491888", "+91 8340855855"]
    COMPANY_PHONE_PRIMARY = "+91 9100490888"
    COMPANY_PHONE_PRIMARY_TEL = "+919100490888"
    COMPANY_WHATSAPP_NUMBER = "919100490888"  # international format, no + or spaces
    COMPANY_EMAIL = "srilakshmiroofing1111@gmail.com"

    COMPANY_HOURS = [
        ("Monday – Saturday", "8:00 AM – 8:00 PM"),
        ("Sunday", "9:00 AM – 2:00 PM"),
    ]

    # Google Maps embed (no API key required, uses a plain place query)
    GOOGLE_MAPS_QUERY = (
        "Survey No. 238, Eshwar Nagar, DVK Road, Anumula, Haliya, "
        "Nalgonda, Telangana 508377"
    )
    GOOGLE_MAPS_EMBED_SRC = (
        "https://maps.google.com/maps?q="
        "Sri+Lakshmi+Roofing+Industry+Anumula+Haliya+Nalgonda+Telangana+508377"
        "&t=&z=15&ie=UTF8&iwloc=&output=embed"
    )
    GOOGLE_MAPS_DIRECTIONS_URL = (
        "https://www.google.com/maps/dir/?api=1&destination="
        "Sri+Lakshmi+Roofing+Industry,+Survey+No.+238,+Eshwar+Nagar,+"
        "DVK+Road,+Anumula,+Haliya,+Nalgonda,+Telangana+508377"
    )

    SITE_DOMAIN = os.environ.get("SITE_DOMAIN", "https://www.srilakshmiroofing.in")

    SOCIAL_LINKS = {
        "facebook": "https://facebook.com/srilakshmiroofing",
        "instagram": "https://instagram.com/srilakshmiroofing",
        "youtube": "https://youtube.com/@srilakshmiroofing",
    }


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
