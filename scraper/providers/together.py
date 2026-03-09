"""
Together AI pricing scraper (hosts Meta Llama models).
Source: https://www.together.ai/pricing
"""

# TODO: Implement actual web scraping from Together AI pricing page


def fetch_prices() -> dict:
    """Fetch current Together AI (Meta Llama) model prices."""
    return {
        "llama-3.3-70b": {
            "input_price_per_1m": 0.60,
            "output_price_per_1m": 0.60,
        },
        "llama-3.1-405b": {
            "input_price_per_1m": 3.50,
            "output_price_per_1m": 3.50,
        },
    }
