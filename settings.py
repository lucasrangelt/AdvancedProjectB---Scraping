USER_AGENT_LIST = 'DOWNLOADER_MIDDLEWARES'
ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 3
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'

DOWNLOAD_HANDLERS = {
    'http' : 'scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler',
    'https' : 'scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler'
}

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'