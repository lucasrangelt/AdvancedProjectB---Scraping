import scrapy
import re

headers = {"User-Agent": "Mozilla/5.0"}

class MercadoLivreSpider(scrapy.Spider):
    name = 'cute_spider'
    url = 'https://lista.mercadolivre.com.br/notebook#D[A:notebook]'

    def start_requests(self):
        yield scrapy.Request('https://lista.mercadolivre.com.br/notebook#D[A:notebook]', meta={'playwright': True})
    
    def parse(self, response):
        items = response.css('li.ui-search-layout__item')
        for i in items:
            title = i.css('h3.poly-component__title-wrapper::text').get() or ""
            clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
            clean_title = clean_title.replace("  ", " ")

            price = i.css('span.andes-money-amount__fraction::text').get() or "0"
            clean_price = int(price.replace(".", ""))

            ram = re.search(r'(\d+\s*GB)\s(?=RAM|MEMORIA|MEMÓRIA)', clean_title, flags=re.IGNORECASE)
            storage = re.search(r'(\d+\s*GB|\d+\s*TB)\sSSD', clean_title, flags=re.IGNORECASE)
            color = re.search(r'\b(?:color|cor)?\s\b(PRETO|BRANCO|CINZA|VERMELHO|AZUL|ROSA|PRATA|AMARELO|VERDE|BLACK|WHITE|SILVER|GREY|GRAY)', clean_title, flags=re.IGNORECASE)

            yield {
                "full_title": clean_title,
                "memory": ram.group(1) if ram else "N/A",
                "storage": storage.group(1) if storage else "N/A",
                "color": color.group(1) if color else "N/A",
                "price": clean_price
            }
        next_page = response.css('li.andes-pagination__button--next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse, meta={'playwright': True})

