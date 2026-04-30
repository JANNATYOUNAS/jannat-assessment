import json
import os

STORAGE_FILE = "data.json"

def save_data(data):
    """Save data to JSON file, avoiding duplicates."""
    existing = load_data()
    existing_ids = {item["id"] for item in existing}

    new_entries = [item for item in data if item["id"] not in existing_ids]
    combined = existing + new_entries

    try:
        with open(STORAGE_FILE, "w") as f:
            json.dump(combined, f, indent=4)
        return len(new_entries)
    except Exception as e:
        print(f"Error saving data: {e}")
        return 0

def load_data():
    """Load data from JSON file."""
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []