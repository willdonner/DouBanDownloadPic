# !/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import time

class BeautifulSoupPic():
    def __init__(self): ##初始化
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'}
        #self.web_url = 'https://www.douban.com/photos/album/127879998'
        #win下目录
        # self.folder_path = 'D:\BeautifulPicture'
        #mac下目录
        self.folder_path = '/Users/willdonner/DevsTest'
    def request(self, url): ##返回网页的请求
        r = requests.get(
            url=url,
        headers=self.headers)
        return r

    def mkdir(self, path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做', path, '的文件夹')
            os.makedirs(path)
            print('创建成功！')
        else:
            print(path, '文件夹已经存在了，不再创建')

    def save_img(self, url, name):
        print('保存准备中...')
        sleep_download_time = 0.5
        time.sleep(sleep_download_time)
        img = self.request(url)
        file_name = name + '.jpg'
        print('开始保存图片')
        f = open(file_name, 'ab')
        f.write(img.content)
        print(file_name + '保存成功')
        f.close()
        
    def geturl(self, url):
            r = self.request(url)
            print('开始获取所有img标签')
            all_a = BeautifulSoup(r.text, 'lxml').find('div', class_='photolst clearfix').find_all('img')
            print('开始创建文件夹')
            self.mkdir(self.folder_path)
            print('开始切换文件夹')
            os.chdir(self.folder_path)
            for a in all_a:
                reimg_url = a['src']
                first_pos1 = reimg_url[0:37]
                first_pos = first_pos1+'l'
                last_pos = reimg_url[38:]
                first_pos += last_pos
                img_name = first_pos[-15:-4]
                self.save_img(first_pos, img_name)
    def get_pic(self):
        #print('请输入你想下载的网址')
        downlode_url = 'https://www.douban.com/photos/album/127879998/'
        print(downlode_url)
        r = self.request(downlode_url)
        print('开始网页get请求')
        print('获取页数')
        print(r.text)
        all_message = BeautifulSoup(r.text, 'lxml').find('div', class_='paginator')
        #for a_page in all_message:
        page = int(all_message.find('span', class_='thispage').get('data-total-page'))
        print(page)
        for page in range(0, page*18, 18):
            if page == 0:
                url = downlode_url
                self.geturl(url)
            else:
                url = downlode_url+'/?start='+str(page)
                self.geturl(url)
beauty = BeautifulSoupPic()  #创建类的实例
beauty.get_pic()
print('下载完成!')