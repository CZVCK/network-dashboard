import sqlite3

conn = sqlite3.connect("network_metrics.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS speed_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    ping REAL,
    download REAL,
    upload REAL
);
""")

conn.commit()
conn.close()

print("Database and table created.")
