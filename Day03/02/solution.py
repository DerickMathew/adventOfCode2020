def getBaseMap(rawMap):
	# clean trailing newline
	baseMap = map(lambda mapline: mapline.split('\n')[0], rawMap)
	return baseMap

def getMapDimensions(baseMap):
	height = len(baseMap)
	width = len(baseMap[0])
	return (height, width)

def getPathForSlope(baseMap, slope):
	(mapHeight, mapWidth) = getMapDimensions(baseMap)
	(slopeRight, slopeDown) = slope
	path = []
	position = 0
	for i in xrange(slopeDown, mapHeight, slopeDown):
		position = (position + slopeRight) % mapWidth
		path.append(baseMap[i][position])
	return path

def solution():
	inputFile = open('../input.txt', 'r') 
	baseMap = getBaseMap(inputFile.readlines())
	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	productOfTreesEncountered = 1
	for slope in slopes:
		path = getPathForSlope(baseMap, slope)
		treesEncountered = len(filter(lambda location: location == '#', path))
		productOfTreesEncountered *= treesEncountered
	print(productOfTreesEncountered)

solution()
