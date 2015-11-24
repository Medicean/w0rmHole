# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.ui import UI
class GetApn():
    ui = UI()
    info = {
        "Author":"Medici.Yan",
        "Description": u'''

    获取 apn
        ''',
    }

    payload = "getapn?mcmdf=inapp_&callback=t"

    options = AttribDict()

    def callback(self, arg):
        if arg[0]:
            self.ui.notify.info('Get success!').success(arg[1][8:-13])
        else:
            self.ui.error('Error!')

register(GetApn)

