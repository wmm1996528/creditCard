from selenium import webdriver

from time import sleep
import re
from redis import Redis
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from queue import Queue
import threading
from xinyongka.parsehtml import parseHtml
class xyk():
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        wb = webdriver.Chrome()
        wb.get('https://mail.qq.com/cgi-bin/loginpage')
        # sleep(2)
        url = wb.find_element_by_id('login_frame').get_attribute('src')
        wb.get(url)
        wb.find_element_by_class_name('switch_btn').click()
        wb.execute_script('document.getElementById("u").value="912594746"')
        wb.execute_script('document.getElementById("p").value="aq918927."')
        wb.find_element_by_xpath('/html/body/div[1]/div[4]/div/div/div[2]/form/div[4]/a').click()
        wb.find_element_by_id('login_button').click()
        while True:
            if 'https://mail.qq.com/cgi-bin/frame_html' in wb.current_url:
                break
        self.sid = re.findall('sid=(.+)&r=', wb.current_url)[0]
        self.s = requests.session()
        self.que= Queue()
        # 获取cookie
        cookie = [item["name"] + "=" + item["value"] for item in wb.get_cookies()]
        self.cookiestr = ';'.join(item for item in cookie)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Cookie': self.cookiestr
        }
        # end

    def run(self):
        for i in range(100):
            th = threading.Thread(target=self.parse,args=(i,))
            th.start()
        while True:
            mailid = self.que.get()
            th = threading.Thread(target=self.down_html, args=(mailid,))
            th.start()
    def parse(self,num):
        url = 'https://mail.qq.com/cgi-bin/mail_list?sid={}&folderid=1&folderkey=1&page={}&s=inbox&topmails=0&showinboxtop=1&ver=29938.0&cachemod=maillist&cacheage=7200&r=&selectall=0'
        url = url.format(self.sid,num)
        res = self.s.get(url,headers=self.headers)
        html = BeautifulSoup(res.text, 'lxml')
        lists = html.find_all('span', attrs={'t': 'u'})
        for li in lists:
            if '信用卡' in li.get_text():
                mailId = li['mailid']
                print(mailId)
                self.que.put(mailId)
    def down_html(self,mailid):

        url = 'https://mail.qq.com/cgi-bin/readmail?folderid=1&folderkey=1&t=readmail&mailid={}&mode=pre&maxage=3600&base=12.06&ver=12514&sid={}'
        url = url.format(mailid, self.sid)

        res = self.s.get(url, headers=self.headers)
        s = parseHtml(res.text)
        print(s)

if __name__ == '__main__':
    xyk = xyk()
    xyk.run()
