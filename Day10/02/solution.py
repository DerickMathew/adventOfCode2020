def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getIncrementCounts(sortedJoltages):
	journeyCount = []
	journeyCount.append(1) # There is always one way to start
	for journeyIndex in xrange(1, len(sortedJoltages)):
		myJourney = 0
		if sortedJoltages[journeyIndex] - 1 in sortedJoltages:
			myJourney += journeyCount[sortedJoltages.index(sortedJoltages[journeyIndex] - 1)]
		if sortedJoltages[journeyIndex] - 2 in sortedJoltages:
			myJourney += journeyCount[sortedJoltages.index(sortedJoltages[journeyIndex] - 2)]
		if sortedJoltages[journeyIndex] - 3 in sortedJoltages:
			myJourney += journeyCount[sortedJoltages.index(sortedJoltages[journeyIndex] - 3)]
		journeyCount.append(myJourney)
	return (max(journeyCount))

def solution():
	lines = getLines()
	joltages = map(lambda joltage: int(joltage), lines)
	joltages.extend([0, int(max(joltages)) + 3])
	sortedJoltages = sorted(joltages)
	print getIncrementCounts(sortedJoltages)

solution()
