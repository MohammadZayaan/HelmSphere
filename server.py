from flask import Flask, request, jsonify, render_template
from ultralytics import YOLO
import cv2
import os
import sqlite3
from datetime import datetime

app = Flask(__name__)
model = YOLO("best.pt")  # your YOLO model file

# ---------- Database Setup ----------
DB_NAME = "helm_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS detections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            helmet_detected TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()
# ------------------------------------


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detect', methods=['POST'])
def detect_helmet():
    if 'video' not in request.files:
        return jsonify({"error": "No video uploaded"}), 400

    file = request.files['video']
    file_path = "input.mp4"
    file.save(file_path)

    cap = cv2.VideoCapture(file_path)
    helmet_found = False

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)
        for r in results:
            boxes = r.boxes
            names = r.names
            for box in boxes:
                cls_id = int(box.cls[0])
                label = names[cls_id].lower()
                conf = float(box.conf[0])
                if "helmet" in label and conf > 0.4:
                    helmet_found = True
                    break
            if helmet_found:
                break
        if helmet_found:
            break

    cap.release()
    os.remove(file_path)

    # ---------- Save to Database ----------
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO detections (filename, helmet_detected, timestamp) VALUES (?, ?, ?)",
              (file.filename, "Yes" if helmet_found else "No", datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()
    # --------------------------------------

    return jsonify({"helmet_detected": helmet_found})


if __name__ == '__main__':
    app.run(port=5000)
