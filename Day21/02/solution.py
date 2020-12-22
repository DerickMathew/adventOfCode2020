from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

# @return foods :  { 0: {'ingredients':[], 'allergens': []}, ... }
def getFoodItems(lines):
	foods = {}
	for i in xrange(len(lines)):
		[rawIngredients, rawAllergens] = lines[i].split(' (contains ')
		ingredients = rawIngredients.split()
		allergens = [a.strip() for a in rawAllergens[:-1].split(',')]
		foods[i] = {
			'ingredients': ingredients,
			'allergens': allergens
		}
	return foods

def getUniqueIngredientsAndAllergens(foods):
	ingredients, allergens = set(), set()
	for item in foods:
		ingredients.update(foods[item]['ingredients'])
		allergens.update(foods[item]['allergens'])
	return (ingredients, allergens)

def getUnIdentifiedAllergen(allergens):
	unmappedAllergens = filter(lambda a: not allergens[a].has_key('ingredient'), allergens)
	chosenAllergen = unmappedAllergens[0]
	chosenTriggers = reduce(lambda f1, f2: set(f1).intersection(set(f2)), allergens[chosenAllergen]['foods'])
	for allergen in unmappedAllergens:
		triggers = reduce(lambda f1, f2: set(f1).intersection(set(f2)), allergens[allergen]['foods'])
		if len(triggers) < len(chosenTriggers):
			chosenTriggers = triggers
			chosenAllergen = allergen
	return chosenAllergen

def getIngredient(allergenMap, choosenAllergen):
	sets = 	map(lambda food: set(food), allergenMap[choosenAllergen]['foods'])
	ingredient = reduce(lambda food1, food2: food1.intersection(food2), sets)
	return list(ingredient)[0]

def eradicateIngredient(allergenMap, ingredient):
	for key in allergenMap:
		allergenMap[key]['foods'] = map(lambda food: filter(lambda i: i != ingredient, food), allergenMap[key]['foods'])
	return allergenMap

def getAllergenMap(foods, indredients, allergens):
	foodMap = foods.copy()
	allergenMap = {}
	for allergen in allergens:
		inFoods = []
		for item in foodMap:
			if allergen in foodMap[item]['allergens']:
				inFoods.append(foodMap[item]['ingredients'])
		allergenMap[allergen] = {'foods': inFoods}
	while len(allergenMap) != len(filter(lambda a: allergenMap[a].has_key('ingredient'), allergenMap)):
		allergen = getUnIdentifiedAllergen(allergenMap)
		allergenMap[allergen]['ingredient'] = getIngredient(allergenMap, allergen)
		allergenMap[allergen]['foods'] = []
		allergenMap = eradicateIngredient(allergenMap, allergenMap[allergen]['ingredient'])
	return allergenMap

def solution():
	lines = getLines()
	start = time()
	foods = getFoodItems(lines)
	(allIndredients, allAllergens) = getUniqueIngredientsAndAllergens(foods)
	allergenMap = getAllergenMap(foods, allIndredients, allAllergens)
	dangerList = map(lambda key: allergenMap[key]['ingredient'], sorted(allergenMap.keys()))
	print ','.join(dangerList)
	end = time()
	print end - start

solution()
