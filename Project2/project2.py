"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1: Kaifeng Yu(ky99)
Partner 2: Fangting Ma(fm128)
Date: Nov 2, 2021
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS function

INPUTS
maze: A Maze object representing the maze.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bfs(maze):
    # clear maze, for every vertex v in maze: 
    # set v.dist = inf 
    # set v.visited = False
    # set v.prev = None
    for v in maze.adjList:
        v.dist = math.inf
        v.visited = False
        v.prev = None
    # push the start node into the queue
    que = Queue()
    maze.start.visited = True
    maze.start.dist = 0
    que.push(maze.start)
    # BFS
    while (not que.isEmpty()):
        v = que.pop()
        # exit earlier if the exit is found
        if v.isEqual(maze.exit):
            break
        for neigh in v.neigh:
            if neigh.visited == False:
                neigh.visited = True
                neigh.prev = v
                neigh.dist = v.dist + 1
                que.push(neigh)
    # retrace the path
    if not v.isEqual(maze.exit):
        return []
    maze.path = [0 for _ in range(v.dist + 1)]
    while v != None:
        maze.path[v.dist] = v.rank
        v = v.prev
    return maze.path

"""
DFS function

INPUTS
maze: A Maze object representing the maze.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def dfs(maze):
    # clear maze, for every vertex v in maze: 
    # set v.dist = inf 
    # set v.visited = False
    # set v.prev = None
    for v in maze.adjList:
        v.dist = math.inf
        v.visited = False
        v.prev = None
    # push the start node into the stack
    stk = Stack()
    maze.start.visited = True
    maze.start.dist = 0
    stk.push(maze.start)
    # DFS
    while (not stk.isEmpty()):
        v = stk.pop()
        # exit earlier if the exit is found
        if v.isEqual(maze.exit):
            break
        for neigh in v.neigh:
            if neigh.visited == False:
                neigh.visited = True
                neigh.prev = v
                neigh.dist = v.dist + 1
                stk.push(neigh)
    # retrace the path
    if not v.isEqual(maze.exit):
        return []
    maze.path = [0 for _ in range(v.dist + 1)]
    while v != None:
        maze.path[v.dist] = v.rank
        v = v.prev
    return maze.path

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""
def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    if alg == 'BFS':
        return bfs(maze)
    else:
        return dfs(maze)
    

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)