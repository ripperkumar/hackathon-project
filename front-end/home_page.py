import streamlit as st
import time
import sys
sys.path.append("/Users/testvagrant/Baganna/hackathon-project/backend/")
from scrapper.HTMLScraper import HTMLScraper
from model.assistant import Assistant
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
            # Assistant().create_assistant(selected_language, selected_tool)
            response =[
                    {
                        "description": "Test case to verify the presence of the blinking text link on the login page",
                        "testCase": "public void testBlinkingTextLinkPresence() {\n" +
                                    "    WebElement blinkingTextLink = driver.findElement(By.cssSelector(\"a.blinkingText\"));\n" +
                                    "    Assert.assertTrue(\"Blinking Text link is not present on the login page\", blinkingTextLink.isDisplayed());\n" +
                                    "    Assert.assertEquals(\"Incorrect link URL\", \"https://rahulshettyacademy.com/documents-request\", blinkingTextLink.getAttribute(\"href\"));\n" +
                                    "}"
                    },
                    {
                        "description": "Test case to verify that username and password input fields are present",
                        "testCase": "public void testUsernamePasswordFields() {\n" +
                                    "    WebElement usernameField = driver.findElement(By.id(\"username\"));\n" +
                                    "    Assert.assertTrue(\"Username field is not present on the login page\", usernameField.isDisplayed());\n" +
                                    "    WebElement passwordField = driver.findElement(By.id(\"password\"));\n" +
                                    "    Assert.assertTrue(\"Password field is not present on the login page\", passwordField.isDisplayed());\n" +
                                    "}"
                    },
                    {
                        "description": "Test case to verify form submission with correct credentials",
                        "testCase": "public void testFormSubmissionWithCorrectCredentials() {\n" +
                                    "    WebElement usernameField = driver.findElement(By.id(\"username\"));\n" +
                                    "    WebElement passwordField = driver.findElement(By.id(\"password\"));\n" +
                                    "    WebElement signInButton = driver.findElement(By.id(\"signInBtn\"));\n" +
                                    "    usernameField.sendKeys(\"rahulshettyacademy\");\n" +
                                    "    passwordField.sendKeys(\"learning\");\n" +
                                    "    signInButton.click();\n" +
                                    "    // Assume redirection or an element existence to check login success\n" +
                                    "    // Example assertion, assuming successElement appears after successful login\n" +
                                    "    WebElement successElement = driver.findElement(By.id(\"successElementId\"));\n" +
                                    "    Assert.assertTrue(\"Login not successful\", successElement.isDisplayed());\n" +
                                    "}"
                    },
                    {
                        "description": "Test case to ensure alert is displayed when incorrect credentials are submitted",
                        "testCase": "public void testAlertOnIncorrectCredentials() {\n" +
                                    "    WebElement usernameField = driver.findElement(By.id(\"username\"));\n" +
                                    "    WebElement passwordField = driver.findElement(By.id(\"password\"));\n" +
                                    "    WebElement signInButton = driver.findElement(By.id(\"signInBtn\"));\n" +
                                    "    WebElement alert = driver.findElement(By.cssSelector(\"div.alert.alert-danger\"));\n" +
                                    "    usernameField.sendKeys(\"incorrectUser\");\n" +
                                    "    passwordField.sendKeys(\"incorrectPass\");\n" +
                                    "    signInButton.click();\n" +
                                    "    // Check if alert is displayed and text is correct\n" +
                                    "    Assert.assertTrue(\"Alert not displayed on incorrect credentials\", alert.isDisplayed());\n" +
                                    "    Assert.assertEquals(\"Incorrect alert message\", \"Incorrect username/password.\", alert.getText().trim());\n" +
                                    "}"
                    }
                ]
            for res in response:
                st.write(res['description'])
                st.code(res['testCase'])
            

