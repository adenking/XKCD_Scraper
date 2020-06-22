import scrapy
from scrapy.loader import ItemLoader
from xkcd_scrapy.items import XkcdScrapyItem


class XKCDSpider(scrapy.Spider):
    name = 'XKCD'

    start_urls = [
        'https://xkcd.com/1/',
    ]

    def parse(self, response):
        comic = ItemLoader(item=XkcdScrapyItem(), response=response)
        comic.add_xpath('comic_title', '//*[@id="ctitle"]/text()')
        try:
            image_url = 'https:' + \
                response.selector.xpath('//*[@id="comic"]/img/@src').get()
            comic.add_value('image_urls', image_url)
        except:
            comic.add_xpath('image_urls', '/html/body/div[2]/div[2]/a/@href')
        comic.add_xpath('image_title', '//*[@id="comic"]/img/@title')
        comic.add_xpath('image_alt_text', '//*[@id="comic"]/img/@alt')
        comic.add_value('comic_number', response.request.url)
        yield comic.load_item()

        next_url = response.xpath('//a[text()="Next >"]/@href').get()
        yield response.follow(next_url, self.parse)
