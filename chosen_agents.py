from main.graphproblem import *


class SimpleProblemSolvingAgentProgram:
    """
    [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """

    def __init__(self, initial_state=None):
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.state = initial_state
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] Formulate a goal and problem, then
        search for a sequence of actions to solve it."""
        self.state = self.update_state(self.state, percept)
        if not self.seq:
            goal = self.formulate_goal(percept)
            problem = self.formulate_problem(self.state, goal)
            self.seq = self.search(problem)
            if not self.seq:
                return None
        return self.seq.pop(0)

    def update_state(self, state, percept):
        raise NotImplementedError

    def formulate_goal(self, state):
        raise NotImplementedError

    def formulate_problem(self, state, goal):
        raise NotImplementedError

    def search(self, problem):
        raise NotImplementedError


class MapSearchAgent(SimpleProblemSolvingAgentProgram):
    def __init__(self, speed, map_graph, initial_state=None):
        """Speed is the average travel velocity for the agent.
        Map_graph stores the graph containing the map locations
        as nodes. State is an abstract representation of the
        state of the world. Seq is the list of actions required
        to get to a particular state from the initial state(root)."""
        self.speed = speed
        self.map_graph = map_graph
        self.state = initial_state
        self.seq = []

    def __call__(self, percept, algorithm):
        """Formulate a goal and problem, then search for a
        sequence of actions to solve it using the given search
        algorithm."""
        self.seq = []
        goal = self.formulate_goal(percept)
        problem = self.formulate_problem(self.state, goal)
        self.seq = self.search(problem, algorithm)
        if not self.seq:
            return None
        return self.seq

    def update_state(self, state, percept):
        return percept

    def formulate_goal(self, state):
        goal = state
        return goal

    def formulate_problem(self, state, goal):
        """Given the initial state and goal state, creates the
        problem environment using the graph containing the
        map locations as nodes."""
        problem = GraphProblem(state, goal, self.map_graph)
        return problem

    def search(self, problem, algorithm):
        """Searches through the given problem using the provided
        algorithm until a solution is found, if any. Returns
        the path to the goal, with the approximate travel time
        appended to the end of path list."""
        result = algorithm(problem)
        seq = result.solution()
        seq.append(result.cost()/self.speed)
        return seq
