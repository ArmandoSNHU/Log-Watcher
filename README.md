# 🔍 Log Watcher

A simple Python-based log watcher that monitors a specified log file for suspicious activity and security-related events in real-time.

## ✅ Features

- Watches a log file line-by-line
- Triggers alerts on keywords like:
  - `Failed password`
  - `error`
  - `sudo`
  - `unauthorized`
- Displays alerts in the terminal
- **NEW:** Writes alerts to `alerts.log` for later review

## 🛠 Usage

1. Make sure `log_watcher.py` and `example.log` are in the same directory.
2. Run the script:
   ```bash
   python3 log_watcher.py
