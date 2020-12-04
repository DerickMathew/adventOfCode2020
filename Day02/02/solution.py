def xor(bool1, bool2):
	return bool1 != bool2

def isCharInOnlyOnePosition(letter, password, position1, position2):
	isCharInFirstPosition = password[position1 - 1] == letter
	isCharInSecondPosition = password[position2 - 1] == letter
	return xor(isCharInFirstPosition, isCharInSecondPosition)

def getCharCountPositions(stringyfiedPositions):
	[position1, position2] = stringyfiedPositions.split('-')
	return [int(position1), int(position2)]

def isPolicySatisfied(policyAndPassword):
	[stringyfiedPositions, rawletter, password] = policyAndPassword.split(' ')
	[position1, position2] = getCharCountPositions(stringyfiedPositions)
	[letter, empty] = rawletter.split(':')
	return isCharInOnlyOnePosition(letter, password, position1, position2)

def solution():
	inputFile = open('../input.txt', 'r') 
	dbLines = inputFile.readlines()
	validPasswords = filter(lambda dbLine: isPolicySatisfied(dbLine), dbLines)
	print len(validPasswords)

solution()
