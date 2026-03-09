# Price Changelog

## 2026-03-09 (v2)
- Added xAI provider: Grok-3 ($3.00/$15.00), Grok-3 Mini ($0.30/$0.50)
- Added Groq provider: Llama 3.3 70B via Groq ($0.59/$0.79), Mixtral 8x7B via Groq ($0.24/$0.24)
- Added Perplexity provider: Sonar Pro ($3.00/$15.00), Sonar ($1.00/$1.00)
- Added scraper stubs for xAI, Groq, Perplexity
- Fixed update_prices.py: price change detection now works for existing models
- Replaced dishonest "Auto-Updated Daily" badge with "Community-Maintained"
- Added Scraper Status section to README for transparency
- Total models tracked: 36 across 12 providers

## 2026-03-09
- Initial release with 30 models tracked
- Providers: OpenAI, Anthropic, Google, Meta, Mistral, DeepSeek, Cohere
- Includes text generation, embedding, and image generation pricing
- Calculator CLI tool for cost estimation
- Provider scraper framework (stub implementations)
- GitHub Actions daily update workflow
