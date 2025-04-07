import time

LOG_FILE = "example.log"
ALERT_FILE = "alerts.log"
KEYWORDS = ["Failed password", "error", "sudo", "unauthorized"]

def write_alert(alert_text):
    with open(ALERT_FILE, "a") as alert_log:
        alert_log.write(alert_text + "\n")

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
                    alert = f"[ALERT] {keyword} detected: {line.strip()}"
                    print(alert)
                    write_alert(alert)

if __name__ == "__main__":
    print("Watching log for suspicious activity...")
    watch_log()
