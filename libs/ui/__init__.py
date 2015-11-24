# coding:utf-8

import os
import sys
import platform

from help import HELP
from clear import CLEAR
from usage import USAGE
from table import TABLE
from notify import NOTIFY
from banner import BANNER
from hilight import HILIGHT


class UI(object):
	'''
	@desc:   终端颜色输出模块
	@create: 2015/08/17
	'''
	def __init__(self):
		'''
		@desc: 根据当前系统创建输出函数
		'''
		os_name = platform.uname()[0]
		self.IS_WIN = os_name == 'Windows'
		self.IS_MAC = os_name == 'Darwin'
		# colors
		if self.IS_WIN:
			# Windows
			self.RED    = 0x0C
			self.GREY   = 0x07
			self.BLUE   = 0x09
			self.CYAN   = 0x0B
			self.LINK   = 0x30
			self.BLACK  = 0x0
			self.GREEN  = 0x0A
			self.WHITE  = 0x0F
			self.PURPLE = 0x0D
			self.YELLOW = 0x0E
		else:
			# Other system(unix)
			self.RED    = '\033[1;31m'
			self.GREY   = '\033[38m'
			self.BLUE   = '\033[1;34m'
			self.CYAN   = '\033[36m'
			self.LINK   = '\033[0;36;4m'
			self.BLACK  = '\033[0m'
			self.GREEN  = '\033[32m'
			self.WHITE  = '\033[37m'
			self.PURPLE = '\033[35m'
			self.YELLOW = '\033[33m'
		# functions
		self.p = self.win_print if self.IS_WIN else self.os_print
		self.help = HELP(self)
		self.usage = USAGE(self)
		self.table = TABLE(self)
		self.clear = CLEAR(self)
		self.banner = BANNER(self)
		self.hilight = HILIGHT(self)
		# notify
		self.notify = NOTIFY(self)
		self.success = self.notify.success
		self.warning = self.notify.warning
		self.error = self.notify.error
		self.info = self.notify.info

	def win_reset(self, color):
		'''
		@desc:  重置终端颜色(for windows)
		'''
		from ctypes import windll
		handler = windll.kernel32.GetStdHandle(-11)
		return windll.kernel32.SetConsoleTextAttribute(handler, color)

	def win_print(self, msg, color, enter = True):
		'''
		@desc: 彩色输出函数(for windows)
		'''
		color = color or self.BLACK
		self.win_reset(color | color | color)
		sys.stdout.write(('%s\n' if enter else '%s') % msg)
		self.win_reset(self.RED | self.GREEN | self.BLUE)
		return self

	def os_print(self, msg, color, enter = True):
		'''
		@desc: 彩色输出函数(for unix[osx|linux..])
		'''
		color = color or self.BLACK
		sys.stdout.write(('%s%s%s\n' if enter else '%s%s%s') % (color, msg, self.BLACK))
		return self
