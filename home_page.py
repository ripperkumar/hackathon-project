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

    # Dropdown with styling
    st.markdown("""
        <style>
            div.Widget.row-widget.stSelectbox >div{
                width: 300px;
            }
        </style>
    """, unsafe_allow_html=True)
    options = ["Select","Java", "JavaScript", "Python", "Ruby"]
    selected_option = st.selectbox("Select an Language:", options, index=0)

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
        st.text(f"Entered text: {input_text}")
        st.text(f"Selected option: {selected_option}")
        st.code(remove_css_js_and_save_html(input_text))

