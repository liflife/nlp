import requests
import re

url = 'https://time.geekbang.org/'
for n in range(1, 2):
    a_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_' + str(n) + '.html'
    # print(a_url)
    html = requests.get(a_url)
    html.encoding = 'gb2312'
    if html.status_code == 200:
        detail_html = re.findall('<a href="(.*?)" class="ulink">', html.text)
        # detail_html=[detail_html[0]]
        print(detail_html)
        for link in detail_html:
            b_url = url + link
            print(b_url)
            b_html = requests.get(b_url)
            b_html.encoding = 'gb2312'
            if b_html.status_code == 200:
                # print(b_html.text)
                b_detail_html = re.findall('<a href="(.*?)">.*?</a></td>', b_html.text)
                print(b_detail_html)
                with open(r'H:\tmp\tdty.txt', 'a', encoding='utf-8') as ff:
                    ff.write(b_detail_html[0] + '\n')
