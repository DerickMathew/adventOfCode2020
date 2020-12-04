def getLines():
	inputFile = open('../input.txt', 'r') 
	return inputFile.readlines()

def getPassports(reportLines):
	passports = []
	newPassport = {}
	for line in reportLines:
		line = line.split('\n')[0]
		if len(line) == 0:
			passports.append(newPassport)
			newPassport = {}
		else:
			for keyValuePair in line.split(' '):
				[key, val] = keyValuePair.split(':')
				newPassport[key] = val
	passports.append(newPassport)
	return passports

def isValidPassport(passport):
	keys = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
	keyCount = sum(map(lambda key: 1 if passport.has_key(key) else 0, keys))
	return keyCount == 7

def solution():
	reportLines = getLines()
	passports = getPassports(reportLines)
	numberOfValidPassports = sum(map(lambda passport: 1 if isValidPassport(passport) else 0,  passports))
	print numberOfValidPassports

solution()
