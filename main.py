#!/usr/bin/python3
# coding=utf-8

# it has all page 698 now
import os
import requests
import subprocess
from selenium import webdriver
from lxml import etree
from time import sleep
from multiprocessing.dummy import Pool

def get_artical_list(res):
    tree = etree.HTML(res.text)
    titles = tree.xpath('//*[@id="timeline"]/div/div[2]/dl/dt/a/text()')
    hrefs = tree.xpath('//*[@id="timeline"]/div/div[2]/dl/dt/a/@href')
    print(hrefs)
    return list(zip([x.strip() for x in titles],hrefs))

def print_pdf(info_tuple):
    title, url = info_tuple
    #os.mknod(title+'.pdf')
    os.system('touch {}.pdf'.format(title))
    child_process = subprocess.Popen(['google-chrome',
            '--headless',
            '--disable-gpu',
            '--print-to-pdf={}.pdf'.format(title),
            url])

if __name__ == '__main__':
    res = requests.get('http://www.freebuf.com/')
    tree = etree.HTML(res.text)
    info_list = get_artical_list(res)
    pool = Pool()
    #options = webdriver.ChromeOptions()
    #options.add_argument('headless')
    #options.add_argument('disable-gpu')
    #driver = webdriver.Chrome(chrome_options=options,
    #        executable_path='/home/rootkit/js/node_modules/chromedriver')
    for x in info_list:
        print_pdf(x)
        sleep(10)
