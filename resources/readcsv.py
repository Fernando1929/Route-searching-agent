import csv


def get_towns(row):
    """Get a list of all possible towns in map."""
    towns = []
    for town in row:
        if town != "Location":
            towns.append(town)
    return towns


def read_town_goal_distance(filename):
    """Read the (x,y) coordinates for each town in the map."""
    try:
        with open(filename, 'r') as f:
            container = {}
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                container.update({row[0]: (float(row[1]), float(row[2]))})
            return container
    except FileNotFoundError:
        print("File does not exist or not in current directory")


def read_town_distances(filename):
    """Read the distance from one town to the next reachable town and store in
    a dictionary. Each town (key) will have a list of reachable towns with their
    corresponding distances."""
    try:
        with open(filename, 'r') as f:
            container = {}  # Will store {town : {other towns with approximate distance} }
            reader = csv.reader(f)
            read_towns = get_towns(next(reader))    # Get all possible towns
            for row in reader:
                container[row[0]] = {}
                for index in range(len(read_towns)):    # Store approximate distance from current town to the others
                    if read_towns[index] != row[0] and read_towns[index] not in container.keys() \
                            and float(row[index+1]) != 0:
                        container[row[0]].update({read_towns[index]: float(row[index+1])})
            return container
    except FileNotFoundError:
        print("File does not exist or not in current directory")
