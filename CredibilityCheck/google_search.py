import requests
from urlAnalysis.filter_domains import filter_domains

def google_search(person, total_results=30):
    api_key = "AIzaSyBZy_dtMSuOzNC3b9gTN4dQyFzMlbGWAQw"
    cse_id = "319193642aa064948"
    search_url = "https://www.googleapis.com/customsearch/v1"

    links = []
    for page in range(0, total_results, 10):  # Google's max results per page is 10
        params = {
            'key': api_key,
            'cx': cse_id,
            'q': person,
            'start': page + 1  # Start can be between 1 and 91 for standard requests
        }
        response = requests.get(search_url, params=params)
        results = response.json()
        page_links = [result['link'] for result in results.get('items', [])]  # Collect full URLs
        links.extend(page_links)

    return links

# Example usage
person_name = 'Donald Trump'
links = google_search(person_name, total_results=30)  # Adjust total_results as needed
print(links)
