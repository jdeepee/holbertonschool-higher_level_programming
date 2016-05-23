from datetime import datetime
import math, json, os

class Person():
	EYES_COLORS = ["Blue", "Green", "Brown"]
	GENRES = ["Female", "Male"]

	def __init__(self, id, first_name, date_of_birth, genre, eyes_color, is_married_to=0, last_name=None, children=[]):
		if id < 0 or type(id) != int:
			raise Exception("id is not an integer")

		if len(first_name) < 1 or type(first_name) != str:
			raise Exception("string is not a string")

		if len(date_of_birth) != 3:
			raise Exception("date_of_birth is not a valid date")

		if type(date_of_birth[0]) != int or type(date_of_birth[1]) != int or type(date_of_birth[2]) != int:
			raise Exception("date_of_birth is not a valid date")

		if genre not in self.GENRES or type(genre) != str:
			raise Exception("genre is not valid")

		if eyes_color not in self.EYES_COLORS or type(eyes_color) != str:
			raise Exception("eyes_color is not valid")

		self.__id = id
		self.__eyes_color = eyes_color
		self.__genre = genre
		self.__date_of_birth = date_of_birth
		self.__first_name = first_name
		self.last_name = last_name
		self.is_married_to = is_married_to
		self.children = children[:]

	def get_id(self):
		return self.__id

	def get_eyes_color(self):
		return self.__eyes_color

	def get_genre(self):
		return self.__genre

	def get_date_of_birth(self):
		return self.__date_of_birth

	def get_first_name(self):
		return self.__first_name

	def __str__(self):
		string = self.__first_name+" "+self.last_name
		return string

	def __repr__(self):
		return self.__str__()

	def is_male(self):
		if self.__genre == "Male":
			return True
		else:
			return False

	def can_be_married(self):
		return any(isinstance(self, person_type) for person_type in [Adult, Senior])

	def is_married(self):
		if self.is_married_to:
			return True
		return False

	def divorce(self, p):
		if not self.__id == p.is_married_to or not p.__id == self.is_married_to:
			raise Exception("Not married to each other")
		self.is_married_to = 0
		p.is_married_to = 0

	def just_married_with(self, p):
		if p.is_married() or self.is_married():
			raise Exception("Already married")

		if not p.can_be_married() or not self.can_be_married():
			raise Exception("Can't be married")

		self.is_married_to = p.__id
		p.is_married_to = self.__id
		if {self.__gender, p.__gender} == {"Male", "Female"}:
			if p.__gender == "Male" and p.last_name:
				self.last_name = p.last_name
			elif self.__gender == "Male" and self.last_name:
				p.last_name = self.last_name

	def can_have_child(self):
		return isinstance(self, Adult)

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color=None, married_to=0, last_name=None):
		if not all(person.can_have_child() for person in [self, p]) or p is None:
			raise Exception("Can't have baby")

		if type(id) != int or id < 0:
			raise Exception("id is not an integer")

		if type(first_name) != str or first_name == '':
			raise Exception("string is not a string")

		if not all(isinstance(n, int) for n in date_of_birth) or len(date_of_birth) != 3:
			raise Exception("date_of_birth is not a valid date")

		if not type(genre) != str or not genre in self.GENRES:
			raise Exception("genre is not valid")

		if eyes_color and (not isinstance(eyes_color, str) or not eyes_color in self.EYES_COLORS):
			raise Exception("eyes_color is not valid")

		if not eyes_color:
			if any(color == "Brown" for color in [self.__eyes_color, p.__eyes_color]):
				eyes_color = "Brown"

			elif any(color == "Blue" for color in [self.__eyes_color, p.__eyes_color]):
				eyes_color = "Blue"

			else:
				eyes_color = "Green"

		baby = Baby(id, first_name, date_of_birth, genre, eyes_color, married_to, last_name)
		self.children.append(id)
		p.children.append(id)
		return baby

	def adopt_child(self, c):
		if not self.can_have_child():
			raise Exception("Can't adopt child")
		self.children.append(c.__id)


	def age(self):
		ref_date = "05/20/2016"
		bd = str(self.__date_of_birth[0])+"/"+str(self.__date_of_birth[1])+"/"+str(self.__date_of_birth[2])
		d1 = datetime.strptime(ref_date, "%m/%d/%Y")
		d2 = datetime.strptime(bd, "%m/%d/%Y")

		days_between = abs((d1 - d2).days)
		years = int(math.floor(days_between/365.242199))
		return years

	def json(self):
		return {
			"id": self.__id,
			"eyes_color": self.__eyes_color,
			"genre": self.__genre,
			"date_of_birth": self.__date_of_birth,
			"first_name": self.__first_name,
			"last_name": self.last_name,
			"is_married_to": self.is_married_to,
			"children": self.children
		}


	def load_from_json(self, json):
		if type(json) != dict:
			raise Exception("json is not valid")

		self.__id = json['id']
		self.__eyes_color = json['eyes_color']
		self.__genre = json['genre']
		self.__date_of_birth = json['date_of_birth']
		self.__first_name = json['first_name']
		self.__last_name = json['last_name']
		self.__is_married_to = json['is_married_to']

	def __cmp__(self, other):
		if self.age() == other.age():
			return True
		return False

	def __lt__(self, other):
		if self.age() < other.age():
			return True
		return False

	def __le__(self, other):
		if self.age() <= other.age():
			return True
		return False

	def __ne__(self, other):
		if self.age() != other.age():
			return True
		return False

	def __gt__(self, other):
		if self.age() > other.age():
			return True
		return False

	def __ge__(self, other):
		if self.age() >= other.age():
			return True
		return False

