def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def get36BitBinaryArray(value):
	binaryArray = []
	counter = 0
	while counter < 36:
		binaryArray.append(value % 2)
		value = value // 2
		counter += 1
	binaryArray = [n for n in reversed(binaryArray)]
	return binaryArray

def getNumberFromBinaryArray(binaryArray):
	binaryArray = [n for n in reversed(binaryArray)]
	power = 0
	number = 0
	for bit in binaryArray:
		number += bit * (2 ** power)
		power += 1
	return number

def getMaskedValue(mask, value):
	binaryArray = get36BitBinaryArray(value)
	outputValueBinary = []
	for pos in xrange(len(binaryArray)):
		if mask[pos] == 'X':
			outputValueBinary.append(binaryArray[pos])
		else:
			outputValueBinary.append(int(mask[pos]))
	return getNumberFromBinaryArray(outputValueBinary)

def processLines(lines):
	mask = 'X' * 36
	memory = {}
	for line in lines:
		if line[:4] == 'mask':
			mask = line[7:]
		else:
			[address, value] = line.split(' = ')
			address = int(address[4:-1])
			value = int(value)
			maskedValue = getMaskedValue(mask, value)
			memory[address] = maskedValue
	return memory

def solution():
	lines = getLines()
	memory = processLines(lines)
	print sum(map(lambda key: memory[key], memory.keys()))

solution()