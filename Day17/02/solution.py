from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def expandHyperCube(hyperCube):
	timeFactor = len(hyperCube) + 2
	depth = len(hyperCube[0]) + 2
	height = len(hyperCube[0][0]) + 2
	width = len(hyperCube[0][0][0]) + 2
	emptyRow = ['.'] * width
	empty2DSpace = [emptyRow] * height
	empty3DSpace = [empty2DSpace] * depth
	updatedHyperCube = [empty3DSpace]
	for i in xrange(len(hyperCube)):
		updatedCube = [empty2DSpace]
		for j in xrange(len(hyperCube[0])):
			updated2DPlane = [emptyRow]
			for k in xrange(len(hyperCube[0][0])):
				plane = ['.']
				plane.extend(hyperCube[i][j][k])
				plane.append('.')
				updated2DPlane.append(plane)
			updated2DPlane.append(emptyRow)
			updatedCube.append(updated2DPlane)
		updatedCube.append(empty2DSpace)
		updatedHyperCube.append(updatedCube)
	updatedHyperCube.append(empty3DSpace)
	return updatedHyperCube

def getActiveNeighbourCount(cube, x, y, z, t):
	activeNeighbourCount = 0
	for i in xrange(x - 1, x + 2):
		for j in xrange(y - 1, y + 2):
			for k in xrange(z - 1, z + 2):	
				for l in xrange(t - 1, t + 2):	
					if not (i == x and j == y and k == z and l == t):
						if 0 <= i < len(cube):
							if 0 <= j < len(cube[0]):
								if 0 <= k < len(cube[0][0]):
									if 0 <= l < len(cube[0][0][0]):
										if cube[i][j][k][l] == '#':
											activeNeighbourCount += 1
	return activeNeighbourCount

def getHyperCubeAfterCycles(hyperCube, cycles):
	if cycles == 0:
		return hyperCube
	expandedCube = expandHyperCube(hyperCube)
	newHyperCube = []
	for i in xrange(len(expandedCube)):
		newCube = []
		for j in xrange(len(expandedCube[0])):
			newPlane = []
			for k in xrange(len(expandedCube[0][0])):
				newRow = []
				for l in xrange(len(expandedCube[0][0][0])):
					activeNeighbours = getActiveNeighbourCount(expandedCube, i, j, k, l)
					cell = expandedCube[i][j][k][l]
					if cell == '#':
						cell = '#' if 1 < activeNeighbours < 4 else '.'
					else:
						cell = '#' if activeNeighbours == 3 else '.'
					newRow.append(cell)
				newPlane.append(newRow)
			newCube.append(newPlane)
		newHyperCube.append(newCube)
	# # uncomment to see each cycle
	# print '===================='
	# print 'Cycles Left : ' + str(cycles - 1)
	# print '===================='
	# for i in xrange(len(newHyperCube)):
	# 	for j in xrange(len(newHyperCube[0])):
	# 		for k in xrange(len(newHyperCube[0][0])):
	# 			print newHyperCube[i][j][k]
	# 		print ' '
	# 	print ' '
	# print ' '
	# print ' '
	return getHyperCubeAfterCycles(newHyperCube, cycles - 1)

def getActiveCellCount(cube):
	count = 0
	for i in xrange(len(cube)):
		for j in xrange(len(cube[0])):
			for k in xrange(len(cube[0][0])):
				for l in xrange(len(cube[0][0][0])):
					count += 1 if cube[i][j][k][l] == '#' else 0
	return count

def solution():
	lines = getLines()
	start = time()
	cycles = 6
	hyperCube = [[map(lambda line: map(lambda char: char, line), lines)]]
	lastHyperCube = getHyperCubeAfterCycles(hyperCube, cycles)
	print getActiveCellCount(lastHyperCube)
	end = time()
	print end - start

solution()
