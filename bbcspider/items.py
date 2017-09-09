# -*- coding: utf-8 -*-

from scrapy import Item, Field


class BbcspiderItem(Item):
    title = Field()
    body = Field()
    url = Field()
