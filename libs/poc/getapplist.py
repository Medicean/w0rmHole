# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.core.config import cache
from libs.ui import UI
import json

class GetApplist(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    获取安装程序列表
        ''',
    }

    payload = "getapplist?mcmdf=inapp_&callback=t"

    options = AttribDict()

    def callback(self, arg):
        _, res = arg
        if _:
            self.ui.notify.success('Get success!')
            # parse json
            try:
                data = json.loads(res[7:-2])
                packages = data['package_infos']
                self.ui.table(
                    'Found (%d) app..' % len(packages),
                    [45, 31],
                    ['PACKAGE_NAME', 'VERSION_NAME'],
                    [[p['package_name'], p['version_name']] for p in packages]
                )
                cache.getapplist = [p['package_name'] for p in packages]
            except Exception, e:
                self.ui.notify.error('(PARSE JSON) -> %s' % e)
        else:
            self.ui.notify.error('Get fail (%s)!' % res)

register(GetApplist)
