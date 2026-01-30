# import streamlit as st
# from google import genai

from openai import AzureOpenAI
import os
from dotenv import load_dotenv
import sqlite3

load_dotenv()

client = AzureOpenAI(
    api_key= os.getenv("AZURE_OPENAI_KEY"),
    api_version= "2025-01-01-preview",
    azure_endpoint= "https://amiparmar-test-resource.cognitiveservices.azure.com/"
)

# Function to load Azure model and provide sql query as response
def get_llm_response(question, prompt):

    response= client.chat.completions.create(
        model= "gpt-4o",
        messages= [
            {
                "role" : "system",
                "content" : prompt
            },
            {
                "role" : "user",
                "content" : question
            }
        ]
    )

    output_text = response.choices[0].message.content

    return output_text

# Function to retrive query from SQL database
def read_sql_query(sql, db):
    conn= sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows= cur.fetchall()
    conn.close()

    return rows

## Define Your Prompt
prompt =   """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS 
    Some Examples for Text to SQL conversion
    Example 1 - How many entries of records are present?
    the SQL command will be : SELECT COUNT(*) FROM STUDENT ;
    Example 2 - Tell me all the students studying in Data Science class?
    the SQL command will be : SELECT * FROM STUDENT where CLASS="Data Science"; 
    
    OUTPUT Format :
    1) The sql code should not have ``` in beginning or end and sql word in output
    2) OUTPUT should be strictly a SQL query.
    """

# Text 2 SQL

question = "Find out unique classes in the table"

print(question)

output_text = get_llm_response(question, prompt)

print(output_text)

rows = read_sql_query(sql= output_text, db= "student.db")
print(rows)


