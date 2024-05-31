from scrapy import Spider


class BooksSpider(Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        # Get all categories in the sidebar using a CSS selector.
        categories = response.css(".side_categories > ul > li > ul > li > a::attr(href)").getall()
        # Parse each category page.
        yield from response.follow_all(categories, callback=self.parse_category_page)

    def parse_category_page(self, response):
        # Check for pagination (other pages in this category).
        pagination = response.css(".next a")
        yield from response.follow_all(pagination, callback=self.parse_category_page)

        # Get books details from the category page, as specified.
        # Fields to extract: book title, book price, book image URL, book details page URL.
        book_entries = response.css("article.product_pod")
        for entry in book_entries:
            yield {
                "title": entry.css("h3 a::attr(title)").get(),
                "price": entry.css(".price_color::text").re_first("£(.*)"),
                "image_url": response.urljoin(entry.css(".image_container a img::attr(src)").get()),
                "details_url": response.urljoin(entry.css("h3 a::attr(href)").get()),
            }
