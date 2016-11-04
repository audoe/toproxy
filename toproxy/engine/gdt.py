#coding:utf-8
#!/usr/bin/env python
import json
import os.path
import pprint

class GDTAd(object):
    def __init__(self):
        pass

    @classmethod
    def open(cls, data):
        data = json.loads(data)
        result = []
        nrows = 1
        for index, i in enumerate(data.get('data', {}).values()):
            for t in i["list"]:
                result.append({'title':t['txt'], "ad_type":u"广点通", 'description':t['desc'], 'url':t.get('rl', ''), 'imgs':",".join([t['img'], t['img2']])})
        return result
