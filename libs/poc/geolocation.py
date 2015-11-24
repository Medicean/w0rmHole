# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.ui import UI
import json
import urllib2

class Geolocation(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Version": "1.0",
        "Description": u'''

    获取目标当前所在的地理位置

        ''',
    }

    payload = "geolocation?mcmdf=inapp_&callback=t"

    options = AttribDict()

    def callback(self, arg):
        if arg[0]:
            data = arg[1][7:-2]

            try:
                data = json.loads(data)

                self.ui.notify.info('Get success!')
                if data.has_key('coords'):
                    info = data['coords']
                    # print ([p, info.get(p)] for p in info.keys())
                    self.ui.table(
                    u'目标地理位置',
                    [20, 21],
                    ['Options', 'Info'],
                    [
                        [u'citycode', data['citycode']],
                        [u'longitude', info['longitude']],
                        [u'latitude', info['latitude']],
                        [u'accuracy', info['accuracy']],
                    ])
                    location_api = "http://api.map.baidu.com/?qt=rgc&x={longitude}&y={latitude}&" \
                                   "dis_poi=1&fromproduct=jsapi&res=api".format(
                        longitude=info['longitude'], latitude=info["latitude"]
                    )
                    req = urllib2.Request(location_api)
                    resp = urllib2.urlopen(req)
                    lodata = json.loads(resp.read())
                    if lodata:
                        self.ui.success(lodata["content"]["address"]).success(lodata["content"]["poi_desc"])
            except:
                self.ui.error('Error!')
        else:
            self.ui.error('Error!')

register(Geolocation)
