# Triplanner

A Claude Code project for planning day trips in Israel, combining a weather MCP server and an AI-powered trip planning skill.

## Contents

### `mcp/` — Weather Israel MCP Server

A Model Context Protocol server that provides weather data for locations in Israel. It uses the [Open-Meteo](https://open-meteo.com/) API for both historical data and forecasts.

**Tools:**
- `get_temperature` — Min/max temperature for a specific location and date
- `get_temperature_range` — Day-by-day temperatures over a date range (great for trip planning)

**Setup:**
```bash
cd mcp
npm install
npm run build
```

**Run:**
```bash
npm start
```

### `.claude/skills/israel-day-trip-planner/` — Day Trip Planner Skill

A Claude Code skill that plans personalized 1-day trips in Israel based on the user's hobbies, starting location, and travel date. It checks the weather via the MCP server and stays within a 1000 NIS budget.

The skill is automatically available when working inside this project with Claude Code.
