# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Self-hosted network monitoring pipeline running on a Raspberry Pi 400. Collects Ookla speed test data on a cron schedule and serves it via a Flask REST API for consumption by an external portfolio dashboard.

## Commands

**Initialize the database:**
```bash
python3 db/create_db.py
```

**Run data collection manually:**
```bash
python3 scripts/collect_speedtest.py
```

**Start the API server (port 5050):**
```bash
python3 scripts/speedtest_api.py
```

**Inspect the database:**
```bash
python3 db/check_db.py
```

## Architecture

Data flows in one direction: cron → collector → SQLite → Flask API → external dashboard.

**`scripts/collect_speedtest.py`** — runs the Ookla CLI (`/usr/bin/speedtest --format=json`), parses the JSON output (converting bytes/s to Mbps), writes to SQLite. Includes 3-retry logic with 20-second delays and logs to `logs/speedtest.log`.

**`scripts/speedtest_api.py`** — minimal Flask server exposing a single endpoint: `GET /api/speedtest`. Returns the last 50 records sorted oldest-to-newest as JSON, intended for client-side charting.

**`db/`** — SQLite schema is a single `speedtests` table: `id`, `timestamp`, `ping_ms`, `download_mbps`, `upload_mbps`. `create_db.py` initializes it; `check_db.py` prints the first 10 rows.

## Deployment Context

All paths are hardcoded for the Raspberry Pi:
- DB: `/home/czvck/Projects/network-dashboard/db/network_metrics.db`
- Logs: `/home/czvck/Projects/network-dashboard/logs/speedtest.log`

Cron schedule on the Pi runs at :05 and :35 each hour:
```
5,35 * * * * sleep 20 && /usr/bin/python3 /home/pi/Projects/network-dashboard/scripts/collect_speedtest.py >> /home/pi/cron.log 2>&1
```

nginx sits in front of the Flask server as a reverse proxy (config not in this repo).

## Key Dependencies

- Python 3 standard library only (no `requirements.txt`)
- `flask` for the API server
- Ookla `speedtest` CLI must be installed separately on the Pi
