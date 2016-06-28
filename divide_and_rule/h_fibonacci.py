import threading

class FibonacciThread(threading.Thread):
	def __init__(self, number):
		threading.Thread.__init__(self)
		
		if type(number) != int:
			raise Exception("number is not an integer")

		self.number = number

	def run(self):
		one = 0;
		two = 1;

		for x in range(self.number):
			(one, two) = (two, one + two)

		print str(self.number) + " => " + str(one);