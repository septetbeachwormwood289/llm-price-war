"""
Google AI pricing scraper.
Source: https://ai.google.dev/pricing
"""

# TODO: Implement actual web scraping from Google AI pricing page


def fetch_prices() -> dict:
    """Fetch current Google model prices."""
    return {
        "gemini-2.5-pro": {
            "input_price_per_1m": 1.25,
            "output_price_per_1m": 10.00,
        },
        "gemini-2.0-flash": {
            "input_price_per_1m": 0.10,
            "output_price_per_1m": 0.40,
        },
        "gemini-1.5-pro": {
            "input_price_per_1m": 1.25,
            "output_price_per_1m": 5.00,
        },
    }
