# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.core.config import cache
from libs.ui import UI
import json

class Getlocstring(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    获取本地字符串
        ''',
    }

    payload = "getlocstring?mcmdf=inapp_&callback=t"

    options = AttribDict()


    def callback(self, arg):
        _, res = arg
        print arg

        if _:
            data = json.loads(res[7:-2])
            if len(data) > 0:
                self.ui.notify.info('Get success!').success(data.get('locstring'))
            else:
                self.ui.notify.error('Get fail (%s)!' % res)
        else:
            self.ui.notify.error('Get fail (%s)!' % res)

register(Getlocstring)


