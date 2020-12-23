from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def moveCrabCup(cups, currentCup, iterations):
	while iterations > 0:
		firstCup = cups[currentCup]['next']
		secondCup = cups[firstCup]['next']
		thirdCup = cups[secondCup]['next']
		fourthCup = cups[thirdCup]['next']
		destCounter = currentCup - 1
		destinationCup = -1
		while destinationCup == -1 and destCounter > 0:
			if not destCounter in [firstCup, secondCup, thirdCup]:
				destinationCup = destCounter
			destCounter -= 1 
		destCounter = 1000000 if destCounter == 0 else destCounter
		while destinationCup == -1:
			if not destCounter in [firstCup, secondCup, thirdCup]:
				destinationCup = destCounter
			destCounter -= 1 
		cups[currentCup]['next'] = fourthCup
		cups[thirdCup]['next'], cups[destinationCup]['next'] = cups[destinationCup]['next'], firstCup
		currentCup = cups[currentCup]['next']
		iterations -= 1
	return cups

def getCupsAfter1(cups):
	onesIndex = cups.index(1)
	updatedCups = cups[onesIndex + 1:] + cups[:onesIndex]
	return updatedCups

def solution():
	lines = getLines()
	start = time()
	cupHolders = [int(i) for i in lines[0]]
	cups = {}
	for i in xrange(len(cupHolders) - 1):
		cups[cupHolders[i]] = {'next': cupHolders[i+1]} 
	for i in xrange(len(cupHolders) + 1, 1000000):
		cups[i] = {'next': i+1}
	cups[cupHolders[len(cupHolders) - 1]] = {'next': len(cupHolders) + 1}
	cups[1000000] = {'next': cupHolders[0]}
	iterations = 10000000
	cups = moveCrabCup(cups, cupHolders[0], iterations)
	firstCupAfter1 = cups[1]['next']
	secondCupAfter1 = cups[firstCupAfter1]['next']
	print (firstCupAfter1, secondCupAfter1)
	print firstCupAfter1 * secondCupAfter1
	end = time()
	print end - start

solution()
