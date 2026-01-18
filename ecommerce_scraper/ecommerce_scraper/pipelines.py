# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import os
import psycopg2
from dotenv import load_dotenv
from itemadapter import ItemAdapter

load_dotenv()

class PostgresPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            host=os.getenv("ENV_HOST"),
            user=os.getenv("ENV_USER"),
            password=os.getenv("ENV_PASSWORD"),
            database=os.getenv("ENV_DATABASE")
        )
        self.cur = self.connection.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS raw_data (
                id SERIAL PRIMARY KEY,
                full_title TEXT,
                memory TEXT,
                storage TEXT,
                color TEXT,
                price TEXT,
                rating TEXT,
                site_name TEXT,
                scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
        """)
        self.connection.commit()
    
    def process_item(self, item, spider):
        self.cur.execute("""
            INSERT INTO raw_data (full_title, memory, storage, color, price, rating) VALUES (%s, %s, %s, %s, %s, %s)
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