

def getTreesEncounted(rightVal, downVal, dotMap, mapHeight, mapWidth):
	treesEncountered = 0
	position = rightVal
	for i in xrange(downVal, mapHeight, downVal):
		if dotMap[i][position] == '#':
			treesEncountered += 1
		position += rightVal
		position = position % mapWidth
	return treesEncountered


def solution():
	inputFile = open('../input.txt', 'r') 
	dotMap = inputFile.readlines()
	mapHeight = len(dotMap)
	[mapLine, empty] = dotMap[0].split('\n')
	mapWidth = len(mapLine)
	options = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	# options = [(1, 2)]
	product = 1
	for option in options:
		trees = getTreesEncounted(option[0], option[1], dotMap, mapHeight, mapWidth)
		# print(str(option[0]) + '\t' + str(option[1])+ '\t' + str(trees))
		product *= trees
	print(product)


solution()




