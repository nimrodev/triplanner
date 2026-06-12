# Location Reviews Sub-Skill

When the user asks to see reviews for the suggested destination, search for recent visitor feedback and present a concise summary.

## How to search

Run 2 searches in parallel:

1. English reviews:
   ```
   site:tripadvisor.com "[destination name]" Israel reviews
   ```

2. Hebrew reviews (often more local and candid):
   ```
   "[destination name]" ביקורות מטיילים המלצות
   ```

## What to surface

From the results, extract and present:

- **Overall vibe** — one sentence summarizing the general sentiment (e.g. "Visitors consistently praise the scenery but warn about crowds on weekends")
- **Top 3 highlights** — the things people mention most positively, with a short quote or paraphrase if available
- **Watch-outs** — 1–2 recurring complaints or practical warnings real visitors mention (parking, long queues, seasonal closures, etc.)
- **Source links** — 2–3 links to the actual review pages so the user can read more

## Presentation format

> ⭐ **What visitors say about [Destination]**
>
> [Overall vibe sentence]
>
> **People love:**
> - [Highlight 1 — with brief quote if available]
> - [Highlight 2]
> - [Highlight 3]
>
> **Worth knowing:**
> - [Watch-out 1]
> - [Watch-out 2 if relevant]
>
> 🔗 [TripAdvisor reviews](url) · [source 2](url)

Keep it tight — this is a quick confidence-check for the user, not a full review digest. After presenting, ask if they'd like to proceed with the plan or explore a different destination.
