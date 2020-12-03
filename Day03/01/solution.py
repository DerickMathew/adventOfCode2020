
def solution():
	inputFile = open('../input.txt', 'r') 
	map = inputFile.readlines()
	mapHeight = len(map)
	[mapLine, empty] = map[0].split('\n')
	mapWidth = len(mapLine)
	rightVal = 3
	downVal = 1
	treesEncountered = 0
	position = rightVal
	for i in xrange(1, mapHeight):
		if map[i][position] == '#':
			treesEncountered += 1
		position += rightVal
		position = position % mapWidth
	print(treesEncountered)


solution()




