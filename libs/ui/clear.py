# coding:utf-8

import os

class CLEAR:
	'''
	@desc: 清空屏幕
	@create: 2015/08/17
	'''
	def __init__(self, ui):
		self.ui = ui

	def __call__(self):
		os.system('cls' if self.ui.IS_WIN else 'clear')
		return self.ui