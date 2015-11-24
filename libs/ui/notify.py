# coding:utf-8

import os

class NOTIFY:
	'''
	@desc: 输出信息
	@create: 2015/08/17
	'''
	def __init__(self, ui):
		self.ui = ui

	def error(self, msg = ''):
		'''
		@desc:  错误信息
		@param: String{msg} 要输出的文本
		'''
		self.ui.p('[!] %s' % msg, self.ui.RED)
		return self.ui

	def warning(self, msg = ''):
		'''
		@desc:  警告信息
		@param: String{msg} 要输出的文本
		'''
		self.ui.p('[-] %s' % msg, self.ui.YELLOW)
		return self.ui

	def info(self, msg = ''):
		'''
		@desc:  提示信息
		@param: String{msg} 要输出的文本
		'''
		self.ui.p('[*] %s' % msg, self.ui.CYAN)
		return self.ui

	def success(self, msg = ''):
		'''
		@desc:  成功信息
		@param: String{msg} 要输出的文本
		'''
		self.ui.p('[+] %s' % msg, self.ui.GREEN)
		return self.ui