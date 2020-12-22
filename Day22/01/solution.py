from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getCards(lines):
	isPlayer1 = True
	player1, player2 = [], []
	for line in lines:
		if line.isdigit():
			if isPlayer1:
				player1.append(int(line))
			else:
				player2.append(int(line))
		elif len(line) == 0:
			isPlayer1 = False
	return(player1, player2)

def play(player1, player2):
	if len(player1) == 0:
		return(player2)
	if len(player2) == 0:
		return(player1)
	p1Card, p2Card = player1[0], player2[0]
	player1, player2 = player1[1:], player2[1:]
	if  p1Card > p2Card:
		player1.extend([p1Card, p2Card])
	else:
		player2.extend([p2Card, p1Card])
	return play(player1, player2)

def getScore(cards):
	score = 0
	while len(cards) > 0:
		score += (cards[0] * len(cards))
		cards = cards[1:]
	return score

def solution():
	lines = getLines()
	start = time()
	(player1, player2) = getCards(lines)
	winnersCards = play(player1, player2)
	score = getScore(winnersCards)
	print score
	end = time()
	print end - start

solution()
