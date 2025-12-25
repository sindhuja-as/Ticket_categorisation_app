from datetime import datetime
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[2]
CSV_FILE = BASE_DIR / "data" / "predictions" / "ticket_predictions_new.csv"

def generate_ticket_id():
    today = datetime.now().strftime("%y%m%d")

    if CSV_FILE.exists():
        df = pd.read_csv(CSV_FILE)

        # filter today's tickets
        today_tickets = df[df["ticket_id"].str.contains(today, na=False)]

        if not today_tickets.empty:
            # get last sequence number
            last_ticket = today_tickets.iloc[-1]["ticket_id"]
            last_seq = int(last_ticket.split("-")[-1])
            next_seq = last_seq + 1
        else:
            next_seq = 1
    else:
        next_seq = 1

    return f"TCK-{today}-{next_seq:04d}"
