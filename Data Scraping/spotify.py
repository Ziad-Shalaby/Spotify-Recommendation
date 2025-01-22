import scrapy
from scrapy.crawler import CrawlerProcess
import sqlite3


class SpotifySpider(scrapy.Spider):
    name = 'spotify'

    def __init__(self):
        self.conn = sqlite3.connect('spotify_songs.db') 
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                artist TEXT,
                link TEXT,
                year TEXT,
                length TEXT
            )
        """)
        self.conn.commit()

    def start_requests(self):
        url = 'https://open.spotify.com/playlist/37i9dQZF1EIWzUjyxUOu1e'
        yield scrapy.Request(url=url, callback=self.parse_front)

    def parse_front(self, response):
        link_to_follow = response.xpath('//a[contains(@href, "/track/")]/@href').getall()
        for url in link_to_follow:
            url = 'https://open.spotify.com' + url
            yield response.follow(url=url, callback=self.parse_page)

    def parse_page(self, response):
        song_name = response.xpath('//h1[contains(@data-encore-id,"text")]/text()').get()
        song_artist = response.xpath('//a[contains(@href,"/artist/")]/text()').get()
        song_year = response.xpath('//span[contains(text(), "20")]/text()').get()
        song_length = response.xpath('//span[contains(text(), ":")]/text()').get()

        self.cursor.execute("""
            INSERT INTO songs (name, artist, link, year, length) VALUES (?, ?, ?, ?, ?)
        """, (song_name, song_artist, response.url, song_year, song_length))
        self.conn.commit()

    def closed(self, reason):
        self.conn.close()


process = CrawlerProcess(settings={
    "LOG_LEVEL": "INFO",
})

process.crawl(SpotifySpider)
process.start()
