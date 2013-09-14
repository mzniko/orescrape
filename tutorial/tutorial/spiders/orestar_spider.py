from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import FormRequest, Request

from tutorial.items import DmozItem

class OreSpider(BaseSpider):
    name = "orescraper"
    allowed_domains = ["https://secure.sos.state.or.us"]
    start_urls = [
        "https://secure.sos.state.or.us/orestar/GotoSearchByName.do"
        ]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//ul/li')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.select('a/text()').extract()
            item['link']= site.select('a/@href').extract()
            item['desc']= site.select('text()').extract()
            items.append(item)
        return items