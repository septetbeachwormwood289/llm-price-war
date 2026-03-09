# Contributing to LLM Price War

Thanks for helping keep LLM pricing data accurate! Here's how you can contribute.

## Reporting a Price Change

1. Open an [issue](https://github.com/munnam77/llm-price-war/issues/new) with:
   - Provider and model name
   - Old price vs new price
   - Link to the official pricing page
   - Date you noticed the change

2. Or submit a PR directly (see below).

## Submitting a Price Update (PR)

1. Fork the repo
2. Edit `data/pricing.json` with the updated prices
3. Run the calculator to verify your changes work:
   ```bash
   python calculator/estimate.py --input-tokens 1000000 --output-tokens 500000
   ```
4. Submit a PR with:
   - Title: `price: update [Provider] [Model] pricing`
   - Body: link to official pricing page confirming the change

## Adding a New Provider

1. Create `scraper/providers/[provider_name].py`:
   ```python
   """
   [Provider] pricing scraper.
   Source: [pricing URL]
   """

   def fetch_prices() -> dict:
       """Fetch current [Provider] model prices."""
       return {
           "model-id": {
               "input_price_per_1m": 0.00,
               "output_price_per_1m": 0.00,
           },
       }
   ```

2. Add provider data to `data/pricing.json` following the existing schema
3. Register the provider in `scraper/update_prices.py`
4. Update the README tables

## Adding a New Model

1. Add the model entry to the appropriate provider in `data/pricing.json`
2. Follow the existing schema (see other models for reference)
3. Update the README comparison tables
4. Test with the calculator

## Model Data Schema

Each text model should have:
```json
{
  "name": "Display Name",
  "type": "text",
  "input_price_per_1m": 0.00,
  "output_price_per_1m": 0.00,
  "context_window": 128000,
  "max_output": 4096,
  "supports_vision": false,
  "supports_function_calling": true,
  "speed_toks": 100,
  "best_for": "Short description",
  "notes": "Additional details"
}
```

Embedding models:
```json
{
  "name": "Display Name",
  "type": "embedding",
  "input_price_per_1m": 0.00,
  "dimensions": 1024,
  "max_input": 8192,
  "notes": "Details"
}
```

## Scraper Development

Provider scrapers live in `scraper/providers/`. Each must:

- Export a `fetch_prices()` function returning a dict of `model_id -> price_data`
- Use only Python standard library (no external dependencies)
- Handle errors gracefully (return empty dict on failure)
- Include the source URL in the module docstring

Currently all scrapers return hardcoded values. To implement actual scraping:
1. Use `urllib.request` to fetch the pricing page
2. Parse HTML/JSON to extract prices
3. Return in the standard format
4. Add error handling for network failures and page structure changes

## Code Standards

- Python 3.8+ compatible
- Standard library only (no pip dependencies)
- Type hints encouraged
- Keep files under 200 lines

## Questions?

Open an issue or start a discussion. Thanks for contributing!
