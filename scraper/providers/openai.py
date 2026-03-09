"""
OpenAI pricing scraper.
Source: https://openai.com/pricing
"""

# TODO: Implement actual web scraping from OpenAI pricing page
# For now, returns hardcoded prices as baseline


def fetch_prices() -> dict:
    """Fetch current OpenAI model prices. Returns dict of model_id -> price data."""
    return {
        "gpt-4o": {
            "input_price_per_1m": 2.50,
            "output_price_per_1m": 10.00,
        },
        "gpt-4o-mini": {
            "input_price_per_1m": 0.15,
            "output_price_per_1m": 0.60,
        },
        "gpt-4.5-preview": {
            "input_price_per_1m": 75.00,
            "output_price_per_1m": 150.00,
        },
        "o1": {
            "input_price_per_1m": 15.00,
            "output_price_per_1m": 60.00,
        },
        "o1-mini": {
            "input_price_per_1m": 1.10,
            "output_price_per_1m": 4.40,
        },
        "o3-mini": {
            "input_price_per_1m": 1.10,
            "output_price_per_1m": 4.40,
        },
    }
