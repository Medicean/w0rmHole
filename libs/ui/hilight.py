# coding:utf-8

import os

class HILIGHT:
    '''
    @desc: 高亮指定字符
    '''

    def __init__(self, ui):
        self.ui = ui

    def hilight(self, obj="", msg='', objcolor=None, msgcolor=None):
        if not objcolor:
            objcolor = self.ui.GREEN
        if not msgcolor:
            msgcolor = self.ui.GREEN
        idx = obj.find(msg)
        if msg in obj:
            self.ui.p('[*] %s' % obj[:idx], objcolor, enter = False)
            self.ui.p('%s' % msg, msgcolor, enter = False)
            self.ui.p('%s' % obj[idx + len(msg):], objcolor)
        else:
            self.ui.p('[*] %s' % obj, objcolor)
        return self.ui
