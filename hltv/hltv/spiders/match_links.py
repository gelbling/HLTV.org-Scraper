import scrapy
from scrapy.crawler import CrawlerProcess

class MatchLinks(scrapy.Spider):

    ######################################################################################################################

    url = 'https://www.hltv.org/results?offset=4700&startDate=2019-01-01&endDate=2022-05-20&stars=1'
    urls = []

    amount = 4789
    roundedAmount = 4700

    count = 0
    while (count <= roundedAmount):
        url = 'https://www.hltv.org/results?offset=' + str(count) + '&startDate=2019-01-01&endDate=2022-05-20&stars=1'
        count += 100
        urls.append(url)

    url = 'https://www.hltv.org/results?offset=' + str(amount - 4700) + '&startDate=2019-01-01&endDate=2022-05-20&stars=1'
    urls.append(url)

    ######################################################################################################################

    name = 'match'
    start_urls = urls

    f = open('match_links_may_22.txt', 'w')

    def parse(self, response):

        print('----------------------------------------')
        
        links = response.css('a[class="a-reset"]').xpath('@href').extract()

        for link in links:
            if 'matches' in link:
                print(link)
                self.f.write('https://www.hltv.org' + link + '\n')

        print('----------------------------------------')


process = CrawlerProcess({
                'USER_AGENT': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
            })

process.crawl(MatchLinks)
process.start()