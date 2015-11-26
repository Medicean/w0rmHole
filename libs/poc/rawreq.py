# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.ui import UI


class RawReq(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    发送原始字串注意拼接字符串

    set RAW sendintent?intent=sms:110&


    payload = "{self.options.RAW}mcmdf=inapp_&callback=t"
        ''',
    }

    payload = "{self.options.RAW}mcmdf=inapp_&callback=t"

    options = AttribDict()

    options.RAW = ""

    def callback(self, arg):
        if arg[0]:
            self.ui.success('Success!')
        else:
            self.ui.error('Error!')
        self.ui.p(arg[1], self.ui.GREEN)
register(RawReq)
