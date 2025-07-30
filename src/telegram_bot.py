import os
import telebot
from datetime import datetime
from src.pnl_tracker import get_daily_pnl_summary  # Make sure this function exists

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# ✅ Function to send real trading signals
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
    bot.send_message(CHAT_ID, msg)

# ✅ Function to send daily PnL summary
def send_daily_pnl():
    summary = get_daily_pnl_summary()
    bot.send_message(CHAT_ID, f"📊 *Daily PnL Summary (IST)*\n\n{summary}", parse_mode="Markdown")

# ✅ /testsignal command – manual trigger
@bot.message_handler(commands=['testsignal'])
def handle_testsignal(message):
    test_signal = {
        'strategy': 'Breakout',
        'pair': 'BTC/USDT',
        'direction': 'LONG',
        'entry': '65000',
        'sl': '64500',
        'tp': '66000',
        'confidence': 92
    }
    send_signal(test_signal)
    bot.reply_to(message, "✅ Test signal sent!")

# ✅ /pnl command – manual PnL summary
@bot.message_handler(commands=['pnl'])
def handle_pnl(message):
    summary = get_daily_pnl_summary()
    bot.reply_to(message, f"📊 *PnL Report (IST)*\n\n{summary}", parse_mode="Markdown")

# ✅ Optional: /start welcome
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🚀 CryptoChamps Bot is live!\nUse /testsignal to test & /pnl for today’s PnL.")

def run_telegram_bot():
    print("✅ Telegram Bot is running...")
    bot.infinity_polling()
