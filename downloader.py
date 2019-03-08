#!/usr/bin/env python3

#authors: lsz


import requests



url = 'https://www.zhihu.com'
headers = {'user-agent':r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
print(headers)
re = requests.get(url, headers=headers)

with open('zhihuIndex.html', 'w') as f:
    f.write(re.text)
    f.close()

print(re.text)
