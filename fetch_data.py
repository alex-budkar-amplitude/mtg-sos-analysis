#!/usr/bin/env python3
"""Fetch Secrets of Strixhaven (SOS) card data from Scryfall API."""

import json
import time
import urllib.request
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SCRYFALL_DELAY = 0.15  # 150ms between requests per Scryfall guidelines

SETS_TO_FETCH = {
    "sos": "all_cards.json",
    "soa": "mystical_archive.json",
}


def fetch_url(url):
    """Fetch JSON from a URL with proper headers."""
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "MTG-SOS-Analysis/1.0",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_set(set_code, output_filename):
    """Fetch all unique cards for a set, handling pagination."""
    base_url = (
        f"https://api.scryfall.com/cards/search?q=e:{set_code}&unique=cards&order=set"
    )
    all_cards = []
    page = 1
    url = base_url

    while url:
        print(f"  Fetching {set_code} page {page}...")
        data = fetch_url(url)

        # Save raw page
        page_file = os.path.join(DATA_DIR, f"{set_code}_page{page}.json")
        with open(page_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"    Saved {page_file} ({len(data['data'])} cards)")

        all_cards.extend(data["data"])

        if data.get("has_more"):
            url = data["next_page"]
            page += 1
            time.sleep(SCRYFALL_DELAY)
        else:
            url = None

    # Save combined file
    output_path = os.path.join(DATA_DIR, output_filename)
    with open(output_path, "w") as f:
        json.dump(all_cards, f, indent=2)

    print(f"  Total: {len(all_cards)} unique cards -> {output_path}")
    return all_cards


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    for set_code, filename in SETS_TO_FETCH.items():
        print(f"\nFetching set: {set_code.upper()}")
        cards = fetch_set(set_code, filename)

        # Print quick summary
        rarities = {}
        colors_count = {}
        for card in cards:
            r = card.get("rarity", "unknown")
            rarities[r] = rarities.get(r, 0) + 1

            card_colors = card.get("colors", [])
            if not card_colors:
                key = "Colorless"
            elif len(card_colors) > 1:
                key = "Multicolor"
            else:
                key = card_colors[0]
            colors_count[key] = colors_count.get(key, 0) + 1

        print(f"\n  Rarity breakdown:")
        for r, c in sorted(rarities.items()):
            print(f"    {r}: {c}")
        print(f"\n  Color breakdown:")
        for col, c in sorted(colors_count.items()):
            print(f"    {col}: {c}")


if __name__ == "__main__":
    main()
