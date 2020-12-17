def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def expandCube(cube):
	depth = len(cube) + 2
	height = len(cube[0]) + 2
	width = len(cube[0][0]) + 2
	emptyRow = ['.'] * width
	empty2DSpace = [emptyRow] * height
	# expand width
	for i in xrange(len(cube)):
		for j in xrange(len(cube[0])):
			updatedRow = ['.']
			updatedRow.extend(cube[i][j])
			updatedRow.append('.')
			cube[i][j] = updatedRow
	# expand height
	for i in xrange(len(cube)):
		updatedPlane = [emptyRow]
		for plane in cube[i]:
			updatedPlane.append(plane)
		updatedPlane.append(emptyRow)
		cube[i] = updatedPlane
	# expand depth
	updatedCube = [empty2DSpace]
	updatedCube.extend(cube)
	updatedCube.append(empty2DSpace)
	return updatedCube

def getActiveNeighbourCount(cube, x, y, z):
	activeNeighbourCount = 0
	for i in xrange(x - 1, x + 2):
		for j in xrange(y - 1, y + 2):
			for k in xrange(z - 1, z + 2):	
				if not (i == x and j == y and k == z ):
					if 0 <= i < len(cube):
						if 0 <= j < len(cube[0]):
							if 0 <= k < len(cube[0][0]):
								if cube[i][j][k] == '#':
									activeNeighbourCount += 1 
	return activeNeighbourCount

def getCubeAfterCycles(cube, cycles):
	if cycles == 0:
		return cube
	expandedCube = expandCube(cube)
	newCube = []
	for i in xrange(len(expandedCube)):
		newPlane = []
		for j in xrange(len(expandedCube[0])):
			newRow = []
			for k in xrange(len(expandedCube[0][0])):
				activeNeighbours = getActiveNeighbourCount(expandedCube, i, j, k)
				cell = expandedCube[i][j][k]
				if cell == '#':
					cell = '#' if 1 < activeNeighbours < 4 else '.'
				else:
					cell = '#' if activeNeighbours == 3 else '.'
				newRow.append(cell)
			newPlane.append(newRow)
		newCube.append(newPlane)
	# # uncomment to see each cycle
	# print '===================='
	# print 'Cycles Left : ' + str(cycles - 1)
	# print '===================='
	# for i in xrange(len(newCube)):
	# 	for j in xrange(len(newCube[0])):
	# 		print newCube[i][j]
	# 	print ' '
	# print ' '
	# print ' '
	return getCubeAfterCycles(newCube, cycles - 1)

def getActiveCellCount(cube):
	count = 0
	for i in xrange(len(cube)):
		for j in xrange(len(cube[0])):
			for k in xrange(len(cube[0][0])):
				count += 1 if cube[i][j][k] == '#' else 0
	return count

def solution():
	lines = getLines()
	cycles = 6
	cube = [map(lambda line: map(lambda char: char, line), lines)]
	lastCube = getCubeAfterCycles(cube, cycles)
	print getActiveCellCount(lastCube)

solution()
