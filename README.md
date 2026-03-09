# LLM Price War

### The most comprehensive, always-updated LLM pricing comparison. Stop overpaying for AI.

[![Models Tracked: 36](https://img.shields.io/badge/Models_Tracked-36-blue)](data/pricing.json)
[![Last Updated: March 2026](https://img.shields.io/badge/Last_Updated-March_2026-green)](#)
[![Community-Maintained](https://img.shields.io/badge/Community--Maintained-orange)](CONTRIBUTING.md)
[![Update Prices](https://github.com/munnam77/llm-price-war/actions/workflows/update-prices.yml/badge.svg)](https://github.com/munnam77/llm-price-war/actions/workflows/update-prices.yml)

**Community-maintained pricing data. Star to stay informed.**

> **Disclaimer:** Prices change frequently. Always verify on the provider's official pricing page before making purchasing decisions. Last verified: March 9, 2026.

---

## Text Generation Models

| Provider | Model | Input ($/1M tokens) | Output ($/1M tokens) | Context Window | Speed (tok/s) | Best For |
|----------|-------|--------------------:|---------------------:|---------------:|--------------:|----------|
| **OpenAI** | GPT-4o | $2.50 | $10.00 | 128K | ~100 | General-purpose flagship |
| | GPT-4o-mini | $0.15 | $0.60 | 128K | ~150 | Cost-efficient tasks |
| | GPT-4.5 Preview | $75.00 | $150.00 | 128K | ~60 | Research, complex reasoning |
| | o1 | $15.00 | $60.00 | 200K | ~40 | Advanced reasoning, math, code |
| | o1-mini | $1.10 | $4.40 | 128K | ~80 | Fast reasoning at lower cost |
| | o3-mini | $1.10 | $4.40 | 200K | ~90 | Reasoning with larger context |
| **Anthropic** | Claude Opus 4 | $15.00 | $75.00 | 200K | ~40 | Complex analysis, writing, code |
| | Claude Sonnet 4 | $3.00 | $15.00 | 200K | ~80 | Balanced performance/cost |
| | Claude Haiku 3.5 | $0.80 | $4.00 | 200K | ~150 | Fast, cheap tasks |
| **Google** | Gemini 2.5 Pro | $1.25 | $10.00 | 1M | ~70 | Long-context analysis |
| | Gemini 2.0 Flash | $0.10 | $0.40 | 1M | ~200 | Ultra-cheap high-volume |
| | Gemini 1.5 Pro | $1.25 | $5.00 | 2M | ~60 | Massive context processing |
| **Meta** | Llama 3.3 70B | ~$0.60 | ~$0.60 | 128K | ~100 | Open-source, self-hostable |
| | Llama 3.1 405B | ~$3.50 | ~$3.50 | 128K | ~30 | Best open-source quality |
| **Mistral** | Mistral Large | $2.00 | $6.00 | 128K | ~80 | Multilingual, EU compliance |
| | Mistral Small | $0.10 | $0.30 | 128K | ~150 | Budget multilingual tasks |
| | Codestral | $0.30 | $0.90 | 256K | ~120 | Code generation, 256K context |
| **DeepSeek** | DeepSeek-V3 | $0.27 | $1.10 | 128K | ~60 | Cheapest capable model |
| | DeepSeek-R1 | $0.55 | $2.19 | 128K | ~30 | Cheap reasoning alternative |
| **xAI** | Grok-3 | $3.00 | $15.00 | 131K | ~70 | Advanced reasoning, competitive with Claude Opus |
| | Grok-3 Mini | $0.30 | $0.50 | 131K | ~150 | Fast, efficient reasoning |
| **Groq** | Llama 3.3 70B (via Groq) | $0.59 | $0.79 | 128K | ~500 | Fastest inference available |
| | Mixtral 8x7B (via Groq) | $0.24 | $0.24 | 32K | ~400 | Ultra-fast MoE model |
| **Perplexity** | Sonar Pro | $3.00 | $15.00 | 200K | ~60 | Search-augmented generation |
| | Sonar | $1.00 | $1.00 | 128K | ~100 | Fast search-augmented |
| **Cohere** | Command R+ | $2.50 | $10.00 | 128K | ~50 | RAG, enterprise search |
| | Command R | $0.15 | $0.60 | 128K | ~80 | Cheap RAG tasks |

*Meta models priced via Together AI hosting. Self-hosting is free (compute costs only).*
*Groq models use Groq LPU hardware for ultra-low latency inference.*
*Perplexity models include real-time web search capabilities.*

---

## Embedding Models

| Provider | Model | Price ($/1M tokens) | Dimensions | Max Input |
|----------|-------|--------------------:|-----------:|----------:|
| OpenAI | text-embedding-3-small | $0.02 | 1,536 | 8,191 |
| OpenAI | text-embedding-3-large | $0.13 | 3,072 | 8,191 |
| Google | text-embedding-004 | $0.006 | 768 | 2,048 |
| Voyage AI | Voyage 3 | $0.06 | 1,024 | 32,000 |
| Cohere | Embed v4 | $0.10 | 1,024 | 512 |
| Mistral | Mistral Embed | $0.10 | 1,024 | 8,192 |

---

## Image Generation

| Provider | Model | Price per Image | Resolution | Speed |
|----------|-------|----------------:|------------|------:|
| OpenAI | DALL-E 3 | $0.040 | 1024x1024 | ~15s |
| OpenAI | DALL-E 3 HD | $0.080 | 1024x1792 | ~20s |
| Stability AI | SD 3.5 | $0.035 | 1024x1024 | ~5s |
| Midjourney | v6 | ~$0.02-0.12 | Up to 2048 | ~30s |

*Midjourney pricing is subscription-based ($10-120/month). Per-image cost depends on plan.*

---

## Price Per Task Comparison

Real-world costs for common tasks:

| Task | Tokens Used | GPT-4o | Claude Sonnet 4 | Gemini 2.0 Flash | DeepSeek-V3 |
|------|------------|-------:|-----------------:|------------------:|------------:|
| Summarize 10-page doc | ~5K in, ~500 out | $0.017 | $0.022 | $0.001 | $0.002 |
| Code review (500 lines) | ~3K in, ~2K out | $0.028 | $0.039 | $0.001 | $0.003 |
| Translate 1000 words | ~2K in, ~2K out | $0.025 | $0.036 | $0.001 | $0.003 |
| Chat conversation (10 turns) | ~10K in, ~5K out | $0.075 | $0.105 | $0.003 | $0.008 |
| RAG query (large context) | ~50K in, ~1K out | $0.135 | $0.165 | $0.005 | $0.015 |

**Cheapest option by task type:**
- Simple classification/extraction: **Gemini 2.0 Flash** ($0.10/$0.40)
- Code generation: **DeepSeek-V3** ($0.27/$1.10)
- Complex reasoning: **DeepSeek-R1** ($0.55/$2.19) vs o3-mini ($1.10/$4.40)
- Long document analysis: **Gemini 2.5 Pro** (1M context at $1.25/$10.00)

---

## Monthly Cost Estimator

**Processing 1M tokens/day (input + output split 2:1):**

| Provider | Model | Daily Cost | Monthly Cost | Annual Cost |
|----------|-------|----------:|-----------:|----------:|
| Google | Gemini 2.0 Flash | $0.20 | $6.00 | $73.00 |
| Mistral | Mistral Small | $0.17 | $5.00 | $60.83 |
| DeepSeek | DeepSeek-V3 | $0.55 | $16.39 | $199.41 |
| OpenAI | GPT-4o-mini | $0.30 | $9.00 | $109.50 |
| Cohere | Command R | $0.30 | $9.00 | $109.50 |
| Meta | Llama 3.3 70B | $0.60 | $18.00 | $219.00 |
| Google | Gemini 2.5 Pro | $4.17 | $125.00 | $1,520.83 |
| OpenAI | GPT-4o | $5.00 | $150.00 | $1,825.00 |
| Anthropic | Claude Sonnet 4 | $7.00 | $210.00 | $2,555.00 |
| Anthropic | Claude Opus 4 | $35.00 | $1,050.00 | $12,775.00 |

*Assumes 667K input + 333K output tokens per day. Actual costs vary by usage pattern.*

---

## Cost Optimization Tips

1. **Route by complexity** -- Use cheap models (Gemini Flash, GPT-4o-mini) for simple tasks, premium models only when needed. A routing layer can cut costs 60-80%.

2. **Batch API discounts** -- OpenAI offers **50% off** via their Batch API for non-time-sensitive workloads.

3. **Prompt caching** -- Anthropic offers **90% discount** on cached prompt tokens. If you send the same system prompt repeatedly, this is massive savings.

4. **Use open-source for high volume** -- At >10M tokens/day, self-hosting Llama 3.3 70B on 2xA100 costs ~$3/hour vs $36/day via API.

5. **Compress your prompts** -- Remove unnecessary whitespace, use abbreviations in system prompts, cache few-shot examples. 20-30% token reduction is common.

6. **Negotiate enterprise pricing** -- All providers offer volume discounts. At $1K+/month spend, ask for custom pricing.

7. **Monitor with budgets** -- Set hard spending limits via provider dashboards. One runaway loop can cost thousands.

---

## Calculator CLI

Estimate costs across all providers from your terminal:

```bash
# Basic comparison
python calculator/estimate.py --input-tokens 1000000 --output-tokens 500000

# Filter by type
python calculator/estimate.py --input-tokens 1000000 --output-tokens 500000 --type text

# JSON output for scripting
python calculator/estimate.py --input-tokens 1000000 --output-tokens 500000 --json

# Sort by monthly cost
python calculator/estimate.py --input-tokens 1000000 --output-tokens 500000 --sort monthly
```

**Output:**
```
=== LLM Cost Comparison ===
Daily usage: 1,000,000 input tokens + 500,000 output tokens

Provider          Model              Daily Cost    Monthly Cost   Annual Cost
---------------------------------------------------------------------------------
Mistral           Mistral Small      $0.25         $7.50          $91.25
Google            Gemini 2.0 Flash   $0.30         $9.00          $109.50
OpenAI            GPT-4o-mini        $0.45         $13.50         $164.25
DeepSeek          DeepSeek-V3        $0.82         $24.60         $299.30
...
```

Requires Python 3.8+. No dependencies -- uses only the standard library.

---

## How It Works

1. **Data source**: `data/pricing.json` contains structured pricing for all models
2. **Community updates**: Pricing data is community-maintained. Automated scrapers are in development -- PRs welcome! GitHub Actions validates data integrity on updates.
3. **History tracking**: Every price change is saved in `data/history/`
4. **Changelog**: All changes logged in [CHANGELOG.md](CHANGELOG.md)

---

## Scraper Status

| Provider | Scraper Status |
|----------|---------------|
| OpenAI | Manual (stub) |
| Anthropic | Manual (stub) |
| Google | Manual (stub) |
| Mistral | Manual (stub) |
| DeepSeek | Manual (stub) |
| Meta (Together AI) | Manual (stub) |
| xAI | Manual (stub) |
| Groq | Manual (stub) |
| Perplexity | Manual (stub) |
| Cohere | No scraper yet |
| Stability AI | No scraper yet |
| Midjourney | No scraper yet |

*All scrapers currently return verified manual data. Real-time scraping via provider APIs is on the roadmap. PRs welcome!*

---

## Contributing

Found a price change? New model released? [Open a PR!](CONTRIBUTING.md)

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Reporting price changes
- Adding new providers/models
- Developing scrapers

---

## License

[MIT](LICENSE) -- Copyright 2026 Cognitive AppDev

---

**Star this repo to get notified of price changes that could save you money.**

Other projects: [awesome-openclaw-security](https://github.com/munnam77/awesome-openclaw-security)
