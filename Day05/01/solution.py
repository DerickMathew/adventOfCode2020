def getLines():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def getSeatNumber(boardingPass):
	decimal = 0
	for letter in boardingPass:
		if letter in 'fFbBlLrR':
			decimal *= 2
			decimal += 1 if letter in 'BbRr' else 0
	return decimal

def solution():
	passes = getLines()
	takenSeats = map(lambda boardingpass: getSeatNumber(boardingpass), passes)
	print max(takenSeats)

solution()
