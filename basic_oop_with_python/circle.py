import math

class Circle():
	def __init__(self, radius):
		self._radius = radius 

	def set_color(self, color):
		self._color = color

	def set_center(self, center):
		self._center = center

	def get_color(self):
		return self._color

	def get_center(self):
		return self._center

	def area(self):
		return self._radius**2*3.14

	def intersection(self, c_bis):
		d = math.sqrt((c_bis._center[1] - self._center[1])**2 + (c_bis._center[0] - self._center[0])**2) 
		total_radi = self._radius + c_bis._radius

		if total_radi > d:
			return True

		else:
			return False

	def intersection_percentage(self, c_bis):
		R = self._radius
		r = c_bis._radius
		d = math.sqrt((c_bis._center[1] - self._center[1])**2 + (c_bis._center[0] - self._center[0])**2)

		seg1 = r**2*math.acos((d**2+r**2-R**2)/(2*d*r)) + R**2*math.acos((d**2+R**2-r**2)/(2*d*R))
		seg2 = 0.5*(math.sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R)))

		return (seg1 - seg2) / self.area()
