import streamlit as st
from user import login
# Third change in april
 
headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
 

with mainSection:
    dataFile = st.text_input("Enter your Test file name: ")
    Topics = st.text_input("Enter your Model Name: ")
    ModelVersion = st.text_input("Enter your Model Version: ")
    processingClicked = st.button ("Start Processing", key="processing")
    if processingClicked:
        st.balloons() 