from src.config import Config
import sqlite3
import pandas as pd
# from pathlib import Path

cfg = Config()

conn = sqlite3.connect(cfg.database_path)

for csv_file in cfg.raw_data_path.glob("*.csv"):
    table_name = csv_file.stem.lower()

    print(f"Processing file : {table_name}")

    df = pd.read_csv(csv_file)

    # print(df.head())
    df.to_sql(
        name = table_name,
        con= conn,
        if_exists= "replace",
        index= False,
        
    )
    # break

if __name__ == "__main__":
    # print(cfg.raw_data_path)
    ...



