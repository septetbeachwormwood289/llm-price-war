"""
Mistral AI pricing scraper.
Source: https://mistral.ai/pricing
"""

# TODO: Implement actual web scraping from Mistral pricing page


def fetch_prices() -> dict:
    """Fetch current Mistral model prices."""
    return {
        "mistral-large": {
            "input_price_per_1m": 2.00,
            "output_price_per_1m": 6.00,
        },
        "mistral-small": {
            "input_price_per_1m": 0.10,
            "output_price_per_1m": 0.30,
        },
        "codestral": {
            "input_price_per_1m": 0.30,
            "output_price_per_1m": 0.90,
        },
    }
