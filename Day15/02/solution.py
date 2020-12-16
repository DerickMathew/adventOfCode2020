import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

# dictionaries are slow when the keys are densely populated 
def aSlowSolution():
	lines = getLines()
	start =  time.time()
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
	end = time.time()
	print end - start

def solution():
	lines = getLines()
	start =  time.time()
	problemLimit = 30000000
	numbers = map(lambda n: int(n), lines[0].split(','))
	lastNumber = numbers[-1]
	position = [-1] * problemLimit
	previous = [-1] * problemLimit
	for index in xrange(len(numbers)):
		position[numbers[index]] = index
	for i in range(len(numbers) - 1, problemLimit):
		newNumber = 0
		if not (previous[lastNumber] == -1):
			newNumber = position[lastNumber] - previous[lastNumber]
		previous[newNumber] = position[newNumber]
		position[newNumber] = i
		lastNumber = newNumber
	print lastNumber
	end = time.time()
	print end - start


solution()
