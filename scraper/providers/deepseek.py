"""
DeepSeek pricing scraper.
Source: https://platform.deepseek.com/api-docs/pricing
"""

# TODO: Implement actual web scraping from DeepSeek pricing page


def fetch_prices() -> dict:
    """Fetch current DeepSeek model prices."""
    return {
        "deepseek-v3": {
            "input_price_per_1m": 0.27,
            "output_price_per_1m": 1.10,
        },
        "deepseek-r1": {
            "input_price_per_1m": 0.55,
            "output_price_per_1m": 2.19,
        },
    }
