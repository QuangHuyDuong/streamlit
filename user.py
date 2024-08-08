import mysql.connector
import streamlit as st



conn = st.connection(
    type="sql",name="mydb"
)

def login(userName: str, password: str) -> bool:
    if (userName is None):
        return False
    args = [userName, password, 0]
    result_args = execute_sql_query("CheckUser", args)
    return result_args

def execute_sql_query(query, args):
    # try:
    #     print(x)
    # except:
    #     print("An exception occurred")
    return True