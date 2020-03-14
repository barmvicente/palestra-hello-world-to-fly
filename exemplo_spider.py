import scrapy


def first(sel, xpath):
    return sel.xpath(xpath).extract_first()


class YoutubeChannelLister(scrapy.Spider):
    name = 'channel-lister'
    youtube_channel = 'portadosfundos'
    start_urls = [f'https://www.youtube.com/user/{youtube_channel}/videos']

    def parse(self, response):
        for sel in response.css("ul#channels-browse-content-grid > li"):
            yield {
                'link': response.urljoin(first(sel, './/h3/a/@href')),
                'title': first(sel, './/h3/a/text()'),
                'views': first(sel, ".//ul/li[1]/text()"),
            }
            