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

def getAddressesFromMask(maskedAddress):
	if len(filter(lambda x: x == 'X', maskedAddress)) == 0:
		return [getNumberFromBinaryArray(maskedAddress)]
	firstXIndex = maskedAddress.index('X')
	addresses = []
	for bit in [0, 1]:
		newAddress = maskedAddress[:]
		newAddress[firstXIndex] = bit
		addresses.extend(getAddressesFromMask(newAddress))
	return addresses

def getMaskedAddresses(mask, address):
	binaryAddress = get36BitBinaryArray(address)
	maskedAddress = []
	for pos in xrange(len(binaryAddress)):
		if mask[pos] == 'X':
			maskedAddress.append('X')
		elif mask[pos] == '0':
			maskedAddress.append(binaryAddress[pos])
		else:
			maskedAddress.append(1)
	addresses = getAddressesFromMask(maskedAddress)
	return addresses

def processLines(lines):
	mask = 'X' * 36
	memory = {}
	for line in lines:
		if line[:4] == 'mask':
			mask = line[7:]
		else:
			[rawAddress, value] = line.split(' = ')
			rawAddress = int(rawAddress[4:-1])
			value = int(value)
			for address in getMaskedAddresses(mask, rawAddress):
				memory[address] = value			
	return memory

def solution():
	lines = getLines()
	memory = processLines(lines)
	print sum(map(lambda key: memory[key], memory.keys()))

solution()