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

def solution():
	lines = getLines()
	start = time()
	tiles = getTiles(lines)	
	blackTileCount = len(filter(lambda tile: tiles[tile] % 2 == 1, tiles))
	print blackTileCount
	end = time()
	print end - start

solution()
