"""Transcripts of a channel's newest videos as timestamped chunks, ready for a vector database.

    python youtube_transcripts_to_chunks.py https://www.youtube.com/@TED 10 > chunks.jsonl
"""
import json
import sys

from _client import run

channel = sys.argv[1] if len(sys.argv) > 1 else "https://www.youtube.com/@TED"
limit = int(sys.argv[2]) if len(sys.argv) > 2 else 10

for video in run("youtube-transcript-scraper", {"videos": [channel], "maxVideosPerSource": limit, "chunkSize": 1000}):
    for c in video.get("chunks", []):
        print(json.dumps({
            "text": c["text"],
            "title": video["title"],
            "url": f"{video['url']}&t={int(c['start'])}s",  # cite the exact moment
            "start": c["start"],
            "end": c["end"],
        }, ensure_ascii=False))
