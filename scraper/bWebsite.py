from bs4 import BeautifulSoup
import requests

source = requests.get('http://www.coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

articles = soup.find_all('article')
for article in articles:
    heading = article.h2.a.text
    print(heading)
    summary = article.find(class_="entry-content").p.text
    print(summary)
    try:
        vid_id = article.iframe['src'].split('/')[4].split('?')[0]
        yt_link = 'https://youtube.com/watch?v=' + vid_id
    except:
        yt_link = None
    print(yt_link)
    print()
