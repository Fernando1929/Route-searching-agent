from main.chosen_agents import MapSearchAgent
from main.search import *
from main.graphproblem import GraphProblem, GPSGraphProblem
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


def test_route_agent(title, start, goal, speed, problem):
    # Initialize agent
    agent = MapSearchAgent(speed, problem, start)
    # Run analysis for the given problem
    print("\nRUNNING ANALYSIS for", title, "\n")
    
    print("Average speed for the algorithm", speed, "KM/H", "\n")

    astar_result = agent(goal, astar_search)
    simulated_annealing_result = agent(goal, simulated_annealing)
    astar_time = astar_result.pop()
    simulated_annealing_time = simulated_annealing_result.pop()

    print(title, "A* Solution\nTravel time: ", astar_time, "Hours", "\nPath: ", astar_result, "\n")
    print(title, "Simulated Annealing Solution\nTravel time: ", simulated_annealing_time, "Hours", "\nPath: ", simulated_annealing_result, "\n")
    performance = abs(astar_time-simulated_annealing_time)/astar_time*speed
    print("Simulated Annealing vs A* performance percentage: ", performance, "%")

# Preparing Puerto Rico Graph
pr_map = UndirectedGraph(read_town_distances('resources/dataExcel2.csv'))
pr_map.locations = read_town_goal_distance("resources/dataExcelStraightLine2.csv")

# Creating Map Problems
romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
pr_problem = GPSGraphProblem('Mayaguez', 'Sanjuan', pr_map)

# Running analysis
test_route_agent("Romania", "Arad", "Bucharest", 100, romania_problem)
test_route_agent("Puerto Rico", "Mayaguez", "Sanjuan", 100, pr_problem)
