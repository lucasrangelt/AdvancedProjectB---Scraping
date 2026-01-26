import scrapy
import re
from ecommerce_scraper.items import EcommerceItem

class AliExpressSpider(scrapy.Spider):
    name = 'cute_aliexpress_spider'
    allowed_domains = ['pt.aliexpress.com']
    categories = {
        "notebook": "https://pt.aliexpress.com/w/wholesale-notebook.html?spm=a2g0o.productlist.search.0",
        "smartphone": "https://pt.aliexpress.com/w/wholesale-smartphone.html?spm=a2g0o.productlist.search.0",
        "tablet": "https://pt.aliexpress.com/w/wholesale-tablet.html?spm=a2g0o.productlist.search.0",
        "console": "https://pt.aliexpress.com/w/wholesale-console.html?spm=a2g0o.productlist.search.0",
        "headset": "https://pt.aliexpress.com/w/wholesale-headset.html?spm=a2g0o.productlist.search.0"
    }

    async def start(self):
        for cat, url in self.categories.items():
            yield scrapy.Request(url, callback=self.parse, meta={'short_title': cat})
    
    def parse(self, response):
        items = response.css('div.hl_ch search-item-card-wrapper-gallery')
        short_title = response.meta['short_title']
        for i in items:
            title = i.css('h3.k7_kw::text').get() or ""
            clean_title = re.sub(r'\bNOVO|FRETE GRATIS|FRETE GRÁTIS|GAMER|PROMOCAO|PROMOÇAO|PROMOCÃO|PROMOÇÃO|OFERTA|™|®', '', title, flags=re.IGNORECASE)
            clean_title = clean_title.replace("  ", " ")

            price = "".join(i.css('span.font-size:20px;decimal_point:,;comma_style:.;currency-symbol:R$;show-decimal:true;symbol_position:left;is-price-power:false::text').get()) or None
            rating = i.css('span.k7_kg::text').get() or None

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
            item["site_name"] = "aliexpress"
            yield item
        # next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
        # if next_page:
        #     yield response.follow(next_page, callback=self.parse)