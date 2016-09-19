import scrapy
#    start_urls=['http://www.emagister.it/corsi_formazione/web/search/?searchAction=search&segment=corsi_formazione%2F&idsegment=6&p=1&rangoPrecioMax=13&rangoPrecioMin=17&idFiltroDuracionMax=20&idFiltroDuracionMin=10&idCategSeg=2']
from scrapy.selector import HtmlXPathSelector
from scrapy.crawler import CrawlerProcess



class CVE(scrapy.Spider):
    name = 'cve'
    #start_urls = ['http://stackoverflow.com/questions?sort=votes']
    start_urls=[]
    print xrange(1,1)
    i=1
    #for i in xrange(1,1):
        #url=http://www.cvedetails.com/vulnerability-list.php?vendor_id=26&product_id=11366&version_id=&page=2&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=726&sha=30679272dc2b04c89b8f6695993a2525fe02746b
        #url=http://www.cvedetails.com/vulnerability-list.php?vendor_id=26&product_id=11366&version_id=&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=726&sha=30679272dc2b04c89b8f6695993a2525fe02746b
        #start_urls.append('http://www.emagister.it/corsi_formazione/web/search/?searchAction=search&segment=corsi_formazione%2F&idsegment=6&p='+str(i)+'&rangoPrecioMax=13&rangoPrecioMin=17&idFiltroDuracionMax=20&idFiltroDuracionMin=10&idCategSeg=2')
    start_urls.append('http://www.cvedetails.com/vulnerability-list.php?vendor_id=26&product_id=11366&version_id=&page='+str(i)+'&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=1&trc=726&sha=30679272dc2b04c89b8f6695993a2525fe02746b')

    def parse(self, response):
        items = response.xpath('//div[@id="pagingb"]/a/@href')
        for href in items:
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_vulnpage)
        '''items=response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')
        #self.logger.info('A response'+ items.data)
        for single_item in items:
            #my_item = MyItem()
            #my_item['value'] = item.select('.//text()').extract()
            my_item=single_item.xpath('.//td/a/@href').extract()
            for m in my_item:
                cve_res=str(m).split("/")
                result=cve_res[len(cve_res)-2]
                if result.startswith( 'CVE' ):
                    yield{ 'cve':result}
                    #print { 'cve':result}
            #yield my_item'''

    def parse_vulnpage(self, response):
        items = response.xpath('//table[@id="vulnslisttable"]/tr[@class="srrowns"]')
        # self.logger.info('A response'+ items.data)
        for single_item in items:
            # my_item = MyItem()
            # my_item['value'] = item.select('.//text()').extract()
            my_item = single_item.xpath('.//td/a/@href').extract()
            for m in my_item:
                cve_res = str(m).split("/")
                result = cve_res[len(cve_res) - 2]
                if result.startswith('CVE'):
                    yield {'cve': result}
                    # print { 'cve':result}
                    # yield my_item
'''
        for href in response.css('.course-title-link::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'title':  response.css('h1::text').extract_first(),
            'price': response.css('.price span::text').extract_first(),
            'school':response.css('.course-tarjeton a::text').extract_first(),
            'link_school':response.css('.course-tarjeton a::attr(href)').extract_first(),
            'hours':response.css('.icons-clock-grey-before::text').extract_first(),
            #'votes': response.css('.question .vote-count-post::text').extract_first(),
            #'#body': response.css('.question .post-text').extract_first(),
            #'tags': response.css('.question .post-tag::text').extract(),
            #'link': response.url,
        }
'''
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
#process.crawl(CVE)
#process.start()
