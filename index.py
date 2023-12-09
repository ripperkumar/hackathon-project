import streamlit as st

import streamlit as st

col1, col2 = st.columns([1, 2])

# Add image to the top-left corner
with col1:
 image = st.image("/Users/TestVagrant-1/Downloads/jv.jpg", use_column_width=False, width=150)

caption_text = "Moye Moye"
with col2:
 st.markdown(f'<div style="float: left; margin-right: 80px; margin-top: 80px; font-size:25px;">{caption_text}</div>', unsafe_allow_html=True)

# Add caption just below the image
caption_text = "Junior Vagrants"
st.markdown(f'<p style="font-size:20px">{caption_text}</p>', unsafe_allow_html=True)


user_input = st.text_input("Link to that website", "Enter URL here")

# Add a dropdown
options = ["Java", "JavaScript"]
selected_option = st.selectbox("Select an option", options)

# Add a button
button_clicked = st.button("Generate Test Script!!")

# Check if the button is clicked
if button_clicked:
    st.write(f"Text entered: {user_input}")
    st.write(f"Selected option: {selected_option}")

generatedOutput = "andja jn dsjn"


st.markdown("""
## Result
            """+ generatedOutput + """ """ )