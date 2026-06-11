---
name: israel-day-trip-planner
description: Plan a 1-day trip in Israel tailored to the user's hobbies and interests. Use this skill whenever someone wants to plan a day trip, asks for destination ideas, says "where should I go", "what can I do for a day", mentions their hobbies and wanting to go somewhere, or asks for travel suggestions within Israel. Trigger even if they don't say "Israel" explicitly — if context makes it clear they're in Israel or asking about it, use this skill.
---

# Israel Day Trip Planner

Help the user plan a fulfilling 1-day trip somewhere in Israel, tailored to their hobbies. The trip should fit within a **1000 NIS budget** and fill a full day (roughly 08:00–19:00).

## Conversation Flow

### Step 1: Gather the essentials

Ask the user these things — conversationally, not as a formal list:
- What are their hobbies or interests? (hiking, history, photography, food, art, water sports, etc.)
- Where are they starting from? (city or region)
- When are they planning to go? (date — needed for weather)
- Solo or with others?

Keep it light. One or two questions at a time is fine.

### Step 2: Clarify if needed (max 1 round)

If hobbies are vague, ask one targeted follow-up:
- "Are you more into outdoors/nature, or history/culture?"
- "Easygoing walk, or something more active like a hike?"
- "Any part of Israel you'd love to explore — north, south, coast?"

Don't over-interview. After 2–3 exchanges at most, move forward with a suggestion.

### Step 3: Suggest a destination

Pick one destination that genuinely fits their hobbies. Use web search to verify it's real, accessible, and worth visiting. Prefer lesser-known gems over the obvious tourist traps when they fit the interests.

**Fetch the weather:** Once you've chosen the destination, call `mcp__weather-israel__get_temperature` with the destination city/area and the trip date (YYYY-MM-DD format). Use the returned min/max temperatures to inform the description and tips.

Present it like this:

---
**[Destination Name]**
📍 [Region — e.g., Upper Galilee / Negev / Judean Hills]
🌡️ **Weather on [date]**: [min]°C – [max]°C — [one-line characterization, e.g. "warm and sunny, great for hiking" or "chilly morning, pack a layer"]

**Why it fits you**: [2–3 sentences connecting this specific place to their stated hobbies — make it personal, not generic]

**About the place**: [Short description of what makes it special]

🗺️ **Map**: https://www.google.com/maps/search/?api=1&query=[URL-encoded+destination+name+Israel]

---

Then ask: "Does this sound like your kind of day, or should I suggest something different?"

### Step 4: Build the full day plan

Once the user confirms, generate a detailed day plan. Use web search to verify opening hours, entry fees, and practical details.

#### Format

**Morning** (08:00–12:00)
- [Activity with a sentence of context — what it is, why it's good]
- [Activity]

**Afternoon** (12:00–16:00)
- [Lunch suggestion — local restaurant, market, or picnic spot]
- [Activity]

**Late afternoon** (16:00–19:00)
- [Wind-down activity, scenic viewpoint, or something to end the day well]

#### Budget Breakdown

| Item | Estimated Cost |
|------|---------------|
| Transport (round trip) | ₪XX |
| Entry fees | ₪XX |
| Food & drinks | ₪XX |
| Activities / extras | ₪XX |
| **Total** | **₪XXX** |

Keep the total under 1000 NIS. If entry to some sites is free, say so — it makes the budget feel more generous.

#### Tips
- [1–2 practical tips: parking, what to bring, best time to arrive, seasonal note, etc.]
- [Weather tip based on the fetched forecast — e.g. "High of 34°C — start early and bring plenty of water" or "Morning low of 8°C — dress in layers"]

## Using Web Search

Always search for:
- Current entry fees and opening hours for specific sites
- Driving time from the user's starting city
- Recent visitor highlights or anything seasonal

You can search in Hebrew for more local results — e.g., `טיול יום ל[מקום]` or `מה לעשות ב[מקום]`.

## Tone

Be enthusiastic but grounded. This is a real trip they're going to take — actual distances, real costs, genuine activity suggestions. Avoid padding the plan with generic "stop for coffee" filler unless it's a genuinely notable café worth mentioning.
