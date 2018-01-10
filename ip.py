#coding:utf-8

import requests
import time
from multiprocessing import Pool

def getProxy():
    iplist=['125.210.121.113:3128','176.9.28.86:1080','5.189.135.164:3128']
    proxy=[]
    for v in iplist:
        ip_dict={'http':v}
        proxy.append(ip_dict)
    print(proxy)
    return proxy

def test_ip():
    ip=getProxy()
    for v in ip:
        try:
            response=requests.get('http://www.baidu.com',proxies=v,timeout=3)
            if response:
                print("success!  ",v)
        except:
            pass


def test(proxy):
    try:
        response = requests.get('http://www.baidu.com', proxies=proxy, timeout=3)
        if response:
            print("success!  ", proxy)
    except:
        pass

if __name__=='__main__':
    # test_ip()
    proxy=getProxy()
    IPPool1 = []
    time1 = time.time()
    for item in proxy:
        IPPool1.append(test(item))
    time2 = time.time()
    print('singleprocess needs ' + str(time2 - time1) + ' s')
    pool = Pool(processes=4)
    IPPool2 = []
    temp = []
    time3 = time.time()
    for item in proxy:
        temp.append(pool.apply_async(test, args=(item,)))
    pool.close()
    pool.join()
    for item in temp:
        IPPool2.append(item.get())
    time4 = time.time()
    print('multiprocess needs ' + str(time4 - time3) + ' s')
