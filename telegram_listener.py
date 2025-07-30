# telegram_listener.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from src.telegram_bot import send_signal
from src.pnl_tracker import get_daily_pnl_summary
from src.telegram_bot import bot

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=f"https://{os.getenv('RAILWAY_URL')}/{TOKEN}")
    return "Webhook set", 200
# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ CryptoChampsBot is online and ready!")

# /testsignal command
async def testsignal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dummy_signal = {
        "pair": "BTC/USDT",
        "direction": "LONG",
        "entry": 29000,
        "sl": 28500,
        "tp": 29500,
        "strategy": "Breakout",
        "confidence": 95
    }
    # Instead of sending real signal to all, we just reply
    msg = f"🚀 TEST SIGNAL\n\n🔹 Pair: {dummy_signal['pair']}\n📍 Direction: {dummy_signal['direction']} (20x)\n🎯 Entry: {dummy_signal['entry']}\n⛔ SL: {dummy_signal['sl']}\n✅ TP: {dummy_signal['tp']}\n📈 Strategy: {dummy_signal['strategy']}\n🤖 Confidence: {dummy_signal['confidence']}%"
    await update.message.reply_text(msg)

# /pnl command
async def pnl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    summary = get_daily_pnl_summary()
    await update.message.reply_text(f"📊 Daily PnL Summary:\n\n{summary}")

def run_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    print("✅ Telegram bot listener running...")
    bot.delete_webhook()   # 🚨 Important to avoid 409 error
    bot.infinity_polling()   # or updater.start_polling() depending on your library
    
    # Register commands
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("testsignal", testsignal))
    app.add_handler(CommandHandler("pnl", pnl))

    app.run_polling()

if __name__ == "__main__":
    run_bot()
