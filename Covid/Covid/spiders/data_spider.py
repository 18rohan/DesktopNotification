import scrapy

class DataSpider(scrapy.Spider):
	name = 'covid'

	start_urls = ['https://www.covid19india.org/']

	def parse(self, response):
		data = response.xpath("//div[@class='level-item is-cherry fadeInUp']")

		yield {
		'data': data.xpath(".//div[@class='level-item is-cherry fadeInUp']").get()
		}




