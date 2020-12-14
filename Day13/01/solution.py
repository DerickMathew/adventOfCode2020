def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getTimeToClosestBus(timeStart, busIds):
	counter = -1
	while 1:
		counter += 1
		for bus in busIds:
			if (timeStart + counter) % bus == 0:
				return (counter, bus)

def solution():
	lines = getLines()
	timeStart = int(lines[0])
	strBusIds = filter(lambda s: s.isdigit(), lines[1].split(','))
	busIds = map(lambda n: int(n), strBusIds)
	(timeWaited, busId) = getTimeToClosestBus(timeStart, busIds)
	print timeWaited * busId

solution()
