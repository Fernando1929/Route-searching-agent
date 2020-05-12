import sys

from chosen_agents import AStarMapSearchAgent
from main.search import *
from main.graphproblem import GraphProblem
from main.graph import Graph
from resources.readcsv import *

romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

############################## Puerto Rico Example ##########################################
pr_map = UndirectedGraph(read_town_distances('resources/dataExcel.csv'))
pr_map.locations = read_town_goal_distance("resources/dataExcelStraightLine.csv")   # Fix this

############################## Romania Example ##########################################
romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
pr_problem = GraphProblem('Mayaguez', 'Sanjuan', pr_map)


def test_astar_search():
    return astar_search(romania_problem).solution()


def astar_search_PR():
    return astar_search(pr_problem).solution()


def simulated_annealing_search():
    return simulated_annealing(romania_problem).solution()


def simulated_annealing_PR():
    return simulated_annealing(pr_problem).solution()


def test_route_agent():
    a_star_agent = AStarMapSearchAgent(100, "Arad")
    print(a_star_agent("Bucharest"))


test_route_agent()
print("TESTING ROMANIA ROUTE PROBLEM")
print('Romania Problem (a star) :', test_astar_search())
print('Romania Problem (simulated annealing) :', simulated_annealing_search())

# PR TESTING
print("\nTESTING PUERTO RICO ROUTE PROBLEM")
print('Puerto Rico Problem (a star):', astar_search_PR())
# print('Puerto Rico Problem (simulated annealing) :', simulated_annealing_PR())