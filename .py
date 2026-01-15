import requests
import json
import os
from datetime import datetime
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil
from colorama import init, Fore

# https://github.com/lI-Isekai-Il

maxwork = 2

init(autoreset=True)

def print_emperor_banner():
    terminal_width = shutil.get_terminal_size().columns
    border = "=" * terminal_width

    lines = [
        "The Immortal Emperor The Manipulator of Humans",
        "The one and The only Vampire lI_Isekai_Il | lI-Isekai-Il.",
        "The Emperor of kings"
    ]

    print(Fore.YELLOW + border)
    for line in lines:
        print(Fore.YELLOW + line.center(terminal_width))
    print(Fore.YELLOW + border)

print_emperor_banner()

# ----------------- Utils -----------------

def save_line(filename, text):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text + "\n")

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

def load_ids(ids_file='IDs.txt'):
    ids = []
    if os.path.exists(ids_file):
        with open(ids_file, 'r', encoding='utf-8') as f:
            for line in f:
                ids.append(line.strip())
    return ids

# ----------------- Save Functions -----------------

FOUNDER_TEXT = (
    "The Immortal Emperor The Manipulator of Humans "
    "The Emperor of kings "
    "The one and The only Vampire lI_Isekai_Il | lI-Isekai-Il."
)

def save_available(online_id, available_file='available.json'):
    entry = {
        "onlineId": online_id,
        "date": datetime.utcnow().isoformat() + 'Z',
        "founder": FOUNDER_TEXT
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

def save_not_available(online_id, not_available_file='notavailable.txt'):
    with open(not_available_file, 'a', encoding='utf-8') as f:
        f.write(online_id + '\n')

# ----------------- Worker -----------------

def check_single_id(online_id, checked_ids, url, headers):
    if online_id in checked_ids:
        return

    payload = {
        "onlineId": online_id,
        "reserveIfAvailable": False
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
    except requests.RequestException as e:
        save_line("unknown_errors.log", f"{online_id} | request failed: {e}")
        print(f"[REQUEST FAILED]       Check https://github.com/lI-Isekai-Il               {online_id}")
        return

    status = response.status_code

    if status in (200, 201):
        save_available(online_id)
        print(f"[AVAILABLE]       Check https://github.com/lI-Isekai-Il               {online_id} ({status})")

    elif status == 400:
        try:
            data = response.json()
        except:
            save_line("unknown_errors.log", f"{online_id} | invalid json")
            print(f"[400 UNKNOWN]       Check https://github.com/lI-Isekai-Il               {online_id}")
            return

        header_code = response.headers.get("X-ErrorCode", "")
        body_code = data[0].get("code") if isinstance(data, list) else ""

        if header_code == "accounts:3101":
            save_line("taken.txt", online_id)
            print(f"[TAKEN]       Check https://github.com/lI-Isekai-Il               {online_id}")

        elif body_code == "1100":
            save_line("invalid_pattern.txt", online_id)
            print(f"[INVALID PATTERN]       Check https://github.com/lI-Isekai-Il               {online_id}")

        elif body_code == "3208":
            save_line("improper.txt", online_id)
            print(f"[IMPROPER]       Check https://github.com/lI-Isekai-Il               {online_id}")

        else:
            save_line("unknown_errors.log", f"{online_id} | {data}")
            print(f"[400 UNKNOWN]       Check https://github.com/lI-Isekai-Il               {online_id}")

    elif status == 406:
        save_line("rejected_policy.txt", online_id)
        print(f"[REJECTED POLICY]       Check https://github.com/lI-Isekai-Il               {online_id}")

    elif status == 429:
        print("[RATE LIMIT] sleeping")
        time.sleep(5)

    else:
        save_line("unknown_errors.log", f"{online_id} | HTTP {status}")
        print(f"[UNHANDLED {status}]       Check https://github.com/lI-Isekai-Il               {online_id}")

    checked_ids.add(online_id)

# ----------------- Main -----------------

def check_online_ids():
    url = "https://accounts.api.playstation.com/api/v1/accounts/onlineIds"

    headers = {
        "Host": "accounts.api.playstation.com",
        "Connection": "keep-alive",
        "sec-ch-ua-platform": "\"Windows\"",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "*/*",
        "Origin": "https://id.sonyentertainmentnetwork.com",
        "Referer": "https://id.sonyentertainmentnetwork.com/",
        "Accept-Language": "en-US,en;q=0.9"
    }

    checked_ids = load_checked_ids()
    all_ids = load_ids()

    with ThreadPoolExecutor(max_workers=maxwork) as executor:
        futures = [
            executor.submit(check_single_id, online_id, checked_ids, url, headers)
            for online_id in all_ids
        ]

        for _ in as_completed(futures):
            pass

if __name__ == "__main__":
    check_online_ids()
