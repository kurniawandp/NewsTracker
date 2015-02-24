import scrapy

from newstracker.items import NewstrackerItem

class GnSpider(scrapy.Spider):
    name = "gn_spider"
    allowed_domains = ["news.google.com"]
    start_urls = [
        "https://news.google.com/news/section?pz=1&cf=all&topic=tc", 
        "https://news.google.com/news/section?pz=1&cf=all&topic=b",
        "https://news.google.com/news/section?pz=1&cf=all&topic=n"
    ]
    
    source_multiplier = {'CNN':1.7, 'PC Magazine':1.5, 'TIME':1.5, 'Wired':1.5, 'CNBC':1.7, 'Forbes':1.7, 'Mashable':1.5, 'Bloomberg':1.7, 'MarketWatch':1.7, 'New York Times':1.7}
    positive_words = {}
    
    def parse(self, response):
        sel = scrapy.Selector(response)
        newss = sel.xpath('//tr')
        items = []
        
        for news in newss:
            #print news.extract()
            
            #Company/Subject Name - Will make this user input most likely in the future
            company_name = 'Apple'
            
            item = NewstrackerItem()
            
            #Title
            my_title = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-title-wrapper"]/h2/a/span/text()')
            if my_title.extract():
                if my_title.re(company_name):
                    item['title'] = my_title.extract()
                else:
                    continue
            
            #URL
            my_url = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-title-wrapper"]/h2/a/@url')
            if my_url.extract():
                item['url'] = my_url.extract()
            
            #Description
            my_desc = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-snippet-wrapper"]/text()')
            if my_desc.extract():
                item['desc'] = my_desc.extract()
            
            #Source
            my_source = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-source-wrapper"]/table/tbody/tr/td[@class="al-attribution-cell source-cell"]/span/text()')
            if my_source.extract():
                item['source'] = my_source.extract()
                
            #Time
            my_time = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-source-wrapper"]/table/tbody/tr/td[@class="al-attribution-cell timestamp-cell"]/span[@class="al-attribution-timestamp"]/text()')
            if my_time.extract():
                item['time'] = my_time.extract()
            
            #Only append relevant results...
            if item:
                items.append(item)
                
        #If there's no results about the company
        if not items:
            print "Nothing about " + company_name + " in URL: " + response.request.url
        else:
            return items
