#-*-coding:utf-8-*- 
#2017-9-10 JoeyChui sa517045@mail.ustc.edu.cn

import re, requests, lxml.html, json, xlwt
from requests.exceptions import RequestException
#from time import sleep

def getOnePage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
    	print('ER:getOnePage')
    	return None

def getTVDisCnt(url):
	html = getOnePage(url)
	tvDisCnt = re.findall(',"view_all_count":(\d+),"copyright', html)[0]
	return int(tvDisCnt)

def getTVDetail(html):
	pattern = re.compile('figure_info">(.*?)</span>.*?a href="(https://v.qq.com/x/cover/\w+\.html).*?videos-vert:title">(.*?)</a>.*?title="(.*?)">.*?svg_icon_play_sm"></.*?num">(.*?)</span>', re.S)
	items = re.findall(pattern, html)
	for item in items:
		tvDate = re.findall('(\d+)-(\d+)-(\d+)', item[0])
		tvDate = str(tvDate[0][0]) + str(tvDate[0][1]) + str(tvDate[0][2])
		print(tvDate)
		yield [item[2], item[3], int(tvDate), getTVDisCnt(item[1]), item[1], 'TencentVideo']

def writeToXLS(content, fileName):
	workbook = xlwt.Workbook(encoding='utf-8')
	booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
	for i, rowVal in enumerate(content):
		for j, colVal in enumerate(rowVal):
			booksheet.write(i, j, colVal)
	workbook.save('%s.xls' % fileName)
	return

def main(page):
	SEEDURL = 'https://v.qq.com/x/list/variety?sort=5&offset=%s' % page
	html = getOnePage(SEEDURL)
	tvDetail = getTVDetail(html)
	writeToXLS(tvDetail, 'TencentVideoZY%s' % page)

main(30)