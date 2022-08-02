import scrapy
from scrapy.crawler import CrawlerProcess
import csv

class MapData(scrapy.Spider):

    ######################################################################################################################

    match_links_f = open('stat_links_may_22.txt', "r")
    lines = match_links_f.read().splitlines()

    ######################################################################################################################
    
    name = 'stat'
    start_urls = lines

    f = open('csgo_data_may_23.csv', 'w', newline='')
    thewriter = csv.writer(f)

    headers = ['game_url','date','map','team1_name','team1_score','team1_firsthalf_score','team1_secondhalf_score','team1_rating','team1_first_kills','team1_clutches_won','team1_player1_id','team1_player1_kills','team1_player1_assists','team1_player1_deaths','team1_player1_kast','team1_player1_kd-diff','team1_player1_adr','team1_player1_fk-diff','team1_player1_rating','team1_player2_id','team1_player2_kills','team1_player2_assists','team1_player2_deaths','team1_player2_kast','team1_player2_kd-diff','team1_player2_adr','team1_player2_fk-diff','team1_player2_rating','team1_player3_id','team1_player3_kills','team1_player3_assists','team1_player3_deaths','team1_player3_kast','team1_player3_kd-diff','team1_player3_adr','team1_player3_fk-diff','team1_player3_rating','team1_player4_id','team1_player4_kills','team1_player4_assists','team1_player4_deaths','team1_player4_kast','team1_player4_kd-diff','team1_player4_adr','team1_player4_fk-diff','team1_player4_rating','team1_player5_id','team1_player5_kills','team1_player5_assists','team1_player5_deaths','team1_player5_kast','team1_player5_kd-diff','team1_player5_adr','team1_player5_fk-diff','team1_player5_rating','team2_name','team2_score','team2_firsthalf_score','team2_secondhalf_score','team2_rating','team2_first_kills','team2_clutches_won','team2_player1_id','team2_player1_kills','team2_player1_assists','team2_player1_deaths','team2_player1_kast','team2_player1_kd-diff','team2_player1_adr','team2_player1_fk-diff','team2_player1_rating','team2_player2_id','team2_player2_kills','team2_player2_assists','team2_player2_deaths','team2_player2_kast','team2_player2_kd-diff','team2_player2_adr','team2_player2_fk-diff','team2_player2_rating','team2_player3_id','team2_player3_kills','team2_player3_assists','team2_player3_deaths','team2_player3_kast','team2_player3_kd-diff','team2_player3_adr','team2_player3_fk-diff','team2_player3_rating','team2_player4_id','team2_player4_kills','team2_player4_assists','team2_player4_deaths','team2_player4_kast','team2_player4_kd-diff','team2_player4_adr','team2_player4_fk-diff','team2_player4_rating','team2_player5_id','team2_player5_kills','team2_player5_assists','team2_player5_deaths','team2_player5_kast','team2_player5_kd-diff','team2_player5_adr','team2_player5_fk-diff','team2_player5_rating','game_type','game_description']

    thewriter.writerow(headers)

    def parse(self, response):
        
        # GAME DATA
        game_url = response.request.url
        date = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[1]/span[1]/text()').get()
        map = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/text()').getall()[1]

        # clean map data
        map = map.strip()

        game_data = []
        game_data.append(game_url)
        game_data.append(date)
        game_data.append(map)

        ######################################################################################################################

        # TEAM 1 DATA
        team1_name = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[2]/a/text()').get()
        team1_score = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[2]/div/text()').get()
        team1_firsthalf_score = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/span[3]/text()').get()
        team1_secondhalf_score = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/span[5]/text()').get()
        team1_rating = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[3]/div[1]/text()').get().split(' : ')[0]
        team1_first_kills = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[4]/div[1]/text()').get().split(' : ')[0]
        team1_clutches_won = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[5]/div[1]/text()').get().split(' : ')[0]

        table1 = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/table[1]/tbody/tr')
        team1_players = []
        for row in table1:
            row_data = row.css('td::text').getall()
            row_data = row_data[2:]
            ids = row.css('a').xpath('@href').extract()
            lis = ids + row_data
            for i in lis:
                team1_players.append(i)

        team1_data = []
        team1_data.append(team1_name)
        team1_data.append(team1_score)
        team1_data.append(team1_firsthalf_score)
        team1_data.append(team1_secondhalf_score)
        team1_data.append(team1_rating)
        team1_data.append(team1_first_kills)
        team1_data.append(team1_clutches_won)
        team1_data = team1_data + team1_players

        ######################################################################################################################

        # TEAM 2 DATA
        team2_name = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[3]/a/text()').get()
        team2_score = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[1]/div[3]/div/text()').get()
        team2_firsthalf_score = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/span[4]/text()').get()
        team2_secondhalf_score = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[2]/div[1]/span[6]/text()').get()
        team2_rating = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[3]/div[1]/text()').get().split(' : ')[1]
        team2_first_kills = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[4]/div[1]/text()').get().split(' : ')[1]
        team2_clutches_won = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/div[5]/div[1]/text()').get().split(' : ')[1]

        table2 = response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/table[2]/tbody/tr')
        team2_players = []
        for row in table2:
            row_data = row.css('td::text').getall()
            row_data = row_data[2:]
            ids = row.css('a').xpath('@href').extract()
            lis = ids + row_data
            for i in lis:
               team2_players.append(i)

        team2_data = []
        team2_data.append(team2_name)
        team2_data.append(team2_score)
        team2_data.append(team2_firsthalf_score)
        team2_data.append(team2_secondhalf_score)
        team2_data.append(team2_rating)
        team2_data.append(team2_first_kills)
        team2_data.append(team2_clutches_won)
        team2_data = team2_data + team2_players
        
        #######################################################################################################################


        row_data = game_data + team1_data + team2_data

        next_link = 'https://www.hltv.org' + response.selector.xpath('/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/div[4]/div[1]/div/a/@href').get()
        yield scrapy.Request(next_link, callback=self.parse_main_page, cb_kwargs={'row_data': row_data})


    def parse_main_page(self,response,row_data):
        description = response.css('div[class="padding preformatted-text"]::text').extract()

        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        
        game_type = ''

        if 'LAN' in description[0]:
            game_type = 'LAN'
        else:
            game_type = 'Online'

        desc = description[0].replace('\n','').replace('*','')

        row_data.append(game_type)
        row_data.append(desc)

        if len(row_data) == 109:
            self.thewriter.writerow(row_data)
            print('*** DATA SCRAPED ***')

        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')



process = CrawlerProcess({
                'USER_AGENT': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
                'ROBOTSTXT_OBEY': False,
                'DOWNLOAD_DELAY': 0.75,
                'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
                'CONCURRENT_REQUESTS_PER_IP': 1,
           })

process.crawl(MapData)
process.start()


    