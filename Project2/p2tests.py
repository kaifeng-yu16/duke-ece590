"""
Math 560
Project 2
Fall 2021

p2tests.py
"""

# Import math and other p2 files.
import math
from p2stack import *
from p2queue import *
from p2maze import *

"""
testMazes function will test all of the mazes.
"""
def testMazes(verbosity=False):
    m = Maze(0,verbosity)
    print('Testing Maze 0, DFS')
    m.solve('DFS',verbosity,False)
    print('Testing Maze 0, BFS')
    m.solve('BFS',verbosity,False)
    m = Maze(1,verbosity)
    print('Testing Maze 1, DFS')
    m.solve('DFS',verbosity,False)
    print('Testing Maze 1, BFS')
    m.solve('BFS',verbosity,False)
    m = Maze(2,verbosity)
    print('Testing Maze 2, DFS')
    m.solve('DFS',verbosity,False)
    print('Testing Maze 2, BFS')
    m.solve('BFS',verbosity,False)
    m = Maze(3,verbosity)
    print('Testing Maze 3, DFS')
    m.solve('DFS',verbosity,False)
    print('Testing Maze 3, BFS')
    m.solve('BFS',verbosity,False)
    m = Maze(4,verbosity)
    print('Testing Maze 4, DFS')
    m.solve('DFS',verbosity,False)
    print('Testing Maze 4, BFS')
    m.solve('BFS',verbosity,False)
    plt.show()
    return

def testStack():
    stk = Stack()
    print(stk.__repr__())
    for i in range(10):
        stk.push(i)
    print(stk.__repr__())
    for j in range(5):
        stk.pop()
    print(stk.__repr__())
    return

def testQueue():
    que = Queue()
    print(que.__repr__())
    for i in range(12):
        que.push(i)
    print(que.__repr__())
    print(que.isFull())
    for j in range(5):
        que.pop()
    print(que.__repr__())

    que2 = Queue()
    print(que2.__repr__())
    for i in range(10):
        que2.push(i)
        que2.pop()
    que2.push(11)
    print(que2.__repr__())
    que2.resize()
    print(que2.__repr__())
    return

################################################################################