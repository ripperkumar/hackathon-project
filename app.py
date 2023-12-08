
import streamlit as st
from home_page import home_page
from about_us_page import about_page
def main():
    st.sidebar.title("Navigation")
    pages = ["Home", "About"]
    choice = st.sidebar.selectbox("Go to", pages)

    if choice == "Home":
        home_page()
    elif choice == "About":
        about_page()

if __name__ == "__main__":
    main()