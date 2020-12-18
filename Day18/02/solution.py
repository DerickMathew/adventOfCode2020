import re

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

def removeParenthesisRecursively(equation):
	if not (re.search('\(', equation)):
		return equation
	matchedEquation =  re.search('\([^\(\)]*\)', equation).group(0)
	startingIndex = equation.index(matchedEquation)
	newEquation = (
		equation[:startingIndex] +
		getflattenedEquation(matchedEquation[1:-1]) + 
		equation[(startingIndex + len(matchedEquation)):]
	)
	return removeParenthesisRecursively(newEquation)

def getflattenedEquation(equation):
	if not not (re.search('\(', equation)):
		return removeParenthesisRecursively(equation)
	return evaluateFlatEquation(equation)

def executeOperator(operators, operands, index):
	[leftOperand, rightOperand] = operands[index: index + 2]
	newOperand = leftOperand + rightOperand
	if operators[index] == '*':
		newOperand = leftOperand * rightOperand
	newOperands = operands[:index] + [newOperand] + operands[index + 2:]
	newOperators = operators[:index] + operators[index + 1:]
	return(newOperators, newOperands)

def evaluateFlatEquation(flatEquation):
	operators = re.findall('[+*]', flatEquation)
	operands = map(lambda n: int(n), re.findall('[0-9]+', flatEquation))
	while len(operators) > 0:
		operatorToExecute = operators.index('+') if '+' in operators else 0
		(operators, operands) = executeOperator(operators, operands, operatorToExecute)
	return str(operands[0])

def processEquation(equation):
	flatEquation = getflattenedEquation(equation)
	return evaluateFlatEquation(flatEquation)

def solution():
	lines = getLines()
	print(sum(map(lambda equation: int(processEquation(equation)), lines)))

solution()
