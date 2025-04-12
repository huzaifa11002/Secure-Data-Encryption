import streamlit as st
from function_modules import encrypt_functions

def retrive_data():
    st.title("Retrieve Data")

    passkey = st.text_input("Enter a passkey", type="password")

    if st.button("Decrypt Data"):
        st.write("Your Decrypted Data")
        st.code(encrypt_functions.decrypt(passkey))
