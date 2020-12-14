import math

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def isVisualNeighourOccupied(seatingMap, x, y, xPlus, yPlus):
	if 0 > (y + yPlus) or (y + yPlus) >= len(seatingMap):
		return False
	if  0 > (x + xPlus) or (x + xPlus) >= len(seatingMap[0]):
		return False
	if seatingMap[y + yPlus][x + xPlus] == 'L':
		return False
	if seatingMap[y + yPlus][x + xPlus] == '#':
		return True
	return isVisualNeighourOccupied(seatingMap, x + xPlus, y + yPlus, xPlus, yPlus)

def getVisualNeigbourCount(seatingMap, x, y):
	visuallyOccupiedCount = 0
	for i in xrange(-1, 2):
		for j in xrange(-1, 2):
			if not(i == 0 and j == 0):
				visuallyOccupiedCount += 1 if isVisualNeighourOccupied(seatingMap, x, y, i, j) else 0
	return visuallyOccupiedCount

def getUpdatedSeatingMap(seatingMap):
	updatedSeatingMap = map(lambda line: map(lambda seat: seat, line), seatingMap)
	for y in xrange(len(updatedSeatingMap)):
		for x in xrange(len(updatedSeatingMap[y])): 
			location = seatingMap[y][x]
			if seatingMap[y][x] != '.':
				neighbourCount = getVisualNeigbourCount(seatingMap, x, y)
				if neighbourCount == 0:
					location = '#'
				elif neighbourCount > 4:
					location = 'L'
			updatedSeatingMap[y][x] = location
	return updatedSeatingMap

def getOccupiedSeatCount(seatingMap):
	return sum(map(lambda row: len(filter( lambda seat: seat == '#', row)), seatingMap))

def isIdenticalMap(map1, map2):
	for y in xrange(len(map1)):
		for x in xrange(len(map1[y])):
			if map1[y][x] != map2[y][x]:
				return False
	return True
			
def solution():
	lines = getLines()
	seatingMap = map(lambda line: map(lambda seat: seat, line), lines)
	updatedSeatingMap = getUpdatedSeatingMap(seatingMap)
	while not isIdenticalMap(seatingMap, updatedSeatingMap):
		seatingMap = []
		for y in xrange(len(updatedSeatingMap)):
			seatingMap.append(updatedSeatingMap[y][:])
		updatedSeatingMap = getUpdatedSeatingMap(seatingMap)
	print getOccupiedSeatCount(seatingMap)

solution()
