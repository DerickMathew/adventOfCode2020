import re

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

def isValidEyeColor(color):
	validOptions = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return color in validOptions

def isValidHairColor(color):
	return bool(re.search('#[0-9abcdef]{6}', color))

def isValidPassportId(passportId):
	return bool(re.search('^[0-9]{9}$', passportId))

def getHeight(heightAsString):
	heightWithoutUnits = re.compile('^[0-9]*').search(heightAsString).group(0)
	return int(heightWithoutUnits)

def isValidHeight(height):
	resultInInches = re.compile('^[0-9]*in$').search(height)
	resultInCentimeters = re.compile('^[0-9]*cm$').search(height)
	if resultInInches:
		heightInInches = getHeight(height)
		return 59 <= heightInInches <= 76
	elif resultInCentimeters:
		heightInCentimeters = getHeight(height)
		return 150 <= heightInCentimeters <= 193
	return False

def isValidYearWithin(yearAsString, lowerLimit, upperLimit):
	if len(yearAsString) == 4:
		year = int(yearAsString)
		return lowerLimit <= year <= upperLimit
	return False

def isValidBirthYear(yearAsString):
	return isValidYearWithin(yearAsString, 1920, 2002)

def isValidIssueYear(yearAsString):
	return isValidYearWithin(yearAsString, 2010, 2020)

def isValidExpirationYear(yearAsString):
	return isValidYearWithin(yearAsString, 2020, 2030)

def validate(passport, code):
	if code == 'byr':
		return isValidBirthYear(passport[code])
	if code == 'eyr':
		return isValidExpirationYear(passport[code])
	if code == 'iyr':
		return isValidIssueYear(passport[code])
	if code == 'ecl':
		return isValidEyeColor(passport[code])
	if code == 'hcl':
		return isValidHairColor(passport[code])
	if code == 'pid':
		return isValidPassportId(passport[code])
	if code == 'hgt':
		return isValidHeight(passport[code])
	return False

def isValidPassport(passport):
	shortCodes = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
	validCodes = filter(lambda code: passport.has_key(code) and validate(passport, code), shortCodes)
	return len(validCodes) == len(shortCodes)

def solution():
	reportLines = getLines()
	passports = getPassports(reportLines)
	validPassportCount = sum(map(lambda passport: 1 if isValidPassport(passport) else 0,  passports))
	print validPassportCount

solution()
