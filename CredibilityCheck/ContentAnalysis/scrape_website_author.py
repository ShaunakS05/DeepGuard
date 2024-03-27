import requests
from bs4 import BeautifulSoup

# Function to scrape the author from a website
def scrape_website_author(url):
    # Reusing the secure URL check from the content scraping function
    if not url.startswith('https://'):
        return "Error: The site isn't secure. Only HTTPS URLs are accepted."

    try:
        response = requests.get(url, timeout=5)  # Consistent timeout as content function
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # The selector might need to be changed based on the common patterns of the website
            # This could be 'meta[name="author"]', '.author-name', etc.
            author_meta = soup.find('meta', attrs={'name': 'author'}) or soup.find(class_='author-name')
            author = author_meta.get('content') if author_meta else 'Author not found'
            return author
        else:
            return f"Error: Unable to access the website. Status code: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error: An error occurred while accessing the site - {e}"

# Example usage
url = 'https://example.com'  # This should be a secure HTTPS URL
content = scrape_website_content(url)
author = scrape_website_author(url)
print(f"Content: {content}\nAuthor: {author}")