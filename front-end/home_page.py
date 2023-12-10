import streamlit as st


import time
import sys
sys.path.append("/Users/testvagrant/Baganna/hackathon-project/backend/")
from backend.scrapper.HTMLScraper import HTMLScraper
from backend.model.assistant import generate_response, create_assistant
def home_page():
    st.title("Auto TestCase Generator")

    # Input textbox with styling
    st.markdown("""
        <style>
            div.Widget.row-widget.stTextInput > div {
                width: 300px;
            }
        </style>
    """, unsafe_allow_html=True)
    input_text = st.text_input("Enter URL:", "")

    # Dropdown with styling
    st.markdown("""
        <style>
            div.Widget.row-widget.stSelectbox >div{
                width: 300px;
            }
        </style>
    """, unsafe_allow_html=True)
    tools = ["Select","Selenium", "PlayWrite", "WebDriverIO"]
    selected_tool = st.selectbox("Select an tool:", tools)
    if selected_tool == "Selenium":
        languages = ["Select","Java", "JavaScript", "Python", "Ruby","CSharp","Kotlin"]
        selected_language = st.selectbox("Select an Language:", languages)
    elif selected_tool == "PlayWrite":
        languages = ["Select","Java", "JavaScript", "Python", ".NET"]
        selected_language = st.selectbox("Select an Language:", languages)
    else:
        languages = ["Select", "JavaScript"]
        selected_language = st.selectbox("Select an Language:", languages)
    # Submit button with styling
    st.markdown("""
        <style>
            div.Widget.stButton > button {
                width: 150px;
                height: 40px;
                background-color: #4CAF51;
                color: white;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)
    if st.button("Generate Testcase"):
        if not input_text:
            st.warning("Please enter URL.")
        elif selected_tool == "Select":
            st.warning("Please select tool.")
        elif selected_language == "Select":
            st.warning("Please select language.")
        else:
            success_mesage = st.success("wait for response")
            time.sleep(1)
            success_mesage.empty()
            html_code = HTMLScraper().remove_css_js_and_save_html(input_text)
            create_assistant(selected_language,selected_tool)
            response = generate_response(html_code)
            st.code(response)

