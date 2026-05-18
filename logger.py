import csv
import os
from datetime import datetime
from config import CSV_FILE

def init_log():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "timestamp",
                "server",
                "latency_ms",
                "download_mbps",
                "upload_mbps"
            ])

def log_results(latency_dict, speed_dict):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        timestamp = datetime.now().isoformat()

        for server, latency in latency_dict.items():
            writer.writerow([
                timestamp,
                server,
                latency,
                speed_dict["download"],
                speed_dict["upload"]
            ])