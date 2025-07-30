from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from src.telegram_bot import send_signal
from src.pnl_tracker import get_daily_pnl_summary

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ CryptoChampsBot is online!")

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
    msg = send_signal(dummy_signal, dry_run=True)
    await update.message.reply_text(msg)

async def pnl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    summary = get_daily_pnl_summary()
    await update.message.reply_text(summary)

def run_telegram_bot():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("testsignal", testsignal))
    app.add_handler(CommandHandler("pnl", pnl))

    app.run_polling()

if __name__ == "__main__":
    run_telegram_bot()
