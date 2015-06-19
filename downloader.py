# coding=UTF-8
import requests, json, ast, os
from bs4 import BeautifulSoup


class Downloader():
    def __init__(self, url):
        self.url = url

    def fetch_info(self):
        response = requests.get(self.url).content
        soup = BeautifulSoup(response, 'lxml')
        title = soup.title.text
        pic_infos_json = self.fetch_pic_infos_json(response)
        images = self.process_json_string(pic_infos_json)

        return title, images

    def fetch_pic_infos_json(self, content):
        key1 = "'[{\"current_num\":1"
        key2 = "var nextTenInfosJson"
        head = content.find(key1)
        tail = content.find(key2)
        return content[head:tail].strip()[:-1]

    def process_json_string(self, json_string):
        return ast.literal_eval(json_string)

    def download_images(self, images):
        images = json.loads(images)
        for image in images:
            image_path = self.path + image.get('pic_url').split('/')[-1].encode('UTF-8')
            image_data = requests.get(image.get('pic_url_1920_b'), image.get('pic_url', None)).content
            with open(image_path, 'wb') as f:
                f.write(image_data)
        return True

    def start(self):
        title, images = self.fetch_info()
        self.path = 'Pictures/%s/' % title
        os.mkdir(self.path)
        self.download_images(images)


if __name__ == '__main__':
    d = Downloader('http://travel.fengniao.com/slide/526/5264127_1.html#p=1')
    d.start()
