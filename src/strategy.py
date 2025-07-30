import random
from src.pnl_tracker import log_trade

# ✅ Example: ultra-strong signal generator
def generate_signals():
    """
    Generate 2 ultra-strong signals per day
    Each signal has: pair, direction, entry, sl, tp, strategy, confidence
    """

    pairs = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT", "BNB/USDT"]
    strategies = ["Breakout", "Reversal", "Trend-following"]

    signals = []
    for _ in range(2):
        pair = random.choice(pairs)
        strategy = random.choice(strategies)
        direction = random.choice(["LONG", "SHORT"])

        entry = round(random.uniform(100, 200), 2)
        tp = entry * (1.01 if direction == "LONG" else 0.99)
        sl = entry * (0.99 if direction == "LONG" else 1.01)

        confidence = random.randint(85, 98)  # ultra-strong

        signals.append({
            "pair": pair,
            "direction": direction,
            "entry": entry,
            "tp": tp,
            "sl": sl,
            "strategy": strategy,
            "confidence": confidence
        })

    return signals


# ✅ This simulates TP/SL outcomes and logs them
def evaluate_signals(signals):
    """
    Pretend to evaluate signals (in real bot this would be price checks)
    Log trades when TP or SL is hit.
    """

    for signal in signals:
        # For now randomly assign TP/SL
        outcome = random.choice(["TP", "SL"])

        # calculate pnl% (with 20x leverage)
        raw_move = abs(signal["tp"] - signal["entry"]) / signal["entry"] * 100
        pnl_percent = raw_move * 20 if outcome == "TP" else -raw_move * 20

        # ✅ log the trade for pnl_tracker
        log_trade(
            pair=signal["pair"],
            direction=signal["direction"],
            entry=signal["entry"],
            tp=signal["tp"],
            sl=signal["sl"],
            outcome=outcome,
            pnl_percent=pnl_percent
        )

        print(f"[LOGGED] {signal['pair']} {signal['direction']} → {outcome} ({pnl_percent:.2f}%)")
