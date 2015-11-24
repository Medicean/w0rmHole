# coding:utf-8

class HELP:
	'''
	@desc: 显示帮助菜单
	@create: 2015/08/17
	'''
	def __init__(self, ui):
		self.ui = ui

	def __call__(self, title = 'HELP MENU', options = []):
		'''
		@param: String{title}  菜单标题
		@param: Array{options} 菜单列表
		'''
		self.ui.p('[*] %s' % title.upper(), self.ui.BLUE)
		self.ui.p('    %s' % ('=' * len(title)), self.ui.GREY)
		for opt in options:
			if isinstance(opt[1], list):
				self.ui.p(' -  ', self.ui.YELLOW, False)
				self.ui.p(opt[0], self.ui.GREEN)
				for o in opt[1]:
					self.ui.p(' ' * 8, self.ui.BLACK, False)
					self.ui.p('%-15s' % o[0], self.ui.CYAN, False)
					self.ui.p('%-s' % o[1], self.ui.GREY)
			else:
				self.ui.p('    %-19s' % opt[0], self.ui.GREEN, False)
				self.ui.p('%-s' % opt[1], self.ui.GREY)
		return self.ui