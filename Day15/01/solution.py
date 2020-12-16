def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def solution():
	lines = getLines()
	numbers = map(lambda n: int(n), lines[0].split(','))
	print numbers
	counter = numbers[:]
	counted = {}
	for x in xrange(len(numbers)):
		counted[numbers[x]] = {'position': x, 'previous': -1}
	for i in xrange(len(numbers), 2020):
		newNumber = 0
		if not (counted[counter[i - 1]]['previous'] == -1):
			newNumber = counted[counter[i - 1]]['position'] - counted[counter[i - 1]]['previous']
		if not counted.has_key(newNumber):
			counted[newNumber] = {'position': i, 'previous': -1}
		counted[newNumber]['previous'] = counted[newNumber]['position']
		counted[newNumber]['position'] = i
		counter.append(newNumber)
	print counter[-1]

solution()
