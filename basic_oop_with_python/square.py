class Square():
	def __init__(self, side_length):
		self.__side_length = side_length

	def set_center(self, center):
		self._center = center

	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def get_center(self):
		return self._center

	def area(self):
		return self.__side_length * self.__side_length

	def __print_top_bottom(self):
		i = 0
		line = ''
		while i < self.__side_length:
			line += "*"
			i += 1

		return line 

	def __print_middle(self):
		i = 0;
		line = ''
		while i < self.__side_length:
			if i == 0 or i == self.__side_length - 1:
				line += '*'
				i += 1
			else:
				line += ' '
				i += 1
		return line

	def __call__(self):
		if self.__side_length <= 0:
			return ''

		elif self.__side_length == 1:
			return '*'

		else:
			i = 2
			square = ''
			square += self.__print_top_bottom() + '\n'

			while i < self.__side_length:
				square += self.__print_middle() + '\n'
				i += 1

			square += self.__print_top_bottom()

			return square
