import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=AAPL+stock+news&sxsrf=AJOqlzWU-WeFAZeiYAn7rnDHctmFtfkZOA:1677320347545&source=lnms&tbm=nws&sa=X&ved=2ahUKEwj5rfWbubD9AhXT9XMBHdKPDBkQ_AUoAXoECAEQAw&biw=1384&bih=778&dpr=1.25"

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the news article titles and links
news_articles = soup.find_all('div', {'class': 'dbsr'})

# Print each article's title and link
for article in news_articles:
    title = article.find('div', {'class': 'JheGif nDgy9d'}).get_text()
    link = article.find('a')['href']
    print(title)
    print(link)
    #print("Title: {title}")
    #print("Link: {link}\n")