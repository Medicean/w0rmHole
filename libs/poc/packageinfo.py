# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.core.config import cache
from libs.ui import UI
import json

class PackageInfo(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    获取安装程序信息
    PACKAGENAME:
        要获取的包名

        eg: set PACKAGENAME com.android.browser
        ''',
    }

    payload = "getpackageinfo?packagename={self.options.PACKAGENAME}&mcmdf=inapp_&callback=t"

    options = AttribDict()
    options.PACKAGENAME = cache.getapplist if cache.has_key('getapplist') else []

    def callback(self, arg):
        _, res = arg
        if _:
            info = json.loads(res[7:-2])
            if len(info) > 0:
                self.ui.notify.info('Get success!').table(
                    'App Info...',
                    [21, 21],
                    ['Options', 'Info'],
                    [[p, info.get('package_infos')[0].get(p)] for p in info.get('package_infos')[0].keys()]
                )
            else:
                self.ui.notify.error('Get fail (%s)!' % res)
        else:
            self.ui.notify.error('Get fail (%s)!' % res)

register(PackageInfo)

