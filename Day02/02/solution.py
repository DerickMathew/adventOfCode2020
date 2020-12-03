
def solution():
	inputFile = open('../input.txt', 'r') 
	passwordFile = inputFile.readlines()
	validPasswordCount = 0
	for line in passwordFile:
		[charRange, rawletter, password] = line.split(' ')
		[posOne, posTwo] = charRange.split('-')
		posOne = int(posOne)
		posTwo = int(posTwo)
		[letter, empty] = rawletter.split(':')
		letterCount = 0
		if (password[posOne - 1] == letter):
			if (password[posTwo - 1] != letter):
				validPasswordCount += 1
		else:			
			if (password[posTwo - 1] == letter):
				validPasswordCount += 1
	print (validPasswordCount)

solution()
