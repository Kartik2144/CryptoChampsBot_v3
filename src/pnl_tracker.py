from datetime import datetime
import pytz

# ✅ In-memory storage for signals and results
signals_log = []

# ✅ Add a signal result (bot will log TP/SL hits here)
def log_trade(pair, direction, entry, tp, sl, outcome, pnl_percent):
    """
    outcome: 'TP' or 'SL'
    pnl_percent: % gain/loss (considering 20x leverage)
    """
    signals_log.append({
        'pair': pair,
        'direction': direction,
        'entry': entry,
        'tp': tp,
        'sl': sl,
        'outcome': outcome,
        'pnl_percent': pnl_percent,
        'timestamp': datetime.now(pytz.timezone("Asia/Kolkata"))
    })

# ✅ Get today's summary (used by /pnl and end-of-day report)
def get_daily_pnl_summary():
    ist = pytz.timezone("Asia/Kolkata")
    today = datetime.now(ist).date()

    today_trades = [t for t in signals_log if t['timestamp'].date() == today]

    if not today_trades:
        return "📭 No trades logged for today yet."

    tp_hits = sum(1 for t in today_trades if t['outcome'] == 'TP')
    sl_hits = sum(1 for t in today_trades if t['outcome'] == 'SL')
    total_pnl = sum(t['pnl_percent'] for t in today_trades)

    report = (
        f"✅ TP Hits: {tp_hits}\n"
        f"❌ SL Hits: {sl_hits}\n"
        f"📊 Net PnL: {total_pnl:.2f}% (20x leverage)"
    )

    return report

# ✅ Optional: reset log at midnight if needed
def reset_daily_pnl():
    signals_log.clear()
