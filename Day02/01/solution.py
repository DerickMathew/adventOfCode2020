
def getCharCountLimits(stringyfiedLimits):
	[lowerLimit, upperLimit] = stringyfiedLimits.split('-')
	return [int(lowerLimit), int(upperLimit)]

def isPolicySatisfied(policyAndPassword):
	[stringyfiedLimits, rawletter, password] = policyAndPassword.split(' ')
	[lowerLimit, upperLimit] = getCharCountLimits(stringyfiedLimits)
	[letter, empty] = rawletter.split(':')
	letterCount = len(filter(lambda char: char == letter, password))
	return (lowerLimit <= letterCount) and (letterCount <= upperLimit)

def solution():
	inputFile = open('../input.txt', 'r') 
	dbLines = inputFile.readlines()
	validPasswords = filter(lambda dbLine: isPolicySatisfied(dbLine), dbLines)
	print len(validPasswords)

solution()
