"""
xAI pricing scraper.
Source: https://docs.x.ai/docs/models#models-and-pricing
"""

# TODO: Implement actual web scraping from xAI pricing page
# For now, returns hardcoded prices as baseline


def fetch_prices() -> dict:
    """Fetch current xAI model prices. Returns dict of model_id -> price data."""
    return {
        "grok-3": {
            "input_price_per_1m": 3.00,
            "output_price_per_1m": 15.00,
        },
        "grok-3-mini": {
            "input_price_per_1m": 0.30,
            "output_price_per_1m": 0.50,
        },
    }
