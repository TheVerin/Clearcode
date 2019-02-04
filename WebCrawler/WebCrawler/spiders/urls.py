import scrapy


class UrlsSpider(scrapy.Spider):

    # Name of our web spider - important for further actions
    name = "urls"

    # List of urls which we want to map
    start_urls = ['http://0.0.0.0:8000']

    def parse(self, response):
        """looking for url adresses of all subsites of domain"""

        domain = 'http://0.0.0.0:8000'

        yield {'url': response.request.url}

        for href in response.css('a::attr(href)'):
            if domain in href.get() or href.get()[0] == "/":
                yield response.follow(href, callback=self.parse)

