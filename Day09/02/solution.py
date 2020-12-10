def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def hasSum(numList, sumsTo):
	for i in xrange(len(numList) - 1):
		for j in xrange(i + 1, len(numList)):
			if numList[i] != numList[j] and numList[i] + numList[j] == sumsTo:
				return True
	return False

def getBreakingNum(numbers):
	preambleLength = 25
	for start in xrange(preambleLength, len(numbers)):
		if not hasSum(numbers[start-preambleLength:start], numbers[start]):
			return numbers[start]

def getSubSetThatSumsUpTo(numList, sumsTo):
	for i in xrange(len(numList)):
		sumValue = 0
		indexExtendsTo = i
		while sumValue <= sumsTo and indexExtendsTo <= len(numList):
			sumValue = sum(numList[i: indexExtendsTo])
			if sumValue == sumsTo:
				return numList[i: indexExtendsTo]
			indexExtendsTo += 1

def solution():
	lines = getLines()
	numbers = map(lambda n: int(n), lines)
	sublist = getSubSetThatSumsUpTo(numbers, getBreakingNum(numbers))
	print min(sublist) + max(sublist)

solution()
