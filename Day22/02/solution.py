from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def getCards(lines):
	isPlayer1 = True
	player1, player2 = [], []
	for line in lines:
		if line.isdigit() and isPlayer1:
			player1.append(int(line))
		elif line.isdigit() and not isPlayer1:
			player2.append(int(line))
		elif len(line) == 0:
			isPlayer1 = False
	return(player1, player2)

def playGame(player1, player2):
	history = set()
	while len(player1) > 0 and len(player2):
		if tuple(player1) in history:
			return (player1, [])
		history.add(tuple(player1))
		doesPlayer1WinRound = False
		p1Card, p2Card = player1[0], player2[0]
		player1, player2 = player1[1:], player2[1:]
		if p1Card <= len(player1) and p2Card <= len(player2):
			(p1,p2) = playGame(player1[:p1Card], player2[:p2Card])
			doesPlayer1WinRound = len(p1) > 0
		elif  p1Card > p2Card:
			doesPlayer1WinRound = True
		if doesPlayer1WinRound:
			player1.extend([p1Card, p2Card])
		else:
			player2.extend([p2Card, p1Card])
	return (player1, player2)

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
	(player1sCards, player2sCards) = playGame(player1, player2)
	winnersCards = player1sCards if len(player1sCards) > 0 else player2sCards
	score = getScore(winnersCards)
	print score
	end = time()
	print end - start

solution()
