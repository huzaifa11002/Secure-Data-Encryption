import streamlit as st
from function_modules import encrypt_functions

def store_data():
    st.title("Store Data")
    user_text = st.text_area("Enter your text to save")
    passkey = st.text_input("Give pass key to stored data", type="password")

    if st.button("Encrypt & Save Data"):
        data_file = encrypt_functions.load_data()
        if user_text and passkey:
            hashed_key = encrypt_functions.hash_key(passkey)
            text = encrypt_functions.encrypt(user_text, passkey)
            data_file[hashed_key] = {"encrypted_text": text}
            encrypt_functions.save_data(data_file)
            st.success("✅Saved Data Successfully")
            st.info("Please remember your passkey ☢")
        else:
            st.error("Both Fields Required ❌")