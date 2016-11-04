#coding:utf-8
#!/usr/bin/env python
import json
import os.path
import pprint
import xlwt
from xlutils.copy import copy
import xlrd
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'SimSun'    # 指定“宋体”
style.font = font 

class QQAd(object):
    def __init__(self):
        pass

    @classmethod
    def open(cls, data):
        data = json.loads(data)
        result = []
        nrows = 1
        for index, i in enumerate(data.get('order', [])):
            webp = [a['url'][:-5] for a in i.get('webp', [])] if isinstance(i.get('webp', []), list) else []
            jpg = [a['url'] for a in i.get('resource_urlList', [])] if isinstance(i.get('resource_urlList', []), list) else []
            print webp
            result.append({'title':i['navTitle'], "ad_type":u"腾讯新闻", 'description':i['abstract'], 'url':i.get('url', ''), 'imgs':",".join(webp+jpg)})
        return result
