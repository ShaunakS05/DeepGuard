import requests
from bs4 import BeautifulSoup

def scrape_website_metadata(url):
    # Dictionary to store metadata
    metadata = {}
    
    try:
        # Send HTTP request to the URL
        response = requests.get(url)
        
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract metadata
        metadata['title'] = soup.find('title').text if soup.find('title') else 'No title found'
        metadata['description'] = soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else 'No description found'
        metadata['keywords'] = soup.find('meta', attrs={'name': 'keywords'})['content'] if soup.find('meta', attrs={'name': 'keywords'}) else 'No keywords found'
        metadata['author'] = soup.find('meta', attrs={'name': 'author'})['content'] if soup.find('meta', attrs={'name': 'author'}) else 'No author found'
    
    except requests.RequestException as e:
        # Print the error message
        print(f"Request failed: {e}")
    except Exception as e:
        # Catch any other exceptions and print the error message
        print(f"An error occurred: {e}")
        
    return metadata

# Example usage
url = 'https://example.com'
print(scrape_website_metadata(url))
