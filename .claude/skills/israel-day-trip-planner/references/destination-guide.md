# Destination Guide

## Picking a destination

Choose one destination that genuinely fits the user's hobbies. Use web search to verify it's real, accessible, and worth visiting. Prefer lesser-known gems over obvious tourist traps when they fit the interests.

## Fetching the weather

Call `mcp__weather-israel__get_temperature` with the destination city/area and the trip date (YYYY-MM-DD format). Use the returned min/max temperatures to inform the description and tips.

## Presentation format

Present the destination like this:

---
**[Destination Name]**
📍 [Region — e.g., Upper Galilee / Negev / Judean Hills]
🌡️ **Weather on [date]**: [min]°C – [max]°C — [one-line characterization, e.g. "warm and sunny, great for hiking" or "chilly morning, pack a layer"]

**Why it fits you**: [2–3 sentences connecting this specific place to their stated hobbies — make it personal, not generic]

**About the place**: [Short description of what makes it special]

🗺️ **Map**: https://www.google.com/maps/search/?api=1&query=[URL-encoded+destination+name+Israel]

---

Then ask:

> "Does this sound like your kind of day? I can also pull up **real visitor reviews** for this spot if you'd like a second opinion before we build the full plan — just say the word."

If the user asks for reviews, read `references/location-reviews.md` and follow the instructions there. After presenting reviews, ask again whether to proceed with this destination or try a different one.

If the user confirms without asking for reviews, move straight to Step 4.
