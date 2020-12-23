from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def moveCrabCup(cups, iterations):
	while iterations > 0:
		currentCup = cups[0]
		nextThree = cups[1:4]
		remainingCups = cups[4:]
		possibleDestinations = filter(lambda cup: cup < currentCup, remainingCups)
		if len(possibleDestinations) > 0:
			destination = map(lambda cup: cup, reversed(sorted(possibleDestinations)))[0]
		else:
			destination = map(lambda cup: cup, reversed(sorted(remainingCups)))[0]
		destinationIndex = remainingCups.index(destination)
		updatedCups = remainingCups[:destinationIndex + 1] + nextThree 
		updatedCups += remainingCups[destinationIndex + 1:]
		updatedCups += [currentCup]
		iterations -= 1
		cups = updatedCups
	return cups 

def getCupsAfter1(cups):
	onesIndex = cups.index(1)
	updatedCups = cups[onesIndex + 1:] + cups[:onesIndex]
	return ''.join(map(lambda n: str(n), updatedCups))

def solution():
	lines = getLines()
	cups = [int(i) for i in lines[0]]
	start = time()
	iterations = 100
	cups = moveCrabCup(cups, iterations)
	print getCupsAfter1(cups)
	end = time()
	print end - start

solution()
