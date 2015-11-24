# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.core.config import cache
from libs.ui import UI
import json

class GetInfo(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    通用获取信息模块,也可以使用相应该的单独模块

    更专业详细的信息请使用相应的单独模块

    INFOTYPE:
        geolocation:    获取地理位置
        getlocstring:   获取本地字符串
        getapn:         获取 apn 信息
        getapplist:     获取安装程序列表,
        getserviceinfo: 获取服务信息,

        如果是 getapplist , 会把结果缓存起来，要想查看单个程序的信息请用 use packageinfo 模块
        ''',
    }

    payload = "{self.options.INFOTYPE}?mcmdf=inapp_&callback=t"

    options = AttribDict()
    options.INFOTYPE = {
        "geolocation": "geolocation",
        "getlocstring": "getlocstring",
        "getapn": "getapn",
        "getapplist": "getapplist",
        "getserviceinfo": "getserviceinfo",
        "getcuid": "getcuid",
    }

    def callback(self, arg):
        _, res = arg
        if _:
            info = json.loads(res[7:-2])

            if len(info) > 0:
                info_keys = info.keys()
                info_keys.remove('error')
                data = info.get(info_keys[0])
                self.ui.notify.info('Get success!')
                if hasattr(data, '__iter__'):
                    if self.options.INFOTYPE == "getapplist":
                        self.ui.table(
                            'Found (%d) app..' % len(data),
                            [45, 31],
                            ['PACKAGE_NAME', 'VERSION_NAME'],
                            [[p['package_name'], p['version_name']] for p in data]
                        )
                        cache.getapplist = [p['package_name'] for p in data]
                else:
                    self.ui.success(info.get(info_keys[0]))
            else:
                self.ui.notify.error('Get fail (%s)!' % res)
        else:
            self.ui.notify.error('Get fail (%s)!' % res)

register(GetInfo)


