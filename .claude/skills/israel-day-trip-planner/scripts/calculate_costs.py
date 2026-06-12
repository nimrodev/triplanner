#!/usr/bin/env python3
"""
Calculate trip costs in ILS and a target currency using live exchange rates.

Usage:
    python3 calculate_costs.py --currency USD --items '[
        {"item": "Transport (round trip)", "cost_ils": 30},
        {"item": "Entry fees", "cost_ils": 0},
        {"item": "Food & drinks", "cost_ils": 80},
        {"item": "Activities / extras", "cost_ils": 20}
    ]'

Output: a markdown budget table with ILS and converted amounts, plus the live rate used.
"""
import argparse
import json
import sys
import urllib.request
import urllib.error

FRANKFURTER_URL = "https://api.frankfurter.app/latest?from=ILS&to={currency}"


def fetch_rate(currency: str) -> float:
    currency = currency.upper()
    if currency == "ILS":
        return 1.0
    url = FRANKFURTER_URL.format(currency=currency)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "israel-trip-planner/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
            return data["rates"][currency]
    except (urllib.error.URLError, KeyError, json.JSONDecodeError) as e:
        print(f"ERROR: Could not fetch exchange rate for {currency}: {e}", file=sys.stderr)
        sys.exit(1)


def format_amount(amount: float, symbol: str) -> str:
    return f"{symbol}{amount:,.0f}" if amount == int(amount) else f"{symbol}{amount:,.2f}"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--currency", required=True, help="Target currency code, e.g. USD, EUR, GBP")
    parser.add_argument("--items", required=True, help='JSON array of {"item": str, "cost_ils": number}')
    args = parser.parse_args()

    currency = args.currency.upper()
    try:
        items = json.loads(args.items)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON for --items: {e}", file=sys.stderr)
        sys.exit(1)

    rate = fetch_rate(currency)
    total_ils = sum(row["cost_ils"] for row in items)
    total_converted = round(total_ils * rate, 2)

    ils_symbol = "₪"
    currency_symbol = currency  # fallback; common symbols below
    symbols = {"USD": "$", "EUR": "€", "GBP": "£", "JPY": "¥", "AUD": "A$",
               "CAD": "C$", "CHF": "CHF ", "CNY": "¥", "INR": "₹", "BRL": "R$"}
    currency_symbol = symbols.get(currency, f"{currency} ")

    # Print markdown table
    header = f"| Item | ILS | {currency} |"
    sep    = "|------|-----|------|"
    print(header)
    print(sep)
    for row in items:
        ils = row["cost_ils"]
        converted = round(ils * rate, 2)
        free_note = "  (free)" if ils == 0 else ""
        print(f"| {row['item']} | {format_amount(ils, ils_symbol)}{free_note} | {format_amount(converted, currency_symbol)}{free_note} |")
    print(f"| **Total** | **{format_amount(total_ils, ils_symbol)}** | **{format_amount(total_converted, currency_symbol)}** |")
    print()
    print(f"_Live rate: 1 ILS = {rate:.4f} {currency} (source: frankfurter.app)_")


if __name__ == "__main__":
    main()
