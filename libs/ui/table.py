# coding:utf-8

class TABLE:
	'''
	@desc: 表格输出
	@create: 2015/08/17
	'''
	def __init__(self, ui):
		self.ui = ui

	def __call__(self, title = False, size = [], menu = [], item = []):
		'''
		@param: Boolean{title} 输出标题(如果指定)
		@param: Array{size}    表格长度分配(总=80)
		@param: Array{menu}    表格菜单头
		@param: Array{item)    表格数据
		'''
		if title:
			self.ui.p('[*] %-s'%title, self.ui.BLUE)

		if len(item) == 0:
			if not title:
				self.ui.warning('No items!')
			return self.ui
		_line = '+'
		# 生成line
		for i in range(len(size)):
			_line += '-' * size[i]
			_line += '+'
		self.ui.p(_line, self.ui.GREY)
		# 输出menu
		self.ui.p('|', self.ui.GREY, False)
		for i in range(len(size)):
			self.ui.p(
				' %-s'%menu[i][:size[i]],
				self.ui.CYAN,
				False
			)
			self.ui.p(
				' ' * (size[i] - len(menu[i][:size[i]]) - 1),
				self.ui.GREY,
				False
			)
			self.ui.p(
				'|',
				self.ui.GREY,
				True if (len(size) - 1) == i else False
			)
		# line
		self.ui.p(_line, self.ui.GREY)
		# 输出item
		for ii in range(len(item)):
			_item = item[ii]
			self.ui.p('|', self.ui.GREY, False)
			for i in range(len(size)):
				_item[i] = str(_item[i])
				self.ui.p(
					' %-s'%_item[i][:(size[i] - 4)] + ('..' if len(_item[i]) > (size[i] - 4) else ''),
					self.ui.GREEN if i == 0 else self.ui.GREY,
					False
				)
				self.ui.p(
					' ' * (size[i] - len(_item[i][:size[i]]) - 2),
					self.ui.GREY,
					False
				)
				self.ui.p(
					' |',
					self.ui.GREY,
					True if (len(size) - 1) == i else False
				)
		# end line
		self.ui.p(_line, self.ui.GREY)
		return self.ui