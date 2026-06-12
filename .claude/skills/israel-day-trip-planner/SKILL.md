---
name: israel-day-trip-planner
description: Plan a 1-day trip in Israel tailored to the user's hobbies and interests. Use this skill whenever someone wants to plan a day trip, asks for destination ideas, says "where should I go", "what can I do for a day", mentions their hobbies and wanting to go somewhere, or asks for travel suggestions within Israel. Trigger even if they don't say "Israel" explicitly — if context makes it clear they're in Israel or asking about it, use this skill.
---

# Israel Day Trip Planner

Help the user plan a fulfilling 1-day trip somewhere in Israel, tailored to their hobbies. The trip should fit within a **1000 NIS budget** and fill a full day (roughly 08:00–19:00).

## Conversation Flow

### Step 1: Gather the essentials

Ask the user — conversationally, not as a formal list:
- What are their hobbies or interests? (hiking, history, photography, food, art, water sports, etc.)
- Where are they starting from? (city or region)
- When are they planning to go? (date — needed for weather)
- Solo or with others?
- Where are they visiting from / what's their home currency? (needed for cost conversion — skip if they mention a local Israeli city and seem to be a local)

Keep it light. One or two questions at a time is fine.

### Step 2: Clarify if needed (max 1 round)

If hobbies are vague, ask one targeted follow-up:
- "Are you more into outdoors/nature, or history/culture?"
- "Easygoing walk, or something more active like a hike?"
- "Any part of Israel you'd love to explore — north, south, coast?"

Don't over-interview. After 2–3 exchanges at most, move forward with a suggestion.

### Step 3: Suggest a destination

Read `references/destination-guide.md` for how to pick a destination, fetch the weather, and present the suggestion.

### Step 4: Build the full day plan

Once the user confirms the destination, read `references/day-plan-format.md` for the schedule format, budget breakdown, and tips.

### Step 5: Offer PDF export

After presenting the full plan, offer to save it as a PDF. If the user agrees, use the `pdf` skill to generate it.

## Tone

Be enthusiastic but grounded. This is a real trip they're going to take — actual distances, real costs, genuine activity suggestions. Avoid padding the plan with generic "stop for coffee" filler unless it's a genuinely notable café worth mentioning.
