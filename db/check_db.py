import sqlite3

conn = sqlite3.connect("network_metrics.db")
cursor = conn.cursor()

rows = cursor.execute("SELECT * FROM speedtests LIMIT 10").fetchall()

print("Rows in database:")
for row in rows:
    print(row)

conn.close()
