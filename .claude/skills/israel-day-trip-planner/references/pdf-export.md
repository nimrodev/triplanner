# PDF Export

## Offer to the user

After presenting the full day plan, always add this at the end:

---
💾 **Want to save this plan?** I can export it as a PDF file for you — just say "save as PDF" or "download the plan".
---

## When the user asks to save

1. Write the full trip plan to `/tmp/trip-plan.md` — include destination header, weather, day schedule, budget table, and tips, formatted cleanly.

2. Run the export script:
   ```
   bash .claude/skills/israel-day-trip-planner/scripts/export-pdf.sh
   ```

3. If the script succeeds, tell the user the file was saved to `~/Desktop/trip-plan.pdf`.

4. If the script fails (pandoc not installed), save the markdown to `~/Desktop/trip-plan.md` and tell the user:
   > "I saved the plan as `~/Desktop/trip-plan.md`. To convert it to PDF, install pandoc with `brew install pandoc` and run `pandoc ~/Desktop/trip-plan.md -o ~/Desktop/trip-plan.pdf`."
