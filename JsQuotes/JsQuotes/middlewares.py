# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import atexit


class SeleniumDownloaderMiddleWare(object):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        self.driver = webdriver.Chrome(options=chrome_options)

        # Close the browser when we finish.
        atexit.register(self.cleanup)

    def process_request(self, request, spider):
        self.driver.get(request.url)
        content = self.driver.page_source

        return HtmlResponse(
            request.url, encoding="utf-8", body=content, request=request
        )

    def process_response(self, request, response, spider):
        return response

    def cleanup(self):
        self.driver.quit()
