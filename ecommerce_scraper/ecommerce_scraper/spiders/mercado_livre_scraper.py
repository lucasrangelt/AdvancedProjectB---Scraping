import scrapy
import re
from ecommerce_scraper.items import EcommerceItem

class MercadoLivreSpider(scrapy.Spider):
    name = 'cute_mercado_livre_spider'
    allowed_domains = ['mercadolivre.com.br']
    categories = {
        "notebook": "https://lista.mercadolivre.com.br/notebook#D[A:notebook]",
        "smartphone": "https://lista.mercadolivre.com.br/smartphone#D[A:smartphone]",
        "tablet": "https://lista.mercadolivre.com.br/tablet#D[A:tablet]",
        "console": "https://lista.mercadolivre.com.br/console#D[A:console]",
        "headset": "https://lista.mercadolivre.com.br/headset#D[A:headset]"
    }

    def start_requests(self):
        for cat, url in self.categories.items():
            yield scrapy.Request(url, callback=self.parse, meta={'short_title': cat})
    
    def parse(self, response):
        items = response.css('li.ui-search-layout__item')
        short_title = response.meta['short_title']
        for i in items:
            title = i.css('a.poly-component__title::text').get() or ""
            clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
            clean_title = clean_title.replace("  ", " ")

            price = i.css('span.andes-money-amount__fraction::text').get() or None
            rating = i.css('span.poly-phrase-label::text').get() or None

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
            item["site_name"] = "mercado_livre"
            yield item
        # next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)