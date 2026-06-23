# Write your solution here

def recipe_analysis(filename):
    recipes = {}
    with open(filename) as recipes_db:
        ctr = 0
        for line in recipes_db:
            line = line.strip()
            if ctr == 0:
                temp_name = line
                recipes[temp_name] = []
                ctr += 1
            elif line == "":
                ctr = 0
            else:
                recipes[temp_name].append(line)
    return recipes


def search_by_name(filename : str, term : str):
    recipes = recipe_analysis(filename)
    found_recipes = []
    for dish in recipes:
        if term.lower() in dish.lower():
            found_recipes.append(dish)
    return found_recipes


def search_by_time(filename : str, time : int):
    recipes = recipe_analysis(filename)
    found_recipes = []
    for dish in recipes:
        if int(recipes[dish][0]) <= time:
            found_recipes.append(f"{dish}, preparation time {recipes[dish][0]} min")
    return found_recipes


def search_by_ingredient(filename: str, ingredient: str):
    recipes = recipe_analysis(filename)
    found_recipes = []
    for dish in recipes:
        for details in recipes[dish][1:]:
            if ingredient in details:
                found_recipes.append(f"{dish}, preparation time {recipes[dish][0]} min")
                break
    return found_recipes
    
