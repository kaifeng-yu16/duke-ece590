"""
Math 560
Project 2
Fall 2021

p2queue.py

Partner 1: Kaifeng Yu(ky99)
Partner 2: Fangting Ma(fm128)
Date: Nov 2, 2021
"""

"""
Queue Class
"""
from matplotlib import set_loglevel


class Queue:

    """
    Class attributes:
    queue    # The array for the queue.
    front    # The index of the front of the queue.
    rear     # The index ONE PAST the rear of the queue.
    numElems # The number of elements in the queue.
    """

    """
    __init__ function to initialize the Queue.
    Note: intially the size of the queue defaults to 3.
    Note: the queue is initally filled with None values.
    """
    def __init__(self, size=3):
        self.queue = [None for x in range(0,size)]
        self.front = 0
        self.rear = 0
        self.numElems = 0
        return

    """
    __repr__ function to print the stack.
    """
    def __repr__(self):
        s = '[ ' + ', '.join(map(str, self.queue)) + ' ]\n'
        s += ('Front: %d' % self.front) + '\n'
        s += ('Rear: %d' % self.rear) + '\n'
        s += ('numElems: %d' % self.numElems) + '\n'
        return s

    """
    isFull function to check if the queue is full.
    """
    def isFull(self):
        return self.numElems == len(self.queue)

    """
    isEmpty function to check if the queue is empty.
    """
    def isEmpty(self):
        return self.numElems == 0

    """
    resize function to resize the queue by doubling its size.
    Note: we also reset the front to index 0.
    """
    def resize(self):
        # unwrap the queue
        if self.front != 0:
            self.queue = self.queue[self.front :] + self.queue[: self.front]
        self.front = 0
        self.rear = self.numElems
        self.queue += [None for _ in range(len(self.queue))]
        return

    """
    push function to push a value into the rear of the queue.
    """
    def push(self, val):
        if self.isFull():
            self.resize()
        self.queue[self.rear] = val
        self.rear += 1
        if self.rear == len(self.queue):
            self.rear = 0
        self.numElems += 1
        return

    """
    pop function to pop the value from the front of the queue.
    """
    def pop(self):
        # if queue is empty, return None
        if self.numElems == 0:
            return None
        # if queue is not empty, return the proper value
        pop_val = self.queue[self.front]
        self.queue[self.front] = None
        self.front += 1
        if self.front == len(self.queue):
            self.front = 0
        self.numElems -= 1
        return pop_val