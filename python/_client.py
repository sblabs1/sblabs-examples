"""Shared helper: run an sblabs Actor on Apify and return its successful rows."""
import os
import sys

from apify_client import ApifyClient


def run(actor: str, run_input: dict) -> list[dict]:
    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first (Apify Console → Settings → API & Integrations).")
    client = ApifyClient(token)
    result = client.actor(f"sblabs/{actor}").call(run_input=run_input)
    rows = list(client.dataset(result["defaultDatasetId"]).iterate_items())
    for r in rows:
        if r.get("status") == "error":
            print(f"skipped {r.get('input')}: {r.get('errorMessage')}", file=sys.stderr)
    return [r for r in rows if r.get("status") == "ok"]
