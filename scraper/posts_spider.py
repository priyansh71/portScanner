import scrapy

class PostsSpider(scrapy.Spider):
    name = "posts"

    start_urls= [
        'https://coreyms.com/',
    ]

    def parse(self,response):
        for post in response.css('article'):
            try:
                heading = post.css('h2 a::text')[0].get()
                summary = post.css('.entry-content p::text')[0].get()
                link = 'https://youtube.com/watch?v=' +  post.css('iframe').attrib['src'].split('/')[4].split('?')[0]
            except:
                heading = None
                summary = None
                link = None
            yield{
                'heading' : heading,
                'summary' : summary,
                'link' : link
            }
        next_page = response.css('li.pagination-next a').attrib['href']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page , callback=self.parse)