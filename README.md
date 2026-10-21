# sblabs examples

Small, copy-paste examples for the [sblabs Actors on Apify](https://apify.com/sblabs): YouTube transcripts and comments, app reviews, Shopify products and Product Hunt launches. Each script is one file, a few dozen lines, and runs in a minute.

> I build and maintain these Actors. They're pay-per-result: you pay for the rows you get, and failed inputs are free. A free Apify account includes monthly credit, which is enough to run every example here.

## The Actors

| Actor | What you get | Price | Try it in one click |
|---|---|---|---|
| [YouTube Transcript Scraper](https://apify.com/sblabs/youtube-transcript-scraper) | Transcripts of videos, playlists or channels as text, timestamped lines, AI-ready chunks, SRT and VTT | $3 / 1,000 transcripts | [Latest 10 videos of a channel as AI chunks](https://apify.com/sblabs/youtube-transcript-scraper/examples/transcripts-of-a-channel-s-latest-10-videos-as-ai-chunks) |
| [YouTube Comments Scraper](https://apify.com/sblabs/youtube-comments-scraper) | Comments and replies with likes, reply counts, pinned and creator-hearted flags | $0.40 / 1,000 comments | [Top 200 comments of a video, with replies](https://apify.com/sblabs/youtube-comments-scraper/examples/top-200-comments-of-a-youtube-video-with-replies) |
| [App Reviews Scraper](https://apify.com/sblabs/app-reviews-scraper) | Google Play and App Store reviews in one run, same fields for both stores | $0.08 / 1,000 reviews | [Newest 500 reviews of an app](https://apify.com/sblabs/app-reviews-scraper/examples/newest-500-reviews-of-an-app-from-google-play-and-app-store) |
| [Shopify Products Scraper](https://apify.com/sblabs/shopify-products-scraper) | Every product of a store: prices, sale prices, variants, SKUs, stock | $0.50 / 1,000 products | [All products of a store](https://apify.com/sblabs/shopify-products-scraper/examples/all-products-prices-and-stock-of-a-shopify-store) |
| [Product Hunt Launches Scraper](https://apify.com/sblabs/product-hunt-launches-scraper) | Daily, weekly and monthly leaderboards with votes, ranks and topics | $0.60 / 1,000 launches | [Yesterday's top 20 launches](https://apify.com/sblabs/product-hunt-launches-scraper/examples/yesterday-s-top-20-product-hunt-launches) |

Prices are for Free and Starter plans; Scale and Business plans pay 10–20% less.

## Setup

```bash
git clone https://github.com/sblabs1/sblabs-examples && cd sblabs-examples
pip install -r requirements.txt
export APIFY_TOKEN=...   # Apify Console → Settings → API & Integrations
cd python
```

## Python examples

| Script | What it does |
|---|---|
| [`youtube_transcripts_to_chunks.py`](python/youtube_transcripts_to_chunks.py) | A channel's newest videos as JSONL chunks with a timestamped link to each moment, ready for any vector database |
| [`youtube_comments_themes.py`](python/youtube_comments_themes.py) | The most-liked comments of a video, plus a ready prompt to get themes and viewer questions from any LLM |
| [`app_reviews_export.py`](python/app_reviews_export.py) | 500 newest reviews from both stores into one CSV, with average rating and 1-star share per store |
| [`shopify_price_tracker.py`](python/shopify_price_tracker.py) | Run it daily: prints new products, price changes, sell-outs and restocks since the last run |
| [`producthunt_daily_digest.py`](python/producthunt_daily_digest.py) | Yesterday's top launches as a Markdown digest for Slack or a newsletter |

```bash
python youtube_transcripts_to_chunks.py https://www.youtube.com/@TED 10 > chunks.jsonl
python youtube_comments_themes.py https://www.youtube.com/watch?v=5MuIMqhT8DM 300
python app_reviews_export.py com.duolingo https://apps.apple.com/us/app/duolingo-language-lessons/id570060128
python shopify_price_tracker.py https://www.allbirds.com
python producthunt_daily_digest.py 10
```

## n8n

[`n8n/youtube-comments-ai-summary-sheets.json`](n8n/youtube-comments-ai-summary-sheets.json): paste a YouTube link into a form, get an AI summary of what viewers think (themes, tone, questions), saved as a row in Google Sheets. Import it in n8n with **⋯ → Import from file**; setup notes are inside the workflow.

## AI agents (MCP)

All five Actors work as tools through the [Apify MCP server](https://mcp.apify.com). Add it to Claude, Cursor or any MCP client and ask things like *"get the top 200 comments of this video and tell me what viewers want next"*.

## Tutorials

- [How to get YouTube transcripts for RAG and AI pipelines (with timestamps)](https://dev.to/sblabs/how-to-get-youtube-transcripts-for-rag-and-ai-pipelines-with-timestamps-24p6)
- [I read 13,674 YouTube comments about vibe coding. Here's what developers actually think](https://dev.to/sblabs/i-read-13674-youtube-comments-about-vibe-coding-heres-what-developers-actually-think-15eh)

## Issues

Something broke, or a field is missing? Open an issue here or on the Actor's Issues tab on Apify.

MIT licensed.
