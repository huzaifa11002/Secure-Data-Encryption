import streamlit as st

def logout():
    st.title("Logout")
    st.warning("Are you sure you want to logout this website?")
    if st.button("Logout", key="logout"):
        st.session_state.clear()
        st.rerun()