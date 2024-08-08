import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import datetime
import numpy as np
import pandas as pd



if "patient_id" not in st.session_state:
    st.session_state.patient_id = None
patient_id = st.session_state.patient_id   
if patient_id :
    st.query_params["id"] = patient_id 




@st.dialog("Cast your vote")
def vote(item):
    st.write(f"Why is {item} your favorite?")
    reason = st.text_input("Because...")
    file1 = st.file_uploader(label="Choose file 1 ....")
    if st.button("Submit"):
        obj =  { "reason": reason , "file1" : file1}
        st.write(obj)



if st.button("Create new "):
    vote("A")
# if st.button("Process "):
#     process()






conn = st.connection(
    type="sql",name="mydb"
)
df = conn.query(
    "select * from league "
    )
builder = GridOptionsBuilder.from_dataframe(df)
builder.configure_pagination(enabled=True,paginationPageSize=20)
builder.configure_selection(selection_mode='multiple', use_checkbox=True)
for column in df.columns :
    if isinstance(df[column], datetime.datetime):
        df[column] = pd.to_datetime(df[column])
    if df[column].dtype == 'object':
        builder.configure_column(column, filter=True)
grid_options = builder.build()
# Display AgGrid
return_value = AgGrid(df, gridOptions=grid_options)

if return_value['selected_rows'] is not None:
    ids = [id + 110 for id in return_value['selected_rows']["id"]] 

    df2 = conn.query(
    "select * from team where id IN :id",
    params={"id": ids},
    )
    t2 = AgGrid(df2)

