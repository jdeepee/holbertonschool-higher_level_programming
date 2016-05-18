''' class Number '''
class Number():

    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return str(self.__value)

    def __add__(self, other):
        ''' Our adding operator '''
        return self.get_value() + other.get_value()

    def __sub__(self, other):
        return self.get_value() - other.get_value()

    def __mul__(self, other):
        return self.get_value() * other.get_value()

    def __div__(self, other):
        return self.get_value() / other.get_value()

    def set_value(self, value):
        ''' setting value of private attribute value '''
        self.__value = value

    def get_value(self):
        ''' getting private attribute value '''
        return self.__value