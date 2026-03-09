#!/usr/bin/env python3
"""
LLM Price Updater

Coordinates price fetching from all provider modules, updates pricing.json,
creates historical snapshots, and outputs a changelog of price changes.
"""

import json
import os
import sys
from datetime import datetime, timezone

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.join(SCRIPT_DIR, "..")
DATA_FILE = os.path.join(ROOT_DIR, "data", "pricing.json")
HISTORY_DIR = os.path.join(ROOT_DIR, "data", "history")

# Import provider modules
sys.path.insert(0, SCRIPT_DIR)
from providers import openai as openai_provider
from providers import anthropic as anthropic_provider
from providers import google as google_provider
from providers import mistral as mistral_provider
from providers import deepseek as deepseek_provider
from providers import together as together_provider
from providers import xai as xai_provider
from providers import groq as groq_provider
from providers import perplexity as perplexity_provider


PROVIDERS = {
    "openai": openai_provider,
    "anthropic": anthropic_provider,
    "google": google_provider,
    "mistral": mistral_provider,
    "deepseek": deepseek_provider,
    "meta": together_provider,
    "xai": xai_provider,
    "groq": groq_provider,
    "perplexity": perplexity_provider,
}


def load_current_pricing() -> dict:
    """Load the current pricing data."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_pricing(data: dict) -> None:
    """Save updated pricing data."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def save_history_snapshot(data: dict, date_str: str) -> str:
    """Save a historical snapshot of pricing data."""
    os.makedirs(HISTORY_DIR, exist_ok=True)
    path = os.path.join(HISTORY_DIR, f"{date_str}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    return path


def compare_prices(old: dict, new: dict) -> list:
    """Compare old and new pricing data, return list of changes."""
    changes = []

    for provider_id, provider in new.get("providers", {}).items():
        old_provider = old.get("providers", {}).get(provider_id, {})
        provider_name = provider.get("name", provider_id)

        for model_id, model in provider.get("models", {}).items():
            old_model = old_provider.get("models", {}).get(model_id, {})

            if not old_model:
                changes.append(f"  NEW: {provider_name} / {model.get('name', model_id)}")
                continue

            for field in ["input_price_per_1m", "output_price_per_1m"]:
                old_val = old_model.get(field)
                new_val = model.get(field)
                if old_val != new_val and new_val is not None:
                    direction = "UP" if (old_val or 0) < new_val else "DOWN"
                    field_label = "input" if "input" in field else "output"
                    changes.append(
                        f"  {direction}: {provider_name} / {model.get('name', model_id)} "
                        f"{field_label}: ${old_val} -> ${new_val}"
                    )

    return changes


def main():
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    print(f"LLM Price Updater - {today}")
    print("=" * 40)

    current_data = load_current_pricing()

    # Fetch prices from each provider
    updated = False
    for provider_id, module in PROVIDERS.items():
        provider_name = current_data["providers"].get(provider_id, {}).get("name", provider_id)
        print(f"\nFetching: {provider_name}...")

        try:
            new_prices = module.fetch_prices()
            if new_prices:
                # Merge new prices into current data
                if provider_id in current_data["providers"]:
                    for model_id, model_data in new_prices.items():
                        if model_id in current_data["providers"][provider_id]["models"]:
                            # Check if any price fields actually changed
                            existing = current_data["providers"][provider_id]["models"][model_id]
                            for key, new_val in model_data.items():
                                old_val = existing.get(key)
                                if old_val != new_val:
                                    updated = True
                            existing.update(model_data)
                        else:
                            current_data["providers"][provider_id]["models"][model_id] = model_data
                            updated = True
                print(f"  OK: {len(new_prices)} models")
            else:
                print(f"  SKIP: No data returned")
        except Exception as e:
            print(f"  ERROR: {e}")

    # Compare with original
    original_data = load_current_pricing()
    changes = compare_prices(original_data, current_data)

    if changes:
        print(f"\n{'=' * 40}")
        print(f"PRICE CHANGES DETECTED ({len(changes)}):")
        print()
        for change in changes:
            print(change)
        print()
        print(f"Summary: {len(changes)} change(s) found across providers.")
        updated = True
    else:
        print("\nNo price changes detected.")

    # Update timestamp and save
    current_data["last_updated"] = today
    save_pricing(current_data)

    # Save historical snapshot
    snapshot_path = save_history_snapshot(current_data, today)
    print(f"\nSnapshot saved: {snapshot_path}")

    if updated:
        print("\nPricing data updated. Run README generator to update tables.")
        return 0
    else:
        print("\nNo changes to commit.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
