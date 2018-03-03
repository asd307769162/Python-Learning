import scrapy
from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains=['dmoztools.net']
    start_urls=[
        'http://dmoztools.net/Computers/Programming/Languages/Python/Books/'
        ]

    def parse(self,response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//div[@id="site-list-content"]/div')
        items = []
        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('div[@class="title-and-desc"]/a/div/text()').extract()
            item['link'] = site.xpath('div[@class="title-and-desc"]/a/@href').extract()
            item['desc'] = site.xpath('div[@class="title-and-desc"]/div/text()').extract()
            items.append(item)
            
        return items
        '''
        print(title, link, desc)
        '''

        '''
        filename = response.url.split("/")[-2]
        with open(filename,'wb') as f:
            f.write(response.body)
        '''
