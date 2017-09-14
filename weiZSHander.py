#-*-coding:utf-8-*- 
#2017-9-10 JoeyChui sa517045@mail.ustc.edu.cn

import json, xlwt

def readWeiZSVaule(fileName):
	with open('%s.txt' % fileName, 'r', encoding='utf-8') as f:
		weiZSVaule = f.read()
		f.close()
	return json.loads(weiZSVaule)

def figureReYiGrade(weiZSVaule, name, date, date2):
	n = date2 - date + 1
	tvPhaseGrade = 0
	while date <= date2:
		tvPhaseGrade =  tvPhaseGrade + int(weiZSVaule[name][str(date)])
		date += 1
	return int(tvPhaseGrade / n)

def writeToXLS(content, fileName):
	workbook = xlwt.Workbook(encoding='utf-8')
	booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
	for i, rowVal in enumerate(content):
		for j, colVal in enumerate(rowVal):
			booksheet.write(i, j, colVal)
	workbook.save('%s.xls' % fileName)
	return

def weiZSHander(tvNameDate, rdFileName, wtFileName):
	reYiGrade = []
	weiZSVaule = readWeiZSVaule(rdFileName)
	for name in tvNameDate:
		print(name)
		date1 = tvNameDate[name].pop(0)
		while True:
			if tvNameDate[name] == []:
				date2 = date1 + 1
				tvPhaseGrade = figureReYiGrade(weiZSVaule, name, date1, date2)
				reYiGrade.append([name, date1, tvPhaseGrade])
				break
			else:
				date2 = tvNameDate[name].pop(0)
			tvPhaseGrade = figureReYiGrade(weiZSVaule, name, date1, date2)
			reYiGrade.append([name, date1, tvPhaseGrade])
			date1 = date2
	writeToXLS(reYiGrade, wtFileName)
	return


tvNameDate = {"中国新歌声":[20170901, 20170908], "中国有嘻哈":[20170902, 20170909], "中餐厅":[20170909], "了不起的孩子":[20170902, 20170909], "大学生来了":[20170802, 20170803, 20170809, 20170810, 20170816, 20170817, 20170823, 20170824, 20170830], "大片起来嗨":[20170907], "天使之路":[20170907], "姐姐好饿":[20170803], "小手牵小狗":[20170907], "开学第一课":[20170901], "开心相对论":[20170904], "快乐男声":[20170908], "我们来了":[20170908], "我们的征途":[20170902], "我爱二次元":[20170808], "挑战者联盟":[20170909], "明日之子":[20170909], "极速前进":[20170901], "极限挑战":[20170903], "火星情报局":[20170909], "爱笑会议室":[20170804], "爸爸去哪儿":[20170907], "脑大洞开":[20170809], "脱口秀大会":[20170908], "金星秀":[20170830], "饭局的诱惑":[20170906]}
rdFileName = 'WeiZS-20170801-20170910'
wtFileName = '综艺热议榜-20170801-20170910'
weiZSHander(tvNameDate, rdFileName, wtFileName)
