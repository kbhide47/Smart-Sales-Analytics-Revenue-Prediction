import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

csv_path = BASE_DIR / "data" / "cleaned" / "cleaned_superstore.csv"
db_path = BASE_DIR / "superstore.db"

df = pd.read_csv(csv_path)

conn = sqlite3.connect(db_path)

df.to_sql(
    "superstore",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Database created successfully!")