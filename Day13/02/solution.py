def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getInverseModulo(nByBusId, modOf):
	newModOf = modOf
	temp1, temp2 = 0, 1
	if modOf == 1:
		return 1
	while nByBusId > 1:
		quotient = nByBusId / modOf
		nByBusId, modOf = modOf, nByBusId % modOf
		temp1, temp2 = temp2 - (quotient * temp1), temp1
	if temp2 < 0:
		temp2 += newModOf
	return temp2

def findOptimalStart(buses):
	keys = buses.keys()
	busIds = map(lambda key: buses[key], keys)
	N = reduce(lambda x, y: x * y, busIds)
	modulo = map(lambda key: buses[key] - key, keys)
	nByBusId = map(lambda key: N / buses[key], keys)
	inverseModulo = []
	sumsTo = 0
	for i in xrange(len(nByBusId)):
		x = getInverseModulo(nByBusId[i], buses[keys[i]])
		inverseModulo.append(x)
		sumsTo += (modulo[i] * nByBusId[i] * x)
	return sumsTo % N


def solution():
	lines = getLines()
	counter = 0
	buses = {}
	for busId in lines[1].split(','):
		if busId.isdigit():
			buses[counter] = int(busId)
		counter += 1
	startTime = findOptimalStart(buses)
	print startTime

solution()

# 756261495958122