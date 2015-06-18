# coding=UTF-8
from bs4 import BeautifulSoup
import requests


class Downloader():
    def __init__(self, url):
        """Initializer for downloader"""
        self.url = url
