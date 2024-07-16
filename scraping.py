import requests
from bs4 import BeautifulSoup
# URL of the website to scrape
url = 'https://traveltalesfromindia.in/'
# Send a GET request to the website
response = requests.get(url)
# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    # Find all the blog post elements (assuming they are contained in <article> tags)
    articles = soup.find_all('article')
         # Iterate through the articles and extract titles and links
    for article in articles:
        # Extract the title (assuming it's in an <h2> tag)
        title_tag = article.find('h2')
        title = title_tag.text if title_tag else 'No title found'

        # Extract the link (assuming it's in an <a> tag within the <h2> tag)
        link_tag = title_tag.find('a') if title_tag else None
        link = link_tag['href'] if link_tag else 'No link found'

        # Print the extracted title and link
        print(f'Title: {title}')
        print(f'Link: {link}')
        print('-' * 40)
else:
      print(f'Failed to retrieve the page. Status code: {response.status_code}')