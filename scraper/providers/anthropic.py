"""
Anthropic pricing scraper.
Source: https://anthropic.com/pricing
"""

# TODO: Implement actual web scraping from Anthropic pricing page


def fetch_prices() -> dict:
    """Fetch current Anthropic model prices."""
    return {
        "claude-opus-4": {
            "input_price_per_1m": 15.00,
            "output_price_per_1m": 75.00,
        },
        "claude-sonnet-4": {
            "input_price_per_1m": 3.00,
            "output_price_per_1m": 15.00,
        },
        "claude-haiku-3.5": {
            "input_price_per_1m": 0.80,
            "output_price_per_1m": 4.00,
        },
    }
