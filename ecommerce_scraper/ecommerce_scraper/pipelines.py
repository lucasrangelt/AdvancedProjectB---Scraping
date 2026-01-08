# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2

class PostgresPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host="db",
            user="lucasrangel",
            password="scrapyword",
            database="scrapy_data"
        )
        self.cur = self.connection.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS notebooks (
                id SERIAL PRIMARY KEY,
                full_title TEXT,
                memory TEXT,
                storage TEXT,
                color TEXT,
                price NUMERIC(10, 2),
                rating NUMERIC(2, 2),
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
        """)
        self.connection.commit()
    
    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO notebooks (full_title, memory, storage, color, price, rating) VALUES (%s, %s, %s, %s, %s, %s)
            """, (
            item["full_title"],
            item["memory"],
            item["storage"],
            item["color"],
            item["price"],
            item["rating"]
        ))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()