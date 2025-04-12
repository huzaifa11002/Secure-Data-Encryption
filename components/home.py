import streamlit as st

if "username" in st.session_state:
    username = st.session_state.username

def home():
        st.title("🔐Secure Data Encryption")
        st.write("This app is designed to ensure the secure handling of sensitive user data through **encryption and decryption mechanisms**.")
        st.markdown(f"""
### 👋 Welcome! **{username}**

### ✅ How It Works

- The application allows users to input any text they wish to **securely store**.
- Before storing the data, the user is required to provide a **passkey**.
- The text is then **encrypted** using this passkey and saved in a secure form.
- Later, if the user wants to view the stored text, they must **enter the same passkey** used during encryption.
- If the correct passkey is provided, the app **decrypts the data** and displays the original text.

### 🔒 Why It Matters

- This ensures that **only the person with the correct passkey** can access the original data.
- The encryption process makes the stored content **unreadable to anyone** without the key.
- It's a simple but powerful method to protect user privacy and secure sensitive information.

### 💡 Use Case

This system can be useful in any scenario where **private messages, credentials, or personal notes** need to be safely stored and accessed later with proper authorization.

---
""")