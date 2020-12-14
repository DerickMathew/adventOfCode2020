def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

[NORTH, EAST, SOUTH, WEST] = [0, 1, 2, 3]
compassDirections = [NORTH, EAST, SOUTH, WEST]

def moveShip(ship, instruction):
	action = instruction[0]
	distance = int(instruction[1:])
	if action == 'F':
		if ship['direction'] == EAST:
			ship['positionX'] += distance
		elif ship['direction'] == WEST:
			ship['positionX'] -= distance
		elif ship['direction'] == NORTH:
			ship['positionY'] += distance
		elif ship['direction'] == SOUTH:
			ship['positionY'] -= distance
	if action == 'R':
		ship['direction'] = compassDirections[(ship['direction'] + (distance // 90)) % 4]
	if action == 'L':
		ship['direction'] = compassDirections[(ship['direction'] - (distance // 90)) % 4]
	if action == 'N':
		ship['positionY'] += distance
	if action == 'S':
		ship['positionY'] -= distance
	if action == 'E':
		ship['positionX'] += distance
	if action == 'W':
		ship['positionX'] -= distance

def solution():
	instructions = getLines()
	ship = {'direction' : EAST, 'positionX': 0, 'positionY': 0}
	for instruction in instructions:
		moveShip(ship, instruction)
	print abs(ship['positionX']) + abs(ship['positionY'])

solution()
