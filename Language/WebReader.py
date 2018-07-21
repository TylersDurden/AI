from urllib2 import urlopen
from urllib2 import URLError
from scapy.all import *
class WebReader:

    site_buffer = []

    def __init__(self):
        # browse web method is looking only for
        # web requests to RESTful API endpoints
        self.site_buffer.append('')


    def browseWeb(self):
        """
        Automated web browswing from starting point
        (Crawler)
        :return:
        """
        webdata = []
        for site in self.site_buffer:
            webdata.append(self.get_http(site))
        return webdata


    @staticmethod
    def get_http(host, decoding='utf-8'):
        """ Make HTTP GET request to host"""
        return urlopen(host).read().decode(decoding)


    def requestUser(self):
        """
        Allow user defined input of web searching
        :return:
        """
        url = input('Enter URL to read: ')
        print('searching '+url)
        return self.get_http(url)


def main():
    webreader = WebReader()

if __name__ == "__main__":
    main()
