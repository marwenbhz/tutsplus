# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TutsplusSpider(CrawlSpider):
    name = 'tutsplusspider'
    allowed_domains = ['tutsplus.com']
    start_urls = ['https://code.tutsplus.com/categories/']
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//a[@class='alphadex__item-link']"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="//a[@class='pagination__button pagination__next-button']"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for post in response.xpath("//li[@class='posts__post']"):
            yield {
                'Title': post.xpath(".//a[@class='posts__post-title ']/h1/text()").extract_first(),
                'Post_img': post.css('img.posts__post-preview-image::attr(src)').extract_first(),
                'Teaser': post.css('div.posts__post-teaser::text').extract_first(),
                'Author_name': post.css('a.posts__post-author-link::text').extract_first(),
                'Author_link': post.css('a.posts__post-author-link::attr(href)').extract_first(),
                'Publish_date': post.css('time.posts__post-publication-date::attr(title)').extract_first(),
		'Tags': post.css('a.posts__post-primary-category-link::text').extract_first(),
		'Url': post.xpath(".//a[@class='posts__post-title ']/@href").extract_first(),
                'Category': response.xpath("//span[@class='content-banner__title-breadcrumb-category']/text()").extract_first()
		  }
