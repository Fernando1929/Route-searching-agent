import csv


def get_towns(row):
    towns = []
    for town in row:
        if town != "Location":
            towns.append(town)
    return towns


def read_town_goal_distance(filename):
    try:
        with open(filename, 'r') as f:
            container = {}
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                container.update({row[0]: row[1]})
            return container
    except FileNotFoundError:
        print("File does not exist or not in current directory")


def read_town_distances(filename):
    try:
        with open(filename, 'r') as f:
            container = {}  # Will store {town : {other towns with approximate distance} }
            reader = csv.reader(f)
            read_towns = get_towns(next(reader))    # Get all possible towns
            for row in reader:
                container[row[0]] = {}
                for index in range(len(read_towns)):    # Store approximate distance from current town to the others
                    container[row[0]].update({read_towns[index]: row[index+1]})
            return container
    except FileNotFoundError:
        print("File does not exist or not in current directory")


towns_for_graph = read_town_distances('dataExcel.csv')  # Change town distance file name here
straightline_distances = read_town_goal_distance('dataExcelStraightLine.csv') # Change town goal approx file name here
# TEST
print(towns_for_graph)
print(straightline_distances)

