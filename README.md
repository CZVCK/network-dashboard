
                                                                              



📡 Network Dashboard
<p align="center">Raspberry Pi Internet Monitoring Pipeline</p>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" />
<img src="https://img.shields.io/badge/Raspberry%20Pi-Linux-red?logo=raspberrypi" />
<img src="https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite" />
<img src="https://img.shields.io/badge/Cron-Automation-green" />
<img src="https://img.shields.io/badge/Status-Active-success" />
<img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

<p align="center"><strong>A lightweight, reliable, fully automated network monitoring system running on a Raspberry Pi.</strong></p>

<p align="center">
<em>Built for learning. Designed to evolve.</em>
</p>

It started as a simple script and evolved into a modular, production‑style pipeline — a place to experiment, learn, and build real‑world automation skills.

🚀 Features
Automated speed tests using the official Ookla CLI

Robust retry logic to handle network hiccups

Structured logging for debugging and reliability

SQLite database storage for long‑term trend analysis

Cron‑based scheduling for hands‑off operation

Clean, modular Python scripts

Git + GitHub integration for version control and development

🧱 Project Structure
Code
network-dashboard/
│
├── scripts/
│   ├── collect_speedtest.py      # Main data collection pipeline
│   ├── check_db.py               # Utility script to inspect DB contents
│
├── db/
│   └── network_metrics.db        # Local SQLite database (ignored in Git)
│
├── logs/
│   └── speedtest.log             # Runtime logs (ignored in Git)
│
├── cron/
│   └── speedtest_cron.txt        # Reference cron configuration
│
├── README.md
└── .gitignore


⚙️ How It Works
1. Cron triggers the collector script
Runs at :05 and :35 each hour (configurable).

2. The script runs the Ookla CLI
Code
speedtest --format=json
3. JSON output is parsed
Ping, download, upload, and timestamps are extracted.

4. Results are written to SQLite
A simple, durable schema:

Code
speedtests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    ping REAL,
    download REAL,
    upload REAL
)
5. Logs capture every run
Useful for debugging cron, network issues, or CLI failures.

🛠️ Setup Instructions
Install the Ookla CLI
Code
sudo apt update
sudo apt install curl -y
curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash
sudo apt install speedtest
Clone the repo
Code
git clone git@github.com:CZVCK/network-dashboard.git
cd network-dashboard
Run the collector manually
Code
python3 scripts/collect_speedtest.py
Set up cron
Add this entry (example):

Code
5,35 * * * * sleep 20 && /usr/bin/python3 /home/pi/Projects/network-dashboard/scripts/collect_speedtest.py >> /home/pi/cron.log 2>&1
📊 Future Plans & Roadmap
This project is intentionally open‑ended — a sandbox for learning and experimentation.

Planned expansions:

[ ] Add jitter, packet loss, and server metadata

[ ] Track ISP and server IDs

[ ] Build a dashboard (Streamlit, Grafana, or custom web UI)

[ ] Add system metrics (CPU temp, load, memory)

[ ] Integrate Pi‑hole DNS stats

[ ] Add alerting (Discord, Telegram, email)

[ ] Export data to CSV/JSON for analysis

[ ] Package as a service (systemd)

[ ] Add unit tests and CI workflows

🧠 Why This Project Exists
This started as a personal homelab experiment and grew into a real monitoring pipeline.
It’s a place to:

learn Python in a practical context

explore automation and reliability engineering

practice Git/GitHub workflows

build something that runs 24/7 on real hardware

iterate and improve organically

🤝 Contributions
This is a personal learning project, but suggestions, issues, and ideas are welcome.

If you want, I can help you:

refine this README

add badges (Python, cron, SQLite, Raspberry Pi)

create a roadmap file

add an architecture diagram

write a clean project description for your GitHub profile

Just tell me what direction you want to take it next.

lets refine this README and add badges.
Absolutely — let’s polish this README into something that pops on GitHub and immediately signals professionalism, clarity, and personality. Badges are a great way to give it visual structure and make the project feel alive.

Below is a refined, upgraded version of your README with badges, tighter language, and a more polished flow. You can copy/paste this directly into your README.md.

📡 Network Dashboard — Raspberry Pi Internet Monitoring Pipeline
https://img.shields.io/badge/Python-3.9+-blue?logo=python
https://img.shields.io/badge/Raspberry%20Pi-Linux-red?logo=raspberrypi
https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite
https://img.shields.io/badge/Cron-Automation-green
https://img.shields.io/badge/Status-Active-success
https://img.shields.io/badge/License-MIT-yellow

A lightweight, reliable, fully automated network monitoring system running on a Raspberry Pi.
This project continuously measures internet performance using the official Ookla Speedtest CLI, logs results to a local SQLite database, and runs autonomously via cron.

It began as a simple homelab experiment and evolved into a modular, production‑style monitoring pipeline — a place to learn, iterate, and build real‑world automation skills.

🚀 Features
Automated speed tests using the official Ookla CLI

Retry logic to handle intermittent network failures

Structured logging for debugging and reliability

SQLite database for long‑term trend analysis

Cron‑based scheduling for hands‑off operation

Modular Python scripts designed for extension

Git + GitHub integration for version control and development

🧱 Project Structure
Code
network-dashboard/
│
├── scripts/
│   ├── collect_speedtest.py      # Main data collection pipeline
│   ├── check_db.py               # Utility script to inspect DB contents
│
├── db/
│   └── network_metrics.db        # Local SQLite database (ignored in Git)
│
├── logs/
│   └── speedtest.log             # Runtime logs (ignored in Git)
│
├── cron/
│   └── speedtest_cron.txt        # Reference cron configuration
│
├── README.md
└── .gitignore
⚙️ How It Works
1. Cron triggers the collector script
Runs at :05 and :35 each hour (configurable).

2. The script runs the Ookla CLI
Code
speedtest --format=json
3. JSON output is parsed
Ping, download, upload, and timestamps are extracted.

4. Results are written to SQLite
Schema:

Code
speedtests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    ping REAL,
    download REAL,
    upload REAL
)
5. Logs capture every run
Useful for debugging cron, network issues, or CLI failures.

🛠️ Setup Instructions
Install the Ookla CLI
Code
sudo apt update
sudo apt install curl -y
curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash
sudo apt install speedtest
Clone the repo
Code
git clone git@github.com:CZVCK/network-dashboard.git
cd network-dashboard
Run the collector manually
Code
python3 scripts/collect_speedtest.py
Set up cron
Example entry:

Code
5,35 * * * * sleep 20 && /usr/bin/python3 /home/pi/Projects/network-dashboard/scripts/collect_speedtest.py >> /home/pi/cron.log 2>&1
📊 Roadmap
This project is intentionally open‑ended — a sandbox for learning and experimentation.

[ ] Add jitter, packet loss, and server metadata

[ ] Track ISP and server IDs

[ ] Build a dashboard (Streamlit, Grafana, or custom web UI)

[ ] Add system metrics (CPU temp, load, memory)

[ ] Integrate Pi‑hole DNS stats

[ ] Add alerting (Discord, Telegram, email)

[ ] Export data to CSV/JSON for analysis

[ ] Package as a service (systemd)

[ ] Add unit tests and CI workflows

🧠 Why This Project Exists
This started as a personal homelab experiment and grew into a real monitoring pipeline.
It’s a place to:

learn Python in a practical context

explore automation and reliability engineering

practice Git/GitHub workflows

build something that runs 24/7 on real hardware

iterate and improve organically

🤝 Contributions
This is a personal learning project, but suggestions, issues, and ideas are welcome.
