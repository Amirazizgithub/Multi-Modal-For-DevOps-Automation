import json
import os
from datetime import datetime

LOG_FILE = "interactions.log"  # Or "interactions.json"


def log_interaction(user_id: str, message: str, module: str, reply: str, status: str):
    """Logs chatbot interactions."""
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "user_id": user_id,
        "message": message,
        "module": module,
        "reply": reply,
        "status": status,
    }
    # Append to a JSON lines file for easy parsing
    with open(LOG_FILE, "a") as f:
        f.write(json.dumps(log_entry) + "\n")


def get_logs():
    """Reads all logs from the file."""
    if not os.path.exists(LOG_FILE):
        return []
    logs = []
    with open(LOG_FILE, "r") as f:
        for line in f:
            logs.append(json.loads(line))
    return logs
