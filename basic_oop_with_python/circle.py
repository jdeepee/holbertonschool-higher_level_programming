import math

''' class Circle '''
class Circle():
	def __init__(self, radius):
		self.__radius = radius 

	def set_color(self, color):
		self.__color = color

	def set_center(self, center):
		self.__center = center

	def get_color(self):
		return self.__color

	def get_center(self):
		return self.__center

	def area(self):
		''' function to return area of circle '''
		return self.__radius**2*math.pi

	def intersection(self, c_bis):
		''' function to tell if circles intersect or not '''
		d = math.sqrt((c_bis.__center[1] - self.__center[1])**2 + (c_bis.__center[0] - self.__center[0])**2) 
		total_radi = self.__radius + c_bis.__radius

		if total_radi > d:
			return True

		else:
			return False

	def intersection_percentage(self, c_bis):
		''' function to give the % amount they intersect '''
		R = self.__radius
		r = c_bis.__radius
		d = math.sqrt((c_bis.__center[1] - self.__center[1])**2 + (c_bis.__center[0] - self.__center[0])**2)

		seg1 = r**2*math.acos((d**2+r**2-R**2)/(2*d*r)) + R**2*math.acos((d**2+R**2-r**2)/(2*d*R))
		seg2 = 0.5*(math.sqrt((-d+r+R)*(d+r-R)*(d-r+R)*(d+r+R)))

		return (seg1 - seg2) / self.area() * 100
