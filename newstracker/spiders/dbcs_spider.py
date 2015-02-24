import scrapy

from newstracker.items import BusinessItem

class DbcsSpider(scrapy.Spider):
    name = "dbcs_spider"
    #allowed_domains = ["g2b.go.kr"]
    start_urls = ["http://www.g2b.go.kr/pt/menu/selectSubFrame.do?framesrc=/pt/menu/frameTgong.do?url=http://www.g2b.go.kr:8101/ep/tbid/tbidList.do?taskClCds=5&bidNm=&searchDtType=1&fromBidDt=2015/01/15&toBidDt=2015/02/14&fromOpenBidDt=&toOpenBidDt=&radOrgan=1&instNm=&area=&regYn=Y&bidSearchType=1&searchType=1"]

    def parse(self, response):
        print response.body
        sel = scrapy.Selector(response)
        newss = sel.xpath('//frame[@name="main"]/html/body/div/div/div/table/tbody/tr')
        items = []
        #print newss.extract()
        for news in newss:
            print news.extract()
            
            item = BusinessItem()
            items.append(item)

        return items
