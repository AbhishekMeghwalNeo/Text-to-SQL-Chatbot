import sqlite3
import pandas as pd
from src.config import Config

cfg = Config()

def read_sql_query(db, sql):

    with sqlite3.connect(db) as conn:
        df = pd.read_sql_query(sql, conn)

    return df

if __name__ == "__main__":

    database = cfg.database_path
    sql = """
        SELECT * FROM customers ;
    """

    df = read_sql_query(database, sql)

    print(df)

