# coding=UTF-8
from bs4 import BeautifulSoup
import requests


class Downloader():
    def __init__(self, url, path):
        """Initializer for downloader"""
        self.origin_url = url
        self.origin_response = requests.get(url)
        self.origin_soup = BeautifulSoup(self.origin_response.content, 'lxml')
        self.origin_path = path

    def count(self):
        """ Get Pictures' Count """
        count_text = self.origin_soup.find_all('span', 'num')[0].text
        self.count = count_text.split('/')[-1]

    def initial_url(self):
        self.url = self.origin_url.split('=')[0] + '='

    def download_image(self, url):
        image = requests.get(url)
        temp_path = self.origin_path + '/' if self.origin_path[-1] == '/' else '' + url.split('/')[-1]
        with open(temp_path, 'wb') as f:
            f.write(image.content)

    def image_url(self, response):
        soup = BeautifulSoup(response.content, 'lxml')
        
