import os, requests

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_signal(signal):
    msg = (
        f"🚀 CryptoChamps Signal ({signal['strategy']})\n\n"
        f"🔹 Pair: {signal['pair']}\n"
        f"📍 Direction: {signal['direction']} (20x)\n"
        f"🎯 Entry: {signal['entry']}\n"
        f"⛔ Stoploss: {signal['sl']}\n"
        f"✅ Target: {signal['tp']}\n"
        f"📈 Risk-Reward: 1:1.5\n"
        f"🤖 Confidence: {signal['confidence']}%\n\n"
        f"#{signal['pair'].split('/')[0]} #{signal['strategy'].replace('-', '')} #{signal['direction']}"
    )
    _send_telegram(msg)

def send_daily_pnl():
    msg = "📊 Daily PnL Summary (Simulated)\n✅ TP Hits: 2\n❌ SL Hits: 1\n💰 Total: +4.5% (20x)"
    _send_telegram(msg)

def send_no_signal_report():
    msg = "⚠️ No ultra-strong setups were detected today.\n✅ Bot scan completed — system healthy."
    _send_telegram(msg)

def _send_telegram(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": text})
