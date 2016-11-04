# coding:utf-8
#!/usr/bin/env python
import json


class JRTTAd(object):

    def __init__(self):
        pass

    @classmethod
    def open(cls, data):
        data = json.loads(data)
        result = []
        for index, i in enumerate(data.get('data', [])):
            content = i['content']
            print content
            content = json.loads(content)
            if content.get('tag', '') != 'ad':
                continue
            title = content['title']
            imgs = [t['url'] for t in content['image_list']]
            url = content['url']
            result.append({'title': title, "ad_type": u"今日头条", 'description': "", 'url': url, 'imgs': ",".join(imgs)})
        print result
        return result
