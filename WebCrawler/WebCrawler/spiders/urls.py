"""
Required tasks:
    - take all urls adresses of subsites in the domain
"""
import scrapy


class UrlsSpider(scrapy.Spider):

    # Name of our web spider - important for further actions
    name = "urls"

    # List of urls which we want to map
    start_urls = ['http://0.0.0.0:8000']

    def parse(self, response):
        """looking for url adresses of all subsites of domain"""

        # You have to initialize your base url adress
        domain = 'http://0.0.0.0:8000'

        # Taking the information about url of the site
        yield {'url': response.request.url}

        # Taking the information above from all subsites of the page (switched by the link in <a>)
        for href in response.css('a::attr(href)'):
            if domain in href.get() or href.get()[0] == "/":
                yield response.follow(href, callback=self.parse)

