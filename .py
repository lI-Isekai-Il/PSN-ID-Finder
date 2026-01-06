
import requests
import json
import os
from datetime import datetime
import time

# https://github.com/lI-Isekai-Il

def save_line(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

# Function to load previously checked IDs from files
def load_checked_ids():
    checked = set()

    files = [
        "available.json",
        "taken.txt",
        "invalid_pattern.txt",
        "improper.txt",
        "rejected_policy.txt",
        "unknown_errors.log",
    ]

    for file in files:
        if not os.path.exists(file):
            continue

        if file.endswith(".json"):
            try:
                with open(file, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    for entry in data:
                        checked.add(entry["onlineId"])
            except:
                pass
        else:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    checked.add(line.strip().split(" | ")[0])

    return checked


# Function to load all IDs from IDs.txt
def load_ids(ids_file='IDs.txt'):
    ids = []
    if os.path.exists(ids_file):
        with open(ids_file, 'r', encoding='utf-8') as f:
            for line in f:
                ids.append(line.strip())
    return ids

# Function to save available ID to JSON
def save_available(online_id, available_file='available.json'):
    entry = {
        "onlineId": online_id,
        "date": datetime.utcnow().isoformat() + 'Z'
    }

    data = []
    if os.path.exists(available_file):
        try:
            with open(available_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            pass

    if online_id not in {e["onlineId"] for e in data}:
        data.append(entry)

    with open(available_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)



# Function to save not available ID to txt
def save_not_available(online_id, not_available_file='notavailable.txt'):
    with open(not_available_file, 'a', encoding='utf-8') as f:
        f.write(online_id + '\n')

# Main function
def check_online_ids():
    url = "https://accounts.api.playstation.com/api/v1/accounts/onlineIds"
    headers = {
        "Host": "accounts.api.playstation.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
        "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
        "Content-Type": "application/json; charset=UTF-8",
        "sec-ch-ua-mobile": "?0",
        "Accept": "*/*",
        "Origin": "https://id.sonyentertainmentnetwork.com",
        "Sec-Fetch-Site": "cross-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://id.sonyentertainmentnetwork.com/",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    checked_ids = load_checked_ids()
    all_ids = load_ids()
    
    for online_id in all_ids:
        if online_id in checked_ids:
            continue  # Skip already checked
        
        payload = {
            "onlineId": online_id,
            "reserveIfAvailable": False
        }
        
        try:
            response = requests.post(url, json=payload, headers=headers)
        except requests.RequestException as e:
            save_line("unknown_errors.log", f"{online_id} | request failed: {e}")
            print(f"[REQUEST FAILED] {online_id}")
            continue
        
        status = response.status_code

        if status in (200, 201):
            save_available(online_id)
            print(f"[AVAILABLE] {online_id} ({status})")

        elif status == 400:
            try:
                data = response.json()
            except:
                save_line("unknown_errors.log", f"{online_id} | invalid json")
                print(f"[400 UNKNOWN] {online_id}")
                continue

            header_code = response.headers.get("X-ErrorCode", "")
            body_code = data[0].get("code") if isinstance(data, list) else ""

            if header_code == "accounts:3101":
                save_line("taken.txt", online_id)
                print(f"[TAKEN] {online_id}")

            elif body_code == "1100":
                save_line("invalid_pattern.txt", online_id)
                print(f"[INVALID PATTERN] {online_id}")

            elif body_code == "3208":
                save_line("improper.txt", online_id)
                print(f"[IMPROPER] {online_id}")

            else:
                save_line("unknown_errors.log", f"{online_id} | {data}")
                print(f"[400 UNKNOWN] {online_id}")

        elif status == 406:
            save_line("rejected_policy.txt", online_id)
            print(f"[REJECTED POLICY] {online_id}")

        elif status == 429:
            print("[RATE LIMIT] sleeping")
            time.sleep(5)
            continue

        else:
            save_line("unknown_errors.log", f"{online_id} | HTTP {status}")
            print(f"[UNHANDLED {status}] {online_id}")

        # Add to checked after processing
        checked_ids.add(online_id)

if __name__ == "__main__":
    check_online_ids()
