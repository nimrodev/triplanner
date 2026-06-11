import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "weather-israel", version: "1.0.0" });

interface GeoResult {
  lat: number;
  lon: number;
  name: string;
}

interface DailyData {
  time: string[];
  temperature_2m_max: number[];
  temperature_2m_min: number[];
}

async function geocode(location: string): Promise<GeoResult> {
  const url = `https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(location)}&count=5&language=en&format=json`;
  const res = await fetch(url);
  const data = (await res.json()) as {
    results?: Array<{ latitude: number; longitude: number; name: string; country_code: string }>;
  };
  if (!data.results?.length) {
    throw new Error(`Location not found: "${location}". Try a city name like Tel Aviv, Jerusalem, Haifa, or Eilat.`);
  }
  // Prefer results in Israel (IL), fall back to first result
  const match = data.results.find((r) => r.country_code === "IL") ?? data.results[0];
  return { lat: match.latitude, lon: match.longitude, name: match.name };
}

async function fetchTemps(lat: number, lon: number, dateFrom: string, dateTo: string): Promise<DailyData> {
  const today = new Date().toISOString().split("T")[0];
  // Use archive API for fully historical ranges, forecast API otherwise
  const base =
    dateTo < today
      ? "https://archive-api.open-meteo.com/v1/archive"
      : "https://api.open-meteo.com/v1/forecast";

  const url =
    `${base}?latitude=${lat}&longitude=${lon}` +
    `&start_date=${dateFrom}&end_date=${dateTo}` +
    `&daily=temperature_2m_max,temperature_2m_min` +
    `&timezone=Asia%2FJerusalem`;

  const res = await fetch(url);
  if (!res.ok) throw new Error(`Weather API error: ${res.status} ${res.statusText}`);
  const data = (await res.json()) as { daily: DailyData };
  return data.daily;
}

server.tool(
  "get_temperature",
  "Get the min/max temperature for a location in Israel on a specific date. Works for past dates and forecasts up to 16 days ahead.",
  {
    location: z
      .string()
      .describe(
        "City or area in Israel, e.g. Tel Aviv, Jerusalem, Haifa, Eilat, Dead Sea, Tiberias, Nazareth, Beer Sheva"
      ),
    date: z.string().describe("Date in YYYY-MM-DD format"),
  },
  async ({ location, date }) => {
    const { lat, lon, name } = await geocode(location);
    const daily = await fetchTemps(lat, lon, date, date);
    const i = daily.time.indexOf(date);
    if (i === -1)
      throw new Error(`No data for ${date}. Forecast is limited to 16 days ahead; older historical data is also available.`);
    return {
      content: [
        {
          type: "text" as const,
          text: `${name} on ${date}: max ${daily.temperature_2m_max[i]}°C, min ${daily.temperature_2m_min[i]}°C`,
        },
      ],
    };
  }
);

server.tool(
  "get_temperature_range",
  "Get day-by-day min/max temperatures for a location in Israel over a date range. Ideal for trip planning. Forecast available up to 16 days ahead; older dates return historical data.",
  {
    location: z
      .string()
      .describe(
        "City or area in Israel, e.g. Tel Aviv, Jerusalem, Haifa, Eilat, Dead Sea, Tiberias, Nazareth, Beer Sheva"
      ),
    date_from: z.string().describe("Start date in YYYY-MM-DD format"),
    date_to: z.string().describe("End date in YYYY-MM-DD format"),
  },
  async ({ location, date_from, date_to }) => {
    const { lat, lon, name } = await geocode(location);
    const daily = await fetchTemps(lat, lon, date_from, date_to);
    const rows = daily.time.map(
      (d, i) =>
        `${d}: max ${daily.temperature_2m_max[i]}°C, min ${daily.temperature_2m_min[i]}°C`
    );
    return {
      content: [
        {
          type: "text" as const,
          text: `${name} temperatures (${date_from} → ${date_to}):\n${rows.join("\n")}`,
        },
      ],
    };
  }
);

const transport = new StdioServerTransport();
await server.connect(transport);
