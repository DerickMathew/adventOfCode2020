from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getAllOrientations(tile):
	return [ 
		tile,
		map(lambda t: [i for i in reversed(t)], map(list,zip(*tile))),
		tile[::-1],
		map(list,zip(*tile))[::-1],
		map(lambda t: [i for i in reversed(t)], tile),
		map(list,zip(*tile)),
		map(lambda t: [i for i in reversed(t)], tile[::-1]),
		map(lambda t: [i for i in reversed(t)], map(list,zip(*tile))[::-1])	
	]

def getTiles(lines):
	tiles = {}
	tileNumber = -1
	originalTile = []
	for line in lines:
		if 'Tile' in line:
			tileNumber = int(line[5:-1])
		elif len(line) == 0:
			tiles[tileNumber] = originalTile
			originalTile = []
		else:
			originalTile.append(map(lambda c: c, line))
	if not tileNumber in tiles:
		tiles[tileNumber] = originalTile
	return tiles

def getTilePositions(tiles, tileMap, placedTiles):
	if len(tiles) == len(placedTiles):
		return tileMap
	for tile in filter(lambda key: key not in placedTiles, tiles.keys()):
		for orientation in getAllOrientations(tiles[tile]):
			for (x, y) in tileMap.keys():
				if not (x, y + 1) in tileMap.keys(): # above
					topEdge = tileMap[(x, y)][0]
					bottomEdge = orientation[len(orientation) - 1]
					if topEdge == bottomEdge:
						placedTiles.append(tile)
						tileMap[(x, y + 1)] = orientation
						return getTilePositions(tiles, tileMap, placedTiles)
				if not (x, y - 1) in tileMap.keys(): # below
					topEdge = orientation[0]
					bottomEdge = tileMap[(x, y)][len(orientation) - 1]
					if topEdge == bottomEdge:
						placedTiles.append(tile)
						tileMap[(x, y - 1)] = orientation
						return getTilePositions(tiles, tileMap, placedTiles)
				if not (x - 1, y) in tileMap.keys(): # left
					leftEdge = map(lambda line: line[0], tileMap[(x, y)])
					rightEdge = map(lambda line: line[-1], orientation)
					if leftEdge == rightEdge:
						placedTiles.append(tile)
						tileMap[(x - 1, y)] = orientation
						return getTilePositions(tiles, tileMap, placedTiles)
				if not (x + 1, y) in tileMap.keys(): # right
					rightEdge = map(lambda line: line[-1], tileMap[(x, y)])
					leftEdge = map(lambda line: line[0], orientation)
					if leftEdge == rightEdge:
						placedTiles.append(tile)
						tileMap[(x + 1, y)] = orientation
						return getTilePositions(tiles, tileMap, placedTiles)

def removeBorder(tile):
	image = []
	for line in tile[1:-1]:
		image.append(''.join(line[1:-1]))
	return image

def getImage(tiles):
	tileMap = {}
	tileMap[(0,0)] = tiles[tiles.keys()[0]]
	placedTiles = [tiles.keys()[0]]
	updatedTileMap = getTilePositions(tiles, tileMap, placedTiles)
	xSet = set()
	ySet = set()
	for (x, y) in updatedTileMap.keys():
		updatedTileMap[(x, y)] = removeBorder(updatedTileMap[(x, y)])
		xSet.add(x)
		ySet.add(y)
	image = []
	for y in reversed(sorted(ySet)):
		imageLine = []
		for x in sorted(xSet):
			imageLine.append(updatedTileMap[(x,y)])
		for line in zip(*imageLine):
			image.append(list(''.join(line)))
	return image

