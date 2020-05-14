"""Provides some utilities widely used by other modules"""
import functools
import random
from main.node import *

import numpy as np


def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)


def distance(a, b):
    """The distance between two (x, y) points."""
    xA, yA = a
    xB, yB = b
    return np.hypot((xA - xB), (yA - yB))


def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn


def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)


def check_consistent(problem):
    """Verifies that the given graph problem is consistent."""
    if not problem:
        return False
    else:
        consistent = False
        original = problem.initial
        for town in problem.graph.nodes():
            if town != problem.goal:
                problem.initial = town
                curr = Node(problem.initial)
                sl_approx = problem.h(curr)
                for neighbor in curr.expand(problem):
                    if neighbor.path_cost + problem.h(neighbor) >= sl_approx:
                        consistent = True
                    else:
                        consistent = False
                        break
                if not consistent:
                    break
        problem.initial = original
        return consistent


def check_admissible(problem):
    """Verifies that the given graph problem is admissible."""
    if not problem:
        return False
    else:
        admissible = False
        original = problem.initial
        for town in problem.graph.nodes():
            if town != problem.goal:
                problem.initial = town
                curr = Node(problem.initial)
                admissible = recursive_admissible(problem, curr, problem.h(curr))
                if not admissible:
                    break
        problem.initial = original
        return admissible


def recursive_admissible(problem, current, target_dist):
    """Recursive method to follow each possible path towards
    the goal for the current node to validate that the
    straight line approximation from the original node
    to the goal is less than or equal to the actual cost."""
    if current.path_cost > target_dist:
        return True
    elif problem.goal_test(current):
        return False
    else:
        admissible = False
        expanded = current.expand(problem)
        if len(expanded) < 3:
            if current.parent in expanded:
                expanded.remove(current.parent)
            else:
                if problem.h(expanded[0]) > problem.h(current) and problem.h(expanded[1]) > problem.h(current):
                    if problem.h(expanded[0]) < problem.h(expanded[1]):
                        expanded.pop(1)
                    else:
                        expanded.pop(0)
        if len(expanded) == 1:
            admissible = recursive_admissible(problem, expanded.pop(), target_dist)
        else:
            for neighbor in expanded:
                if problem.h(neighbor) < problem.h(current):
                    admissible = recursive_admissible(problem, neighbor, target_dist)
        return admissible

