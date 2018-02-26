# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup as bs
headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-TW,zh;q=0.8,en-US;q=0.6,en;q=0.4',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Content-Length':'47',
'Content-Type':'application/x-www-form-urlencoded',
'Cookie':'sto-id-20480-group-moodle-80=LIBPHGIMFAAA; _ga=GA1.3.692409477.1489982926; _gat=1; MoodleSessionntustMoodle=u0lv3conv29cfpvag8ie71b014; _ga=GA1.4.231816741.1488343503',
'Host':'moodle.ntust.edu.tw',
'Origin':'http://moodle.ntust.edu.tw',
'Referer':'http://moodle.ntust.edu.tw/login/index.php',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
}
payload = {'username':'帳號','password':'密碼'}
rs = requests.session()
#登入
res = rs.post('http://moodle.ntust.edu.tw/login/index.php', headers = headers, data = payload)
#資料
for i in range(1, 40000, 1):
    load = {'id': i}
    res2 = rs.get('http://moodle.ntust.edu.tw/user/profile.php?id=' + str(i), params = load)
    soup = bs(res2.text)
    try:
        if not soup.title.string.split(":")[0] == u'國立臺灣科技大學數位學習平台':
            print soup.title.string.split(":")[0]
            with open('A.txt', 'a') as f:
                f.write(soup.title.string.split(":")[0].encode('utf8') + '\n')
            f.close()
    except:
        print 'Error Message'