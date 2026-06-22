# Write your solution here
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    record = {}
    record["name"] = name
    record["director"] = director
    record["year"] = year
    record["runtime"] = runtime
    database.append(record)