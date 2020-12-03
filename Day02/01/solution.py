
def solution():
	inputFile = open('../input.txt', 'r') 
	passwordFile = inputFile.readlines()
	validPasswordCount = 0
	for line in passwordFile:
		[charRange, rawletter, password] = line.split(' ')
		[lowerRange, upperRange] = charRange.split('-')
		lowerRange = int(lowerRange)
		upperRange = int(upperRange)
		[letter, empty] = rawletter.split(':')
		letterCount = 0
		for char in password:
			if char == letter:
				letterCount += 1
		if (lowerRange <= letterCount) and (letterCount <= upperRange):
			validPasswordCount += 1
	print (validPasswordCount)

solution()
