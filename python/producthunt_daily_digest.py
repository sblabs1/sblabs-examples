"""Yesterday's top Product Hunt launches as a short Markdown digest (paste into Slack, a newsletter, Notion).

    python producthunt_daily_digest.py 10
"""
import sys

from _client import run

n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
rows = run("product-hunt-launches-scraper", {"period": "daily", "featuredOnly": True, "maxLaunchesPerPeriod": n})

print(f"## Product Hunt top {len(rows)} for {rows[0]['periodLabel'] if rows else 'yesterday'}\n")
for r in rows:
    print(f"{r['position']}. **[{r['name']}]({r['productUrl']})**: {r['tagline']} "
          f"({r['votes']} votes, {', '.join(r['topics'][:2])})")
