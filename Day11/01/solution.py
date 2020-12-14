def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getNeigbourCount(seatingMap, x, y):
	neighbourCount = 0
	for neighbourY in xrange(y-1, y+2):
		for neighbourX in xrange (x-1, x+2):
			if 0 <=neighbourX < len(seatingMap[0]) and 0 <= neighbourY < len(seatingMap):
				if not(x == neighbourX and y == neighbourY):
					neighbourCount += 1 if seatingMap[neighbourY][neighbourX] == '#' else 0
	return neighbourCount

def getUpdatedSeatingMap(seatingMap):
	updatedSeatingMap = map(lambda line: map(lambda seat: seat, line), seatingMap)
	for y in xrange(len(updatedSeatingMap)):
		for x in xrange(len(updatedSeatingMap[y])): 
			location = seatingMap[y][x]
			if seatingMap[y][x] != '.':
				neighbourCount = getNeigbourCount(seatingMap, x, y)
				if neighbourCount == 0:
					location = '#'
				elif neighbourCount > 3:
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
