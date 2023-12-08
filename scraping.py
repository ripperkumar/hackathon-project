import requests
from bs4 import BeautifulSoup

def remove_css_js_and_save_html(url, output_file="output.html"):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove CSS and JS code
            for script in soup(["script", "style"]):
                script.extract()

            # Save the filtered HTML content to a file
            with open(output_file, 'w', encoding='utf-8') as file:
                file.write(soup.prettify())
            print(f"Filtered HTML content (without CSS and JS) saved to {output_file}")
            return "File generated"
        else:
            print(f"Failed to retrieve HTML. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

