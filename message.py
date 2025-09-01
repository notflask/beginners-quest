import requests
import bcrypt
import string
from bs4 import BeautifulSoup
from time import sleep

BASE_URL = "https://msg-web.2024-bq.ctfcompetition.com/"
FLAG_MAX_LEN = 40
CHARSET = string.ascii_uppercase + string.digits + "_{}"

SAVE_FILE = "flag.txt"

def get_server_hash(salt: bytes, retries=3) -> bytes:
    for attempt in range(retries):
        try:
            resp = requests.get(BASE_URL, params={"salt": salt.decode()}, timeout=10)
            resp.raise_for_status()

            soup = BeautifulSoup(resp.text, "html.parser")

            for tag in soup.find_all("pre"):
                text = tag.get_text().strip()

                if text.startswith("$2"):
                    return text.encode()
                
        except Exception as e:
            print(f"[!] attempt {attempt+1} failed: {e}")
        sleep(2)

    raise ValueError("hash not found in response after retries")

def save_progress(flag: bytes):
    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        f.write(flag.decode(errors="ignore"))

def load_progress() -> bytes:
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return f.read().encode()
    except FileNotFoundError:
        return b""

def bruteforce_flag():
    known = load_progress()
    charset = CHARSET.encode()

    print(f"[] resuming from: {known.decode(errors='ignore')}")

    for i in range(len(known), FLAG_MAX_LEN):
        print(f"\n[] brute-forcing byte {i + 1}...")
        salt = b"A" * (71 - len(known))
        real_hash = get_server_hash(salt)

        found = False

        for c in charset:

            guess = known + bytes([c])

            if bcrypt.checkpw((salt + guess)[:72], real_hash):
                known += bytes([c])
                save_progress(known)
                print(f"[✓] found: {chr(c)} → {known.decode(errors='ignore')}")
                found = True
                break

        if not found:
            print("[!] no match found ")
            break

    print(f"\n[] flag: {known.decode(errors='ignore')}")

if __name__ == "__main__":
    bruteforce_flag()
