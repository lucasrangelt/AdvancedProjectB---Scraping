import scrapy
import re
from ecommerce_scraper.items import EcommerceItem

class ShopeeSpider(scrapy.Spider):
    name = 'cute_shopee_spider'
    allowed_domains = ['shopee.com.br']
    categories = {
        "notebook": "https://shopee.com.br/search?keyword=notebook",
        "smartphone": "https://shopee.com.br/search?keyword=smartphone",
        "tablet": "https://shopee.com.br/search?keyword=tablet",
        "console": "https://shopee.com.br/search?keyword=console",
        "headset": "https://shopee.com.br/search?keyword=headset"
    }

    async def start(self):
        for cat, url in self.categories.items():
            yield scrapy.Request(url, callback=self.parse, meta={'short_title': cat})
    
    def parse(self, response):
        items = response.css('li.col-xs-2-4 shoppee-search-item-result__item')
        short_title = response.meta['short_title']
        for i in items:
            title = i.css('div.line-clamp-2 break-words min-w-0 min-h-[2.5rem] text-sm th:text-[12px] my:text-[12px] km:text-[12px]::text').get() or ""
            clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
            clean_title = clean_title.replace("  ", " ")

            price = i.css('span.truncate text-base/5 font-medium::text').get() or None
            rating = i.css('div.text-shopee-black87 text-xs/sp14 flex-none::text').get() or None

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
            item["site_name"] = "shopee"
            yield item
        # next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)