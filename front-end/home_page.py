import streamlit as st
import time
import sys
sys.path.append("/Users/testvagrant/Documents/junior-vagrants/")
from backend.model.Assistant import Assistant

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
    tools = ["Select","Selenium", "PlayWright", "WebDriverIO"]
    selected_tool = st.selectbox("Select a tool:", tools)
    if selected_tool == "Selenium":
        languages = ["Select","Java", "JavaScript", "Python", "Ruby","CSharp","Kotlin"]
        selected_language = st.selectbox("Select a Language:", languages)
    elif selected_tool == "PlayWright":
        languages = ["Select","Java", "JavaScript", "Python", ".NET"]
        selected_language = st.selectbox("Select a Language:", languages)
    else:
        languages = ["Select", "JavaScript"]
        selected_language = st.selectbox("Select a Language:", languages)
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
            myAssistant = Assistant()
            # html_code = scrapper.remove_css_js_and_save_html(input_text)
            myAssistant.create_assistant(selected_language,selected_tool)
            response = myAssistant.generate_response(input_text)
            st.code(response)

