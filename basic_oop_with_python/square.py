class Square():
	def __init__(self, side_length):
		self._side_length = side_length

	def set_center(self, center):
		self._center = center

	def set_color(self, color):
		self._color = color

	def get_color(self):
		return self._color

	def get_center(self):
		return self._center

	def area(self):
		return self._side_length * self._side_length

	def print_square(self):
		if (self._side_length == 1):
			print "*"

		else:
			i = 0
			gap = self._side_length - 4
			height = self._side_length - 2

			print "*" * self._side_length

			while(i < height):
				print "*",
				print " " * gap,
				print "*"

				i += 1

			print "*" * self._side_length
