"""Newest reviews of an app from Google Play and the App Store in one CSV, plus a rating summary.

    python app_reviews_export.py com.duolingo https://apps.apple.com/us/app/duolingo-language-lessons/id570060128
"""
import csv
import sys
from collections import Counter

from _client import run

apps = sys.argv[1:] or ["com.duolingo", "https://apps.apple.com/us/app/duolingo-language-lessons/id570060128"]
rows = run("app-reviews-scraper", {"apps": apps, "maxReviewsPerApp": 500, "countries": ["us"], "sort": "newest"})

fields = ["store", "appId", "rating", "title", "text", "date", "appVersion", "thumbsUp", "developerReply"]
with open("reviews.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
    w.writeheader()
    w.writerows(rows)

for store in sorted({r["store"] for r in rows}):
    stars = Counter(r["rating"] for r in rows if r["store"] == store)
    total = sum(stars.values())
    avg = sum(k * v for k, v in stars.items()) / total
    print(f"{store}: {total} reviews, average {avg:.2f}, 1-star share {stars[1] / total:.0%}")
print("saved reviews.csv")