class Baby(Person):
	def can_run(self):
		return False

	def need_help(self):
		return True

	def is_young(self):
		return True

	def can_vote(self):
		return False

	def can_be_married(self):
		return False

	def can_have_child(self):
		return False

	def is_married(self):
		return False

	def divorce(self, p):
		raise Exception("Not currently married")

	def just_married_with(self, p):
		raise Exception("Can't be married")

	def can_have_child(self):
		return False

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
		raise Exception("Can't have a child")

	def adopt_child(self, c):
		raise Exception("Can't adopt a person")

	def who_are_my_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [person for person in list_person if self.get_id() in person.children]

	def who_are_my_grand_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [person for list2 in [grandparent for grandparent in [parent.who_are_my_parents(list_person) for parent in self.who_are_my_parents(list_person)]] for person in list2]

class Teenager(Person):
	def can_run(self):
		return True

	def need_help(self):
		return False

	def is_young(self):
		return True

	def can_vote(self):
		return False

	def can_be_married(self):
		return False

	def can_have_child(self):
		return False

	def is_married(self):
		return False

	def divorce(self, p):
		raise Exception("Not currently married.")

	def just_married_with(self, p):
		raise Exception("Can't be married")

	def can_have_child(self):
		return False

	def has_child_with(self, p, id, first_name, date_of_birth, genre, eyes_color):
		raise Exception("Can't have a child")

	def adopt_child(self, c):
		raise Exception("Can't adopt a person")

	def who_are_my_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [person for person in list_person if self.get_id() in person.children]

	def who_are_my_grand_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [person for list2 in [grandparent for grandparent in [parent.who_are_my_parents(list_person) for parent in self.who_are_my_parents(list_person)]] for person in list2]


class Adult(Person):
    def can_run(self):
        return True

    def need_help(self):
        return False

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def can_have_child(self):
        return True

	def who_are_my_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [person for person in list_person if self.get_id() in person.children]

	def who_are_my_grand_parents(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [person for list2 in [grandparent for grandparent in [parent.who_are_my_parents(list_person) for parent in self.who_are_my_parents(list_person)]] for person in list2]


class Senior(Person):
    def can_run(self):
        return False

    def need_help(self):
        return True

    def is_young(self):
        return False

    def can_vote(self):
        return True

    def can_be_married(self):
        return True

    def can_have_child(self):
        return False

	def who_are_my_grandchildren(self, list_person):
		if not list_person or not isinstance(list_person, list) or not all(isinstance(person, Person) for person in list_person):
			raise Exception("list_person is not valid")

		return [grandchild for grandchild in list_person if grandchild.get_id() in [person for list2 in [child.children for child in [person for person in list_person if person.get_id() in self.children]] for person in list2]]

def save_to_file(list, filename):
    output_list = []
    for person in list:
        data = person.json()
        data['type'] = person.__class__.__name__
        output_list.append(data)

    f = open(filename, 'w')
    f.write(json.dumps(output_list))
    f.close()

def load_from_file(filename):
	f = open(filename, 'r')
	data = f.read()
	data = json.loads(data)
	family = list()
	new_person = [0, 'new', [1,1,1], 'Male', 'Brown']
	for person in data:
		if person['type'] == 'Baby':
			new = Baby(new_person[0], new_person[1], new_person[2], new_person[3], new_person[4])
		elif person['type'] == 'Teenager':
			new = Teenager(new_person[0], new_person[1], new_person[2], new_person[3], new_person[4])
		elif person['type'] == 'Adult':
			new = Adult(new_person[0], new_person[1], new_person[2], new_person[3], new_person[4])
		elif person['type'] == 'Senior':
			new = Senior(new_person[0], new_person[1], new_person[2], new_person[3], new_person[4])
		new.load_from_json(person)
		family.append(new)
	f.close()
	return family
