import schedule, time
from src.signal_engine import scan_and_send_signals
from src.telegram_bot import send_daily_pnl

def job():
    scan_and_send_signals()

# Schedule scans
schedule.every(30).minutes.do(job)

# Daily PnL & fail-safe signal at midnight IST
schedule.every().day.at("23:55").do(send_daily_pnl)
schedule.every().day.at("23:56").do(send_no_signal_report)

print("🚀 CryptoChampsBot_v3 started...")

while True:
    schedule.run_pending()
    time.sleep(1)