def hasSeaMonster(image, y, x):
	checklist = []
	checklist.append(image[y][x + 18])
	checklist.append(image[y + 1][x])
	checklist.append(image[y + 1][x + 5])
	checklist.append(image[y + 1][x + 6])
	checklist.append(image[y + 1][x + 11])
	checklist.append(image[y + 1][x + 12])
	checklist.append(image[y + 1][x + 17])
	checklist.append(image[y + 1][x + 18])
	checklist.append(image[y + 1][x + 19])
	checklist.append(image[y + 2][x + 1])
	checklist.append(image[y + 2][x + 4])
	checklist.append(image[y + 2][x + 7])
	checklist.append(image[y + 2][x + 10])
	checklist.append(image[y + 2][x + 13])
	checklist.append(image[y + 2][x + 16])
	return len(filter(lambda x: x != '#', checklist)) == 0

def getSeaMonsterCount(image):
	seaMonsterHeight = 3
	seaMonsterLength = 20
	seaMonsterCount = 0 
	for y in xrange(len(image) - seaMonsterHeight):
		for x in xrange(len(image[0]) - seaMonsterLength):
			seaMonsterCount += 1 if hasSeaMonster(image, y, x) else 0
	return seaMonsterCount

def getSeasRoughness(images):
	seaMonsterCount = max(map(lambda image: getSeaMonsterCount(image), images))
	seaMonsterPixelCount = 15 * seaMonsterCount
	hashCount = sum(map(lambda l: len(filter(lambda p: p == '#', l)), images[0]))
	return hashCount - seaMonsterPixelCount

def solution():
	lines = getLines()
	start = time()
	tiles = getTiles(lines)
	image = getImage(tiles)
	images = getAllOrientations(image)
	print getSeasRoughness(images)
	end = time()
	print end - start


def markSeaMonster(image, y, x):
	checklist = []
	checklist.append(image[y][x + 18])
	checklist.append(image[y + 1][x])
	checklist.append(image[y + 1][x + 5])
	checklist.append(image[y + 1][x + 6])
	checklist.append(image[y + 1][x + 11])
	checklist.append(image[y + 1][x + 12])
	checklist.append(image[y + 1][x + 17])
	checklist.append(image[y + 1][x + 18])
	checklist.append(image[y + 1][x + 19])
	checklist.append(image[y + 2][x + 1])
	checklist.append(image[y + 2][x + 4])
	checklist.append(image[y + 2][x + 7])
	checklist.append(image[y + 2][x + 10])
	checklist.append(image[y + 2][x + 13])
	checklist.append(image[y + 2][x + 16])
	monsterMap = [
		(y, x + 18), (y + 1, x), 
		(y + 1, x + 5), (y + 1, x + 6),
		(y + 1, x + 11), (y + 1, x + 12),
		(y + 1, x + 17), (y + 1, x + 18),
		(y + 1, x + 19), (y + 2, x + 1),
		(y + 2, x + 4), (y + 2, x + 7),
		(y + 2, x + 10), (y + 2, x + 13),
		(y + 2, x + 16)
	]
	if len(filter(lambda x: x != '#', checklist)) != 0:
		return image
	newImage = []	
	for y in xrange(len(image)):
		newImage.append(image[y][:])
		for x in xrange(len(image)):
			if (y, x) in monsterMap:
				newImage[y][x] = 'O'
	return newImage

def markSeaMonsters(image):
	seaMonsterHeight = 3
	seaMonsterLength = 20
	seaMonsterCount = 0 
	for y in xrange(len(image) - seaMonsterHeight):
		for x in xrange(len(image[0]) - seaMonsterLength):
			if hasSeaMonster(image, y, x):
				image = markSeaMonster(image, y, x)
	return image

def printSeaMonsterMap():
	lines = getLines()
	start = time()
	tiles = getTiles(lines)
	image = getImage(tiles)
	images = getAllOrientations(image)
	seaMonsterImage = filter(lambda image: getSeaMonsterCount(image), images)[0]
	mappedSeaMonsters = markSeaMonsters(seaMonsterImage)
	print ''
	for line in mappedSeaMonsters:
		print ''.join(line)
	print ''

solution()
printSeaMonsterMap()
