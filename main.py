import threading
import schedule, time
from src.signal_engine import scan_and_send_signals
from src.telegram_bot import send_daily_pnl
from telegram_listener import run_bot 

def job():
    scan_and_send_signals()
def start_listener():
    print("📡 Starting Telegram listener...")
    run_bot()   # Starts the Telegram bot commands

def start_worker():
    print("🚀 Starting CryptoChamps signal engine...")
    scan_and_send_signals()  # Runs your signal logic

iif __name__ == "__main__":
    # Start Telegram listener in a separate thread
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.daemon = True  # ✅ allows process to exit cleanly if main stops
    listener_thread.start()

    # Start worker (signals)
    start_worker()
    
# Schedule scans
schedule.every(30).minutes.do(job)

# Daily PnL & fail-safe signal at midnight IST
schedule.every().day.at("23:55").do(send_daily_pnl)

print("🚀 CryptoChampsBot_v3 started...")

while True:
    schedule.run_pending()
    time.sleep(1)
