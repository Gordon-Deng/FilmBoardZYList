# coding = utf-8
#2017-9-10 JoeyChui sa517045@mail.ustc.edu.cn

import urllib, requests

def getWID(keyword):
    header = {
                 "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
                 "Referer":"http://data.weibo.com/index?sudaref=www.google.com"
             }
    url = "http://data.weibo.com/index/ajax/hotword?word={}&flag=nolike&_t=0".format(keyword)
    result = requests.get(url, headers = header).json()
    wid = result["data"]["id"]
    return wid

def getWeiZSOrigin(keyword, sDate, eDate):
    keyword = urllib.parse.quote(keyword)
    wid = getWID(keyword)
    header = {
			  "Connection":"keep-alive",
			  "Accept-Encoding": "gzip, deflate, sdch",
			  "Accept": "*/*",
			  "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
			  "Accept-Language": "zh-CN,zh;q=0.8",
			  "Referer": "http://data.weibo.com/index/hotword?wid={}&wname={}".format(wid, keyword),
			  "Content-Type": "application/x-www-form-urlencoded",
			  "Host":"data.weibo.com"
    		 }
    url = "http://data.weibo.com/index/ajax/getchartdata?wid={}&sdate={}&edate={}".format(wid, sDate, eDate)
    result = requests.get(url, headers = header).json()
    return result

def getWeiZSVaule(weiZSOrigin):
    weiZSVaule = weiZSOrigin['zt']
    return weiZSVaule

def writeToTXT(content, fileName):
    with open('%s.txt' % fileName, 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()
    return
'''
def writeToXLS(content, fileName):
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    for i, rowVal in enumerate(content):
        for j, colVal in enumerate(rowVal):
            booksheet.write(i, j, colVal)
    workbook.save('%s.xls' % fileName)
    return
'''

def crawlWeiZS(keywords, sDate, eDate):
    for keyword in keywords:
        f = open('%s.txt' % keyword, 'w')
        weiZSOrigin = getWeiZSOrigin(keyword, sDate, eDate)
        weiZSVaule = getWeiZSVaule(weiZSOrigin)
        print(int(weiZSVaule[0]['day_key'].replace('-', '')) == 20170801)
        f.write(str(weiZSVaule))
        f.close()


keywords = ["中国新歌声"]
sDate, eDate = "2017-08-01", "2017-08-10"
crawlWeiZS(keywords, sDate, eDate)
