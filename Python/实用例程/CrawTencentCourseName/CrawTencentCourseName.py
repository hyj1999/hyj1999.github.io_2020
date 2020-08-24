#CrawTencentCourseName.py
import requests
from bs4 import BeautifulSoup
import bs4


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillCourseList(clist, html):
    soup = BeautifulSoup(html, "html.parser")
    clist.append(soup.title.string[0:-12])
    cclist = []
    for li in soup.find('ol').contents[3]('ol')[0].children:
        if isinstance(li, bs4.element.Tag):
            nt = li('div')[1]
            cclist.append([nt('h5')[0].string, nt('span')[0].string])
    clist.append(cclist)
 

'''
start  起始网址代码（包括start）
end    结束网址代码（不包括end）
fname  数据保存到文件的名称（不包括扩展名）
mode   是否重新生成文件
       True  是
       False 否
'''
def printUnivList(start, end, mode=False):
    fname='CourseList({}-{})'.format(start,end)
    if mode == True:
        with open('{}.md'.format(fname), 'w', encoding = 'UTF-8') as f:
            f.write('## 腾讯课堂课程汇总\n\n|课程名称|特征数字|详细信息|课程网址|\n|:----:|:----:|:----:|:----:|\n')
    for n in range(start,end):
        try:
            cinfo = []
            url = 'https://ke.qq.com/course/{}'.format(n)
            html = getHTMLText(url)
            fillCourseList(cinfo, html)
            cinfo.append(str(n))
        except:
            continue
        CourseListString = '|' + cinfo[0] + '|' + cinfo[2] + '|' + '[点击进入](./CourseDetail/{}.html)'.format(n) + \
                           '|[点击进入](https://ke.qq.com/course/' + cinfo[2] + ')|\n'
        with open('{}.md'.format(fname), 'a', encoding = 'UTF-8') as f:
            f.write(CourseListString)
        if mode == True:
            with open('./CourseDetail/{}.md'.format(n), 'w', encoding = 'UTF-8') as f:
                f.write('## {}&emsp;&emsp;课程详情\n\n|课程名称|课程时间|\n|:----:|:----:|\n'.format(cinfo[0]))
        for c in cinfo[1]:
            with open('./CourseDetail/{}.md'.format(n), 'a', encoding = 'UTF-8') as f:
                f.write('|'+c[0]+'|'+c[1]+'|\n')
        print("\r      {}已完成".format(n))


print('开始爬取。。。')
n = eval(input("选择第几个文件："))
printUnivList(1000000+(n-1)*1000, 1000000+n*1000, mode=True)
input('爬取结束，按任意键退出。。。')



