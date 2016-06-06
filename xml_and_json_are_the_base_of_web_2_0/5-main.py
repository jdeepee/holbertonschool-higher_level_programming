import json

from xml.dom.minidom import Document
from car import Car

def load(input): 
	if isinstance(input, dict):
		return {load(key): load(value)
				for key, value in input.iteritems()}

	elif isinstance(input, list):
		return [load(element) for element in input]

	elif isinstance(input, unicode):
		return input.encode('utf-8')

	return input

file = open('5-main.json') 
file_contents = load(json.loads(file.read()))
file.close

cars = [] # create empty arrays.
brands = []
doors = 0

doc = Document()
cars_parent = doc.createElement('cars')
doc.appendChild(cars_parent)

for i in file_contents: #Iterate through each element.
	c = Car(i)
	cars.append(c)
	brands.append(c.get_brand())
	doors += c.get_nb_doors()
	car_node = c.to_xml_node(doc)
	cars_parent.appendChild(car_node)

print len(set(brands)) 
print doors
print cars[3]
print doc.toxml(encoding='utf-8')