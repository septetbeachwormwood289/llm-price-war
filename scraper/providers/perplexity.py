"""
Perplexity pricing scraper.
Source: https://docs.perplexity.ai/guides/pricing
"""

# TODO: Implement actual web scraping from Perplexity pricing page
# For now, returns hardcoded prices as baseline


def fetch_prices() -> dict:
    """Fetch current Perplexity model prices. Returns dict of model_id -> price data."""
    return {
        "sonar-pro": {
            "input_price_per_1m": 3.00,
            "output_price_per_1m": 15.00,
        },
        "sonar": {
            "input_price_per_1m": 1.00,
            "output_price_per_1m": 1.00,
        },
    }
