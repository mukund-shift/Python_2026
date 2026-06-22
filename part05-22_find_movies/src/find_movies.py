# Write your solution here
def find_movies(database: list, search_term: str):
    hits = []
    for i in range(len(database)):
        if search_term in database[i]["name"].lower():
            hits.append(database[i])
    return hits


