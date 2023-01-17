import scrapy


class AutorreformaSpider(scrapy.Spider):
    name = "autorreforma"
    allowed_domains = ['autorreformapsb.com.br']

    def start_requests(self):
        urls = [
            'https://www.autorreformapsb.com.br/videos/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for autorreforma in response.css(".dt-css-grid"):
            yield {
                "posicao": autorreforma.css("a::attr(href)").getall(),
                "imagem": autorreforma.css("a img::attr(src)").getall(), 
                "título": autorreforma.css(".post-entry-content h3 a::attr(title)").getall()}

        page = response.url.split("/")[-2]
        filename = f'autorreforma-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)