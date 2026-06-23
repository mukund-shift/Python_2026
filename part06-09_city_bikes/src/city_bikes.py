# tee ratkaisu tänne
# Write your solution here
def get_station_data(filename: str):

    with open(filename) as stations:
        station_data = {}
        for line in stations:
            line = line.strip()
            details = line.split(";")
            if details[0] == "Longitude":
                continue
            station_data[details[3]] = (float(details[0]), float(details[1]))
        return station_data


def distance(stations: dict, station1: str, station2: str):
    import math
    longitudes = (float(stations[station1][0]), float(stations[station2][0]))
    latitudes = (float(stations[station1][1]), float(stations[station2][1]))
    
    x_km = (longitudes[0] - longitudes[1]) * 55.26
    y_km = (latitudes[0] - latitudes[1]) * 111.2

    distance = math.sqrt((x_km**2) + (y_km**2))
    return distance


def greatest_distance(stations: dict):
    max_d = None
    for i in stations:
        for j in stations:
            if i == j:
                continue
            d = distance(stations, i, j)
            if max_d == None or d > max_d:
                stat1 = i
                stat2 = j
                max_d = d
    return stat1, stat2, max_d
            


if __name__ == "__main__":
    result = get_station_data("stations1.csv")
    d = greatest_distance(result)
    print(d)