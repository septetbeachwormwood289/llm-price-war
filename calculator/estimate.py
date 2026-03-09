#!/usr/bin/env python3
"""
LLM Cost Estimator CLI

Reads pricing data and outputs a sorted comparison table for given token usage.
Requires Python 3.8+. Uses only the standard library.
"""

import argparse
import json
import os
import sys

# ANSI color codes
BOLD = "\033[1m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
DIM = "\033[2m"
RESET = "\033[0m"

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "..", "data", "pricing.json")


def load_pricing(path: str) -> dict:
    """Load pricing data from JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Pricing data not found at {path}", file=sys.stderr)
        print("Make sure you're running from the repo root or data/pricing.json exists.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(1)


def calculate_costs(data: dict, input_tokens: int, output_tokens: int, model_type: str = "text") -> list:
    """Calculate daily, monthly, annual costs for all models of a given type."""
    results = []

    for provider_id, provider in data["providers"].items():
        provider_name = provider["name"]
        for model_id, model in provider["models"].items():
            if model.get("type") != model_type:
                continue

            input_price = model.get("input_price_per_1m")
            output_price = model.get("output_price_per_1m")

            if input_price is None:
                continue

            # For embedding models, there's no output cost
            if output_price is None:
                output_price = 0

            daily_cost = (input_tokens / 1_000_000) * input_price + (output_tokens / 1_000_000) * output_price
            monthly_cost = daily_cost * 30
            annual_cost = daily_cost * 365

            results.append({
                "provider": provider_name,
                "model": model.get("name", model_id),
                "input_price": input_price,
                "output_price": output_price,
                "daily": daily_cost,
                "monthly": monthly_cost,
                "annual": annual_cost,
                "context_window": model.get("context_window"),
                "batch_discount": model.get("batch_discount"),
            })

    return results


def format_currency(amount: float) -> str:
    """Format a dollar amount with appropriate precision."""
    if amount < 0.01:
        return f"${amount:.4f}"
    elif amount < 1:
        return f"${amount:.3f}"
    elif amount < 100:
        return f"${amount:.2f}"
    else:
        return f"${amount:,.2f}"


def format_number(n: int) -> str:
    """Format large numbers with commas."""
    return f"{n:,}"


def print_table(results: list, input_tokens: int, output_tokens: int, use_color: bool = True) -> None:
    """Print a formatted comparison table."""
    b = BOLD if use_color else ""
    g = GREEN if use_color else ""
    y = YELLOW if use_color else ""
    c = CYAN if use_color else ""
    d = DIM if use_color else ""
    r = RESET if use_color else ""

    print()
    print(f"{b}=== LLM Cost Comparison ==={r}")
    print(f"Daily usage: {c}{format_number(input_tokens)}{r} input tokens + {c}{format_number(output_tokens)}{r} output tokens")
    print()

    # Column widths
    w_provider = max(len("Provider"), max((len(r["provider"]) for r in results), default=8))
    w_model = max(len("Model"), max((len(r["model"]) for r in results), default=5))
    w_daily = 12
    w_monthly = 14
    w_annual = 14

    # Header
    header = (
        f"{b}{'Provider':<{w_provider}}  "
        f"{'Model':<{w_model}}  "
        f"{'Daily Cost':>{w_daily}}  "
        f"{'Monthly Cost':>{w_monthly}}  "
        f"{'Annual Cost':>{w_annual}}{r}"
    )
    print(header)
    print("-" * (w_provider + w_model + w_daily + w_monthly + w_annual + 8))

    for i, row in enumerate(results):
        daily_str = format_currency(row["daily"])
        monthly_str = format_currency(row["monthly"])
        annual_str = format_currency(row["annual"])

        # Highlight cheapest in green
        color = g if i == 0 else ""
        end = r if i == 0 else ""

        line = (
            f"{color}{row['provider']:<{w_provider}}  "
            f"{row['model']:<{w_model}}  "
            f"{daily_str:>{w_daily}}  "
            f"{monthly_str:>{w_monthly}}  "
            f"{annual_str:>{w_annual}}{end}"
        )
        print(line)

    print()

    # Show savings info
    if len(results) >= 2:
        cheapest = results[0]
        most_expensive = results[-1]
        if most_expensive["monthly"] > 0:
            savings = ((most_expensive["monthly"] - cheapest["monthly"]) / most_expensive["monthly"]) * 100
            print(
                f"{d}Cheapest: {g}{cheapest['model']}{r}{d} at {g}{format_currency(cheapest['monthly'])}/month{r}"
            )
            print(
                f"{d}Most expensive: {y}{most_expensive['model']}{r}{d} at "
                f"{y}{format_currency(most_expensive['monthly'])}/month{r}"
            )
            print(f"{d}Potential savings: up to {g}{savings:.0f}%{r}{d} by switching to cheapest option{r}")

    # Batch discount note
    batch_models = [r for r in results if r.get("batch_discount")]
    if batch_models:
        print()
        print(f"{d}Batch API discounts available:{r}")
        for m in batch_models:
            discount_pct = int(m["batch_discount"] * 100)
            batch_monthly = m["monthly"] * (1 - m["batch_discount"])
            print(
                f"  {m['provider']} {m['model']}: {discount_pct}% off "
                f"-> {format_currency(batch_monthly)}/month"
            )

    print()


def print_json(results: list, input_tokens: int, output_tokens: int) -> None:
    """Print results as JSON."""
    output = {
        "input_tokens_per_day": input_tokens,
        "output_tokens_per_day": output_tokens,
        "models": [
            {
                "provider": r["provider"],
                "model": r["model"],
                "input_price_per_1m": r["input_price"],
                "output_price_per_1m": r["output_price"],
                "daily_cost": round(r["daily"], 4),
                "monthly_cost": round(r["monthly"], 2),
                "annual_cost": round(r["annual"], 2),
            }
            for r in results
        ],
    }
    print(json.dumps(output, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Estimate LLM API costs across providers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --input-tokens 1000000 --output-tokens 500000
  %(prog)s --input-tokens 100000 --output-tokens 100000 --type embedding
  %(prog)s --input-tokens 5000000 --output-tokens 2000000 --sort monthly --json
  %(prog)s -i 1000000 -o 500000 --no-color
        """,
    )
    parser.add_argument(
        "-i", "--input-tokens",
        type=int,
        required=True,
        help="Number of input tokens per day",
    )
    parser.add_argument(
        "-o", "--output-tokens",
        type=int,
        required=True,
        help="Number of output tokens per day",
    )
    parser.add_argument(
        "--type",
        choices=["text", "embedding"],
        default="text",
        help="Model type to compare (default: text)",
    )
    parser.add_argument(
        "--sort",
        choices=["daily", "monthly", "annual"],
        default="daily",
        help="Sort by cost column (default: daily)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        dest="json_output",
        help="Output as JSON instead of table",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable colored output",
    )
    parser.add_argument(
        "--data",
        default=DATA_FILE,
        help="Path to pricing.json (default: auto-detect)",
    )

    args = parser.parse_args()

    if args.input_tokens < 0 or args.output_tokens < 0:
        print("Error: Token counts must be non-negative.", file=sys.stderr)
        sys.exit(1)

    data = load_pricing(args.data)
    results = calculate_costs(data, args.input_tokens, args.output_tokens, args.type)

    if not results:
        print(f"No models found for type '{args.type}'.", file=sys.stderr)
        sys.exit(1)

    results.sort(key=lambda r: r[args.sort])

    use_color = not args.no_color and sys.stdout.isatty()

    if args.json_output:
        print_json(results, args.input_tokens, args.output_tokens)
    else:
        print_table(results, args.input_tokens, args.output_tokens, use_color)


if __name__ == "__main__":
    main()
