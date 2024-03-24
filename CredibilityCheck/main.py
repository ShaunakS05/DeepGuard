from google_search import google_search
from urlAnalysis.filter_domains import filter_domains
from ContentAnalysis.scrape_website_content import scrape_website_content
from ContentAnalysis.extract_quotes import extract_quotes
from ContentAnalysis.SentimentAnalysis.get_author_sentiment import get_author_sentiment

person = "Donald Trump"
links = filter_domains(google_search(person))
# print(links)

Final_Links = []
# Now you have to scrape content from the domains

  # if not ("3" in get_author_sentiment(content , person) or quotes.len() == 0):
  #   Final_Links.append(extract_quotes_to_json(link))
  #   print(Final_Links)

def main(links):
  for link in links:
    content = scrape_website_content(link)
    quotes = extract_quotes(content)
    print(content)

main(links)