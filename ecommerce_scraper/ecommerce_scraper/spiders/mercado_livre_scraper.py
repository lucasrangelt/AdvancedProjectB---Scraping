import scrapy
import re
from ecommerce_scraper.items import NotebookItem

class MercadoLivreSpider(scrapy.Spider):
    name = 'cute_mercado_livre_spider'
    allowed_domains = ['mercadolivre.com.br']
    start_urls = ['https://lista.mercadolivre.com.br/notebook#D[A:notebook]']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)
    
    def parse(self, response):
        items = response.css('li.ui-search-layout__item')
        for i in items:
            title = i.css('a.poly-component__title::text').get() or ""
            clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
            clean_title = clean_title.replace("  ", " ")

            price = i.css('span.andes-money-amount__fraction::text').get() or None
            if price is not None:
                clean_price = price.replace(".", "")
                clean_price = float(clean_price.replace(",", "."))

            rating = i.css('span.poly-phrase-label::text').get() or None
            if rating is not None:
                clean_rating = float(rating)

            ram = re.search(r'(\d+\s*GB)\s*(?=RAM|MEMORIA|MEMÓRIA)', clean_title, flags=re.IGNORECASE)
            storage = re.search(r'(\d+\s*GB|\d+\s*TB)\s*SSD', clean_title, flags=re.IGNORECASE)
            color = re.search(r'\b(?:color|cor)?\s\b(PRETO|BRANCO|CINZA|VERMELHO|AZUL|ROSA|PRATA|AMARELO|VERDE|BLACK|WHITE|SILVER|GREY|GRAY)', clean_title, flags=re.IGNORECASE)

            item = NotebookItem()
            item["full_title"] = clean_title
            item["memory"] = ram.group(1) if ram else "N/A"
            item["storage"] = storage.group(1) if storage else "N/A"
            item["color"] = color.group(1) if color else "N/A"
            item["price"] = clean_price if clean_price else None
            item["rating"] = clean_rating if clean_rating else None
            yield item
        next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)