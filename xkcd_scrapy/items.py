# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import MapCompose


def extract_page_number(text):
    comic_number = text[17:-1]
    return comic_number


class XkcdScrapyItem(scrapy.Item):
    comic_title = scrapy.Field(serializer=str)
    comic_image = scrapy.Field()
    images = scrapy.Field()
    image_urls = scrapy.Field()
    image_title = scrapy.Field(serializer=str)
    image_alt_text = scrapy.Field(serializer=str)
    comic_number = scrapy.Field(input_processor=MapCompose(extract_page_number))
