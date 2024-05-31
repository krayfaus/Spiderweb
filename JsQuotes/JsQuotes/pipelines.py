# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ItemPipeline:
    def process_item(self, item, spider):
        # Make sure to escape any double quotes.
        # The text seem to use UNICODE quotes (“”), but let's make sure.
        item["text"] = item["text"].replace('"', '\\"')

        return item
