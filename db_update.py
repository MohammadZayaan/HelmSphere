import sqlite3
from datetime import datetime, timedelta

DB = "helm_data.db"   # change if your DB has a different name

conn = sqlite3.connect(DB)
c = conn.cursor()

# Two sample timestamps (now and 1 minute before)
t1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t2 = (datetime.now() - timedelta(minutes=1)).strftime("%Y-%m-%d %H:%M:%S")

rows = [
    ("demo_nohelmet_1.mp4", "No", t2),
    ("demo_nohelmet_2.mp4", "No", t1),
]

c.executemany("INSERT INTO detections (filename, helmet_detected, timestamp) VALUES (?, ?, ?)", rows)
conn.commit()
conn.close()
print("Inserted 2 'No' records into", DB)
