import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.crawler import CrawlerProcess


#example of URL to scrape all Window Server vulnerabilites
URL_TO_SCRAPE='http://www.cvedetails.com/vulnerability-list.php?vendor_id=26&product_id=11366&version_id=&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=726&sha=30679272dc2b04c89b8f6695993a2525fe02746b'


class CVE(scrapy.Spider):
    name = 'cve'
    start_urls=[]
    start_urls.append(URL_TO_SCRAPE)


    def parse(self, response):
        items = response.xpath('//div[@id="pagingb"]/a/@href')
        for href in items:
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_vulnpage)

    def parse_vulnpage(self, response):
        items = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')
        for single_item in items:
            my_item = single_item.xpath('.//td/a/@href').extract()
            for m in my_item:
                cve_res = str(m).split("/")
                result = cve_res[len(cve_res) - 2]
                if result.startswith('CVE'):
                    yield {'cve': result}



#if you want to debug or integrate the project un-comment the lines below
'''
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
#process.crawl(CVE)
#process.start()
'''
