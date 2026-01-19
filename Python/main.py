import requests

def fetch_users(url):
    try:
        response = requests.get(url, timeout=5)
        return response
    except requests.RequestException as e:
        raise RuntimeError(f"API error: {e}")

def is_valid_user(user):
    return all(field in user and user[field] for field in ("id", "name", "email"))

def validate_response(response):
    if response.status_code != 200:
        raise ValueError("Invalid status code")

    if "application/json" not in response.headers.get("Content-Type", ""):
        raise ValueError("Invalid content type")

    data = response.json()

    if not isinstance(data, list):
        raise ValueError("Invalid JSON structure")

    valid_users = [u for u in data if is_valid_user(u)]
    return valid_users

import json
import csv

def save_to_json(filename, data):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def save_to_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "email"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

