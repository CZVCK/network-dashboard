
                                                                              



📡 Network Dashboard
<p align="center">Raspberry Pi Internet Monitoring Pipeline</p>
<p align="center">
<img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" />
<img src="https://img.shields.io/badge/Raspberry%20Pi-Linux-red?logo=raspberrypi" />
<img src="https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite" />
<img src="https://img.shields.io/badge/Cron-Automation-green" />
<img src="https://img.shields.io/badge/Status-Active-success" />
</p>

<p align="center"><strong>A lightweight, reliable, fully automated network monitoring system running on a Raspberry Pi.</strong></p>

<p align="center">
<em>Built for learning. Designed to evolve.</em>
</p>

It started as a simple script and evolved into a modular, production‑style pipeline — a place to experiment, learn, and build real‑world automation skills.

🚀 Features
Automated speed tests using the official Ookla CLI

  -Robust retry logic to handle network hiccups

  -Structured logging for debugging and reliability

  -SQLite database storage for long‑term trend analysis

  -Cron‑based scheduling for hands‑off operation

  -Clean, modular Python scripts

  -Git + GitHub integration for version control and development

🧱 Project Structure
  -Code<pre>
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
</pre>  


⚙️ How It Works
  1. Cron triggers the collector script
  Runs at :05 and :35 each hour (configurable).

  2. The script runs the Ookla CLI
  -Code<pre>
speedtest --format=json
3. JSON output is parsed
Ping, download, upload, and timestamps are extracted.

4. Results are written to SQLite
A simple, durable schema:

  -Code<pre>
speedtests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    ping REAL,
    download REAL,
    upload REAL
)
</pre>

5. Logs capture every run
  -Useful for debugging cron, network issues, or CLI failures.

🛠️ Setup Instructions
Install the Ookla CLI
  -Code<pre>
sudo apt update
sudo apt install curl -y
curl -s https://install.speedtest.net/app/cli/install.deb.sh | sudo bash
sudo apt install speedtest
</pre>  
Clone the repo
  -Code<pre>
git clone git@github.com:CZVCK/network-dashboard.git
cd network-dashboard
</pre>  
Run the collector manually
  -Code<pre>
python3 scripts/collect_speedtest.py
</pre>

Set up cron
Add this entry (example):

  -Code<pre>
5,35 * * * * sleep 20 && /usr/bin/python3 /home/pi/Projects/network-dashboard/scripts/collect_speedtest.py >> /home/pi/cron.log 2>&1</pre>
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

  -learn Python in a practical context

  -explore automation and reliability engineering

  -practice Git/GitHub workflows

  -build something that runs 24/7 on real hardware

  -iterate and improve organically

🤝 Contributions
  This is a personal learning project, but suggestions, issues, and ideas are welcome.

