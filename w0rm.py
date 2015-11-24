#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Wormhole Exploit tool
---------------------
For baidu app (port:40310)
GitHub: https://github.com/medicean/w0rmHole
'''
import os
import sys
from libs.ui import UI
from libs.core.consoles import BaseConsole
from libs.core.config import (paths, TARGET)


def pathsInit():
    paths.ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    paths.LIBS_PATH = os.path.join(paths.ROOT_PATH, 'libs')
    paths.POC_PATH = os.path.join(paths.LIBS_PATH, 'poc')

def targetInit():

    if len(sys.argv) < 2:
        ui.banner().usage('./w0rm.py', 'target [port]')
        sys.exit(0)

    if len(sys.argv) == 2:
        port = 40310
    else:
        port = int(sys.argv[2])
    TARGET.RHOST = sys.argv[1]
    TARGET.RPORT = port
    sys.argv = sys.argv[0:1]

if __name__ == '__main__':
    ui = UI()
    pathsInit()
    targetInit()
    BaseConsole().check()
