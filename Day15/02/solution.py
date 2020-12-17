from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

# dictionaries are slow when the keys are densely populated 
def aSlowMapSolution():
	lines = getLines()
	start =  time()
	numbers = map(lambda n: int(n), lines[0].split(','))
	lastNumber = numbers[-1]
	lastInstance = {}
	for index in xrange(len(numbers)):
		lastInstance[numbers[index]] = (index, -1)
	for i in xrange(len(numbers) - 1, 30000000):
		newNumber = 0
		(position, previous) = lastInstance[lastNumber]
		if not (previous == -1):
			newNumber = position - previous
		if not lastInstance.get(newNumber):
			lastInstance[newNumber] = (i, -1)
		else: 
			(newNumPosition, newNumPrevious) = lastInstance[newNumber]
			lastInstance[newNumber] = (i, newNumPosition)
		lastNumber = newNumber
	print lastNumber
	end = time()
	print end - start

def solution():
	lines = getLines()
	start = time()
	problemLimit = 30000000
	numbers = [int(n) for n in lines[0].split(',')]
	lastNumber = numbers[-1]
	previous = [-1] * problemLimit
	for index in xrange(len(numbers) - 1):
		previous[numbers[index]] = index
	for i in xrange(len(numbers) - 1, problemLimit - 1):
		newNumber = 0
		if not (previous[lastNumber] == -1):
			newNumber = i - previous[lastNumber]
		previous[lastNumber] = i 
		lastNumber = newNumber
	print(lastNumber)
	end = time()
	print(end - start)

solution()
