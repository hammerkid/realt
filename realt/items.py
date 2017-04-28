# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    date = scrapy.Field()
    agency = scrapy.Field()
    tel = scrapy.Field()
    region = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    rooms = scrapy.Field()
    floor = scrapy.Field()
    build_type = scrapy.Field()
    squares = scrapy.Field()
    plan = scrapy.Field()
    ceiling_height = scrapy.Field()
    building_year = scrapy.Field()
    wc_paln = scrapy.Field()
    balcony = scrapy.Field()
    facing = scrapy.Field()
    addition_info = scrapy.Field()
    etc = scrapy.Field()
    sale_conds = scrapy.Field()
    owner = scrapy.Field()
    cost = scrapy.Field()