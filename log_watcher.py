import time

LOG_FILE = "example.log"  # Replace with actual log path, e.g., /var/log/auth.log
KEYWORDS = ["Failed password", "error", "sudo", "unauthorized"]

def watch_log():
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)  # Jump to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue
            for keyword in KEYWORDS:
                if keyword.lower() in line.lower():
                    print(f"[ALERT] {keyword} detected: {line.strip()}")

if __name__ == "__main__":
    print("Watching log for suspicious activity...")
    watch_log()
