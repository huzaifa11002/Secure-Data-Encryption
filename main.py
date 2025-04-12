import streamlit as st
from streamlit_option_menu import option_menu
from components.login import login
from components.home import home
from components.store_data import store_data
from components.retrive_data import retrive_data
from components.logout import logout


def main():

    st.set_page_config("Secure Data Encryption", layout="centered")
    st.markdown(
    """
    <style>
    .element-container > div:first-child {
        background-color: transparent !important;
    }

    .menu .container-xxl[data-v-5af006b8] {
        background-color: #1e1e1e !important;  /* dark background */
        border-radius: .5rem;
    }

    .p-3 {
        padding: 1rem !important;
        background-color: #1e1e1e !important;
    }
    </style>
    """, unsafe_allow_html=True)

    if st.session_state.get("logged_in", False):
        
        with st.sidebar:    
            menu = option_menu(
            menu_title="Main Menu",
            options=["Home", "Store Data", "Retrieve Data", "Logout"],
            icons=[],
            menu_icon=None,
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "transparent"},
                "nav-link": {"font-size": "16px", "text-align": "left", "margin": "5px"},
                "nav-link-selected": {"background-color": "#ff4b4b"},
            },
        )
        
        if menu == "Home":  
            home()

        elif menu == "Store Data":  
            store_data()

        elif menu == "Retrieve Data":
            retrive_data()

        elif menu == "Logout":
            logout()
    
    else:
        login()


if __name__ == "__main__":
    main()
