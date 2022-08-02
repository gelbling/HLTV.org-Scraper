import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class StatLinks(scrapy.Spider):

    ######################################################################################################################
    match_links_f = open('match_links_may_22.txt', "r")
    lines = match_links_f.read().splitlines()
    ######################################################################################################################

    name = 'stat'
    start_urls = lines

    f = open('stat_links.txt', 'w')

    def parse(self, response):

        print('----------------------------------------')
        
        links = response.css('a[class="results-stats"]').xpath('@href').extract()

        for link in links:
            if '/stats/' in link:
                print(link)
                self.f.write('https://www.hltv.org' + link + '\n')

        print('----------------------------------------')


process = CrawlerProcess({
                'USER_AGENT': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                'ROBOTSTXT_OBEY': False,
                'DOWNLOAD_DELAY': 0.75,
                'CONCURRENT_REQUESTS_PER_DOMAIN': 3,
                'CONCURRENT_REQUESTS_PER_IP': 3,
           })

process.crawl(StatLinks)
process.start()


    