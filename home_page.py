import streamlit as st
from scraping import remove_css_js_and_save_html

def home_page():
    st.title("Auto Test Generator")

    # Input textbox with styling
    st.markdown("""
        <style>
            div.Widget.row-widget.stTextInput > div {
                width: 300px;
            }
        </style>
    """, unsafe_allow_html=True)
    input_text = st.text_input("Enter Link:", "")
    if not input_text:
        st.warning("Please enter url.")
    # Dropdown with styling
    st.markdown("""
        <style>
            div.Widget.row-widget.stSelectbox >div{
                width: 300px;
            }
        </style>
    """, unsafe_allow_html=True)
    tools = ["Select","Selenium", "PlayWrite", "WebDriverIO"]
    selected_tool = st.selectbox("Select an tool:", tools, index=0)
    if not selected_tool:
        st.warning("Please select tool.")
    if selected_tool == "Selenium":
        languages = ["Select","Java", "JavaScript", "Python", "Ruby","CSharp","Kotlin"]
        selected_language = st.selectbox("Select an Language:", languages, index=0)
    elif selected_tool == "PlayWrite":
        languages = ["Select","Java", "Node.js", "Python", ".NET"]
        selected_language = st.selectbox("Select an Language:", languages, index=0)
    else:
        languages = ["Select", "JavaScript"]
        selected_language = st.selectbox("Select an Language:", languages, index=0)
    if not selected_language:
        st.warning("Please select language.")
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
    if st.button("Generate Testcase In Selenium"):
        # Display the entered text and selected option
        st.code(remove_css_js_and_save_html(input_text))

