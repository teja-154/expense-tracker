import json
import os

FILE = "expenses.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_data(expense):
    with open(FILE, "w") as f:
        json.dump(expense, f, indent=4)
