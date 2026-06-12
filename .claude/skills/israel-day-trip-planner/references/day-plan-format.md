# Day Plan Format

Use web search to verify opening hours, entry fees, and practical details before building the plan.

## Schedule format

**Morning** (08:00–12:00)
- [Activity with a sentence of context — what it is, why it's good]
- [Activity]

**Afternoon** (12:00–16:00)
- [Lunch suggestion — local restaurant, market, or picnic spot]
- [Activity]

**Late afternoon** (16:00–19:00)
- [Wind-down activity, scenic viewpoint, or something to end the day well]

## Budget breakdown

After estimating the ILS costs for each item, run the cost calculator script to get live currency conversion and a formatted table:

```bash
python3 <skill-base-dir>/scripts/calculate_costs.py \
  --currency <USER_CURRENCY_CODE> \
  --items '[
    {"item": "Transport (round trip)", "cost_ils": XX},
    {"item": "Entry fees",             "cost_ils": XX},
    {"item": "Food & drinks",          "cost_ils": XX},
    {"item": "Activities / extras",    "cost_ils": XX}
  ]'
```

Replace `<skill-base-dir>` with the base directory of this skill (shown at the top when the skill loads), and `<USER_CURRENCY_CODE>` with the user's currency (e.g. `USD`, `EUR`, `GBP`). If the user is local (ILS), pass `--currency ILS` and the table will show ILS only.

Paste the script's markdown output directly into the chat. It includes the live exchange rate source line automatically.

Keep the total under 1000 NIS. If entry to some sites is free, say so — it makes the budget feel more generous.

## Tips

- [1–2 practical tips: parking, what to bring, best time to arrive, seasonal note, etc.]
- [Weather tip based on the fetched forecast — e.g. "High of 34°C — start early and bring plenty of water" or "Morning low of 8°C — dress in layers"]

## Web search guidance

Always search for:
- Current entry fees and opening hours for specific sites
- Driving time from the user's starting city
- Recent visitor highlights or anything seasonal

You can search in Hebrew for more local results — e.g., `טיול יום ל[מקום]` or `מה לעשות ב[מקום]`.
