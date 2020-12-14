def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def moveShip(ship, instruction):
	action = instruction[0]
	distance = int(instruction[1:])
	if action == 'F':
		ship['positionX'] += ship['waypointX'] * distance
		ship['positionY'] += ship['waypointY'] * distance
	if action == 'R':
		for turn in xrange(distance // 90):
			(x, y) = (ship['waypointX'], ship['waypointY'])
			(ship['waypointX'], ship['waypointY']) = (y, -x)
	if action == 'L':
		for turn in xrange(distance // 90):
			(x, y) = (ship['waypointX'], ship['waypointY'])
			(ship['waypointX'], ship['waypointY']) = (-y, x)
	if action == 'N':
		ship['waypointY'] += distance
	if action == 'S':
		ship['waypointY'] -= distance
	if action == 'E':
		ship['waypointX'] += distance
	if action == 'W':
		ship['waypointX'] -= distance

def solution():
	instructions = getLines()
	ship = {'positionX': 0, 'positionY': 0, 'waypointX': 10, 'waypointY': 1}
	for instruction in instructions:
		moveShip(ship, instruction)
	print abs(ship['positionX']) + abs(ship['positionY'])

solution()
