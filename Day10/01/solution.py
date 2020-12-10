def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getIncrementCounts(sortedJoltages):
	(oneJump, twoJump, threeJump) = (0, 0, 0)
	for joltageIndex in xrange(len(sortedJoltages) - 1):
		if sortedJoltages[joltageIndex] + 1 == sortedJoltages[joltageIndex + 1]:
			oneJump += 1
		elif sortedJoltages[joltageIndex] + 2 == sortedJoltages[joltageIndex + 1]:
			twoJump += 1
		elif sortedJoltages[joltageIndex] + 3 == sortedJoltages[joltageIndex + 1]:
			threeJump += 1
	return (oneJump, twoJump, threeJump)


def solution():
	lines = getLines()
	joltages = map(lambda joltage: int(joltage), lines)
	joltages.extend([0, int(max(joltages)) + 3])
	sortedJoltages = sorted(joltages)
	(oneJump, twoJump, threeJump) = getIncrementCounts(sortedJoltages)
	print oneJump * threeJump

solution()
