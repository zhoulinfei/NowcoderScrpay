# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class MyspiderSpider(CrawlSpider):
    name = 'mySpider'
    allowed_domains = ['www.nowcoder.com']
    start_urls = []
    # 665 字节；239华为；134阿里；138腾讯；139百度；151京东；179美团；149网易；147小米；652滴滴；732拼多多；
    tags = [665, 239, 134, 138, 139, 151, 179, 149, 147, 652, 732]
    for tag in tags:
        for i in range(1, 11):
            url = 'https://www.nowcoder.com/discuss/tag/' + str(
                tag) + '?type=2&order=3&pageSize=30&expTag=0&query=&page=' + str(i)
            start_urls.append(url)

    reg = "www.nowcoder.com/discuss/[0-9]{5,6}\?type=2&order=\d+&pos=\d+&page=\d+"
    rules = (
        Rule(LinkExtractor(allow=reg), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        from NowcoderScrapy.items import NowcoderscrapyItem
        item = NowcoderscrapyItem()
        item["tag"] = re.search("665|239|134|138|139|151|179|149|147| 652 | 732", response.text).group()
        item["title"] = response.xpath('//span[@class="js-post-title"]/text()').extract()[0]
        item["content"] = response.xpath('//div[@class="post-topic-main"]').extract()[0]
        item["date"] = response.xpath('//span[@class="post-time"]/text()').extract()[0]
        return item
