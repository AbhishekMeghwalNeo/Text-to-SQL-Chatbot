import sqlite3
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

# Function to retrive query from SQL database
# def read_sql_query(sql, db):
#     conn= sqlite3.connect(db)
#     cur = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.close()

#     return rows

# Function to retrive query from SQL database
def read_sql_query(sql, db):
    """
    Function to read SQL db tables with a query.
    
    :param sql: Description
    :param db: Description
    """
    with sqlite3.connect(db) as conn:
        df = pd.read_sql_query(sql, conn)
    return df

if __name__ == "__main__":
    print(f" Database Name : {os.getenv("database")}")
    database = os.getenv("database")

    sql = """
        SELECT * FROM customers ;
    """

    df = read_sql_query(sql, database)
    
    print(type(df))
    print(df.head(5))