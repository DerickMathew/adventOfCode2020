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
	for seat in xrange(2**10):
		if seat not in takenSeats:
			if (seat + 1) in takenSeats and (seat - 1) in takenSeats:
				mySeat = seat
	print mySeat

solution()
