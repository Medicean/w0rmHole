# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.ui import UI


class SendIntent(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    调用其它程序

    INTENT:
        sms:    调用发短信程序     eg: set INTENT sms:110
        tel:    调用打电话程序     eg: set INTENT tel:110
        geo:    调用 GPS
        smsto:  发短信
        http:// 调用浏览器打开网页  eg: set INTENT http://google.com
        file:// 打开本地文件
        mailto: 发送邮件

        content://contacts/people/1 查看编号为 1 的用户名片
        其它的自行补充
        ''',
    }

    payload = "sendintent?intent={self.options.INTENT}&mcmdf=inapp_&callback=t"

    options = AttribDict()

    options.INTENT = [
            'sms:',
            'tel:',
            'geo:',
            'smsto:',
            'http://',
            'file://',
            'mailto:',
            'content://contacts/people/',
        ]

    def callback(self, arg):
        if arg[0]:
            self.ui.success('Success!')
        else:
            self.ui.error('Error!')

register(SendIntent)
