from bs4 import BeautifulSoup
import requests

def scrape_news(ticker, date_range):
    # Construct the URL
    url = f"https://www.google.com/search?q={ticker}+stock+news&tbm=nws&tbs=cdr:1,cd_min:{date_range[0]},cd_max:{date_range[1]}"
    #print("URL:", url)
    #https://www.google.com/search?q=AAPL+stock+news&tbm=nws&tbs=cdr:1,cd_min:2023-02-18,cd_max:2023-02-25
    
    # Send a GET request to the URL and get the HTML content
    response = requests.get(url)
    #print("Response:", response)

    soup = BeautifulSoup(response.content, 'html5lib')

    heading_object=soup.find_all( 'h3' )
    #print(heading_object)
    
    # Iterate through the object 
    # and print it as a string.
    for info in heading_object:
        print(info.getText())
        print("------")
    
    """ # Find all the news article titles and links
    news_articles = soup.find_all('div', {'class': 'dbsr'})
    print("Found", len(news_articles), "news articles")

    # Print each article's title and link
    for article in news_articles:
        title = article.find('div', {'class': 'JheGif nDgy9d'}).get_text()
        link = article.find('a')['href']
        print(f"Title: {title}")
        print(f"Link: {link}\n") """

ticker = "AAPL"
date_range = ["2022-01-01", "2022-02-28"]        
scrape_news(ticker, date_range)