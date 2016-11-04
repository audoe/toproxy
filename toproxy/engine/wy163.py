#coding:utf-8
#!/usr/bin/env python
import json
import os.path
import pprint

class WYAd(object):
    def __init__(self):
        pass

    @classmethod
    def open(cls, data):
        data = json.loads(data.decode('gb2312').encode('utf8'))
        result = []
        for index, i in enumerate(data):
            ads = i["ads"]
            for ad in ads:
                result.append({'title':ad['main_title'], "ad_type":u"网易新闻", 'description':"", 'url':ad.get('action_params', {}).get("link_url", ""), 'imgs':','.join(ad.get('res_url', []))})
        print result
        return result
