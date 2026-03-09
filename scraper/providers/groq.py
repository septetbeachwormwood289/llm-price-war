"""
Groq pricing scraper.
Source: https://groq.com/pricing
"""

# TODO: Implement actual web scraping from Groq pricing page
# For now, returns hardcoded prices as baseline


def fetch_prices() -> dict:
    """Fetch current Groq model prices. Returns dict of model_id -> price data."""
    return {
        "llama-3.3-70b-groq": {
            "input_price_per_1m": 0.59,
            "output_price_per_1m": 0.79,
        },
        "mixtral-8x7b-groq": {
            "input_price_per_1m": 0.24,
            "output_price_per_1m": 0.24,
        },
    }
