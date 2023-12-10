from openai import OpenAI
import shelve
from dotenv import load_dotenv
import os
import time
import sys
sys.path.append('/Users/testvagrant/Baganna/hackathon-project/backend/')
from scrapper.HTMLScraper import HTMLScraper
load_dotenv()
OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
client = OpenAI(api_key=OPEN_AI_API_KEY)
assistant = None
# --------------------------------------------------------------
# Get the code
# --------------------------------------------------------------
# url_to_scrape = "https://rahulshettyacademy.com/loginpagePractise/"
# html_scraper = HTMLScraper()
# code = html_scraper.remove_css_js_and_save_html(url_to_scrape)

# --------------------------------------------------------------
# Create assistant
# --------------------------------------------------------------
# language = "Java"
# tool = "Selenium"
class Assistant:
    def create_assistant(language, tool):
        global assistant 
        assistant = client.beta.assistants.create(
            name="Automation code Generator",
            instructions=f"""Generate Automation code in ``` {language} language in {tool} tool ```.Cover all edge cases by assertion and checking for element is present.\
            '''Assume the user has created the WebDriver. ''' \
            ''' Generate test cases only, focusing on assertions and element presence, following Page Object Model'''\
            ''' Provide code only, no import statements, no beforeClass or afterClass methods.'''\
            ```Generate responses in code, not scenarios.
            Segregate different test cases into separate responses.
            Provide responses in JSON format.```
            """,
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-1106-preview",
        )
        return assistant

    # --------------------------------------------------------------
    # Thread management
    # --------------------------------------------------------------
    def check_if_thread_exists(wa_id):
        with shelve.open("threads_db") as threads_shelf:
            return threads_shelf.get(wa_id, None)


    def store_thread(wa_id, thread_id):
        with shelve.open("threads_db", writeback=True) as threads_shelf:
            threads_shelf[wa_id] = thread_id


    # --------------------------------------------------------------
    # Generate response
    # --------------------------------------------------------------
    def generate_response(message_body):
        # If a thread doesn't exist, create one and store it
        print(f"Creating new thread")
        thread = client.beta.threads.create()
        thread_id = thread.id

        # Add message to thread
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=message_body,
        )

        # Run the assistant and get the new message
        new_message = run_assistant(thread)
        return new_message


    # --------------------------------------------------------------
    # Run assistant
    # --------------------------------------------------------------
    def run_assistant(thread):
        # Run the assistantx
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=assistant.id,
        )

        # Wait for completion
        while run.status != "completed":
            # Be nice to the API
            time.sleep(0.5)
            run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

        # Retrieve the Messages
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        new_message = messages.data[0].content[0].text.value
        return new_message
