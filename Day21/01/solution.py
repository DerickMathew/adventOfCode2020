from time import time

def getLines():
	inputFile = open('../input.txt', 'r') 
	lines = inputFile.readlines()
	return map(lambda line: line.split('\n')[0], lines)

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
	ingredients = set()
	allergens = set()
	for item in foods:
		ingredients.update(foods[item]['ingredients'])
		allergens.update(foods[item]['allergens'])
	return (ingredients, allergens)

def getUnIdentifiedAllergen(allergenMap):
	unidentifiedAllergens = filter(lambda a: not allergenMap[a].has_key('ingredient'), allergenMap)
	chosenAllergen = unidentifiedAllergens[0]
	chosenOptions = reduce(lambda food1, food2: set(food1).intersection(set(food2)), allergenMap[chosenAllergen]['foods'])
	for allergen in unidentifiedAllergens:
		allergenOptions = reduce(lambda food1, food2: set(food1).intersection(set(food2)), allergenMap[allergen]['foods'])
		if len(allergenOptions) < len(chosenOptions):
			chosenOptions = allergenOptions
			chosenAllergen = allergen
	return chosenAllergen

def getIngredient(allergenMap, choosenAllergen):
	sets = []
	for food in allergenMap[choosenAllergen]['foods']:
		sets.append(set(food))
	ingredient = reduce(lambda food1, food2: food1.intersection(food2), sets)
	return list(ingredient)[0]

def eradicateIngredient(allergenMap, ingredient):
	for key in allergenMap:
		foodList = []
		for food in allergenMap[key]['foods']:
			foodList.append(filter(lambda i: i != ingredient, food))
		allergenMap[key]['foods'] = foodList
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
		choosenAllergen = getUnIdentifiedAllergen(allergenMap)
		allergenMap[choosenAllergen]['ingredient'] = getIngredient(allergenMap, choosenAllergen)
		allergenMap[choosenAllergen]['foods'] = []
		allergenMap = eradicateIngredient(allergenMap, allergenMap[choosenAllergen]['ingredient'])
	return allergenMap

def getAllOccurencesOfSafeIngredients(foods, unsafeIngredients):
	allIngredients = []
	for key in foods:
		allIngredients.extend(foods[key]['ingredients'])
	safeIngredients = filter(lambda i: not i in unsafeIngredients, allIngredients)
	return safeIngredients

def solution():
	lines = getLines()
	start = time()
	foods = getFoodItems(lines)
	(allIndredients, allAllergens) = getUniqueIngredientsAndAllergens(foods)
	allergenMap = getAllergenMap(foods, allIndredients, allAllergens)
	chosenIngredients = map(lambda a: allergenMap[a]['ingredient'], allergenMap.keys())
	print len(getAllOccurencesOfSafeIngredients(foods, chosenIngredients))
	end = time()
	print end - start

solution()
