# -*- coding: utf-8 -*-

# Scrapy settings for newstracker project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'newstracker'

SPIDER_MODULES = ['newstracker.spiders']
NEWSPIDER_MODULE = 'newstracker.spiders'

#ITEM_PIPELINES = {
#    'newstracker.pipelines.NewstrackerPipeline':300
#}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newstracker (+http://www.yourdomain.com)'
