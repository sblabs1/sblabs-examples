"""Track a Shopify store's prices: run it daily, it compares with the last run and prints changes.

    python shopify_price_tracker.py https://www.allbirds.com
"""
import json
import pathlib
import sys

from _client import run

store = sys.argv[1] if len(sys.argv) > 1 else "https://www.allbirds.com"
snapshot = pathlib.Path("prices.json")

now = {p["url"]: {"title": p["title"], "price": p["priceMin"], "onSale": p["onSale"], "available": p["available"]}
       for p in run("shopify-products-scraper", {"stores": [store], "maxProductsPerStore": 0, "includeVariants": False})}
before = json.loads(snapshot.read_text()) if snapshot.exists() else {}

for url, p in now.items():
    old = before.get(url)
    if old is None and before:
        print(f"NEW      {p['title']} at {p['price']}")
    elif old and old["price"] != p["price"]:
        print(f"PRICE    {p['title']}: {old['price']} → {p['price']}")
    elif old and old["available"] != p["available"]:
        print(f"{'RESTOCK' if p['available'] else 'SOLD OUT':<8} {p['title']}")
for url in before.keys() - now.keys():
    print(f"REMOVED  {before[url]['title']}")

snapshot.write_text(json.dumps(now, indent=1))
print(f"{len(now)} products saved to {snapshot}")
