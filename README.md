# Scrapy

## 1 — Written Assignment

Please see [EmailResponse.md](EmailResponse.md).

## 2 — Coding

I've used [`uv`](https://pypi.org/project/uv/) to manage the Python virtual enviroment and dependencies for the two spiders, here's a simple guide on how to get it running. Alternatively, you can just use `pip` to install the requirements.txt file.

```bash
# You may install uv with pip
pip install uv

# Activate the virtual environment on macOS and Linux.
source .venv/bin/activate

# Activate the virtual environment on Windows.
.venv\Scripts\activate

# Install the dependencies.
uv pip install -r requirements.txt
```

## 2.1 — Books Spider

Project link: https://app.zyte.com/p/753973/1

```bash
cd Books

# Scrap all 1000 books.
scrapy crawl books -O books.jsonl

# Use the CLOSESPIDER_ITEMCOUNT setting to stop the spider earlier.
scrapy crawl books -O books_750.jsonl -s CLOSESPIDER_ITEMCOUNT=750
```

Extracted data: [books.json](Books/books.json)

## 2.2 — Quotes Spider

This spider uses a simple downloader middleware for Selenium to process JS before scrapping.

```bash
cd JsQuotes

scrapy crawl quotes -O quotes.jsonl
```

Extracted data: [quotes.json](JsQuotes/quotes.json)
