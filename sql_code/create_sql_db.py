import sqlite3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# -------- CONFIG --------
CSV_FOLDER = Path("data")          # folder containing CSV files
DB_NAME = os.getenv("database")         # output SQLite database
# ------------------------

# Connect to SQLite database
conn = sqlite3.connect(DB_NAME)

for csv_file in CSV_FOLDER.glob("*.csv"):
    table_name = csv_file.stem.lower()  # file name without .csv

    print(f"Processing {csv_file.name} → table '{table_name}'")

    # Read CSV
    df = pd.read_csv(csv_file)

    # Write to SQLite
    df.to_sql(
        table_name,
        conn,
        if_exists="replace",   # replace if table already exists
        index=False
    )

conn.close()

print("\n✅ Database created successfully!")
print(f"📦 SQLite DB: {DB_NAME}")


