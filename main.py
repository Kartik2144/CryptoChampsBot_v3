import threading
import schedule, time
from src.signal_engine import scan_and_send_signals
from src.telegram_bot import send_daily_pnl

def job():
    scan_and_send_signals()
def start_listener():
    run_bot()   # This will run the Telegram command listener

if __name__ == "__main__":
    # Start Telegram listener in a background thread
    listener_thread = threading.Thread(target=start_listener)
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
