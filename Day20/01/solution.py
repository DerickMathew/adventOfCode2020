from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getAllEdges(tile):
	edges = []
	edges.append(tile[0])
	edges.append([i for i in reversed(tile[0])])
	edges.append(tile[::-1][0])
	edges.append([i for i in reversed(tile[::-1][0])])
	edges.append(map(list,zip(*tile))[0])
	edges.append([i for i in reversed(map(list,zip(*tile))[0])])
	edges.append(map(list,zip(*tile))[::-1][0])
	edges.append([i for i in reversed(map(list,zip(*tile))[::-1][0])])
	return edges

def getOrientation(tiles):
	orientations = {
		'r0f0': tiles,
		'r0f1': map(lambda t: [i for i in reversed(t)], tiles),
		'r1f0': tiles[::-1],
		'r1f1': map(lambda t: [i for i in reversed(t)], tiles[::-1]),
		'r2f0': map(list,zip(*tiles)),
		'r2f1': map(lambda t: [i for i in reversed(t)], map(list,zip(*tiles))),
		'r3f0': map(list,zip(*tiles))[::-1],
		'r3f1': map(lambda t: [i for i in reversed(t)], map(list,zip(*tiles))[::-1])
	}
	return orientations

def getTiles(lines):
	tiles = {}
	tileNumber = -1
	originalTile = []
	for line in lines:
		if 'Tile' in line:
			tileNumber = int(line[5:-1])
		elif len(line) == 0:
			# tiles[tileNumber] = getOrientation(originalTile)
			edges = getAllEdges(originalTile)
			tiles[tileNumber] = {'tile': originalTile, 'edges': edges}
			originalTile = []
		else:
			originalTile.append(map(lambda c: c, line))
	if not tileNumber in tiles:
		# tiles[tileNumber] = getOrientation(originalTile)
		edges = getAllEdges(originalTile)
		tiles[tileNumber] = {'tile': originalTile, 'edges': edges}
	return tiles

def getMatches(tiles):
	matches = {}
	for tile in tiles:
		edgeCount = 0
		for otherTile in filter(lambda t: t != tile, tiles):
			for edge in tiles[tile]['edges']:
				if edge in tiles[otherTile]['edges']:
					edgeCount += 1
		matches[tile] = edgeCount
	return matches


def solution():
	lines = getLines()
	start = time()
	tiles = getTiles(lines)
	matches = getMatches(tiles)
	prod = 1
	for m in matches:
		prod *= m if matches[m] == 4 else 1
	print prod
	end = time()
	print end - start

solution()
