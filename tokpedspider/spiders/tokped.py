# -*- coding: utf-8 -*-
import scrapy
import collections
from pprint import pprint

class TokpedSpider(scrapy.Spider):
    name = 'tokped'
    allowed_domains = ['mabes.dev']
    start_urls = ['http://mabes.dev/tokped_category.html']

    collected_category = {}

    def parse(self, response):
        # Get all category
        wrapper = response.xpath('//*[h1[. ="Semua Kategori"]]/following-sibling::div[@class="row-fluid mb-20"]')
        for cats in wrapper:
            first_cat_wrapper = cats.xpath('.//div[@class="rel-category-wrapper"]')
            for first_cat in first_cat_wrapper:
                first_cat_data = first_cat.xpath('.//i[@class="icon-caret-right"]/following-sibling::a/text()').extract_first()
                self.collected_category[first_cat_data] = {}
                # get second level category
                second_cat_wrapper = first_cat.xpath('.//ul[@class="rel-category-wrapper_allcat"]')
                if not second_cat_wrapper:
                    # def goto category page get the top sold product
                for second_cat in second_cat_wrapper:
                    second_cat_data = second_cat.xpath('.//li/a/text()').extract_first()
                    self.collected_category[first_cat_data][second_cat_data] = {}
                    # get third level category
                    third_cat_wrapper = second_cat.xpath('.//ul[@class="rel-category-wrapper_lv3"]/li')
                    if not third_cat_wrapper:
                        # def goto category page get the top sold product
                    for third_cat in third_cat_wrapper:
                        third_cat_data = third_cat.xpath('.//a/text()').extract_first()
                        self.collected_category[first_cat_data][second_cat_data][third_cat_data] = {}
                        # def goto category page get the top sold product

        pprint(self.collected_category)

    pass
