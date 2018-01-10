# coding:utf-8

import requests
import re
import time
import random
import xlsxwriter
from models import session, Qunaer
from urllib import error


class QunaerSpider():
    def __init__(self):
        self.page = 1
        self.end_page = 3469
        self.User_Agent=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                         'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36",
                         "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                         "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
                         "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
                         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
                         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
                         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
                         "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                         "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
                         "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
                         "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
                         "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
                         ]
        self.iplist=['176.235.11.6:8080','176.9.28.86:1080','5.189.135.164:3128',
                     '64.33.171.19:8080','166.111.131.52:3128','51.15.196.77:8888',
                     '93.94.223.18:8080','123.125.159.122:80','50.205.154.101:3128',
                     '118.114.77.47:8080']
        self.ipdict=[]
        self.headres = {
            'User-Agent': self.User_Agent[random.randint(0, 22)]
        }
        self.name=[]
        self.quality = []
        self.sight_pop_data=[]
        self.sight_info_data = []
        self.sight_data=[]
        self.path = 'static/qunaer.xlsx'

    def get_end_page(self):
        pass

    def change_to_ipdict(self):
        for v in self.iplist:
            proxy={'http':v}
            self.ipdict.append(proxy)

#使用代理加本机（结果一直用本机ip到七百多页，被要求输入验证码，后数据一直为0）
    """
    def get_html(self, page,timeout,proxy=None,num_retries=6):
        URL = 'http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest&page=' + str(
            page)
        if  proxy==None:
            try:
                return requests.get(URL,headers=self.headres,timeout=timeout)
            except:
                if num_retries>0:
                    time.sleep(10)
                    print(u"获取网页出错，10s后获取倒数第%s次"%num_retries)
                    return self.get_html(page,timeout,num_retries-1)
                else:
                    print("开始使用代理")
                    time.sleep(10)
                    ip_proxy=random.choice(self.ipdict)
                    return self.get_html(page,timeout,ip_proxy)
        else:
            try:
                ip_proxy=random.choice(self.ipdict)
                return requests.get(page,headers=self.headres,proxies=ip_proxy,timeout=timeout)
            except:
                if num_retries>0:
                    time.sleep(10)
                    ip_proxy=random.choice(self.ipdict)
                    print("正在更换代理，10s后重新获取倒数第%d次"%num_retries)
                    print("当前代理是： ",ip_proxy)
                    return self.get_html(page,timeout,ip_proxy,num_retries-1)
                else:
                    print('代理不好使了！取消代理')
                    return self.get_html(page,3)
                    
                    """
        # try:
        #     response = requests.get(URL, headers=self.headres)
        #     # print(response.text)
        #     return response.text
        # except error as e:
        #     if hasattr(e, 'code'):
        #         print("HTTPError" + e.code)
        #     elif hasattr(e, 'reason'):
        #         print("URLError" + e.reason)
    def get_html(self, page):
        URL = 'http://piao.qunar.com/ticket/list.htm?keyword=%E7%83%AD%E9%97%A8%E6%99%AF%E7%82%B9&region=&from=mpl_search_suggest&page=' + str(
            page)
        """
        try:
            response = requests.get(URL, headers=self.headres,proxies=random.choice(self.ipdict),timeout=3)
            print(0)
            print(response.text)
            return response.text
        except:
            print(1)
            self.get_html(page)
            # error as e:
            # if hasattr(e, 'code'):
            #     print("HTTPError" + e.code)
            # elif hasattr(e, 'reason'):
            #     print("URLError" + e.reason)
        """
        i=0
        while i <= 10:
            try:
                proxy=random.choice(self.ipdict)
                print(proxy)
                response = requests.get(URL, headers=self.headres, proxies=proxy, timeout=4)
                print(0)
                # print(response.text)
                return response.text
            except Exception as e:
                print(e)
                i += 1

    def get_data(self,page):
        html = self.get_html(page)

        sight_name_patterns=re.compile(r'<div.*?class="sight_item_show">.*?<div.*?class="show loading">.*?<a.*?>.*?<img.*?data-original="(.*?)".*?>.*?</a>.*?</div>.*?</div>')
        sight_info_patterns = re.compile(
            r'<div.*?class="sight_item_about">.*?<a.*?class="name".*?>(.*?)</a>.*?'
            r'<div.*?class="sight_item_info">.*?<div.*?class="clrfix">.*?<span.*?class="area">.*?<a.*?>(.*?)</a>.*?</span>.*?'
            r'<div.*?class="sight_item_hot">.*?<span.*?>热度 (.*?)</span>.*?</div>.*?</div>.*?'
            r'<p.*?>.*?<span.*?>地址：(.*?)</span>.*?</p>.*?'
            r'<div.*?>(.*?)</div>.*?</div>.*?</div>', re.S)
        pop_patterns=re.compile(r'<div.*?class="sight_item_pop">.*?<table>(.*?)'
                                r'</table>.*?</div>',re.S)
        sight_pop_patterns=re.compile(
            r'<span.*?class="sight_item_price">.*?<em>(.*?)</em>.*?</span>.*?'
            r'<td.*?class="sight_item_sold-num">月销量：<span.*?>(.*?)</span>.*?</td>.*?',re.S)
        clrfix_patterns = re.compile(r'<div.*?class="clrfix">(.*?)</div>', re.S)
        quality_patterns = re.compile(r'<span.*?class="level">(.*?)</span>', re.S)

        sight_info_items = re.findall(sight_info_patterns, html)
        for item in sight_info_items:
            self.sight_info_data.append(
                [item[0], item[1], item[2], item[3], item[4]])
        # print(self.sight_info_data)
        print('info: ',len(self.sight_info_data))
        # for v in self.sight_info_data:
        #     print(v)

        sight_name_item=re.findall(sight_name_patterns,html)
        for v in sight_name_item:
            self.name.append(v)
        print('name: ',len(self.name))

        clrfix_item = re.findall(clrfix_patterns, html)
        for v in clrfix_item:
            quality_item = re.findall(quality_patterns, v)
            if len(quality_item) == 0:
                quality_item.append(" ")
            # print(quality_item)
            for v in quality_item:
                self.quality.append(v)
                # print(self.quality)
        print('quality: ',len(self.quality))

        pop_items = re.findall(pop_patterns, html)
        for v in pop_items:
            sight_pop_items=re.findall(sight_pop_patterns,v)
            if len(sight_pop_items) == 0:
                sight_pop_items.append(" ")
            for v in sight_pop_items:
                self.sight_pop_data.append(v)
        print('pop: ',len(self.sight_pop_data))
        time.sleep(1)

    def manage_data(self):
        self.sight_data=self.sight_info_data
        for v in range(len(self.sight_data)):
            self.sight_data[v].append(self.sight_pop_data[v][0])
            self.sight_data[v].append(self.sight_pop_data[v][1])
            self.sight_data[v].append(self.quality[v])
            self.sight_data[v].append(self.name[v])
            # print(self.sight_info_data[v])

    def output(self):
        row = 1
        col = 0
        w = xlsxwriter.Workbook(self.path)
        worksheet = w.add_worksheet(u"所有数据")
        worksheet.write("A1", u'景点名称')
        worksheet.write('B1', u'景点位置')
        worksheet.write('C1', u'景点热度')
        worksheet.write("D1", u"景点地址")
        worksheet.write("E1", u'景点简介')
        worksheet.write('F1', u'景点票价')
        worksheet.write('G1', u'月销量')
        worksheet.write('H1', u'景区')
        worksheet.write("I1", u"图片地址")

        for v in self.sight_data:
            worksheet.write(row, col, v[0])
            worksheet.write(row, col + 1, v[1])
            worksheet.write(row, col + 2, v[2])
            worksheet.write(row, col + 3, v[3])
            worksheet.write(row, col + 4, v[4])
            worksheet.write(row, col + 5, v[5])
            worksheet.write(row, col + 6, v[6])
            worksheet.write(row, col + 7, v[7])
            worksheet.write(row, col + 8, v[8])
            row += 1
        w.close()

    def mysql_database(self):
        for v in self.sight_data:
            name = v[0]
            position = v[1]
            heat = v[2]
            address = v[3]
            info = v[4]
            price = v[5]
            monthly_sales = v[6]
            quality = v[7]
            img = v[8]
            data = Qunaer(name=name, position=position, heat=heat, address=address, info=info, price=price,
                          monthly_sales=monthly_sales, img=img, quality=quality)
            session.add(data)
            session.commit()
        session.close()

    def main(self):
        self.change_to_ipdict()
        print("Start...")
        # self.page=31
        # self.get_data(self.page)
        while self.page <= self.end_page:
            # html=self.get_html(self.page)
            self.get_data(self.page)
            print("第%d页成功！" % self.page)
            self.page += 1
        self.manage_data()
        print("Success!")
        print("正在写入文件...")
        self.output()
        print("写入完成！")
        print("正在存入数据库...")
        self.mysql_database()
        print("数据存储完成！")


if __name__ == '__main__':
    qunaer = QunaerSpider()
    qunaer.main()
