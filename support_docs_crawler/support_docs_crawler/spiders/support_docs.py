import scrapy
import logging
from uni2ascii import uni2ascii
from scrapy.spiders import SitemapSpider

class SupportDocsSpider(SitemapSpider):
    name = 'support_docs_spider'
    sitemap_urls = ['https://wordpress.com/support/sitemap-1.xml']
    custom_settings = {'CLOSESPIDER_PAGECOUNT': 700}

    def parse(self, response):

        def extract_title(query):
            try:
                string_unicode = response.xpath(query).extract_first().strip()
                string_encode = string_unicode.encode("ascii", "ignore")
                clean_title = string_encode.decode()
                return clean_title
            except Exception:
                logging.debug("This is missing the title! It's probably not a support doc.")
                pass


        def extract_description(query):
            string_unicode = response.xpath(query).extract_first().strip()
            string_encode = string_unicode.encode("ascii", "ignore")
            clean_description = string_encode.decode()
            return clean_description

        def extract_link(query):
            return rresponse.request.url

        yield {
            'topic_title': extract_title('//div[@class="post"]/h2/text()'),
            'topic_description': extract_description('/html/head/meta[@name="description"]/@content'),
            'topic_url': response.request.url,
        }

        pass
