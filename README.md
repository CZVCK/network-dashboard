# Network Dashboard

A self-hosted network monitoring pipeline running on a Raspberry Pi. 
Collects speed test data every 30 minutes via cron, stores results in 
SQLite, and serves them through a Flask API proxied by nginx.



## What it does

Runs the Ookla CLI on a schedule, parses the JSON output, and writes 
ping, download, and upload metrics to a local database. Logs every run 
so I can tell when cron misbehaves or the network drops out. The Flask 
API at `/speedtest` lets me query the data from my portfolio dashboard.

## Stack

- Python, SQLite, Flask, nginx
- Ookla CLI for speed tests
- Cron for scheduling
- Raspberry Pi 400 (runs 24/7)

## Project Structure

```
network-dashboard/
├── scripts/
│   ├── collect_speedtest.py   # data collection pipeline
│   └── check_db.py            # inspect DB contents
├── db/
│   └── network_metrics.db     # SQLite database (gitignored)
├── logs/
│   └── speedtest.log          # runtime logs (gitignored)
├── cron/
│   └── speedtest_cron.txt     # cron reference config
└── speedtest_api.py           # Flask API (port 5050)
```
## Setup

Install the Ookla CLI:

    sudo apt update && sudo apt install curl -y
    curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash
    sudo apt install speedtest

Clone and run:

    git clone git@github.com:CZVCK/network-dashboard.git
    cd network-dashboard
    python3 scripts/collect_speedtest.py

Cron entry:

    5,35 * * * * sleep 20 && /usr/bin/python3 /home/pi/Projects/network-dashboard/scripts/collect_speedtest.py >> /home/pi/cron.log 2>&1

## What's next
- Chart.JS dashboard
- Jitter and packet loss tracking
- Outage tracker
- Pi-hole DNS stats integration
