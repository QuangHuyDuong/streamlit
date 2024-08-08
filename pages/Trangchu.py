import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder
from datetime import datetime
from faker import Faker
import random
from sqlalchemy import text

query = text('SELECT * FROM `my table`')
fake = Faker()

# if 'loggedIn' not in st.session_state:
#     st.switch_page("App.py")  
if "patient_id" not in st.session_state:
    st.session_state.patient_id = None


conn = st.connection(
    type="sql",name="mydb",autocommit=True
)
with conn.session as s:
    for i in range(20):
        s.execute(
            text("insert into `doctors` ( `name`, `phone_number`, `contact_info`, `created_at`, `updated_at`) values(:name,:phone,:address,CURRENT_TIMESTAMP,CURRENT_TIMESTAMP)" ),
            params= dict(
                name = fake.name(),
                phone = fake.phone_number(),
                address =fake.address()
                )
            
        )

prompt =  st.text_input(label="Input id")
if prompt:
    df = conn.query(
    "select * from league " 
    )

    builder = GridOptionsBuilder.from_dataframe(df)
    builder.configure_pagination(enabled=True,paginationPageSize=20)
    builder.configure_selection(selection_mode='single', use_checkbox=False)
    for column in df.columns :
        if isinstance(df[column], datetime.datetime):
            df[column] = pd.to_datetime(df[column])
        if df[column].dtype == 'object':
            builder.configure_column(column, filter=True)
    grid_options = builder.build()
# Display AgGrid
    return_value = AgGrid(df, gridOptions=grid_options)
    if return_value['selected_rows'] is not None:
        st.session_state.patient_id=1
        st.switch_page("pages/Main.py")
    else:
        st.write("No row selected")


