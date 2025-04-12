import streamlit as st
from function_modules import authentication

def login():

    if "username" not in st.session_state:
        st.session_state.username = ""

    st.title("Login")
    tab1,tab2 = st.tabs(["**Register**", "**Login**"])

    with tab1:
        st.subheader("Account Register")
        username = st.text_input("Enter a username")
        password = st.text_input("Enter a password", type="password", key="register_username")
        confirm_password = st.text_input("Enter a confirm password", type="password", key="register-password")
        
        if st.button("Register", key="register"):
            
            if not username or not password or not confirm_password:
                st.error("All Fields Required")
            elif password != confirm_password:
                st.error("Password and Confirm Password do not match")
            else:
                if authentication.register_user(username, password):
                    st.success("Account Registered Successfully")
                else:
                    st.error("Username Already Exists")

    with tab2:
        st.subheader("Account Login")
        username = st.text_input("Enter a username", key="login_username")
        password = st.text_input("Enter a password", type="password", key="login-password")
        
        if st.button("Login", key="login"):
            if not username or not password:
                st.error("All Fields Required")

            if username and password:
                if authentication.login_user(username,password):
                    st.session_state["logged_in"] = True
                    st.session_state.username = username
                    st.success("Login Successfully")
                    st.rerun()
                else:
                    st.error("User Not Found")