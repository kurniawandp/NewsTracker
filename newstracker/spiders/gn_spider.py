import scrapy
import urllib, json
import subprocess
import unicodedata

from newstracker.items import NewstrackerItem

class GnSpider(scrapy.Spider):
    name = "gn_spider"
    allowed_domains = ["news.google.com"]
    start_urls = [
        "https://news.google.com/news/section?pz=1&cf=all&topic=tc", # Technology 
        "https://news.google.com/news/section?pz=1&cf=all&topic=b",  # Business
        "https://news.google.com/news/section?pz=1&cf=all&topic=w",  # World
        "https://news.google.com/news/section?pz=1&cf=all&topic=n"   # United States
    ]
    
    source_multiplier = {'CNN':1.7, 'PC Magazine':1.5, 'TIME':1.5, 'Wired':1.5, 'CNBC':1.7, 'Forbes':1.7, 'Mashable':1.5, 'Bloomberg':1.7, 'MarketWatch':1.7, 'New York Times':1.7}

    
    def parse(self, response):
        sel = scrapy.Selector(response)

        newss = sel.xpath('//tr')
        items = []
        
        for news in newss:
            #print news.extract()
            
            #Company/Subject Name - Will make this user input most likely in the future
            company_name = 'Google'
            
            item = NewstrackerItem()
            
            url = "http://text-processing.com/api/sentiment/"

            #Title
            my_title = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-title-wrapper"]/h2/a/span/text()')
            if my_title.extract():
                if my_title.re(company_name):
                    item['title'] = my_title.extract()[0].encode('utf-8')
                    print "'text=" + my_title.extract()[0].encode('utf-8')+"'"
                    #print "\"text="+item['title'][0].encode('utf-8')+"\""
                    cmdping = "curl -d 'text=" + my_title.extract()[0].encode('utf-8') + "' http://text-processing.com/api/sentiment/"
                    print cmdping
                    p = subprocess.Popen(cmdping, stdout=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    item['t_label'] = output.split()[-1][1:-2]
                else:
                    continue
            

            #URL
            my_url = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-title-wrapper"]/h2/a/@url')
            if my_url.extract():
                item['url'] = my_url.extract()[0].encode('utf-8')
            
            #Description
            my_desc = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-snippet-wrapper"]/text()')
            if my_desc.extract():
                item['desc'] = my_desc.extract()[0].encode('utf-8')
                cmdping = "curl -d 'text=" + my_desc.extract()[0].encode('utf-8') + "' http://text-processing.com/api/sentiment/"
                p = subprocess.Popen(cmdping, stdout=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                item['d_label'] = output.split()[-1][1:-2]
            

            #Source
            my_source = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-source-wrapper"]/table/tbody/tr/td[@class="al-attribution-cell source-cell"]/span/text()')
            if my_source.extract():
                item['source'] = my_source.extract()[0].encode('utf-8')
                
            #Time
            my_time = news.xpath('td[@class="esc-layout-article-cell"]/div[@class="esc-lead-article-source-wrapper"]/table/tbody/tr/td[@class="al-attribution-cell timestamp-cell"]/span[@class="al-attribution-timestamp"]/text()')
            if my_time.extract():
                item['time'] = my_time.extract()[0].encode('utf-8')
            
            #Only append relevant/full results...
            if item:
                items.append(item)
                
        #If there's no results about the company
        if not items:
            print "Nothing about " + company_name + " in URL: " + response.request.url
        else:
            return items
