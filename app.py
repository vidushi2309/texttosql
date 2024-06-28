from dotenv import load_dotenv
load_dotenv() ## load all enviornment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

##Configure our api key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# function to load google gemini model and provide sql query as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to retrive query from the sql database
def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define your Prompt

prompt=[
    """
    You are an Expert in converting English questions to SQL query!
    The SQL Database has the name EMPLOYEE and has the following columns- NAME, DESIGNATION,RATING and SALARY \n\nFor example,
    \nExample 1 - How many entries of records are present the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the Employees with designation of Engineer?,
    the SQL command will be something like this SELECT * FROM EMPLOYEE where DESIGNATION="Engineer";
    also the sql code should not have ''' in beginning or end and sql word in output






"""
]

## Streamlit App

st.set_page_config(page_title="A ChatBOT to retrieve data")
st.header("Vidushi's App to Retrieve SQL data")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask Anything")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"EMPLOYEE.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)

        
