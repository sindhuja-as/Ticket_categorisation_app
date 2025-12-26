import pandas as pd
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "data" / "predictions"
DB_PATH.mkdir(exist_ok=True)

CSV_FILE = DB_PATH / "ticket_predictions_new.csv"

def store_prediction(ticket_data: dict):
    
    record = {
        "ticket_id": ticket_data["ticket_id"],
        "complaint_text": ticket_data["complaint_text"],
        "predicted_category": ticket_data["predicted_category"],
        "confidence": str(ticket_data["confidence"]) + ' %',
        "routed_to": ticket_data["routed_to"],
        "status":ticket_data['status'],
        "created_at": ticket_data['created_at']
    }

    df = pd.DataFrame([record])

    if CSV_FILE.exists():
        df.to_csv(CSV_FILE, mode="a", header=False, index=False)
    else:
        df.to_csv(CSV_FILE, index=False)
