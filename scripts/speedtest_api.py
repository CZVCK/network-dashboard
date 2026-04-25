from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)
DB_PATH = os.path.expanduser('~/speedtests.db')  # adjust path if needed

@app.route('/api/speedtest')
def speedtest():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''
        SELECT timestamp, ping_ms, download_mbps, upload_mbps
        FROM speedtests
        ORDER BY timestamp DESC
        LIMIT 50
    ''')
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    rows.reverse()  # chronological order for charting
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)