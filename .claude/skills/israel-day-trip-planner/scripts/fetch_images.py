#!/usr/bin/env python3
"""
Fetch 2 representative Wikimedia Commons images for a destination and download them to /tmp.

Usage:
    python3 fetch_images.py "Agamon HaHula"

Output:
    Prints JSON with image info:
    [
      {"url": "https://...", "title": "...", "local_path": "/tmp/trip_img_0.jpg"},
      {"url": "https://...", "title": "...", "local_path": "/tmp/trip_img_1.jpg"}
    ]
"""
import json
import sys
import urllib.request
import urllib.parse
import os

COMMONS_API = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "israel-trip-planner/1.0"


def search_images(query: str, limit: int = 2) -> list[dict]:
    """Search Wikimedia Commons for images of the destination."""
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrnamespace": "6",  # File namespace
        "gsrsearch": f"{query} Israel",
        "gsrlimit": str(limit * 3),  # Fetch extra to filter out non-photos
        "prop": "imageinfo",
        "iiprop": "url|mime|size",
        "iiurlwidth": "800",
    }
    url = COMMONS_API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=8) as resp:
        data = json.loads(resp.read())

    pages = data.get("query", {}).get("pages", {}).values()
    results = []
    for page in pages:
        info = page.get("imageinfo", [{}])[0]
        mime = info.get("mime", "")
        if mime not in ("image/jpeg", "image/png"):
            continue
        thumb = info.get("thumburl") or info.get("url")
        if not thumb:
            continue
        results.append({
            "url": thumb,
            "title": page.get("title", "").replace("File:", ""),
        })
        if len(results) >= limit:
            break
    return results


def download_image(url: str, path: str) -> bool:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            with open(path, "wb") as f:
                f.write(resp.read())
        return True
    except Exception:
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_images.py <destination name>", file=sys.stderr)
        sys.exit(1)

    destination = " ".join(sys.argv[1:])
    images = search_images(destination, limit=2)

    if not images:
        print(json.dumps([]))
        return

    results = []
    for i, img in enumerate(images):
        ext = ".jpg" if "jpeg" in img["url"] else ".png"
        local_path = f"/tmp/trip_img_{i}{ext}"
        ok = download_image(img["url"], local_path)
        if ok:
            results.append({
                "url": img["url"],
                "title": img["title"],
                "local_path": local_path,
            })

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
