import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from realt.items import RealtItem


class QuotesSpider(CrawlSpider):

    name = "realt"
    allowed_domains = ['realt.by']
    start_urls = ['https://realt.by/sale/flats/']
    rules = (
        Rule(LinkExtractor(allow=('flats/object')), callback='parse_item', follow=False),
    )


    def parse_item(self, response):
        item = RealtItem()
        item['title'] = response.xpath('//*[@id="c1030"]/div/h1/text()').extract()
        item['date'] = response.xpath('//*[@id="c1030"]/div/table[1]/tbody/tr[1]/td[2]/text()').extract()
        item['url'] = response.url
        item['agency'] = response.xpath('//*[@id="c1030"]/div/table[1]/tbody/tr[3]/td[2]/a/text()').extract()
        item['tel'] = response.xpath('//*[@id="c1030"]/div/table[1]/tbody/tr[2]/td[2]/div[2]/strong/nobr[1]/a/text()').extract()
        item['region'] = response.xpath('//*[@id="c1030"]/div/table[2]/tbody/tr[1]/td[2]/a/text()').extract()
        item['city'] = response.xpath('//*[@id="c1030"]/div/table[2]/tbody/tr[2]/td[2]/a/strong/text()').extract()
        item['district'] = response.xpath('//*[@id="c1030"]/div/table[2]/tbody/tr[4]/td[2]/a[1]/text()').extract()
        item['rooms'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[1]/td[2]/div[2]/strong/text()').extract()
        item['floor'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[2]/td[2]/text()').extract()
        item['build_type'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[3]/td[2]/text()').extract()
        item['squares'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[4]/td[2]/strong/text()').extract()
        item['plan'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[5]/td[2]/text()').extract()
        item['ceiling_height'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[6]/td[2]/text()').extract()
        item['building_year'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[7]/td[2]/text()').extract()
        item['wc_paln'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[8]/td[2]/text()').extract()
        item['balcony'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[9]/td[2]/text()').extract()
        item['facing'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[10]/td[2]/text()').extract()
        item['addition_info'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[11]/td[2]/text()').extract()
        item['etc'] = response.xpath('//*[@id="c1030"]/div/table[3]/tbody/tr[12]/td[2]/div[2]/text()').extract()
        item['sale_conds'] = response.xpath('//*[@id="c1030"]/div/table[4]/tbody/tr[1]/td[2]/div[2]/text()').extract()
        item['owner'] = response.xpath('//*[@id="c1030"]/div/table[4]/tbody/tr[2]/td[2]/text()').extract()
        item['cost'] = response.xpath('//*[@id="c1030"]/div/table[4]/tbody/tr[3]/td[2]/div[2]/strong/span[1]/text()').extract()
        return item


