import requests
from bs4 import BeautifulSoup

# Function to scrape content from a website, strictly using HTTPS
def scrape_website_content(url):
    # Ensure the URL starts with 'https://'
    if not url.startswith('https://'):
        return "Error: The site isn't secure. Only HTTPS URLs are accepted."

    # Send a GET request to the URL
    try:
        response = requests.get(url, timeout=5)  # Added timeout for safety
        # If the request was successful
        if response.status_code == 200:
            # Parse the content of the page with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            # Extract the main content
            # You might need to adjust the selector depending on the website's structure
            main_content = soup.find(id='main') or soup
            # Convert the main content to text
            text = main_content.get_text(separator=' ', strip=True)
            return text
        else:
            return f"Error: Unable to access the website. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        # Handle exceptions for timeout, SSL errors, etc.
        return f"Error: An error occurred while accessing the site - {e}"

# Example usage
url = 'google.com'  # This should be a secure HTTPS URL
content = scrape_website_content(url)
print(content)
