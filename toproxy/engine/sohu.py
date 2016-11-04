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

class SohuAd(object):
    def __init__(self):
        pass

    @classmethod
    def open(cls, data):
        data = json.loads(data)
        if isinstance(data, dict):
            return []
        result = []
        for d in data:
            print d['resource']
            imgs = d['resource']['file']
            title = d['resource1']['adcode']
            url = d['resource1']['click']
            result.append({'title':title, "ad_type":u"搜狐新闻", 'description':"", 'url':url, 'imgs':imgs})
        return result
