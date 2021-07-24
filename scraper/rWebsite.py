# import csv
from requests_html import HTML, HTMLSession

# csv_file = open('scraped.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Headline','Summary', 'Link'])

session = HTMLSession()
r = session.get('https://www.coreyms.com/')

articles = r.html.find('article')
for article in articles:
    headline = article.find('.entry-title-link', first=True).text
    print(headline)
    summary = article.find('.entry-content p', first=True).text
    print(summary)
    try:
        vid_src = article.find('iframe', first=True).attrs['src']
        vid_id = vid_src.split("/")[4].split("?")[0]
        yt_link = 'https://youtube.com/watch?v=' + vid_id
    except:
        yt_link = None
    print(yt_link)
    print()

#     csv_writer.writerow([headline, summary,yt_link])

# csv_file.close()
