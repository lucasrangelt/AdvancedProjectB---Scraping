import scrapy
import re
from ecommerce_scraper.items import EcommerceItem

class EBaySpider(scrapy.Spider):
    name = 'cute_ebay_spider'
    allowed_domains = ['www.ebay.com']
    categories = {
        "notebook": "https://www.ebay.com/sch/i.html?_nkw=notebook",
        "smartphone": "https://www.ebay.com/sch/i.html?_nkw=smartphone",
        "tablet": "https://www.ebay.com/sch/i.html?_nkw=tablet",
        "console": "https://www.ebay.com/sch/i.html?_nkw=console",
        "headset": "https://www.ebay.com/sch/i.html?_nkw=headset"
    }

    async def start(self):
        for cat, url in self.categories.items():
            yield scrapy.Request(url, callback=self.parse, meta={'short_title': cat})
    
    def parse(self, response):
        items = response.css('li.s-card s-card--horizontal')
        short_title = response.meta['short_title']
        for i in items:
            title = i.css('span.su-styled-text primary default::text').get() or ""
            clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
            clean_title = clean_title.replace("  ", " ")

            price = i.css('span.su-styled-text primary bold large-1 s-card__price::text').get() or None
            price = price.replace("R$", "").strip() if price else None
            rating = None

            ram = re.search(r'(\d+\s*GB)\s*(?=RAM|MEMORIA|MEMÓRIA)', title, flags=re.IGNORECASE)
            storage = re.search(r'(\d+\s*GB|\d+\s*TB)\s*SSD', title, flags=re.IGNORECASE)
            color = re.search(r'\b(?:color|cor)?\s\b(PRETO|BRANCO|CINZA|VERMELHO|AZUL|ROSA|PRATA|AMARELO|VERDE|BLACK|WHITE|SILVER|GREY|GRAY)', title, flags=re.IGNORECASE)

            item = EcommerceItem()
            item["short_title"] = short_title
            item["full_title"] = clean_title
            item["memory"] = ram.group(1) if ram else "N/A"
            item["storage"] = storage.group(1) if storage else "N/A"
            item["color"] = color.group(1) if color else "N/A"
            item["price"] = price if price else None
            item["rating"] = rating if rating else None
            item["site_name"] = "ebay"
            yield item
        # next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)