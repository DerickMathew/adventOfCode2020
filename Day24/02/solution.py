from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getTile(path):
	x, y = 0, 0
	while len(path) > 0:
		if path[0] in ['n','s']:
			y += 1 if path[0] == 'n' else -1
			x += 1 if path[1] == 'e' else -1
			path = path[2:]
		else:
			x += 2 if path[0] == 'e' else -2
			path = path[1:]
	return (x, y)

def getTiles(tilepaths):
	tiles = {}
	for tilepath in tilepaths:
		tile = getTile(list(tilepath))
		if not tile in tiles.keys():
			tiles[tile] = 0
		tiles[tile] += 1
	return tiles

def getNeighbours(x, y):
	return [
		(x + 2, y), (x - 2, y),
		(x + 1, y + 1), (x + 1, y - 1), 
		(x - 1, y + 1), (x - 1, y - 1)
	]

def addNeighbours(tiles):
	newTiles = {}
	for tile in map(lambda x: x, filter(lambda key: tiles[key] % 2 == 1, tiles)):
		newTiles[tile] = 1
		for neighbouringTile in getNeighbours(*tile):
			if not neighbouringTile in newTiles:
				newTiles[neighbouringTile] = 0
	return newTiles

def flipTiles(tiles):
	tiles = addNeighbours(tiles)
	newTiles = {}
	for tile in tiles:
		newTiles[tile] = tiles[tile]
		blackNeighborCount = 0
		for neighbouringTile in getNeighbours(*tile):
			if neighbouringTile in tiles and tiles[neighbouringTile] == 1:
				blackNeighborCount += 1
		if tiles[tile] % 2 == 1 and blackNeighborCount == 0 or blackNeighborCount > 2:
			newTiles[tile] = 0
		elif blackNeighborCount == 2:
			newTiles[tile] = 1
	return newTiles

def solution():
	lines = getLines()
	start = time()
	tiles = getTiles(lines)
	for i in xrange(100):
		tiles = flipTiles(tiles)
	print len(filter(lambda tile: tiles[tile] % 2 == 1, tiles))
	end = time()
	print end - start

solution()
