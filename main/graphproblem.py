from main.utils import *
from main.problem import Problem
from math import sin, cos, sqrt, atan2, radians
import numpy as np


class GraphProblem(Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)

        return m

    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node], locs[self.goal]))

            return int(distance(locs[node.state], locs[self.goal]))
        else:
            return np.inf

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        locs = getattr(self.graph, 'locations', None)
        return int(distance(locs[state], locs[self.goal]))


class GPSGraphProblem(GraphProblem):
    """Specialized Graph Problem class for graphs that use GPS coordinates
    for node locations."""

    def h(self, node):
        """h function is straight-line distance from a node's state to goal
        using Longitude and Latitude GPS coordinates."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                coords = locs[node]
            else:
                coords = locs[node.state]
        else:
            return np.inf

        # approximate radius of earth in km
        R = 6373.0

        lat1 = radians(coords[0])
        lon1 = radians(coords[1])
        lat2 = radians(locs[self.goal][0])
        lon2 = radians(locs[self.goal][1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c
        return distance
