#!/usr/bin/env python3
import subprocess
import json
import sqlite3
import time
import logging
from pathlib import Path

# ====== CONFIG ======
DB_PATH = "/home/czvck/Projects/network-dashboard/db/network_metrics.db"
LOG_PATH = Path("/home/czvck/Projects/network-dashboard/logs/speedtest.log")
RETRIES = 3
RETRY_DELAY = 20  # seconds
SPEEDTEST_CMD = ["/usr/bin/speedtest", "--format=json"]
# ====================

# Ensure log directory exists
LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    filename=str(LOG_PATH),
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def run_speedtest_once():
    """
    Run Ookla speedtest CLI once and return (ping_ms, download_mbps, upload_mbps).
    Raises subprocess.CalledProcessError or ValueError on failure.
    """
    result = subprocess.run(
        SPEEDTEST_CMD,
        capture_output=True,
        text=True,
        timeout=120
    )

    if result.returncode != 0:
        raise subprocess.CalledProcessError(
            result.returncode, result.args, output=result.stdout, stderr=result.stderr
        )

    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse speedtest JSON: {e}\nOutput: {result.stdout}")

    # Adjust keys if needed based on actual CLI output
    ping_ms = data["ping"]["latency"]
    download_mbps = data["download"]["bandwidth"] * 8 / 1_000_000  # bytes/s → Mbps
    upload_mbps = data["upload"]["bandwidth"] * 8 / 1_000_000

    return ping_ms, download_mbps, upload_mbps


def run_speedtest_with_retries(retries=RETRIES, delay=RETRY_DELAY):
    """
    Retry wrapper around run_speedtest_once.
    """
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"Speedtest attempt {attempt}/{retries}")
            ping, down, up = run_speedtest_once()
            logging.info(
                f"Speedtest success: ping={ping:.2f} ms, "
                f"down={down:.2f} Mbps, up={up:.2f} Mbps"
            )
            return ping, down, up
        except Exception as e:
            logging.warning(f"Speedtest attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(delay)
            else:
                logging.error(f"Speedtest failed after {retries} attempts: {e}")
                raise


def init_db():
    """
    Ensure the table exists.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS speedtests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            ping_ms REAL,
            download_mbps REAL,
            upload_mbps REAL
        )
        """
    )
    conn.commit()
    conn.close()


def save_result(ping, download, upload):
    """
    Insert a row into the DB.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO speedtests (ping_ms, download_mbps, upload_mbps)
        VALUES (?, ?, ?)
        """,
        (ping, download, upload),
    )
    conn.commit()
    conn.close()
    logging.info("Saved result to database")


def main():
    logging.info("=== Speedtest run started ===")
    init_db()
    ping, download, upload = run_speedtest_with_retries()
    save_result(ping, download, upload)
    logging.info("=== Speedtest run completed ===")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Also print so cron.log captures it
        print(f"Fatal error in collect_speedtest.py: {e}")
        logging.exception("Fatal error in collect_speedtest.py")
        raise
