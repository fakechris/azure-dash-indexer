from urlparse import urljoin

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request

from azure_cmdlets.items import AzureCmdletsItem

class AzureSpider(BaseSpider):
    name = "azure"
    allowed_domains = ["msdn.microsoft.com",]
    start_urls = ["http://msdn.microsoft.com/en-us/library/azure/jj554330.aspx",]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        level2_links = hxs.xpath('//div[@class="toclevel2"]//a/@href').extract()
        for level2_page in level2_links:
            yield Request(urljoin("http://msdn.microsoft.com", level2_page), callback=self.parse)
            # crawl
        title = hxs.xpath('//h1/text()').extract()
        content = hxs.xpath('//div[@class="topic"]').extract()
        item = AzureCmdletsItem()
        #import pdb; pdb.set_trace()
        item['content'] = content[0]
        item['title'] = title[0]
        yield item
