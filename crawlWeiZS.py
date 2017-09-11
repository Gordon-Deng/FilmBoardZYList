# coding = utf-8

import urllib, requests

def CrawlWeiZS(keyword, sdate, edate):
    keyword = urllib.parse.quote(keyword)
    #first requests:get cookie_id
    cookie_header = {
                     "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
                     "Referer":"http://data.weibo.com/index?sudaref=www.google.com"
                    }
    first_requests_url = "http://data.weibo.com/index/ajax/hotword?word={}&flag=nolike&_t=0".format(keyword)
    requests_result = requests.get(first_requests_url, headers = cookie_header).json()
    cookie_id = requests_result["data"]["id"]

	#second requests:get WeiZhiShu data
	header = {
			  "Connection":"keep-alive",
			  "Accept-Encoding": "gzip, deflate, sdch",
			  "Accept": "*/*",
			  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
			  "Accept-Language": "zh-CN,zh;q=0.8",
			  "Referer": "http://data.weibo.com/index/hotword?wid={}&wname={}".format(cookie_id, keyword),
			  "Content-Type": "application/x-www-form-urlencoded",
			  "Host":"data.weibo.com"
    		 }

    second_requests_url = "http://data.weibo.com/index/ajax/getchartdata?wid={}&sdate={}&edate={}".format(cookie_id, sdate, edate)
    requests_result = requests.get(second_requests_url, headers = header).json()
    return requests_result

'''
    #获取日期
    date_url = "http://data.weibo.com/index/ajax/getdate?month=1&__rnd=1498190033389"
    dc = requests.get(date_url,headers=header).json()
    edate,sdate = dc["edate"],dc["sdate"]

    import cProfile
    cProfile.run('CrawlWeiZS("杨幂", "2013-03-01", "2017-08-01")')
'''

keywords = ["黄晓明", "杨幂", "刘德华", "周杰伦", "关晓彤", "周杰伦", 
            "刘亦菲", "高圆圆", "古力娜扎", "唐嫣", "许嵩", "apple", "google"]
sdate, edate = "2013-03-01", "2017-08-01"

for keyword in keywords:
    f = open(r'C:\Users\JoeyChui\Desktop\{}.txt'.format(keyword), 'w+')
    f.write(str(CrawlWeiZS(keyword, sdate, edate)))
    f.close()
