# coding:utf-8

class USAGE:
	'''
	@desc: 显示命令使用
	@create: 2015/08/17
	'''
	def __init__(self, ui):
		self.ui = ui

	def __call__(self, cmd = '', arg = ''):
		'''
		@desc:  显示命令帮助
		@param: String{cmd} 帮助命令
		@param: String{arg} 命令参数
		'''
		self.ui.p('[?] Usage: ', self.ui.YELLOW, False)
		self.ui.p('%s ' % cmd, self.ui.GREEN, False)
		self.ui.p(arg, self.ui.CYAN)
		return self.ui