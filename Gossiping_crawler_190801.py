# This script is to crawl information from the web version of PTT forum, https://www.ptt.cc/bbs/index.html. With a slight change of the code, the target
# could be changed from Gossiping to other billboard. 

# The web version of PTT is subject to auto-deletion. Thus, the page numbers as well as the page addresses are not available now. Modification is needed
# for the page information part.

from bs4 import BeautifulSoup
import requests
import csv
import bs4
import time
import http.cookiejar, urllib.request  
import copy
import sys

# defind the get contents function, including requesting the page source, finding correct classes, and stripping redundent informaition. Finally store the
# clean form of data into corresponding files
def get_contents(rurl):
    for line in co.split(';'):
        name,value=line.strip().split('=',1)
        cookies[name]=value
    # as PTT requires user to be 18 years old or above, cookies were needed to circumvent the age check
    r = requests.get(rurl,cookies=cookies)
    soup = BeautifulSoup(r.text,'lxml')
    a = list(soup.find_all('span', class_ = 'article-meta-value'))
    if len(a)<4:
        print(rurl)
    else:
        for i in range(0,4):
            a[i] = list(a[i].stripped_strings)[0]
        b = list(soup.find_all('span', class_ = 'f2'))
        for i in range(0,len(b)):
            b[i] = list(b[i].stripped_strings)
            if b[i] == []:
                continue
            else:
                b[i] = b[i][0]
                if b[i].find('※ 發信站: 批踢踢實業坊(ptt.cc), 來自:') == -1:
                    b[i] = ''
                else:
                    b[i] = b[i].replace('※ 發信站: 批踢踢實業坊(ptt.cc), 來自: ','')
                    a.extend([b[i]])
        c = list(soup.find('div',id="main-container"))
        d = list(c)[1].get_text()
        count = d.find(a[3])+24
        a.extend([d[count:d.find('--')]])
        with open("/Users/danielchiang/Dropbox/PTT data/arti_data.csv",'a', newline='') as p:
            writer = csv.writer(p)
            writer.writerow(a)
    
        e = list(soup.find_all('div', class_="push"))
        for i in range(0,len(e)):
            temp = a[0:3]
            e1 = e[i].find('span', class_ = 'hl push-tag') or e[i].find('span', class_ = 'f1 hl push-tag')
            e2 = e[i].find('span', class_ = 'f3 hl push-userid')
            e3 = e[i].find('span', class_ = 'f3 push-content')
            e4 = e[i].find('span', class_ = 'push-ipdatetime')
            if e1 == None or e2 == None or e3 == None or e4 == None:
                continue
            else: 
                e2 = list(e2.stripped_strings)
                e3 = list(e3.stripped_strings)
                e4 = list(e4.stripped_strings)
                if e1 == [] or e2 == [] or e3 == [] or e4 == []:
                    continue
                else:
                    f1 = list(e1.stripped_strings)[0]
                    f2 = e2[0]
                    f3 = e3[0]
                    f4 = e4[0]
                    temp.extend([f1,f2,f3,f4])
                    with open("/Users/danielchiang/Dropbox/PTT data/push_data.csv",'a', newline='') as q:
                        writer = csv.writer(q)
                        writer.writerow(temp)


co = '__cfduid=db07d2e21acbb3699967611a2f63348831543802350; _ga=GA1.2.279296032.1543802352; over18=1; _gid=GA1.2.1440098831.1564452876; _gat=1'
cookies={}
for line in co.split(';'):
    name,value=line.strip().split('=',1)
    cookies[name]=value

# I set the page number 932~12501 to capture all the posts two months before and after the date PTT stoped accepting non-NTU registration. The exact page
# number would vary according to the date the code is run. This range for page numbers work only on Aug 1st 2019.

for i in range(932,12501):
    print(i)
    page_num = str(i)
    url = "https://www.ptt.cc/bbs/Gossiping/index" + page_num + ".html"
    r = requests.get(url,cookies=cookies)
    soup = BeautifulSoup(r.text,'lxml')
    a = list(soup.find_all('div', class_ = 'title'))
    aa = []
    for s in a:
        if s.find('a') == None:
            continue
        else:
            aa.extend(['https://www.ptt.cc'+s.find('a')['href']])
    for i in aa:
        print(i)
        get_contents(i)
    time.sleep(2)
