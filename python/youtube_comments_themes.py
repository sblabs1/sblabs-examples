"""Most-liked comments of a video, plus a prompt you can paste into any LLM to get themes.

    python youtube_comments_themes.py https://www.youtube.com/watch?v=5MuIMqhT8DM 300
"""
import sys

from _client import run

video = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/watch?v=5MuIMqhT8DM"
n = int(sys.argv[2]) if len(sys.argv) > 2 else 300

rows = run("youtube-comments-scraper", {"videos": [video], "maxComments": n, "sort": "top"})
rows.sort(key=lambda r: r["likes"] or 0, reverse=True)

print(f"{len(rows)} comments on: {rows[0]['videoTitle'] if rows else video}\n")
print("Top 10 by likes:")
for r in rows[:10]:
    print(f"  {r['likes'] or 0:>7}  {' '.join(r['text'].split())[:100]}")

lines = "\n".join(f"- ({r['likes'] or 0} likes) {' '.join(r['text'].split())[:400]}" for r in rows)
print("\n--- prompt ---\nGroup these YouTube comments into 5-8 themes with tone and one quote each, "
      "then list the 3 most common viewer questions.\n\n" + lines)
