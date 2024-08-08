import streamlit as st
from user import login



headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
 


def Register_Clicked():
    st.switch_page("pages/Register.py")
def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    
def show_logout_page():
    loginSection.empty()
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
    
def LoggedIn_Clicked(userName, password):
    if login(userName, password):
        st.session_state['loggedIn'] = True
    else:
        st.session_state['loggedIn'] = False
        st.error("Invalid user name or password")
    
def show_login_page():
    with loginSection:
        if st.session_state['loggedIn'] == False:
            userName = st.text_input (label="", value="", placeholder="Enter your user name")
            password = st.text_input (label="", value="",placeholder="Enter password", type="password")
            
            col1, col2, col3, col4, col5, col6, col7= st.columns(7)

            with col1:
                st.button ("Login", on_click=LoggedIn_Clicked, args= (userName, password))

            with col2:
                if st.button ("Register"):
                    st.switch_page("pages/Register.py")



with headerSection:
    st.title("Streamlit Application")
    #first run will have nothing in session_state
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            st.switch_page("pages/Trangchu.py")  
        else:
            show_login_page()
